from SPARQLWrapper import SPARQLWrapper, JSON
import numpy as np
import pandas as pd
import random
sparql = SPARQLWrapper("http://dbpedia.org/sparql")


def table_generator(classtype):
    """
    参数：自定义的类
    返回：关键字的表和选项
    """
    keyword = classtype.get_name()
    filter_dict = classtype.get_filters()
    option = classtype.opt
    query = f"""
    SELECT ?{keyword} ?{option} WHERE {{
    ?{keyword} rdf:type <http://dbpedia.org/ontology/{keyword}>.
    """
    for filter_key, filter_value in filter_dict.items():
        if filter_key.find('undefined') < 0:
            query += f"""
            ?{keyword} <http://dbpedia.org/ontology/{filter_key}> ?{filter_key}.
            """
        query += f""" 
        FILTER {filter_value}
        """
    query += f"""
    OPTIONAL {{?{keyword} <http://dbpedia.org/ontology/{option}> ?{option}.
    }}
    }}
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    quiz_dict = {}
    ## 字典中，key是问题主题，值是正确答案
    for result in results["results"]["bindings"]:
        quizText = result[keyword]["value"].split("/")[-1].replace("_", " ")
        if quizText.find("History") >= 0:
            continue
        try:
            rightOpt = result[option]["value"].split("/")[-1].replace("_", " ")
        except KeyError:
            continue
        quiz_dict[quizText] = rightOpt
    return quiz_dict
