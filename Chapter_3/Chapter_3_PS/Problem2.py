letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

a = input("name : ")
b = input("date : ")

print(letter.replace("<|Name|>" , a).replace("<|Date|>" , b))