import click
from .api_wrapper import request_data


@click.command(help="Stop a Scan by Scan_ID")
@click.argument('scanid')
def stop(scanid):
    try:
        request_data('POST', '/scans/{}/stop'.format(scanid))
        print("\nStopping your scan {} now.\n".format(scanid))
    except AttributeError:
        click.echo("Scan is not in the running state")
