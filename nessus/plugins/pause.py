import click
from .api_wrapper import request_data


@click.command(help="Pause a Scan by Scan_ID")
@click.argument('scanid')
def pause(scanid):
    try:
        request_data('POST', '/scans/{}/pause'.format(scanid))
        print("\npausing your scan {} now.\n".format(scanid))
    except AttributeError:
        click.echo("Scan is not in the running state")
