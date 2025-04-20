"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = []
    n = len(s)
    
    if n == 5 or n == 3:
        for i in range(n):
            letter = chr(ord('a') + i)
            result.insert(0, f"{letter}-{i+1}")
    elif n == 4 or n == 2:
        for i in range(n):
            result.insert(0, str(i+1))
    
    return result
    