#!/usr/bin/env python3

import requests


def parse_http(endpoint: str = "https://postman-echo.com/get"):
    response = requests.get(params={"foo1": "bar1", "foo2": "bar2"}, url=endpoint)
    if response.status_code == 200:
        return response
    else:
        return None
