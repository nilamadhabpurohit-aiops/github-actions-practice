#!/bin/bash

echo "Running test"

if [ 2 -eq 3 ]
then
  echo "Test passed"
else
  exit 1
fi