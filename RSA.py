import math,random
def encrypt(txt,publicKey):
    e,N = publicKey
    enc = []
    for letter in  txt:
        M = ord(letter)
        C = pow(M,e,N)
        enc.append(C)
    
    return enc

def decrypt(enc,privateKey):
    d,N = privateKey
    dec = ""
    for C in enc:
        D = pow(C,d,N)
        dec += chr(D)
    
    return dec
    
def KeyGeneration():
    P = 11
    Q = 13
    N = P * Q
    phi = (P - 1) * (Q - 1)
    
    e = random.randint(3,phi)
    while math.gcd(e,phi) != 1:
        e = random.randint(3,phi)
    
    d = pow(e,-1,phi)
    return (e,N),(d,N)

if __name__ == "__main__":
    
    publicKey,privateKey = KeyGeneration()
    txt = "encryption"
    enc = encrypt(txt,publicKey)
    print(enc)
    dec = decrypt(enc,privateKey)
    print(dec)
    
