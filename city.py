from natasha import AddrExtractor, MorphVocab

# Создаем экземпляр MorphVocab
morph_vocab = MorphVocab()

# Создаем экземпляр AddrExtractor с использованием MorphVocab
extractor = AddrExtractor(morph_vocab)

# Текст для извлечения адресов
text = "Москва, ул. Тверская, д. 10"

# Извлекаем адреса
matches = extractor(text)

# Выводим результаты
for match in matches:
    print(match.fact)
