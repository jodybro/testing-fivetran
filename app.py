#!/usr/bin/env python3

import json
import os

from src.testing_fivetran import args
from src.testing_fivetran import parse_http
from src.testing_fivetran import db


cli_args = args.cli_args()
http_response = parse_http.parse_http().json()

# Example usage
json_str = """
{

    "id": 1,
    "name": "John Doe",
    "age": 30,
    "is_active": true,
    "height": 1.75,
    "address": {
        "street": "123 Main St",
        "city": "Anytown"

    },
    "hobbies": ["reading", "swimming"]
}
"""


json_data = json.loads(json_str)
table_name = "users"

client = db.connect_db()
c = client.cursor()
c.execute("SELECT * FROM users")
client.commit()
print(c.fetchall())
client.close()
