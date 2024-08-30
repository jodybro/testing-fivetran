#!/usr/bin/env python3

import os
import sys
import sqlite3


def ensure_db_exists(db_file: str = "out.db"):
    if not os.path.exists(db_file):
        with open(db_file, "w"):
            pass
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
        conn.commit()
        conn.close()
