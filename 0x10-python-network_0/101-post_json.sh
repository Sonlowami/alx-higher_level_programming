#!/bin/bash
# send a post request from a file
curl -sfd "@$2" "$1"
