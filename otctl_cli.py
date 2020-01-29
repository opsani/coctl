import click
import requests
import yaml
import os


@click.group()
@click.option('--file', '-f', type=click.File('w'), help='The name of the config file or "otconfig.yaml" by default', default='otconfig.yaml')
@click.option('--token', '-t', help='The Optune app token (or OT_TOKEN environment variable)', envvar='OT_TOKEN')
@click.option('--domain', '-d', help='The Optune domain (or OT_DOMAIN enviornment varaible)', envvar='OT_DOMAIN')
@click.option('--app', '-a', help='The Optune application (or OT_APP environment variable)', envvar='OT_APP')
@click.pass_context
def cli(ctx,file,token,domain,app):
    ctx.ensure_object(dict)
    ctx.obj['file']=file
    ctx.obj['token']=token
    ctx.obj['domain']=domain
    ctx.obj['app']=app

@cli.command()
@click.pass_context
def get(ctx):

    """Get the latest config from the API"""
    click.echo("Getting the configuration")
    url=f"https://api.optune.ai/accounts/{ctx.obj['domain']}/applications/{ctx.obj['app']}/config/"
    response=requests.get(
        url,
        headers={"Content-type": "application/merge-patch+json",
            "Authorization": f"Bearer {ctx.obj['token']}"}
    )
    click.echo(response.content)

@cli.command()
@click.pass_context
def put(ctx):

    """Push the config file, or config patch to the API"""
    click.echo("This would push the config")

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
    print(response.request.body)
    print(response.request.headers)
    print(response.request.url)
    json_response=response.json()
    click.echo(f"we got {response.json()}")

if __name__ == '__main__':
    cli(obj={})