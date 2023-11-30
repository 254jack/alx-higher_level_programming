#!/bin/bash
# fun effort in breaking to http protocols on servers
curl -s -L -X PUT -d "user_id=98" -H "Origin: School" 0.0.0.0:5000/catch_me
