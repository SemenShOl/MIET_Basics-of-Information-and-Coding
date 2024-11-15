import os
import chardet
from collections import Counter

def read_file_bytes(filepath):
    with open(filepath, "rb") as f:
        return f.read()

def analyze_octets(filepath):
    data = read_file_bytes(filepath)
    octet_counts = Counter(data)
    most_common_all = octet_counts.most_common(4)
    non_ascii_printable_counts = {octet: count for octet, count in octet_counts.items() if not (0x20 <= octet <= 0x7E)}
    most_common_non_ascii = Counter(non_ascii_printable_counts).most_common(4)
    
    print("4 наиболее частых октета среди всех использованных:")
    for octet, count in most_common_all:
        print(f"Октет: {hex(octet)}, Количество: {count}")
    
    print("\n4 наиболее частых октета, не являющихся кодами печатных символов ASCII:")
    for octet, count in most_common_non_ascii:
        print(f"Октет: {hex(octet)}, Количество: {count}")


def analyze_all_octets(filepath):
    data = read_file_bytes(filepath)
    return dict(Counter(data))


def analyze_text(filepath):
    data = read_file_bytes(filepath)
    encoding = chardet.detect(data)['encoding']
    print(f"Определённая кодировка: {encoding}")
    
    if encoding is None:
        print("Кодировка не распознана.")
        return

    try:
        text = data.decode(encoding)
    except (UnicodeDecodeError, LookupError):
        print(f"Ошибка декодирования файла в кодировке {encoding}.")
        return

    if any(char in "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" for char in text):
        print("Файл содержит русские символы.")
    else:
        print("Файл не содержит русских символов.")


def subtask1():
    print('\n\nЗадание 3 (a)')
    for filename in os.listdir("sources/tasks_3/"):
        if filename.endswith(".txt"): 
            print(f'\nfile: {filename}')
            analyze_octets(f'sources/tasks_3/{filename}')
            continue
        else:
            continue

def subtask2():
    print('\n\nЗадание 3 (b)')
    for octet, count in analyze_all_octets("sources/tasks_3/MyTask.txt").items():
        print(f"Октет: {hex(octet)}, Количество: {count}")

def subtask3():
    print('\n\nЗадание 3 (c)')
    analyze_text("sources/tasks_3/MyTask.txt")


subtask1()
subtask2()
subtask3()