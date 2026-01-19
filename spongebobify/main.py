import argparse
import importlib.metadata
from random import choice


__version__ = importlib.metadata.version("spongebobify")


def aye_aye(message: str) -> str:
    return "".join(choice((str.upper, str.lower))(letter) for letter in message)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="spongebobify",
        description="Are ya ready kids? aYE AyE! You can now make your text...sARcaStiC!",
    )
    parser.add_argument(
        "text",
        nargs="+",
        help="The text to make sArCAstIC.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"spongebobify version: {__version__}",
    )

    args = parser.parse_args()

    full_text = " ".join(args.text)
    print(aye_aye(full_text))


if __name__ == "__main__":
    main()
