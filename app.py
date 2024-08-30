#!/usr/bin/env python3

import json
import os

from src.testing_fivetran import args
from src.testing_fivetran import parse_http

cli_args = args.cli_args()
http_response = parse_http.parse_http().json()
print(json.dumps(http_response, indent=4))
