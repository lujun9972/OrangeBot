#!/bin/bash
source /home/lujun9972/.bashrc
cd /home/lujun9972/github/OrangeBot/
source env/bin/activate
python weather_reporter.py $@
