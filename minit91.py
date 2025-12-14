
'''print ("welcome to minit decode/encoder (idk how to name this program btw)" )
print ("print [enc] for encoding and [dec] for decoding message" )
print ("example: dec [input]")'''

#decoding things
enc = {'a':'1','b':'a','c':'7','d':'*','e':'2','f':'|','g':'+','h':'q',
'i':'i','j':'s','k':'<','l':'z', 'm':'?','n':'N','o':'c', 'p':'~', 
'q':'x', 'r':'4', 's':'6', 't':'d', 'u':'0', 'v':'8', 'w':'>', 'x':',', 'y':'!',
'z':'@', ' ':'_', '.':'=', ',':'%',
'1':'#', '2':'$', '3':'^','4':'`','5':'&', '6':'/', '7':'*', '8':'(', '9':'+',
'-':'"', '/':'¼','*':'{', ':':';'}
dec = {v:k for k,v in enc.items()}

def encrypt(text):
    return ''.join(enc.get(ch, '?') for ch in text)  # '?' для незаданных букв
    
def decrypt(cipher):
    return ''.join(dec.get(ch, '?') for ch in cipher)

'''while True:
    try:
        line = input("<@minit91> $ ")
    except KeyboardInterrupt:
        print("\nexit")
        break
    if not line:
        continue
    
    mode, *text = line.split(maxsplit=1)
    text = text[0] if text else ""
    text = text.lower()
# искал медь if else if else
    if mode == "enc":
        print(encrypt(text))
    elif mode == "dec":
        print(decrypt(text))'''
