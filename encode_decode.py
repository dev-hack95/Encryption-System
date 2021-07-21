encryption={'a':'c',
            'b':'v',
            'c':'+',
            'd':'x',
            'e':'2',
            'f':'>',
            'g':'-',
            'h':'?',
            'i':'K',
            'j':'A',
            'k':'{',
            'l':'!',
            'm':'%',
            'n':'(',
            'o':'S',
            'p':'P',
            'q':'<',
            'r':'~',
            's':']',
            't':'L',
            'u':'|',
            'v':'Q',
            'w':'.',
            'x':'&',
            'y':'#',
            'z':'Z',
            ' ':' ',
            ':':'8',
            '.':'}',
            '\n':'7',
            '\\':'3',
            '1':'V',
            '@':')'}
#You can add your extra key and values for this encryption 

def encode(str, encryption):
    
    result = ""
    for c in str:
        result =  result + encryption[c]
    return result

def decode(str, encryption):
    
    return encode(str, invert(encryption))

def invert(encryption):
    
    result = {}
    for key,value in encryption.items():
        result[value] = key
    return result

resp = input("""\nEnter the operation that do you want to peform
                1)Write and encode
                2)Encode
                3)Decode
                4)Exit
>> """)

if resp == '1':
    file = open(input("Enter_filename: "),"w+")
    text=input("Enter_data: ").lower()
    x=encode(text, encryption)
    file.write(x)
    file.close()

elif resp == '2':
    file = open(input("Enter_filename: "), "r+")
    text = file.read()
    x = encode(text.lower(),encryption)
    file.seek(0)
    file.truncate()
    file.write(x)
    file.close()
elif resp == '3':
    file = open(input("Enter_filename: "), "r+")
    text = file.read()
    y=decode(text.strip("\n"),encryption)
    file.seek(0)
    file.truncate()
    file.write(y)
    file.close()

elif resp == '4':
    quit()
else:
    quit()
