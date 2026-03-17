#!/bin/bash

echo "Running tests"

python -m py_compile app.py

if [ $? -eq 0 ]
then
 echo "Tests passed"
else
 exit 1
fi