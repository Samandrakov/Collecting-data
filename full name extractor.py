from yargy import Parser, rule, and_, or_
from yargy.predicates import gram, is_capitalized


from natasha import NamesExtractor, MorphVocab

# Создаем правило для извлечения ФИО
NAME = rule(
    and_(
        gram('Name'),
        is_capitalized()
    ),
    and_(
        gram('Surn'),
        is_capitalized()
    ),
    or_(
        gram('Patr'),
        gram('Surn')
    ).optional()
)

# Используем NamesExtractor из Natasha для извлечения имени
def extract_full_names(text):
    morph_vocab = MorphVocab()
    extractor = NamesExtractor(morph_vocab)
    matches = extractor(text)
    full_names_list = [match.fact for match in matches]
    return full_names_list

# Используем Yargy для извлечения ФИО
def extract_fio_with_yargy(text):
    parser = Parser(NAME)
    matches = list(parser.findall(text))
    fio_list = [' '.join([_.value for _ in match.tokens]) for match in matches]
    return fio_list

# Пример использования
text = "Привет, Анна Ивановна Сидорова! Как ваш день?"
full_names_natasha = extract_full_names(text)
fio_yargy = extract_fio_with_yargy(text)

print("Natasha:", full_names_natasha)
print("Yargy:", fio_yargy)


