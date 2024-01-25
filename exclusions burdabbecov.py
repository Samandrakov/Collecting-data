from yargy import Parser, rule, and_
from yargy.predicates import gram, is_capitalized

# Создаем правило для извлечения нетипичной фамилии
NON_STANDARD_SURNAME = rule(
    is_capitalized().repeatable(),
    gram('Surn').interpretation('surname')
)

# Используем Yargy для извлечения нетипичных фамилий
def extract_non_standard_surnames(text):
    parser = Parser(NON_STANDARD_SURNAME)
    matches = list(parser.findall(text))
    surnames_list = [match.fact.surname for match in matches]
    return surnames_list

# Пример использования
text = "Привет, Бурдаббеков! Как ваш день?"
non_standard_surnames = extract_non_standard_surnames(text)
print("Non-standard Surnames:", non_standard_surnames)
