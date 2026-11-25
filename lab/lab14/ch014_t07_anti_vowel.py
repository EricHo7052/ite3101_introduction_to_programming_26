def anti_vowel(text):
    vowels = "aeiou"
    for i in text:
        if i.lower() in vowels:
            text = text.replace(i, "")
    return text
