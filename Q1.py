given = "This is a cool sentence"


def length_sorting(given):
    words_split = given.split()  #splitting the text 
    in_order = sorted(words_split, key=len) #sorting with length
    return ' '.join(in_order)#return sends the whole string as the output when this fn is called.
    
answer = length_sorting(given)
print(answer)  
#answer should get us "a is this cool sentence"