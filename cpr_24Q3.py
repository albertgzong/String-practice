def trim_abc(string):
    lookup = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for char in string:
        if lookup.find(char) != -1 or lookup.upper().find(char) != -1:
            continue
        else:
            result += char
    
    if result.find(".") == -1 and result != "":
        return f"{result}.00"
    elif result == "":
        return result
    else:
        return f"{float(result):.2f}"
    
string1 = "abCDef123.4567"
string2 = "ghijk47.2"
string3 = "lMN158"
string4 = "834.194"
string5 = "bahookey"

print(trim_abc(string1))
print(trim_abc(string2))
print(trim_abc(string3))
print(trim_abc(string4))
print(trim_abc(string5))