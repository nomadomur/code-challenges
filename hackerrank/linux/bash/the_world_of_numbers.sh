#!/bin/bash

# Ikki butun son berilgan, X va Y, ularning yig'indisini, ayirmasini, ko'paytmasini va bo'linmasini toping.
read -r X
read -r Y

sum=$((X + Y))
diff=$((X - Y))
prod=$((X * Y))
quot=$((X / Y))

echo "$sum"
echo "$diff"
echo "$prod"
echo "$quot"