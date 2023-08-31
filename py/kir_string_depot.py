#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 15:10:18 2023

@author: doreen nixdorf
"""

import os


class ResourceNames:
    """pathames for resource files
    """
    def __init__(self):
        self.root = "/".join(os.getcwd().split("/")[:-1])
        self.fn_corpuslist = self.root+"/resources/verzeichnis.txt"
        self.fn_namedentities = self.root+"/resources/extern.csv"
        self.fn_freqfett = self.root+"/resources/freq_fett.csv"
        self.fn_db = self.root+"/resources/db_kirundi.csv"
        self.fn_dates = self.root+"/resources/dates.txt"
        self.dir_tagged = self.root+"/results/tagged/"
        self.dir_searched = self.root+"/results/searched/"



# welche charSets funktionieren evtl
encodings = [
    #"ascii",
    #"big5",
    #"big5hkscs",
    #"cp037",
    #"cp424",
    #"cp437",
    #"cp500",
    #"cp720",
    #"cp737",
    #"cp775",
    #"cp850",
    #"cp852",
    #"cp855",
    #"cp856",
    #"cp857",
    #"cp858",
    #"cp860",
    #"cp861",
    #"cp862",
    #"cp863",
    #"cp864",
    #"cp865",
    #"cp866",
    #"cp869",
    #"cp874",
    #"cp875",
    #"cp932",
    #"cp949",
    #"cp950",
    #"cp1006",
    #"cp1026",
    #"cp1140",
    #"cp1250",
    #"cp1251",
    #"cp1252",
    #"cp1253",
    #"cp1254",
    #"cp1255",
    #"cp1256",
    #"cp1257",
    #"cp1258",
    #"euc_jp",
    #"euc_jis_2004",
    #"euc_jisx0213",
    #"euc_kr",
    #"gb2312",
    #"gbk",
    #"gb18030",
    #"hz",
    #"iso2022_jp",
    #"iso2022_jp_1",
    #"iso2022_jp_2",
    #"iso2022_jp_2004",
    #"iso2022_jp_3",
    #"iso2022_jp_ext",
    #"iso2022_kr",
    #"latin_1",
    #"iso8859_2",
    #"iso8859_3",
    #"iso8859_4",
    #"iso8859_5",
    #"iso8859_6",
    #"iso8859_7",
    #"iso8859_8",
    #"iso8859_9",
    #"iso8859_10",
    #"iso8859_13",
    #"iso8859_14",
    #"iso8859_15",
    #"iso8859_16",
    #"johab",
    #"koi8_r",
    #"koi8_u",
    #"mac_cyrillic",
    #"mac_greek",
    #"mac_iceland",
    #"mac_latin2",
    #"mac_roman",
    #"mac_turkish",
    #"ptcp154",
    #"shift_jis",
    #"shift_jis_2004",
    #"shift_jisx0213",
    #"utf_32",
    #"utf_32_be",
    #"utf_32_le",
    "utf_16",
    #"utf_16_be",
    ##"utf_16_le",
    #"utf_7",
    #"utf_8",
    #"utf_8_sig",
]


class CorpusCategories:
    """categories of corpus from University
    """
    def __init__(self):
        self.cc = [
            '1920s','1940s','1950s','1960s','1970s',\
            '1980s','1990s','2000s','2010s','ORAL','WRITTEN',\
            'Chansons','Poésie','Théâtre','Contes','Romans','Magazines',\
            'Nouvelles','Informations',\
            'Culture_traditionnelle','Éducation','Santé','Société',\
            'Écologie','Paix','Lois','Politique','Histoire','Religion']

class PossibleTags:
    """Part-of-Speech tags the program uses
    """
    def __init__(self):
        self.pt1 = [
             "ADJ", "ADV", "CONJ", "EMAIL","F","INTJ", "NI", "NOUN",
             "NUM", "NUM_ROM","PRON","PROPN","PROPN_CUR","PROPN_LOC","PROPN_NAM",
             "PROPN_ORG","PROPN_PER", "PROPN_REL","PROPN_SCI","PROPN_THG",
             "PROPN_VEG","PREP" ,"SYMBOL", "UNK", "VERB", "WWW"]
        self.pt2 = ",.:!?(){}[]'\""

def first_line_in_pos_collection():
    """headline for lemmafreq.csv
    """
    first_line = "lemma;id;PoS;count;counted forms;forms"
    return first_line

class NounPrepositions:
    """more variants if nouns are written inclusive prepositions without apostrophe
    """
    def __init__(self):
        self.qu_nta = r"([na]ta|[mk]u|s?i)"
        self.qu_ca_vowel = r"([bkmrt]?w|[rv]?y|[nsckzbh])"
        self.qu_ca_konsonant = r"([nckzbh]|[bkmrt]?w|[rv]?y)[ao]"


def punctuation():
    """returns string of punctuationmarks etc.
    does not include currency signs
    """
    return ',.;:!?(){}[]\'"´`#%&+-*/<=>@\\^°_|~'

def sortletter(letter):
    """returns True, False, vowel or 'not in use'
    """
    #iki
    if letter in "bdgjlmnrvwyz":
        return "weak_consonant"
    #igi
    if letter in "cfhkpst":
        return "hard_consonant"
    #ic
    if letter in "aeiou":
        return "vowel"
    #foreign qx
    return "not_in_use"

def breakdown_consonants(mystring) :
    """returns changed consonants in case of some combinations of letters
    """
    for i in range(len(mystring)-1) :
        if mystring[i] == "n" :
            if mystring[i+1] in r"[bpvf]" :
                mystring =mystring.replace(mystring[i],"m")
    mystring = mystring.replace("nr","nd").replace("nh","mp").replace("mh","mp")\
        .replace("nn","n").replace(r"[nm]m","m")
    return mystring


class Search:
    """query and filenames for result, frequency distributions and tagged text
    """
    def __init__(self, fn_in, multiple = False):
        self.fn_in = fn_in
        self.multiple = multiple
        self.wtl = ""
        self.nots = ""
        self.questions = ""
        self.short =""
        self.fn_tag = ""
        self.fn_freqlemmac = ""
        self.fn_search = ""
        self.set_fntag()
    def __str__(self):
        return f"wtl={self.wtl}, questions={self.questions}, \
            short={self.short}, fn_tag={self.fn_tag}"
    def __repr__(self):
        return f"wtl={self.wtl}, questions={self.questions}, \
            short={self.short}, fn_tag={self.fn_tag}"

    #f_out = input("Gushingura ifishi rishasha hehe?\n : ")
    def set_fntag(self):
        """set filenames to store tagged file and lemma frequency distribution
        for lemmafreq still undecided if csv or json
        """
        root_tagg = ResourceNames().dir_tagged
        myname = self.fn_in.split("/")[-1]
        # TODO check if f_in is json or txt
        short = myname.find(".")
        self.short = myname[:short]
        self.fn_tag= root_tagg+"tag__"+self.short+".json"
        self.fn_freqlemmac = root_tagg+"fl__"+self.short+".csv"
    def set_search(self, wtl,nots,questions) :
        """combine filename of analysed file and search-questions for making 
        a filename to store the search results
        """
        self.wtl = wtl
        self.nots = nots
        self.questions = questions
        search = ""
        for i, quest in enumerate(self.questions) :
            if nots[i] =="!":
                search += "!"+quest+"_"
            else:
                search += quest+"_"
        self.fn_search = ResourceNames().dir_searched+self.short+"__"+search+".txt"


# TODO check with TextMeta.set_corpuscategories
#Achtung: "Culture traditionnelle" und "Culture traditionelle"
# 1. Schreibfehler, 2. Leerzeichen im Begriff !
def collect_corpuscategories() :
    """collects different parts of pathnames of kirundi corpus as a list
    """
    paths_list = ResourceNames().fn_corpuslist
    categories = []
    for i in paths_list :
        elements = i.split("/")
        for element in elements[:-1]:
            if element.strip() not in categories :
                categories.append(element)
    for uninteresting in ["Constantin","Ernest","Ferdinand","Doreen"\
                          "Manoah","Yvette","G-MdS"]:
        categories.remove(uninteresting)
    return categories
