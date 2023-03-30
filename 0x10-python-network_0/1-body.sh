#!/bin/bash
# Curl a resource and only display the body if status code is 200
curl -sfL "$1"
