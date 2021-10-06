import click
import pprint
from .api_wrapper import request_data


@click.command(help="Launch a Scan by Scan_ID")
@click.argument('scanid')
def launch(scanid):
    try:
        launch_scan = request_data('POST', '/scans/{}/launch'.format(scanid))
        print("\nLaunching your scan {} now.\n".format(scanid))
        pprint.pprint(launch_scan.json())
    except AttributeError:
        click.echo("Scan ID not found")
