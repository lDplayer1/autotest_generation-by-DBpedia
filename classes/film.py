from classes.super_class import superclass
import random
from SPARQLWrapper import SPARQLWrapper, JSON

class film(superclass):
    def __init__(self):
        super().__init__()
        self.name = "Film"
        self.filters = {}
        self.opt = "director"
        self.wrongOpt = ""
    def get_name(self):
        return self.name
    def get_filters(self):
        return self.filters
    def get_opt(self):
        return self.opt
