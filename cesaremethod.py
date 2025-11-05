num = int(input())
word = input()

def cipher(num, word):
    text = ''
    for char in word:
        if char.isalpha():
            start = ord('A')
            shifted = (ord(char.upper()) - start + num) % 26 + start
            text += chr(shifted)
        else:
            text += char
    return text

text = cipher(num, word)
print(text)