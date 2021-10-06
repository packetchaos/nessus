import click
from .plugins import plugin_loader


@click.group(help="This tool is not Supported by Tenable. \n ")
@click.pass_context
def cli(ctx):
    pass


plugin_loader(cli)
