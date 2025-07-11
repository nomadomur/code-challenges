#!/bin/bash

# Given two integers, X and Y, find their sum, difference, product, and quotient.

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