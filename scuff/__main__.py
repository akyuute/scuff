from . import tools
from .cli import ArgParser

def main() -> None:
    args = ArgParser().parse_args()
    print(args)

##    conversions = {
##        'ast': tools.parse,
##        'json': tools.*_to_json,
##        '':
##    }
    source = args.source



if __name__ == '__main__':
    main()
