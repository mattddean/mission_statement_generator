import random

def expand(s, d):
    if s not in d:
        return s
    exp = getAnExpansion(s, d)
    result = ""
    if isinstance(exp, list):
        for item in exp:
            result += expand(item, d) + " "
    else:
        result = exp
    return result

def getAnExpansion(s, d):
    array = d[s]
    return array[random.randrange(0,len(array), 1)]

dictionary = {
    "S": [["NP", "VP"]],
    "NP": [["N"], ["PRE", "N"]],
    "VP": [["ADV", "VERB_PHRASE_START"], ["VERB_PHRASE_START"]],
    "VERB_PHRASE_START": [["VERB_PHRASE_END"], ["VERB_MOD", "VERB_PHRASE_END"]],
    "VERB_PHRASE_END": [["V", "O"], ["V", "OBJECT_PHRASE"]],
    "OBJECT_PHRASE": [["MOD", "O"], ["O"]],
    "PRE": ["without fail,", "with passion,", "with vigor,", "with resolve,", "without heistation,"],
    "N": ["our employees", "we", "we the people", "our people", "our volunteers"],
    "ADV": ["always", "faithfully", "purposefully", "helpfully", "excellently"],
    "V": ["produce", "attain", "build", "develop", "construct"],
    "VERB_MOD": ["strive to", "help to", "work to", "push to", "press to"],
    "MOD": ["effective", "powerful", "creative", "innovative", "productive"],
    "O": ["results", "outcomes", "change", "balance", "products"]
}

def getMissionStatement():
    random.seed()
    base = expand("S", dictionary)
    separator = " "
    base = separator.join((base.split()))
    return base[0].upper() + base[1:] + "."

def main():
    print(getMissionStatement())

main()