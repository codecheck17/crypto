
P = 23
G = 9


a = int(input("Enter Private Key of User A: "))
b = int(input("Enter Private Key of User B: "))

pub_a = pow(G,a,P)
pub_b = pow(G,b,P)

c_pa = pow(pub_b,a,P)
c_pb = pow(pub_a,b,P)

print(c_pa == c_pb)
