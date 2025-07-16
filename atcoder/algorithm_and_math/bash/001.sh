#!/bin/bash

add() {
    local a=$1
    local b=$2
    echo $((a + b))
}

fixed_value=5
read user_input
result=$(add $user_input $fixed_value)
echo "${result}"
