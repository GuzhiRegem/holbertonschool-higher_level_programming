#!/bin/bash
#comment
curl -sI "$1" | head -n1 | cut -d" " -f2
