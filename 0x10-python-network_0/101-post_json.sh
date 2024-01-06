#!/bin/bash
# Script sends JSON POST request to URL with given JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
