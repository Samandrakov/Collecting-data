from natasha import DatesExtractor, MorphVocab

text = "Завтра будет 25 января 2024 года, а послезавтра - 26.01.24"

morph_vocab = MorphVocab()
extractor = DatesExtractor(morph_vocab)

matches = extractor(text)

date_list = [match.fact.as_json for match in matches]

print(date_list)
