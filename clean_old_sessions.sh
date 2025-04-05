#!/bin/bash

# find /home/kam7il/flask_session/ -type f -mtime +60 -print
find /home/kam7il/flask_session/ -type f -mtime +60 -exec rm -f {} +
