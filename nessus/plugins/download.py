import click
import time
from .api_wrapper import request_data


def check_status(token):
    scan_status = 'not ready'

    while scan_status != 'ready':
        scan_status = request_data('GET', '/tokens/{}/status'.format(token)).json()['status']
        time.sleep(2.5)
    return scan_status


def download_scan(token, name, ext):
    get_download = request_data('GET', '/tokens/{}/download'.format(token))

    with open('{}.{}'.format(name, ext), 'wb') as nessus_scan:
        nessus_scan.write(get_download.content)


@click.command(help="Download a scan")
@click.option("--ext", default="nessus", help="File Type / Extension: nessus, csv, pdf")
@click.option("--name", default="nessus_scan", help="The name of the file to be saved")
@click.option("--scanid", default=None, help="Scan ID of the scan you want to download")
def download(ext, name, scanid):

    request_download = request_data('POST', "/scans/{}/export/".format(scanid), payload={"format": "{}".format(ext)})

    new_token = request_download.json()['token']

    if check_status(new_token) == 'ready':
        download_scan(new_token, name, ext)
