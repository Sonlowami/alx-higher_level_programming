#!/usr/bin/env bash
# Print only the status code to stdout
curl -sw '%{http_code}' -o /dev/null "$1"
