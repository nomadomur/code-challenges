#!/usr/bin/bash

# 003 - Sum of N Integers
# Ishga tushirish vaqti cheklovi: 1 soniya / Xotira cheklovi: 1024 MiB
# Ball: 1000 ball
# Muammo matni
# Butun son N va N ta butun son A1, A2, ⋯, AN beriladi. (Kirish shakli uchun "Kirish" bo'limiga qarang)
# A1 + A2 + ⋯ + AN ni chiqaring.

sum_of_n() {
    local n=$1
    for((i=0;i<n;i++)); do
        n=$((n + i))
    done
    echo "$n"
}