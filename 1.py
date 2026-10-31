import random
import time


def partition(arr, low, high, ascending):
    pivot = arr[high]  # Вибираємо останній елемент як півоту
    i = low - 1

    for j in range(low, high):
        # Якщо сортуємо за зростанням — шукаємо менші elements, якщо за спаданням — більші
        if (arr[j] <= pivot) if ascending else (arr[j] >= pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high, ascending=True):
    """Метод сортування QuickSort"""
    if low < high:
        p = partition(arr, low, high, ascending)
        quick_sort(arr, low, p - 1, ascending)  # Ліва частина
        quick_sort(arr, p + 1, high, ascending)  # Права частина


def is_sorted(arr, ascending=True):
    """Метод перевірки: повертає True або False"""
    for i in range(len(arr) - 1):
        if ascending and arr[i] > arr[i + 1]:
            return False
        if not ascending and arr[i] < arr[i + 1]:
            return False
    return True


# --- ПЕРЕВІРКА ТА ОЦІНКА ЧАСУ ---
sizes = [1000, 10000, 100000]

for size in sizes:
    # Створюємо масив випадкових дробових чисел
    data = [round(random.uniform(-100, 100), 2) for _ in range(size)]

    # Сортування за зростанням
    arr1 = data.copy()
    t1 = time.time()
    quick_sort(arr1, 0, len(arr1) - 1, ascending=True)
    time_asc = (time.time() - t1) * 1000  # у мілісекундах

    # Сортування за спаданням
    arr2 = data.copy()
    t2 = time.time()
    quick_sort(arr2, 0, len(arr2) - 1, ascending=False)
    time_desc = (time.time() - t2) * 1000

    print(f"Масив {size} елементів:")
    print(f"  За зростанням: {time_asc:.1f} мс | Відсортовано: {is_sorted(arr1, True)}")
    print(f"  За спаданням:  {time_desc:.1f} мс | Відсортовано: {is_sorted(arr2, False)}")
    print("-" * 40)