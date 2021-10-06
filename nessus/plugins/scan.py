import click
import pprint
from .api_wrapper import request_data


@click.command(help="Create a scan from the command line")
@click.argument('targets')
@click.option('-discovery', is_flag=True, help="Scan using the Discovery Template")
@click.option('--custom', default='', help="Scan using a custom Scan Template")
@click.option('--policy', default='', help="Use Policy ID")
def scan(targets, discovery, custom, policy):
    # If a Template isn't chosen we will assume a Basic Network scan
    template = '731a8e52-3ea6-a291-ec0a-d2ff0619c19d7bd788d6be818b65'

    if discovery:
        template = 'bbd4f805-3966-d464-b2d1-0079eb89d69708c3a05ec2812bcf'

    if len(custom) == 52:
        template = custom

    click.echo("creating your scan of : {}  Now...".format(targets))

    # Begin Payload Creation
    payload = dict(uuid=template,
                   settings={"name": "Python Created Scan of " + targets,
                             "enabled": "True",
                             "text_targets": targets})

    if policy:

        try:
            # Add policy to payload
            payload["settings"]["policy_id"] = policy

        except KeyError:
            click.echo("\nCheck your Credential UUID\n")
            exit()

    # create a new scan
    data = request_data('POST', '/scans', payload=payload)

    pprint.pprint(data.json())
