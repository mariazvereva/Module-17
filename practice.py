numbers = list(input("Введите последовательность чисел через пробел ").split()) # преобразование в список
numbers = [int(x) for x in numbers] #преобразование списка в список чисел
y = int(input("Введите любое число 'y', находящееся в диапазоне последовательности "))

for i in range(1, len(numbers)): #сортировка списка по методу вставок
    x = numbers[i]
    idx = i
    while idx > 0 and numbers[idx - 1] > x:
        numbers[idx] = numbers[idx - 1]
        idx -= 1
        numbers[idx] = x
print ("Упорядоченный по возрастанию список:", numbers)


if y!=min(numbers) and y!=max(numbers):
    def binary_search(numbers, y):  # поиск номера позиции элемента перед "y"
        if y < numbers[0] or y > numbers[-1]:
            return "Элемент 'y' отсутствует в диапазоне введенных в последовательности чисел"
        left = 0
        right = len(numbers)
        while left < right - 1:
            middle = (right + left) // 2
            if y > numbers[middle]:
                left = middle
            else:
                right = middle
        return left
    print("Номер позиции элемента перед заданным числом 'y' -", binary_search(numbers, y))
else:
    print ("Элемент 'y' равен минимальному/максимальному значению в заданной последовательности чисел")





