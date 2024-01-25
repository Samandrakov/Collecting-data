from natasha import NamesExtractor, MorphVocab

def extract_names(text):
    morph_vocab = MorphVocab()
    extractor = NamesExtractor(morph_vocab)
    matches = extractor(text)
    names_list = [match.fact.first for match in matches]
    return names_list

# Пример использования
text = "Василий Петрович Мусоргский 1995 год рождения, женат"
names = extract_names(text)
print(names)
