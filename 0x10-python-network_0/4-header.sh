#!/bin/bash
# Send a custom header to the server
curl -sH "X-School-User-Id: 98" "$1"
