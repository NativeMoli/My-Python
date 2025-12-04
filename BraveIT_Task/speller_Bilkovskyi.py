# speller.py
import sys, re

def speller_Bilkovskyi(text_file, dict_file, output_file="errors.txt"):
    with open(dict_file, encoding="utf-8") as f:
        dictionary = set(line.strip().lower() for line in f if line.strip())

    seen, errors = set(), []

    with open(text_file, encoding="utf-8") as f:
        for line in f:
            for w in line.split():
                w = re.sub(r"'s$", "", w, flags=re.IGNORECASE)
                w = re.sub(r"[^a-zA-Z]", "", w).lower()
                if w and w not in dictionary and w not in seen:
                    errors.append(w)
                    seen.add(w)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(errors))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python speller_Bilkovskyi.py shakepeare.txt dictionary.txt")
        sys.exit(1)
    speller(sys.argv[1], sys.argv[2])
