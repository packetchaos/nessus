import click
from .api_wrapper import request_data


@click.command(help="Get the status of a scan")
@click.argument('scanid')
def status(scanid):
    get_status = request_data('GET', '/scans')

    for scan in get_status.json()['scans']:
        if str(scan['id']) == str(scanid):
            click.echo("\nStatus: {}\n".format(scan['status']))

