#!/bin/bash
# Script that takes an URL and displays the body of the respons
curl GET -sH "X-School-User-Id: 98" "$1"
