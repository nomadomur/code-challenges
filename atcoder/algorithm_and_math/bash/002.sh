#!/usr/bin/bash

# 002 - Sum of 3 Integers
# Ishga tushirish vaqti cheklovi: 1 soniya / Xotira cheklovi: 1024 MiB
# Ball: 1000 ball
# Muammo matni
# 3 ta butun son A1, A2, A3 beriladi.
# A1 + A2 + A3 ni chiqaring.

sum_of_three() {
    local a=$1
    local b=$2
    local c=$3
    echo $((a + b + c))
}

read a b c
result=$(sum_of_three $a $b $c)
echo "${result}"