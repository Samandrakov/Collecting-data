from natasha import NamesExtractor, MorphVocab, AddrExtractor, DatesExtractor
import re
import json

# Входной текст
# text = "Привет, меня зовут Петров Павел ВасиЛьевич , я родился первого января 80 года в Москве в 15:30 или 3:30 а Вася нет, не знаю никакого Васю"
text = input('Введите текст для обработки: ')
# Словарь, в который собираются данные
result_dict = {}
def name_extraction(input_text, dict):
    #Необходимо сохранять текст с заглавными буквами иначе может не распознать ФИО
    morph_vocab = MorphVocab()
    extractor = NamesExtractor(morph_vocab)

    matches = extractor(input_text)
    try:
        i = 1
        for match in matches:

            # if match.fact.first != None:
            if match.fact.first and match.fact.middle is None and match.fact.last is None:
                #Пример вывода Name(first='Павел', last=None, middle=None)

                print(match.fact)
                print(f"1)Имя\n")
                # print(f"first name: {match.fact.first}\n")
                first = match.fact.first
                dict[f'first_{i}'] = first.lower().capitalize()
                i += 1
                pass

            if match.fact.first and match.fact.middle and match.fact.last is None:
                print(f"2)ФИ")
                # print(f"\nfirst name: {match.fact.first} \nmiddle name: {match.fact.middle}\n")
                first = match.fact.first
                middle = match.fact.middle.lower().capitalize()
                dict[f'first_{i}'] = first.lower().capitalize()
                dict[f'middle_{i}'] = middle.lower().capitalize()
                i += 1
                pass

            if match.fact.first and match.fact.middle and match.fact.last:
                print(f"3)ФИО\n")
                # print(f"first name: {match.fact.first} \nmiddle name: {match.fact.middle} \nlast name: {match.fact.last}\n")
                first = match.fact.first
                middle = match.fact.middle
                last = match.fact.last
                dict[f'first_{i}'] = first.lower().capitalize()
                dict[f'middle_{i}'] = middle.lower().capitalize()
                dict[f'last_{i}'] = last.lower().capitalize()
                i += 1
                pass

            else:
                pass
                # print('False data')
    except Exception as e:
        print("Error in name extraction")
    # print(dict)

name_extraction(text, result_dict)

def city_extraction(input_text, dict):

    morph_vocab = MorphVocab()
    extractor = AddrExtractor(morph_vocab)
    matches = extractor(input_text)

    # Выводим результаты
    for match in matches:
        try:
            i = 1
            if match.fact.value != None:
                #Пример вывода AddrPart(value='Москве', type=None)
                # print(match.fact)
                dict[f'location_{i}'] = match.fact.value
            else:
                pass
        except Exception as e:
            print("Error in city extraction")

    # print(dict)

city_extraction(text, result_dict)

def date_extraction(input_text, dict):
    input_text = input_text.lower()
    date_pattern = re.compile(r'\b(?:\d{2}[./]\d{2}[./]\d{4}|\d{4}-\d{2}-\d{2}|\d{1,2} '
                              r'(?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря) '
                              r'\d{4}|\b(?:первого|второго|третьего|четвертого|пятого|шестого|седьмого|восьмого|девятого|'
                              r'десятого|одинадцатого|двенадцатого|тринадцатого|четырнадцатого|пятнадцатого|шестнадцатого|'
                              r'семнадцатого|восемнадцатого|девятнадцатого||\d{1,2}) '
                              r'(?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря) '
                              r'(?:\d{2}|двадцатого) года\b|\d{2}[./]\d{2}[./]\d{2})')

    dates_found = re.findall(date_pattern, input_text)

    # print(dates_found)
    i = 0
    j = 0
    try:
        for date in dates_found:
            i += 1
            dict[f'date_{i}']= dates_found[j]
            j += 1
        # print(dict)
    except Exception as e:
        print("Error in date extraction")

date_extraction(text, result_dict)

def time_extraction(input_text, dict):
    time_pattern = re.compile(r'\b(?:2[0-3]|[01]?\d)(?::[0-5]?\d)?\b')





    times_found = re.findall(time_pattern, input_text)

    i = 0
    j = 0
    try:
        for date in times_found:
            i += 1
            dict[f'time_{i}']= times_found[j]
            j += 1
        # print(dict)
    except Exception as e:
        print("Error in date extraction")

time_extraction(text, result_dict)

json_data = json.dumps(result_dict, ensure_ascii=False)

print(f"Json: {json_data}")




