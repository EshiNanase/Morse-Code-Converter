from data import morse_dictionary_en


def converter_type():
    converter = input('Would you like to decipher or encrypt your phrase? (en/de)\n')
    if converter != 'en' and converter != 'de':
        print("Sorry, I didn't understand you")
        converter_type()
    return converter


def converter_phrase(converter):
    if converter == 'en':
        return converter_phrase_encrypt()
    return converter_phrase_decipher()


def converter_phrase_encrypt():
    phrase = input("Type your phrase. Please, use only english letters\n")
    if all(x.isalpha() or x.isspace() for x in phrase):
        return phrase
    print("Sorry, your phrase seems to have digits or punctuation marks\n")
    converter_phrase_encrypt()


def converter_phrase_decipher():
    phrase = input("Type your phrase. Please, use only '-' as dashes and '' as dots and separate words with '/'. Like that '*-/-*-'\n")
    if decipher_check(phrase):
        return phrase
    print("Sorry, your phrase seems to have letters, digits or punctuation marks\n")
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
    deciphered_phrase = []
    phrase = phrase.split('/')
    for letter in phrase:
        if letter != '':
            deciphered_phrase += list(morse_dictionary_en.keys())[list(morse_dictionary_en.values()).index(letter)]
    print(deciphered_phrase)


def converter_process_encrypt(phrase):
    encrypted_phrase = ''
    for letter in phrase:
        if letter != ' ':
            encrypted_phrase += morse_dictionary_en[letter.title()] + '/'
    print(encrypted_phrase)


def again():
    question = input('Would you like to use the script again? Type y/n\n')
    if question.lower() == 'y':
        return True
    return False
