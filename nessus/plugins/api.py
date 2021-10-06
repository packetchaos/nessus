import click
import pprint
from .api_wrapper import request_data


@click.command(help="Explore the API")
@click.argument('url')
@click.option('-raw', is_flag=True, help="Return raw Json")
@click.option('--limit', default=50, help="Change API Request Limit")
@click.option('--offset', default=0, help="Change API Request Offset")
def api(url, limit, offset, raw):
    params = {"limit": limit, "offset": offset}
    try:
        data = request_data('GET', url, params=params)
        if not raw:
            pprint.pprint(data.json())
        else:
            click.echo(data.json())

    except Exception as E:
        click.echo(E)
