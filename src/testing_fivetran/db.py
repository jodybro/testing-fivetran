#!/usr/bin/env python3

from os import getcwd
from typing import Any, Dict, Union

from sqlalchemy import create_engine
from sqlalchemy.dialects.sqlite.pysqlite import Engine as SQLiteEngine

DEFAULT_DB_FILE = getcwd() + "/out.db"


def ensure_db_exists(db_file) -> Union[SQLiteEngine, Exception]:
    try:
        engine = create_engine(f"sqlite:///{db_file}")
        return engine
    except:
        raise Exception("Cannot connect to db")


def connect_db(db_file: str = DEFAULT_DB_FILE):
    return


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


def insert_data(
    data: Dict[str, Any],
    table_name: str = "data",
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


def generate_create_table_sql(data: Dict[str, Any]) -> str:
    # FIX: Error if column name is illegal
    columns = []
    for k, v in data.items():
        column_type = json_to_sqlite_type(v)
        columns.append(f"{k} {column_type}")
    columns_sql = ", \n".join(columns)
    # TODO: Error if table exists
    return f"CREATE TABLE ({columns_sql})"
