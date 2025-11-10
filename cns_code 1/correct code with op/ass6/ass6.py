import random,hashlib

def is_prime(n):
    if n<=1:return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:return False
    return True

def gcd(a,b):
    while b!=0:a,b=b,a%b
    return a

def mod_inverse(a,m):
    for i in range(1,m):
        if (a*i)%m==1:return i
    return None

def generate_keypair():
    p=q=1
    while not is_prime(p):p=random.randint(100,1000)
    while (not is_prime(q)) or p==q:q=random.randint(100,1000)
    n=p*q
    phi=(p-1)*(q-1)
    e=random.randint(1,phi)
    while gcd(e,phi)!=1:e=random.randint(1,phi)
    d=mod_inverse(e,phi)
    return (e,n),(d,n)

def rsa_encrypt(msg,key):
    e,n=key
    return [pow(ord(c),e,n) for c in msg]

def rsa_decrypt(enc,key):
    d,n=key
    return ''.join(chr(pow(c,d,n)) for c in enc)

def sign(msg,priv):
    h=hashlib.sha256(msg.encode()).hexdigest()
    return rsa_encrypt(h,priv)

def verify(msg,sig,pub):
    h=hashlib.sha256(msg.encode()).hexdigest()
    return rsa_decrypt(sig,pub)==h

pubX,privX=generate_keypair()
pubY,privY=generate_keypair()

print("Keys Generated")
print("X Public:",pubX)
print("X Private:",privX)
print("Y Public:",pubY)
print("Y Private:",privY)

msg=input("X Enter Message: ")

cipher=rsa_encrypt(msg,pubY)
sig=sign(msg,privX)

print("\nSent Cipher:",cipher)
print("Signature:",sig)

recv=rsa_decrypt(cipher,privY)

ok=verify(recv,sig,pubX)

print("\nY Received:",recv)
if ok:print("Signature Valid. Integrity + Non-repudiation OK.")
else:print("Signature Invalid.")
