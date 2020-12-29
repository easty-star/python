checklist = list(input('Введите текст: '))
for i in range(1, len(checklist), 2):
    checklist[i - 1], checklist[i] = checklist[i], checklist[i - 1]
print(checklist)