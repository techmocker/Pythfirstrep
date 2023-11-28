#!/bin/bash

name=$1

if [ "$name" = "Mario" ] || [ "$name" = "Luigi" ]; then
    echo "Lets a go!"
elif [ "$name" = "DeinEigenesName" ]; then
    echo "Thats meee!"
else
    echo "Kenn ich nicht!"
fi
