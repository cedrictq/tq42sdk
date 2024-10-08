from tq42.exceptions.tq42_api_error import TQ42APIError

_MESSAGE = """
Unable to Execute: `{}`

We were unable to automatically detect the default org and/or proj ID required to run this command.
Please set an org and proj yourself by running the following commands:

`tq42 org set <ORG_ID>`
`tq42 proj set <PROJ_ID>`

These IDs can be either found on terraquantum.io or via the corresponding CLI commands `tq42 org list` / `tq42 proj list`.
For a list of available commands, type `tq42 --help` or consult the documentation at tq42.com/help.
""".strip()


class NoDefaultError(TQ42APIError):
    """
    Raised when the default organisation and/or project cannot be detected

    Attributes:
        command (str): the command for which the error occurred
    """

    def __init__(self, command: str):
        self.command = command

    def __str__(self):
        return _MESSAGE.format(self.command)
