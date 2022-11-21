from data import morse_dictionary_ru


def converter_type():
    converter = input('Вы хотите зашифровать или расшифровать ваш текст? (en/de)\n')
    if converter != 'en' and converter != 'de':
        print("Простите, я вас не понял")
        converter_type()
    return converter


def converter_phrase(converter):
    if converter == 'en':
        return converter_phrase_encrypt()
    return converter_phrase_decipher()


def converter_phrase_encrypt():
    phrase = input('Напишите вашу фразу. Пожалуйста, используйте только русские буквы\n')
    if all(x.isalpha() or x.isspace() for x in phrase):
        return phrase
    print("Простите, в вашей фразе присутствуют цифры или знаки препинания\n")
    converter_phrase_encrypt()


def converter_phrase_decipher():
    phrase = input("Напишите вашу фразу. Пожалуйста, используйте только '-' в качестве тире и '*' в качестве точек и разделите слова с помощью '/'. Пример: '*-/-*-'\n")
    if decipher_check(phrase):
        return phrase
    print("Простите, в вашей фразе присутствуют цифры или знаки препинания\n")
    converter_phrase_decipher()


def decipher_check(phrase):
    symbols = ["-", "*", "/"]
    for letter in phrase:
        if letter not in symbols:
            return False
    return True


def converter_process(converter, phrase):
    if converter == 'de':
        return converter_process_decipher(phrase)
    return converter_process_encrypt(phrase)


def converter_process_decipher(phrase):
    deciphered_phrase = ''
    phrase = phrase.split('/')
    for letter in phrase:
        if letter != '':
            deciphered_phrase += list(morse_dictionary_ru.keys())[list(morse_dictionary_ru.values()).index(letter)]
    print(deciphered_phrase)


def converter_process_encrypt(phrase):
    encrypted_phrase = ''
    for letter in phrase:
        if letter != ' ':
            encrypted_phrase += morse_dictionary_ru[letter.title()] + '/'
    print(encrypted_phrase)


def again():
    question = input('Хотите запустить скрипт еще раз? Напишите да/нет\n')
    if question.lower() == 'да':
        return True
    return False
