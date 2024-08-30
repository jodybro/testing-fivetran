#!/usr/bin/env python3

import argparse


def cli_args():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(
        description="cli tool to read json and export to sqlite3 db"
    )
    parser.add_argument(
        "-i",
        "--input-file",
        help="json file to read",
        required=False,
        default="data.json",
    )

    parser.add_argument(
        "-d", "--db-file", help="sqlite3 db file", required=False, default="out.db"
    )
    return parser.parse_args()
