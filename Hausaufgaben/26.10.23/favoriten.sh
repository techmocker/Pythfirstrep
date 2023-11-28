#!/bin/bash

# Aufgabe 3 - Variablen

# Frage 1
echo -e "\e[32mBitte geben Sie Ihr Lieblingsessen ein:\e[0m"
read favFood

# Frage 2
echo -e "\e[32mBitte geben Sie Ihr Lieblingstier ein:\e[0m"
read favAnimal

# Frage 3
echo -e "\e[32mBitte geben Sie Ihr Lieblingsland ein:\e[0m"
read favCountry

# Frage 4
echo -e "\e[32mBitte geben Sie Ihre Lieblingsstadt ein:\e[0m"
read favCity

# Antworten Ausgabe
echo -e "Lieblingsessen: \e[32m$favFood\e[0m"
echo -e "Lieblingstier: \e[32m$favAnimal\e[0m"
echo -e "Lieblingsland: \e[32m$favCountry\e[0m"
echo -e "Lieblingsstadt: \e[32m$favCity\e[0m"
