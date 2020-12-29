goods = []
const = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
constant = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    if input('Чтобы завершить нажмите "Q", \n"Enter", чтобы продолжить: ').lower() == 'q':
        break
    num += 1
    for i in const.keys():
        answer = input(f'{i}: ')
        const[i] = int(answer) if (i == 'цена' or i == 'количество') else answer
        constant[i].append(const[i])
    goods.append((num, const.copy()))
    print('Аналитика по товарам:')
    for key, value in constant.items():
        print(key, value)

