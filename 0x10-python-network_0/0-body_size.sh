#!/bin/bash
# This sends a request to a URL with curl, and displays the size of the response
curl -s "$1" | wc -c
