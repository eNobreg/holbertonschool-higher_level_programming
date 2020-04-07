#!/bin/bash
# Comment
curl -sIXGET $1 | grep Allow | cut -d" " -f 2
