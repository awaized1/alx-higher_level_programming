#!/bin/bash
# Code displays the HTTP methods the URL will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
