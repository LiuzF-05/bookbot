#counts the words in a file and returns them as an int
def count_words(path):
    with open (path) as f:
        text=f.read()
        split=text.split()
        return len(split)

#counts the individual chars of a file and returns them as a dictionary{}
def count_chars(path):
    with open(path) as f:
        text=f.read()
        lower=text.lower()
        chars={}
        for char in lower:
            if char in chars:
                chars[char]+=1
            elif char not in chars:
                chars[char]=1
    return chars

def sort_on(dict):
    return dict["num"]

def sorting(dict):
    keys=[]
    for char, num in dict.items():
        if char.isalpha():
            keys.append({"char": char, "num": num})
    keys.sort(reverse=True, key=sort_on)
    return keys
