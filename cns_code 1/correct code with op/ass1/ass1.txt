import string, random

def caesar_encrypt(txt, s):
    r=""
    for c in txt:
        if c.isalpha():
            b=ord('A') if c.isupper() else ord('a')
            r+=chr((ord(c)-b+s)%26+b)
        else:
            r+=c
    return r

def caesar_decrypt(txt, s):
    return caesar_encrypt(txt,-s)

def mono_encrypt(txt,key):
    r=""
    for c in txt:
        if c.upper() in key:
            if c.isupper():
                r+=key[c]
            else:
                r+=key[c.upper()].lower()
        else:
            r+=c
    return r

def mono_decrypt(txt,key):
    rk={v:k for k,v in key.items()}
    r=""
    for c in txt:
        if c.upper() in rk:
            if c.isupper():
                r+=rk[c]
            else:
                r+=rk[c.upper()].lower()
        else:
            r+=c
    return r

def vig_encrypt(txt,key):
    r=""
    key=key.upper()
    j=0
    for c in txt:
        if c.isalpha():
            s=ord(key[j%len(key)])-65
            if c.isupper():
                r+=chr((ord(c)-65+s)%26+65)
            else:
                r+=chr((ord(c.upper())-65+s)%26+65).lower()
            j+=1
        else:
            r+=c
    return r

def vig_decrypt(txt,key):
    r=""
    key=key.upper()
    j=0
    for c in txt:
        if c.isalpha():
            s=ord(key[j%len(key)])-65
            if c.isupper():
                r+=chr((ord(c)-65-s)%26+65)
            else:
                r+=chr((ord(c.upper())-65-s)%26+65).lower()
            j+=1
        else:
            r+=c
    return r

def rail_encrypt(txt,n):
    if n<=1: return txt
    f=[[] for _ in range(n)]
    r=0; d=1
    for c in txt.replace(" ",""):
        f[r].append(c)
        r+=d
        if r==n-1 or r==0:
            d*=-1
    return "".join("".join(r) for r in f)

def rail_decrypt(txt,n):
    if n<=1: return txt
    m=[[] for _ in range(n)]
    r=0; d=1
    for _ in txt:
        m[r].append(None)
        r+=d
        if r==n-1 or r==0: d*=-1
    i=0
    for a in range(n):
        for b in range(len(m[a])):
            m[a][b]=txt[i]; i+=1
    r=0; d=1
    col=[0]*n
    out=""
    for _ in txt:
        out+=m[r][col[r]]
        col[r]+=1
        r+=d
        if r==n-1 or r==0: d*=-1
    return out

def ver_gen(l):
    return [random.randint(0,255) for _ in range(l)]

def ver_encrypt(txt,key):
    return [ord(txt[i])^key[i] for i in range(len(txt))]

def ver_decrypt(ct,key):
    return "".join(chr(ct[i]^key[i]) for i in range(len(ct)))

while True:
    print("\n1 Caesar")
    print("2 Monoalphabetic")
    print("3 Polyalphabetic (Vigenere)")
    print("4 Rail Fence")
    print("5 Vernam")
    print("6 Exit")
    ch=int(input("Choice: "))
    if ch==1:
        p=input("Text: ")
        s=int(input("Shift: "))
        e=caesar_encrypt(p,s)
        print("Encrypted:",e)
        print("Decrypted:",caesar_decrypt(e,s))
    elif ch==2:
        key={}
        alpha=list(string.ascii_uppercase)
        sub=alpha.copy()
        random.shuffle(sub)
        for i in range(26):
            key[alpha[i]]=sub[i]
        p=input("Text: ")
        e=mono_encrypt(p,key)
        print("Key:",key)
        print("Encrypted:",e)
        print("Decrypted:",mono_decrypt(e,key))
    elif ch==3:
        p=input("Text: ")
        k=input("Key: ")
        e=vig_encrypt(p,k)
        print("Encrypted:",e)
        print("Decrypted:",vig_decrypt(e,k))
    elif ch==4:
        p=input("Text: ")
        r=int(input("Rails: "))
        e=rail_encrypt(p,r)
        print("Encrypted:",e)
        print("Decrypted:",rail_decrypt(e,r))
    elif ch==5:
        p=input("Text: ")
        key=ver_gen(len(p))
        e=ver_encrypt(p,key)
        print("Key:",key)
        print("Encrypted:",e)
        print("Decrypted:",ver_decrypt(e,key))
    elif ch==6:
        break
    else:
        print("Invalid")
