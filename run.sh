#!/bin/bash
path=/Neuro/Neuro/src
cd $path
python3.5 server.py > log.out 2>&1 &
