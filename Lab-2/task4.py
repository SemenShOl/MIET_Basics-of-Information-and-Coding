import collections
import math

# Чтение файла и преобразование содержимого в список байтов
def read_file_as_bytes(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

# Подсчёт вхождений двухсимвольных подстрок и односимвольных вхождений
def count_substrings(data):
    count_pairs = collections.defaultdict(int)
    count_single = collections.defaultdict(int)

    # Проходим по файлу и считаем пары символов
    for i in range(len(data) - 1):
        aj, ak = data[i], data[i + 1]
        count_pairs[(aj, ak)] += 1
        count_single[aj] += 1

    return count_pairs, count_single

# Вычисление условных вероятностей P(ak|aj)
def compute_conditional_probabilities(count_pairs, count_single):
    conditional_probs = {}

    for (aj, ak), pair_count in count_pairs.items():
        if count_single[aj] > 0:
            conditional_probs[(aj, ak)] = pair_count / count_single[aj]

    return conditional_probs

# Вычисление информации Iсм1(Q)
def compute_information_content(data, count_pairs, count_single):
    total_info_bits = 0

    for (aj, ak), pair_count in count_pairs.items():
        if count_single[aj] > 0:
            probability = pair_count / count_single[aj]
            # Информация на паре символов -log2(P(ak|aj))
            info = -math.log2(probability)
            total_info_bits += pair_count * info

    return total_info_bits + 8

def main(filename):
    # data = read_file_as_bytes(filename)
    data = "абв\nабв\t😊"
    # Шаг 1: Подсчёт вхождений подстрок
    count_pairs, count_single = count_substrings(data)

    # Шаг 2: Вычисление условных вероятностей
    conditional_probs = compute_conditional_probabilities(count_pairs, count_single)

    # Шаг 3: Вычисление информации Iсм1(Q)
    total_info_bits = compute_information_content(data, count_pairs, count_single)

    # Печать результатов
    # print(f"Условные вероятности P(ak|aj):")
    # for (aj, ak), prob in conditional_probs.items():
    #     print(f"P({chr(ak)}|{chr(aj)}) = {prob:.4f}")

    print(f"\nСуммарное количество информации в файле: {total_info_bits:.2f} бит")
    print(f"Количество информации в байтах: {total_info_bits / 8:.2f} байт")

if __name__ == "__main__":
    filename = "./sources/task_5/unicode.txt"  # Замените на имя вашего файла
    main(filename)


