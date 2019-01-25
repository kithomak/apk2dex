import os, argparse

from apk2dex import apk2dex, apk2dex_folder


def main(args):
    if os.path.isfile(args.input):
        apk2dex(args.input, args.output, args.verbose)
    elif os.path.isdir(args.input):
        apk2dex_folder(args.input, args.output, args.verbose, args.log)
    else:
        raise ValueError("Incorrect input file or folder.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple APK to DEX extractor.')
    parser.add_argument("input", help="Input apk file or a folder of apks.")
    parser.add_argument('-o', "--output", default=".",
                        help="Output folder. Defaults to the current working folder.")
    parser.add_argument('-v', '--verbose', action="store_true", help="Print verbrose messages.")
    parser.add_argument('-l', "--log", help="Log file. Default is no logging.")
    args = parser.parse_args()

    main(args)


