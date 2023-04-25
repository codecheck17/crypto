import math
import numpy as np
def create_matrix_from(key):
    mat = []
    n = int(math.sqrt(len(key)))
    for i in range(0,len(key),n):
        mat.append([ord(x)-97 for x in key[i:i+n]])
    return mat

def multiply(P, K):
    n = len(K)
    C = np.zeros(n)
    for i in range(n):
        for j in range(n):
            C[i] = (C[i] + K[i][j] * P[j]) % 26
   
    return C

def Hill(message, K):
    cipher_text = []
    n = len(K)
    for i in range(0,len(message), n):
        P = [ord(x)-97 for x in message[i:i+n]]
        C = multiply(P,K)
        cipher_text.append(''.join([chr(round(x) % 26 + 97) for x in C]))

    return ''.join(cipher_text)


if __name__ == "__main__":
    message = "ACT AND ACT"
    key = "GYBNQKURP"
    message = ''.join(message.lower().split())
    key = ''.join(key.lower().split())
    
    K = create_matrix_from(key)
    cipher_text = Hill(message, K)
    print ('Cipher text: ', cipher_text)
    
    det = np.linalg.det(K)
    adj = np.linalg.inv(K) * det      
    K_inv = (pow(math.ceil(det),-1,26) * adj) % 26
    
    plain_text = Hill(cipher_text, K_inv)
    print ('Plain text: ', plain_text)
