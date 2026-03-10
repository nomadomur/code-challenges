#!/bin/bash

# 001 - Print 5+N
# Ishga tushirish vaqti cheklovi: 1 soniya / Xotira cheklovi: 1024 MiB
# Ball: 1000 ball
# Muammo matni
# 5 ta olma bor, N ta mandarin bor.
# Butun son N beriladi, shuning uchun olma va mandarinlarni birgalikda nechta ekanligini chiqaruvchi dastur yarating.

add() {
    local a=$1
    local b=$2
    echo $((a + b))
}

fixed_value=5
read user_input
result=$(add $user_input $fixed_value)
echo "${result}"
