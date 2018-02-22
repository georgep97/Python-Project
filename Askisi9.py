from __future__ import print_function

text = raw_input("Give brainfuck code: ")

aristera=0
dexia = len(text)-1
data=""
index=0

if aristera < 0:
    aristera = 0
if aristera >= len(text):
    aristera = len(text) - 1
if dexia < 0:
    dexia = 0
if dexia >= len(text):
    dexia = len(text) - 1

pinakas = [0] * 30000
pointer = 0
i = aristera
print ('To metafrasmeno keimeno einai: ', end="")
while i <= dexia:
    s = text[i]
    if s == '>':
        pointer += 1
        if pointer >= len(pinakas):
            pointer = 0
    elif s == '<':
        pointer -= 1
        if pointer < 0:
            pointer = len(pinakas) - 1
    elif s == '+':
        pinakas[pointer] += 1
    elif s == '-':
        pinakas[pointer] -= 1
    elif s == '.':
        print(chr(pinakas[pointer]), end="")
    elif s == ',':
        if index >= 0 and index < len(data):
            pinakas[pointer] = ord(data[index])
            index += 1
        else:
            pinakas[pointer] = 0
    elif s =='[':
        if pinakas[pointer] == 0:
            loop = 1
            while loop > 0:
                i += 1
                c = text[i]
                if c == '[':
                    loop += 1
                elif c == ']':
                    loop -= 1
    elif s == ']':
        loop = 1
        while loop > 0:
            i -= 1
            c = text[i]
            if c == '[':
                loop -= 1
            elif c == ']':
                loop += 1
        i -= 1
    i += 1
