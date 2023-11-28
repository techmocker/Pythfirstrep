# Aufgabe 5 - Arithmetische Operationen

# Frage 1: Was passiert, wenn ich zwei Variablen ohne Zusatz von Klammern addiere?
# Antwort: Hier werden die Variablen wie Text behandelt und einfach aneinandergereiht.

# Frage 2: Wie behandelt Bash Variablen standardmäßig?
# Antwort: Bash behandelt Variablen standardmäßig wie Text

# Frage 3: Wie kann ich zwei Zahlen in Bash addieren?
# Antwort: Um zwei Zahlen in Bash zu addieren, musst du ihm sagen das es sich um Zahlen handelt.


# Skript zur Addition von zwei Zahlen
if [ $# -ne 2 ]; then
    echo "Gib 2 Zahlen an die zu berechnen werden sollen."
else
    num1="$1"
    num2="$2"
    
    # Überprüfen, ob die Eingaben Zahlen sind
    if [[ $num1 =~ ^[0-9]+$ ]] && [[ $num2 =~ ^[0-9]+$ ]]; then
        sum=$((num1 + num2))
        echo "Ergebnis: $sum"
    else
        echo "Bitte gib nur Zahlen an."
    fi
fi
