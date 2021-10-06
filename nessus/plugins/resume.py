import click
from .api_wrapper import request_data


@click.command(help="Resume a Scan by Scan_ID")
@click.argument('scanid')
def resume(scanid):
    try:
        request_data('POST', '/scans/{}/resume'.format(scanid))
        print("\nresuming your scan {} now.\n".format(scanid))
    except AttributeError:
        click.echo("Scan is not in the paused state")
