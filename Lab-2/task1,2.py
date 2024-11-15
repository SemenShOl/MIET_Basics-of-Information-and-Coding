import os
import math
from collections import Counter, OrderedDict

def read_file(filepath):
    with open(filepath, "rb") as f:
        return f.read()

def read_file_utf(filepath, encoding="utf-8"):
    with open(filepath, "r", encoding=encoding) as f:
        return f.read()

def calculate_probabilities_and_info(counts, total_symbols):
    probabilities = {}
    info_content = {}
    for byte, count in counts.items():
        p = count / total_symbols
        probabilities[byte] = p
        if p > 0:
            info_content[byte] = -math.log2(p)
    return probabilities, info_content

def calculate_total_information(info_content, counts):
    total_info = 0
    for byte, info in info_content.items():
        total_info += info * counts[byte]
    return total_info

def analyze_file(filepath):
    data = read_file(filepath)
    total_symbols = len(data)
    counts = Counter(data)
    
    probabilities, info_content = calculate_probabilities_and_info(counts, total_symbols)
    total_info_bits = calculate_total_information(info_content, counts)

    for octet, count in Counter(data).items():
        print(f"Символ: {hex(octet):<4}, Количество вхождений: {count:<6} | Количество информации: {info_content[octet]:<10.2f} | Вероятность: {probabilities[octet]:<20.5f}")

    data_by_count_d = [(l,k) for k,l in sorted([(j,i) for i,j in Counter(data).items()],reverse=True)]
    print("\nСимволы по количеству вхождений:")
    for octet, count in data_by_count_d:
        print(f"Символ: {hex(octet):<4}, Количество вхождений: {count:<6} | Количество информации: {info_content[octet]:<10.2f} | Вероятность: {probabilities[octet]:<20.5f}")

    print(f"\nДлина файла в символах: {total_symbols}")
    print(f"Длина файла в битах: {total_symbols * 8}")
    print(f"Суммарное количество информации в битах: {total_info_bits:.2f}")
    print(f"Суммарное количество информации в октетах: {total_info_bits / 8:.2f}")
    
    E = math.ceil(total_info_bits / 8)
    G64 = E + 256 * 8
    G8 = E + 256 * 1
    print(f"Оценка минимальной длины сжатого файла: {E} октетов")
    print(f"Оценка длины архива G64: {G64} октетов")
    print(f"Оценка длины архива G8: {G8} октетов")

def analyze_file_unicode(filepath, encoding="utf-8"):
    data = read_file_utf(filepath)
    total_symbols = len(data)
    counts = Counter(data)
    
    probabilities, info_content = calculate_probabilities_and_info(counts, total_symbols)
    total_info_bits = calculate_total_information(info_content, counts)

    print(f"Длина файла в символах Unicode: {total_symbols}")
    print(f"Длина файла в битах: {total_symbols * 8}")
    print(f"Суммарное количество информации в битах: {total_info_bits:.2f}")
    print(f"Суммарное количество информации в октетах: {total_info_bits / 8:.2f}")
    
    E = math.ceil(total_info_bits / 8)
    G64 = E + 64 + len(counts) * 64
    G8 = E + 64 + len(counts) * 8
    
    print(f"Оценка минимальной длины сжатого файла: {E} октетов")
    print(f"Оценка длины архива G64: {G64} октетов")
    print(f"Оценка длины архива G8: {G8} октетов")

def task1():
    analyze_file(f'sources/tasks_1,2/abcd.txt')
    # for filename in os.listdir("sources/tasks_1,2/"):
    #     if (filename != "Example1.txt"):
    #         print(f'\nfile: {filename}')
    #         analyze_file(f'sources/tasks_1,2/{filename}')

def task2():
    print('\n\nСравнение файла Example1.txt')
    analyze_file(f'sources/tasks_1,2/Example1.txt')
    print('\nUnicode:')
    analyze_file_unicode(f'sources/tasks_1,2/Example1.txt')

task1()
# task2()