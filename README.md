# An CLI tool for the Opsani Optimization API: otctl

This is a simple application that can consume an Opsani service configuration and post it to the domain/app, or query the service for the current domain/app configurations.

## Work in progress

Currently only config read (get) and optimization restart (restart) are supported.

## Installation

It is recommended that you launch this in a Docker container, or deploy in a python virtual environment:

```bash
python3 -m venv .
. bin/activate
python3 -m pip install .
```

## Basic usage

Export the configuration (or pass as CLI parameters):

```bash
export OT_TOKEN=ASFDASDFASDFASDF
export OT_DOMAIN=domain.name
export OT_APP=app.name
```

Get the current configuration from your domain/app:

```bash
otctl get
```

Restart the optimization:

```bash
otctl restart
```

## TODO

1. Write the configuration to a file with `get` if a -f or --file parameter is passed
2. Read from a configuration (YAML) file with `put` if -f or --file is passed, or use config.yaml as a default if no file parameter is passed
3. Basic configuration validation
