import argparse


def main():
    arg_parser = argparse.ArgumentParser(
        prog='listening',
        description='Copyright by Ja',
        # usage='%(prog)s [option] function firstPath lastPath',
        epilog='have you a nice day :)',
        fromfile_prefix_chars='@',  # inportowanie argumentów z pliku txt
        allow_abbrev=False,  # pisanie skrutowo argumentów
    )
    arg_parser.add_argument(
        'Start_Path',
        metavar='first_path',
        type=str,
        help='The path to first folder'
    )
    arg_parser.add_argument(
        'End_Path',
        metavar='last_path',
        type=str,
        help='The path to last folder'
    )
    arg_parser.add_argument(
        '-i',
        '--infinity',
        action='store_true',
        help='set time update [s]'
    )
    args = arg_parser.parse_args()

    return args
