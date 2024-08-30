#!/usr/bin/env python3

import os
import sqlite3
from typing import Dict, Any


def ensure_db_exists(db_file):
    print(db_file)
    if not os.path.exists(db_file):
        with open(db_file, "w") as f:
            f.write("")
    else:
        pass


def connect_db(db_file: str):
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
    # FIX: Error if column name is illegal
    columns = []
    for k, v in data.items():
        column_type = json_to_sqlite_type(v)
        columns.append(f"{k} {column_type}")
    columns_sql = ", \n".join(columns)
    # TODO: Error if table exists
    return f"CREATE TABLE ({columns_sql})"
