#!/bin/bash
# usage: build2.sh <game>   (builds with common + juice + generated place art)
T=${TWEEGO_HOME:-$HOME/tweego-home}
G=/home/claude/unsolved-crimes/games
export TWEEGO_PATH=$T/tweego/storyformats
g=$1
if [ "$g" = "the-missing-smile" ]; then
  src="$G/the-missing-smile.twee"; out="$G/the-missing-smile.html"; places="$G/places/the-missing-smile.places.twee"
else
  src="$G/common/common.twee $G/$g/$g.twee"; out="$G/$g/$g.html"; places="$G/places/$g.places.twee"
fi
[ -f "$places" ] || places=""
$T/tweego/tweego -o $out $src $G/common/juice.twee $places
