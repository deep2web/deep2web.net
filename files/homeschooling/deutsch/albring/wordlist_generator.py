import itertools

known = '1234'  # bekannte Ziffern

# Liste aller Großbuchstaben des Alphabets plus die Zeichen 'S', 'I', 'W', 'Y', 'G'
zeichen = list('abcdefghijklmnopqrstuvwxyzSIWYG'.upper())

# Erstelle alle zweistelligen Kombinationen
kombinationen = [''.join(k) for k in itertools.product(zeichen, repeat=2)]

# Speichere die Kombinationen in einer Textdatei
with open('kombinationen.txt', 'w') as f:
    for kombination in kombinationen:
        f.write(kombination + known + '\n')
