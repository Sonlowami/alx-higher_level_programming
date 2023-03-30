#!/usr/bin/env bash
# Find all HTTP methods a server supports
curl -sILX "OPTIONS" "$1" | grep -i "allow" | cut -f 2 -d ":" | xargs
