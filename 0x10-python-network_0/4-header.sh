#!/bin/bash
# send custom headers to servers
curl -s -H "X-School-User-Id: 98" "$1"
