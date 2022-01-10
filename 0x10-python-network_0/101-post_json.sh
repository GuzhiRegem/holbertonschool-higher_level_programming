#!/bin/bash
#comment
curl -sH "Content-Type:Application/json" "$1" -d @"$2"
