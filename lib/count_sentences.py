#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value = ''):
        self.value = value
    @property
    def value(self):
        return self._value
    @value.setter

    def value(self,value):
        if isinstance(value,str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        if self._value[-1].__contains__("."):
            return True
        else:
            return False
        
    def is_question(self):
        if self._value[-1].__contains__("?"):
            return True
        else:
            return False
        
    def is_exclamation(self):
        if self._value[-1].__contains__("!"):
            return True
        else:
            return False
    def count_sentences(self):
        sentences_ends = r'[.!?](?:\s|$)'
        sentences = re.findall(sentences_ends,self._value)
        return len(sentences)
