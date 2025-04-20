"""
generic script

text: "fooziman" output => "fo-zi-an" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    result = []
    if len(s) > 3:
        result.append(s[0:2]) 
        result.append("-")     
        result.append(s[3:5])  
        result.append("-")      
    if len(s) > 5:
        result.append(s[6:8]) 
    if len(s) == 3:
        result.append(s[0:2])
        result.append("-") 
    elif len(s) <= 2:
        return s              

    return "".join(result)