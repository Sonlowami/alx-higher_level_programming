#!/usr/bin/env bash
# Post data to the server
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
