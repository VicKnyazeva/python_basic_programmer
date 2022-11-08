# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

from string import punctuation

pattern = "абв"


def output_word(outpit_file, text):
    skip = text.find(pattern) >= 0
    if not skip:
        outpit_file.write(text)


with open("in.txt", "r", encoding="utf-8") as file:
    data = str(file.read())
    with open("out.txt", "w", encoding="utf-8") as outpit_file:
        cp = 0  # текущая позиция в тексте
        sp = -1  # позиция последнего пробела или знака препинания
        wp = -1
        for w in data:
            if w.isspace() or any(p in w for p in punctuation):
                if cp - sp > 1:  # накопилось слово?
                    word = data[sp + 1: cp]
                    output_word(outpit_file, word)
                sp = cp
            else:
                if cp - wp > 1:   # накопились промежутки?
                    outpit_file.write(data[wp + 1: cp])
                wp = cp

            cp += 1

        if cp - sp > 1:  # накопилось слово?
            word = data[sp + 1: cp]
            output_word(outpit_file, word)
        if cp - wp > 1:  # накопились промежутки?
            outpit_file.write(data[wp + 1: cp])
