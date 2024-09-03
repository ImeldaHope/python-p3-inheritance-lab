#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        self.knowledge = []
        super().__init__(first_name, last_name)
    def learn(self, string_value):
        self.knowledge.append(string_value)