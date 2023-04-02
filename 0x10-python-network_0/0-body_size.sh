#!/bin/bash
# curl a URL and display the size of the body
curl -so /dev/null -w "%{size_download}\n" "$1"
