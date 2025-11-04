def word_count(w):
    words = len(w.split())
    return words

def character_count(c):
    characterCount = {}
    lower_string = c.lower()
    for a in lower_string:
        if a in characterCount:
            characterCount[a] = characterCount[a] + 1
        else:
            characterCount[a] = 1
    return characterCount

'''
def create_dict(dictCount):
    result = []
    for d in dictCount:
        print(type(result))           # should be <class 'dict'>
        print(len(result))            # how many entries?
    return dictCount["num"]
'''
def sort_on(d):
    return d["num"]

def character_sort(counts):
    items = []
    for ch, cnt in counts.items():
        items.append({"char": ch, "num": cnt})
    # you'll sort items next
    items.sort(reverse=True, key=sort_on)
    return items


 
 



