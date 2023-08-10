#!/usr/bin/env python3
# coding:utf-8

# this code sorts a list of words written in ancient greek, without taking into consideration the accents and the breathings.


def is_char_in_range(char, shift=0):
    return 0x1F00 <= ord(char)-shift <= 0x1F0F


def remove_diacritics(w):
    """Removes all the breathings and accents in the word `w`."""
    w = w.lower()
    new_w = ""
    for char in w:
        if is_char_in_range(char) or is_char_in_range(char, 0x80) or ord(char) in range(0x1FB0, 0x1FBD):  # α
            new_w += "α"
        elif is_char_in_range(char, 0x10):  # ε
            new_w += "ε"
        elif is_char_in_range(char, 0x20) or is_char_in_range(char, 0x90) or ord(char) in range(0x1FC2, 0x1FC8) or ord(char) == 0x1FCC:  # η
            new_w += "η"
        elif is_char_in_range(char, 0x30) or ord(char) in range(0x1FD0, 0x1FDD):  # ι
            new_w += "ι"
        elif is_char_in_range(char, 0x40):  # ο
            new_w += "ο"
        elif is_char_in_range(char, 0x50):  # υ
            new_w += "υ"
        elif is_char_in_range(char, 0x60) or is_char_in_range(char, 0xA0) or ord(char) in range(0x1FF0, 0x1FF8) or ord(char) == 0x1FFC:  # ω
            new_w += "ω"
        elif ord(char) in [0x1FE4, 0x1FE5, 0x1FEC]:  # ρ
            new_w += "ρ"
        else:
            new_w += char
    return new_w


with open("vocagrec.txt", "r+", encoding="utf-8") as voca_file:
    voca = voca_file.readlines()

voca = [word for word in voca if "Vocabulaire" not in word and word != "\n"]
voca.sort(key=remove_diacritics)
#  print(voca)

with open("vocagrecOUTPUT.txt", "w+", encoding="utf-8") as voca_file_output:
    voca_file_output.writelines(voca)

