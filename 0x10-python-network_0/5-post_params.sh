#!/bin/bash
# Script to display body of a redirect
curl -s $1 -XPOST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD"
