import click
import requests
import yaml
import json
import os
'''
An CLI tool for the Opsani Optimization API.

coctl: Continuous Optimization Control

Copyright 2020 Opsani, Inc.

Licensed under the BSD-3-Clause license
'''

@click.group()
@click.option('--token', '-t', help='The Optune app token (or OT_TOKEN environment variable)', envvar='CO_TOKEN')
@click.option('--domain', '-d', help='The Optune domain (or OT_DOMAIN enviornment varaible)', envvar='CO_DOMAIN')
@click.option('--app', '-a', help='The Optune application (or OT_APP environment variable)', envvar='CO_APP')
@click.pass_context
def cli(ctx,token,domain,app):
    ctx.ensure_object(dict)
    ctx.obj['token']=token
    ctx.obj['domain']=domain
    ctx.obj['app']=app

@cli.command()
@click.option('--file', '-f', type=click.File('w'), help='The name of the config file or "coconfig.yaml" by default', default='coconfig.yaml')
@click.pass_context
def get(ctx,file):

    """Get the latest config from the API"""
    click.echo("Getting the configuration")
    url=f"https://api.optune.ai/accounts/{ctx.obj['domain']}/applications/{ctx.obj['app']}/config/"
    response=requests.get(
        url,
        headers={"Content-type": "application/merge-patch+json",
            "Authorization": f"Bearer {ctx.obj['token']}"}
    )
    data=response.json()
    yaml.dump(data,file)

@cli.command()
@click.option('--file', '-f', type=click.File('r'), help='The name of the config file or "coconfig.yaml" by default', default='coconfig.yaml')
@click.pass_context
def put(ctx,file):

    """Push the config file, or config patch to the API"""
    click.echo(f"Push {file.name} as a patch to the API")
    data=json.dumps(yaml.load(file, Loader=yaml.FullLoader))
    click.echo(data)
    url=f"https://api.optune.ai/accounts/{ctx.obj['domain']}/applications/{ctx.obj['app']}/config/"
    response=requests.put(
        url,
        params={'reset': 'true', 'patch': 'true'},
        headers={"Content-type": "application/merge-patch+json",
            "Authorization": f"Bearer {ctx.obj['token']}"},
        data=data
    )
    #click.echo(response.requests.body)
    click.echo(response.json())

@cli.command()
@click.pass_context
def restart(ctx):

    """Reset the app service and restart the optimization"""
    click.echo("Restarting the optimization service")
    url=f"https://api.optune.ai/accounts/{ctx.obj['domain']}/applications/{ctx.obj['app']}/config"
    response=requests.put(
        url,
        params={'reset':'true','patch':'true'},
        json={},
        headers={"Content-type": "application/merge-patch+json",
            "Authorization": f"Bearer {ctx.obj['token']}"}
    )

    click.echo(f"we got {response.json()}")

if __name__ == '__main__':
    cli(obj={})
