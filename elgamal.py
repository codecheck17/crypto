import random
def encrpyt(txt,public):
    encrypted = []
    e1,e2,p = public
    for letter in txt:
        M = ord(letter)
        r = random.randint(10,10)
        C1 = pow(e1,r,p)
        C2 = (M * pow(e2,r,p)) % p
        encrypted.append((C1,C2))
    
    return encrypted

def decrypt(encrypted,private):
    d,p = private
    decrypted_text = ""
    for C1,C2 in encrypted:
        M = (C2 * pow(pow(C1,d,p),-1,p)) % p
        decrypted_text += chr(M)
    
    return decrypted_text

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)

def KeyGeneration():
    p = random.randint(pow(10, 20), pow(10, 50))
    e1 = random.randint(2, p) 
    
    d = random.randint(pow(10, 20), p)
    while gcd(d,p) != 1:
        d = random.randint(pow(10, 20), p)
    
    e2 = pow(e1,d,p)
    
    return (e1,e2,p),(d,p)

if __name__ == "__main__":
    
    public , private = KeyGeneration()
    txt = "encryption"
    
    enc = encrpyt(txt,public)
    print(enc)
    dec = decrypt(enc,private)
    print(dec)
    
