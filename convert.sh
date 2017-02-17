#!/bin/bash

src=$1
dst=$2

ffmpeg -i $1 -q:a 0 -q:v 0 -strict -2 $dst
