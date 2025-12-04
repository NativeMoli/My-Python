MORSE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}

MORSE_REV = {v: k for k, v in MORSE.items()}


def text_to_morse(text):
    return " ".join(MORSE[ch] for ch in text.upper() if ch in MORSE)


def morse_to_text(code):
    return "".join(MORSE_REV[s] for s in code.split())


def main():

    assert text_to_morse("SOS") == "... --- ..."
    assert morse_to_text("... --- ...") == "SOS"



if __name__ == "__main__":
    main()
