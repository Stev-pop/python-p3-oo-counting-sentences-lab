#!/usr/bin/env python3

class MyString:

    def __init__(self, value=""):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, tested_word):
        if isinstance(tested_word, str):
            self._value = tested_word
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        value = self.value
        for marker in ['?', '!']:
            value = value.replace(marker, '.')
        
        sentences = [s for s in value.split('.') if s]
        
        return len(sentences)
