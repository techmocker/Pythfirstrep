#!/bin/bash

number1=$1
number2=$2

if [ $number1 -gt $number2 ]; then
    echo "$number1 ist GRÖSSER als $number2."
elif [ $number1 -lt $number2 ]; then
    echo "$number1 ist KLEINER als $number2."
else
    echo "$number1 ist GLEICH $number2."
fi
