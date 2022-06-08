#!/bin/bash
scoreB=0
scoreR=0
for i in {1..10}; do
    python3 paintwars.py > log.txt
    tmp=$(grep "Team Blue " log.txt | sed s/"^.*: "//)
    let "scoreB = scoreB + tmp"
    tmp=$(grep "Team Red " log.txt | sed s/"^.*: "//)
    let "scoreR = scoreR + tmp"
done
let "scoreB = scoreB / 10"
let "scoreR = scoreR / 10"
echo "Score Red $scoreR"
echo "Score Blue $scoreB"