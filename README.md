# An CLI tool for the Opsani Optimization API: coctl

This is a simple application that can consume an Opsani service configuration and post it to the domain/app, or query the service for the current domain/app configurations.

## Work in progress

Currently only config read (get) and optimization restart (restart) are supported.

## Installation

It is recommended that you launch this in a Docker container, or deploy in a python virtual environment:

```bash
python3 -m venv .
. bin/activate
python3 -m pip install -e .
python3 -m pip install -r requirements.txt
```

## Basic usage

Export the configuration (or pass as CLI parameters):

```bash
export CO_TOKEN=ASFDASDFASDFASDF
export CO_DOMAIN=domain.name
export CO_APP=app.name
```

### Get config

Get the current configuration from your domain/app:

```bash
coctl get
```

Get the current config to a specific file:

```bash
coctl get -f config-state.yaml
```

### Put config

Put a YAML config in `coconfig.yaml` to the app config first get the config, then re-put it to the application endpoint.

```bash
coctl get
coctl put
```

For a YAML document with a specific `perf:` metric, update the `optimization:` configuration

```bash
cat > optimization.yaml <<EOF
optimization:
  mode: saturation
  perf: metrics['requests throughput']
EOF
```

```bash
coctl put -f optimization.yaml
```

### Change just the optimiization

Restart the optimization:

```bash
coctl restart
```

## TODO

1. Add a Dockerfile and instructions
2. Basic configuration validation
