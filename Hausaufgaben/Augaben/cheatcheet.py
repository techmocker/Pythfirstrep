import tkinter as tk

def show_shortcuts():
    shortcuts = """
    Allgemein:
    - Datei öffnen: Ctrl + O
    - Datei speichern: Ctrl + S
    - Alles speichern: Ctrl + Shift + S
    - Rückgängig machen: Ctrl + Z
    - Wiederholen: Ctrl + Y
    - Kopieren: Ctrl + C
    - Ausschneiden: Ctrl + X
    - Einfügen: Ctrl + V
    - Alles markieren: Ctrl + A
    - Suchen: Ctrl + F
    - Ersetzen: Ctrl + H

    Editor-Navigation:
    - Nächster Tab: Ctrl + Tab
    - Vorheriger Tab: Ctrl + Shift + Tab
    - Nächster Editor: Ctrl + PageDown
    - Vorheriger Editor: Ctrl + PageUp
    - Datei schließen: Ctrl + W

    Code-Bearbeitung:
    - Zeile nach oben/unten verschieben: Alt + ↑/↓
    - Kommentarzeilen ein/ausblenden: Ctrl + /
    - Code formatieren: Shift + Alt + F
    - Schnelle Vorschläge anzeigen: Ctrl + Space
    - Definition anzeigen: F12
    """

    root = tk.Tk()
    root.title("VS Code Tastenkürzel")
    
    text = tk.Text(root, wrap=tk.WORD, width=60, height=20)
    text.insert(tk.END, shortcuts)
    text.pack()

    root.mainloop()

show_shortcuts()
