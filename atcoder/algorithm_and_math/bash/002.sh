#!/usr/bin/bash

sum_of_three() {
    local a=$1
    local b=$2
    local c=$3
    echo $((a + b + c))
}

read a b c
result=$(sum_of_three $a $b $c)
echo "${result}"