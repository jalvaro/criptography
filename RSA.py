import sys
sys.setrecursionlimit(1000000)  # long type,32bit OS 4B,64bit OS 8B(1bit for sign)

# return (g, x, y) a*x + b*y = gcd(x, y)
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, x, y = egcd(b % a, a)
		return (g, y - (b // a) * x, x)

def mulinv(b, n):
	g, x, _ = egcd(b, n)
	if g == 1:
		return x % n

def pow_modulus_n(a, b, n):
	res = 1
	for i in range(b):
		res = (res * a)%n
	return res

def factorisation(n):
	fact = []
	i = 2
	while i<=n:	 
		if n%i==0:	  
			fact.append(i)
			n//= i
		else:
			i+=1
	return fact

def phi(n):
	primes = factorisation(n)
	return (primes[0]-1) * (primes[1]-1)

###########################

def find_secret(e, n):
	return mulinv(e, phi(n))

def find_d_for_each_pair_n_e(listNE, listD):
	(n,e) = listNE[0]
	d = listD[0]

	res = {}

	for (n,e) in listNE:
		phiN = phi(n)

		print "(", n, ",", e, ")", find_secret(e, n)

		for d in listD:
			if 1 == ((e*d)%phiN):
				res[(n,e)] = d

	return res

def encrypt_msg_send_a_to_b(m, n_b, e_b):
	return encrypt(m, n_b, e_b)

def encrypt(m, n, e):
	#return pow(m, e)%n
	return pow_modulus_n(m, e, n)

def decrypt_brute_force(c, n, e):
	iterations = 200
	for i in range(iterations):
		if encrypt(i, n, e) == c:
			return i
	return -1

def decrypt_msg_send_a_to_b(c, n_b, e_b):
	return decrypt(c, n_b, e_b)

def decrypt(c, n, e):
	d = find_secret(e, n)

	#return pow(c, d)%n
	return pow_modulus_n(c, d, n)

def sign_msg_by_a(m, n_a, d_a):
	return sign(m, n_a, d_a)

def sign(m, n, d):
	return pow_modulus_n(m, d, n)


#############################
print "Exercise: Find d for each pair (e, n)"
listNE = [(21877,8779), (3611,131), (40309,5399), (737,43)]
listD = [5255, 14739, 131, 307]
print(find_d_for_each_pair_n_e(listNE, listD))

#############################
print ""
print "Exercise encrypt"
m = 163
n_b = 407
e_b = 277
#print(encrypt_msg_send_a_to_b(m, n_b, e_b))



#print(decrypt(encrypt(63, 763, 67), 763, 67))
#print(encrypt(61, 9797, 6653))
#print "enc-dec --> m: ", 61, ", encrypted: ", encrypt(61, 9797, 6653), ", decrypted: ", decrypt(encrypt(61, 9797, 6653), 9797, 6653)


#############################
print ""
print "Exercise: decrypt"

c = 224
n_b = 403
e_b = 277
print "decrypt_brute_force\t --> m: ", decrypt_brute_force(c, n_b, e_b)
print "decrypt\t\t\t --> m: ", decrypt_msg_send_a_to_b(c, n_b, e_b)
print "comprovacio\t\t --> c: ", encrypt_msg_send_a_to_b(decrypt_msg_send_a_to_b(c, n_b, e_b), n_b, e_b)


#############################
print ""
print "Exercise: decrypt 5"

c = 473
n_b = 4717
e_b = 4341
print "decrypt_brute_force\t --> m: ", decrypt_brute_force(c, n_b, e_b)
print "decrypt\t\t\t --> m: ", decrypt_msg_send_a_to_b(c, n_b, e_b)
print "comprovacio\t\t --> c: ", encrypt_msg_send_a_to_b(decrypt_msg_send_a_to_b(c, n_b, e_b), n_b, e_b)

#############################
print ""
print "Exercise: sign message"

m = 1328
n_a = 2627
d_a = 23
print sign_msg_by_a(m, n_a, d_a)
print "comprovacio --> ", pow_modulus_n(sign_msg_by_a(m, n_a, d_a), 767, n_a)
