# An CLI tool for the Opsani Optimization API: coctl

This is a simple application that can consume an Opsani service configuration and post it to the domain/app, or query the service for the current domain/app configurations.

## Work in progress

Basic get (download current configuration), and put (apply a patch to the upstream config, merge with what's there) is aavailable.  there's also a restart function, but that could also be handled by passing a null '{}' document to put.

Inputs are not validated
Error handling could certainly be improved


## Installation

It is recommended that you launch this in a Docker container, or deploy in a python virtual environment:

```bash
python3 -m venv .
. bin/activate
python3 -m pip install -e .
```

or:

```bash
docker build . -t coctl:latest
alias coctl='docker run -it --rm --name coctl -v $(pwd)/:/work coctl:latest '
```

## Basic usage

Export the configuration (or pass as CLI parameters):

```bash
export CO_TOKEN=ASFDASDFASDFASDF
export CO_DOMAIN=domain.name
export CO_APP=app.name
```

For Docker use, set an alias _after_ setting the environment variables, and you won't have to pass the env variables:

```bash
alias coctl="docker run -it --rm --name coctl -v $(pwd)/:/work/ -e CO_TOKEN=$CO_TOKEN -e CO_DOMAIN=$CO_DOMAIN -e CO_APP=$CO_APP coctl:latest "
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

1. Basic configuration validation
2. Basic environment variable validation
3. Remove the need for the --file option, treat as an argument instead
