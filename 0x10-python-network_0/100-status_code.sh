#!/bin/bash
# Code Sends GET request to URL and displays response status code
curl -s -o /dev/null -w "%{http_code}" "$1"
