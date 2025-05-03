def crypt(string):
    result = ""
    for char in string:
        if char.isalpha():
            result += chr(ord(char) + 2)
        else:
            result += char
    return result


print(crypt("abcd"))
print(crypt("Hello!"))
