#!/usr/bin/env python3

import json
import os

from typing import Dict, Any
from src.testing_fivetran import args
from src.testing_fivetran import db


cli_args = args.cli_args()
DEFAULT_DB_FILE = os.getcwd() + "/out.db"


# TODO: Use proper data structure from http response
def insert_data(
    data: Dict[str, Any],
    table_name: str = "fivetran",
    db_file: str = DEFAULT_DB_FILE,
) -> bool:
    # TODO: Use a fucking context manager amar
    conn = db.connect_db(DEFAULT_DB_FILE)
    c = conn.cursor()
    c.execute(db.generate_create_table_sql(data))
    conn.commit()
    conn.close()
    conn = db.connect_db(db_file)
    c = conn.cursor()
    c.execute(f"INSERT INTO {table_name} VALUES (?)", (json.dumps(data),))
    conn.commit()
    conn.close()
    return True


if __name__ == "__main__":
    # TODO: Motherfucking context manager again amar
    conn = db.connect_db(DEFAULT_DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    result = cursor.fetchall()
    for row in result:
        print(row)
    conn.close()
