#!/bin/bash

# Ikki butun son berilgan, X va Y, X < Y yoki X > Y yoki X = Y ekanligini aniqlang.
# Quyidagi qatorlardan faqat bittasi:
    # X Y dan kichik
    # X Y dan katta
    # X Y ga teng

read -r X
read -r Y

if [ "$X" -gt "$Y" ]; then
    echo "X is greater than Y"
elif [ "$X" -lt "$Y" ]; then
    echo "X is less than Y"
else
    echo "X is equal to Y"
fi