#!/bin/bash
# send a post request from a file
curl -sd "@$2" "$1"
