"""Console script for ddb_single_table."""

import fire


def help():
    print("ddb_single_table")
    print("=" * len("ddb_single_table"))
    print(
        "Bootstrap your single table design n with simple patterns, integrations and queries."
    )


def main():
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
