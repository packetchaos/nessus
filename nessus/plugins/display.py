import click
from .api_wrapper import request_data


@click.command(help="Display scans in Nessus Pro")
@click.option("-scans", is_flag=True, help="Display all scans in Nessus pro")
def display(scans):
    if scans:
        scan_info = request_data('GET', '/scans')

        print("\n{:45} : {}".format("Scan Name", "Scan ID"))
        print("-" * 100)
        for scan in scan_info.json()['scans']:
            print("{:45} : {}".format(scan['name'], scan['id']))

        print()
