#!/bin/bash

# Überprüfen, ob genau 4 Argumente übergeben wurden
if [ "$#" -ne 4 ]; then
    echo "Nur 4 Argumente: Lieblingsessen, Lieblingstier, Lieblingsland und Lieblingsstadt."
    exit 1
fi

# Die Argumente als Variablen zuweisen
favFood="$1"
favAnimal="$2"
favCountry="$3"
favCity="$4"

# Ausgabe der Variablen
echo "Lieblingsessen: $favFood"
echo "Lieblingstier: $favAnimal"
echo "Lieblingsland: $favCountry"
echo "Lieblingsstadt: $favCity"

# Ausgabe der Anzahl aller Argumente
echo "Anzahl der Argumente: $#"
