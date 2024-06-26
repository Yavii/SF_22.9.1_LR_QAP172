# Функция проверки корректности ввода пользователем
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# Функция сортировки списка методом вставок
def sort_by_asc(list_array):
    for i in range(1, len(list_array)):
        x = list_array[i]
        idx = i
        while idx > 0 and list_array[idx - 1] > x:
            list_array[idx] = list_array[idx - 1]
            idx -= 1
        list_array[idx] = x
    return list_array

# Функция двоичного поиска
def binary_search(array, x):
    low = -1
    high = len(array)

    while high - low > 1:
        mid = (high + low) // 2
        if array[mid] < x:
            low = mid
        else:
            high = mid

    return high


# Ввод последовательности чисел и числа для поиска позиции
sequence = input("Введите последовательность чисел через пробел: ")
number_to_find = input("Введите число для поиска позиции в списке: ")
numbers = sequence.split()

# Проверка на корректность ввода числовых данных
all_numbers = all(is_number(num) for num in numbers)
entered_value = is_number(number_to_find)
if all_numbers and entered_value:
    print("Все введенные значения являются числами.")
elif (not all_numbers) or (not entered_value):
    print("Ошибочный ввод. Для работы программы требуется ввод чисел.")

# Выполнение основных функция программы, если все элементы - числа
if all_numbers and entered_value:
    numbers = list(map(int, numbers))
    print("Преобразованная в список последовательность чисел: ", numbers)
    sort_numbers = sort_by_asc(numbers)
    print("Отсортированный по возрастанию элементов список:", sort_numbers)
    number_to_find = int(number_to_find)
    position = binary_search(sort_numbers, number_to_find)
    if position < len(sort_numbers) and sort_numbers[position] >= number_to_find:
        print(
            f"Номер позиции элемента, который меньше {number_to_find}, а следующий за ним больше или равен: {position}")
    else:
        print(f"Все элементы меньше {number_to_find}.")
