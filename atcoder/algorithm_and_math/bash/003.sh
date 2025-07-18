#!/usr/bin/bash

sum_of_n() {
    local n=$1
    for((i=0;i<n;i++)); do
        n=$((n + i))
    done
    echo "$n"
}