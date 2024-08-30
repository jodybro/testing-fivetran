#!/usr/bin/env python3

import os
import sqlite3
import json
from typing import Dict, Any

DEFAULT_DB_FILE = os.getcwd() + "/out.db"


def ensure_db_exists(db_file: str = DEFAULT_DB_FILE):
    print(db_file)
    if not os.path.exists(db_file):
        with open(db_file, "w") as f:
            f.write("")
            f.close()
    else:
        pass


def connect_db(db_file: str = DEFAULT_DB_FILE):
    return sqlite3.connect(db_file)


def json_to_sqlite_type(value: Any) -> str:
    if isinstance(value, bool):
        return "INTEGER"  # SQLite doesn't have a boolean type, so we use INTEGER
    elif isinstance(value, int):
        return "INTEGER"
    elif isinstance(value, float):
        return "REAL"
    elif isinstance(value, (str, list, dict)):
        return "TEXT"  # We'll store complex types as JSON text
    else:
        return "TEXT"


def generate_create_table_sql(data: Dict[str, Any]) -> str:
    columns = []
    for k, v in data.items():
        column_type = json_to_sqlite_type(v)
        columns.append(f"{k} {column_type}")
    columns_sql = ", \n".join(columns)
    return f"CREATE TABLE users ({columns_sql})"


def insert_data(
    data: Dict[str, Any],
    table_name: str = "fivetran",
    db_file: str = DEFAULT_DB_FILE,
) -> bool:
    ensure_db_exists()
    conn = connect_db(db_file)
    c = conn.cursor()
    c.execute(generate_create_table_sql(data))
    conn.commit()
    conn.close()
    conn = connect_db(db_file)
    c = conn.cursor()
    c.execute(f"INSERT INTO {table_name} VALUES (?)", (json.dumps(data),))
    conn.commit()
    conn.close()
    return True
