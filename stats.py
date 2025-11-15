def get_num_words(n):
    with open(n,'r') as f:
        n=f.read().split()
        i=0
        for _ in n:
            i=i+1
        
    return i

def r_dict(n):
    with open(n,'r') as f:
        n=f.read().split()
    s={}
    for word in n:
        word=word.lower()
        for letter in word:
            if letter not in s:
                s[letter]=0
            s[letter]=s[letter]+1
    return s 
