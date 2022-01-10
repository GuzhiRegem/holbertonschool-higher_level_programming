#!/bin/bash
#comment
curl -s --head -X OPTIONS "$1" | grep "Allow:" | cut -d':' -f2 | sed 's/^ *//g'
