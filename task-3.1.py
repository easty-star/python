def my_div(num_1, num_2):
    try:
        num_1, num_2 = float(num_1), float(num_2)
        answer = num_1 / num_2
    except ValueError:
        return 'error', 'Ошибка числа'
    except ZeroDivisionError:
        return 'Деление на ноль!'
    return answer


my_div(input(), input())