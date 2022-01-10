#!/bin/bash
#comment
curl -so /dev/null "$1" -w "%{http_code}"
