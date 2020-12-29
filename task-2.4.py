line = input('Введите текст, через пробел: ')
words = line.split()
for i, word in enumerate(words, 1):
    print(i, word[:10])
