
def returnNestedKeyValues(inputDict: dict):
    Keys, Values = list(inputDict.keys()), list(inputDict.values())
    i = 0
    while(i < len(Values)):
        if type(Values[i]) == dict:
            nestedKeys, nestedValues = returnNestedKeyValues(Values[i])
            Keys.insert(i+1, nestedKeys)
            Values.pop(i)
            Values.insert(i, nestedValues)
            Values.insert(i, "(%)")
            i += 1
        i += 1
    return Keys, Values


def returnNestedDictionary(keys: list, values: list):
    i = 0
    while(i < len(values)):
        if values[i] == "(%)":
            nestedDict = returnNestedDictionary(keys[i+1], values[i+1])
            keys.pop(i+1)
            values.pop(i)
            values.pop(i)
            values.insert(i, nestedDict)
        i += 1
    return dict(zip(keys, values))
