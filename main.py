import ru
import en


def process():
    language = input("Choose your language/Выберите свой язык (en/ru)\n")
    if language == 'en':
        process_en()
    elif language == 'ru':
        process_ru()
    else:
        print("Sorry, I don't recognize your language/Простите, не знаю такого языка")
        process()


def process_ru():
    converter = ru.converter_type()
    phrase = ru.converter_phrase(converter)
    ru.converter_process(converter, phrase)
    if ru.again():
        process()


def process_en():
    converter = en.converter_type()
    phrase = en.converter_phrase(converter)
    en.converter_process(converter, phrase)
    if en.again():
        process()


process()
