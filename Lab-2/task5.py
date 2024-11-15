from collections import defaultdict
import math

def calculate_conditional_probabilities_unicode(text):
    # Подсчёт частоты пар символов
    count_pairs = defaultdict(lambda: defaultdict(int))
    count_single = defaultdict(int)
    
    for i in range(len(text) - 1):
        aj = text[i]
        ak = text[i + 1]
        count_pairs[aj][ak] += 1
        count_single[aj] += 1
    
    # Последний символ не участвует в паре
    count_single[text[-1]] += 1

    # Условные вероятности P(ak|aj)
    conditional_probabilities = defaultdict(dict)
    for aj in count_pairs:
        for ak in count_pairs[aj]:
            conditional_probabilities[aj][ak] = count_pairs[aj][ak] / count_single[aj]
    
    return conditional_probabilities, count_single

def calculate_total_information_unicode(text):
    # Вычисляем условные вероятности и частоты
    conditional_probabilities, count_single = calculate_conditional_probabilities_unicode(text)

    # Общая длина текста
    total_symbols = len(text)
    
    total_info_bits = 0
    for aj in conditional_probabilities:
        for ak in conditional_probabilities[aj]:
            p_ak_aj = conditional_probabilities[aj][ak]
            if p_ak_aj > 0:
                total_info_bits += count_single[aj] * (-p_ak_aj * math.log2(p_ak_aj))

    # Нормализуем информацию на размер текста
    total_info_bits /= total_symbols
    
    return total_info_bits

# Пример использования с Unicode текстом
text = "абв\nабв\t😊"
total_info_bits = calculate_total_information_unicode(text)
total_info_bytes = total_info_bits / 8

# Печатаем результат
print(f"Суммарное количество информации в файле: {total_info_bits:.2f} бит")
print(f"Количество информации в байтах: {total_info_bytes:.2f} байт")
