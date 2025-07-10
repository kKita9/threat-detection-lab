## Suricata Container

This container runs [Suricata](https://suricata.io/) in IDS mode for monitoring network traffic of specific lab services.

### Features

- Based on `jasonish/suricata:latest`
- Runs in live capture mode on `eth0`
- Designed to run in the **network namespace of another container** (`network_mode: "container:..."`)
- Generates alerts and flow data in `eve.json` and `fast.log`

### Usage

This container is intended to be run alongside another service (e.g., `ssh-lab`, `ftp-lab`, `dvwa`) and shares its network stack.

Each instance is defined in the main project's `docker-compose.yml` like so:

```yaml
suricata-ssh:
  build: environments/suricata
  network_mode: "container:ssh-lab"
  cap_add:
    - NET_ADMIN
    - NET_RAW
  volumes:
    - ./logs/suricata/ssh:/var/log/suricata
```

### Logs

Suricata will write logs to the mounted volume:

- `eve.json` – structured JSON logs (alerts, flows, anomalies)
- `fast.log` – plain text alerts
- `stats.log` – engine statistics
- `suricata.log` – runtime and debug messages

Example path on host:

```
./logs/suricata/ssh/eve.json
```

### Notes

- Suricata requires elevated privileges (NET_ADMIN, NET_RAW)
- It must be attached directly to another container’s network namespace to see its traffic
- One Suricata instance per monitored container is recommended
