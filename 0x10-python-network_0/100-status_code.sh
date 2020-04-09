#!/bin/bash

curl -os /dev/null -w "%{http_code}" "$1"
