from .api import api
from .scan import scan
from .download import download
from .launch import launch
from .status import status
from .stop import stop
from .resume import resume
from .pause import pause
from .display import display


def plugin_loader(group):
    group.add_command(api)
    group.add_command(download)
    group.add_command(launch)
    group.add_command(status)
    group.add_command(stop)
    group.add_command(resume)
    group.add_command(pause)
    group.add_command(display)
    group.add_command(scan)
