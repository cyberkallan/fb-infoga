#!/bin/bash

apt-get update && apt-get upgrade -y
apt-get install python -y
echo ""
echo "Done! Now you can run 'pip install requirements.txt' commands."
