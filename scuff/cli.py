from argparse import ArgumentParser, SUPPRESS

from . import __version__


PROG = __package__


class ArgParser(ArgumentParser):
    '''
    A custom command line parser used by the command line utility.
    '''

    def __init__(self) -> None:
        super().__init__(
            prog=PROG,
            argument_default=SUPPRESS,
        )
        self.add_arguments()

    def add_arguments(self) -> None:
        '''
        Equip the parser with all its arguments.
        '''

        self.add_argument(
            'source',
            help="The file path or literal Scuff to process.",
        )

        self.add_argument(
            '--to-json', '-j',
            dest='json',
            action='store_true',
            help="Convert `source` to JSON.",
        )

        self.add_argument(
            '--show-ast', '-a',
            dest='ast',
            action='store_true',
            help="Parse `source` and show its equivalent AST.",
        )

        self.add_argument(
            '--debug',
            action='store_true',
            help="Use debug mode. (Not implemented)",
        )

        self.add_argument(
            '--version', '-v',
            action='version',
            version=f"{__package__} {__version__}",
        )

