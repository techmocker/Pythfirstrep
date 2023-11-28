#!/bin/bash

# nur 4 Argumente erlaubt
if [ $# -ne 4 ]; then
    echo "Nur 4 Zahlen erlaubt."
    exit 1
fi

# Argumente aufteilen
num1=$1
num2=$2
num3=$3
num4=$4

# Vergleich und Sortierung
if [ $num1 -le $num2 ] && [ $num1 -le $num3 ] && [ $num1 -le $num4 ]; then
    smallest=$num1
    if [ $num2 -le $num3 ] && [ $num2 -le $num4 ]; then
        second=$num2
        if [ $num3 -le $num4 ]; then
            third=$num3
            largest=$num4
        else
            third=$num4
            largest=$num3
        fi
    elif [ $num3 -le $num2 ] && [ $num3 -le $num4 ]; then
        second=$num3
        if [ $num2 -le $num4 ]; then
            third=$num2
            largest=$num4
        else
            third=$num4
            largest=$num2
        fi
    else
        second=$num4
        third=$num2
        largest=$num3
    fi
fi

# Ausgabe der Zahlen
echo "Sortierte Zahlen: $smallest $second $third $largest"
