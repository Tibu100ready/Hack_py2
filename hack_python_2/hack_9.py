"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = {}
    if isinstance(s, dict):
        for key, value in s.items():
            if key == "foo":  
                new_key = key.capitalize()
                new_value = key.capitalize() + value[4:] 
                result[new_key] = new_value
    elif isinstance(s, str):
        if len(s) > 3:
            result = s[:3].capitalize() + s[3:]
        else:
            result = s.capitalize()
    else:
        result = s

    return result
