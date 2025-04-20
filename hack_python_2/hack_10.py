"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = []
    num = 1
    for item in s:
        new_item = {}
        for _ in item:
            new_item[str(num)] = str(num + 1)
            num += 2
        result.append(new_item)

    return result
