#!/bin/bash
# Comment
curl -sIXGET $1 | grep Content-Length | cut -d" " -f 2
