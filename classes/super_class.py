import random

class superclass():
    def __init__(self):
        self.name = None
        self.filters = {}
        self.opt = None
        self.wrongopt = None
    def get_name(self):
        return self.name
    def get_filters(self):
        return self.filters