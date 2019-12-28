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
	res = 1
	for prime in primes:
		res = res*(prime-1)
	return res

###########################

def get_public_key(b, alpha, p):
	return pow_modulus_n(alpha, b, p)

def decrypt_brute_force(alpha_exp_v, alpha_exp_b, p, enc_m):
	for alpha in range(p):
		for v in range(p):
			if pow_modulus_n(alpha, v, p) == alpha_exp_v:
				for b in range(p):
					if pow_modulus_n(alpha, b, p) == alpha_exp_b:
						print alpha, "\t", v, "\t", b, "\t\t", pow_modulus_n(alpha, v, p), "\t", pow_modulus_n(alpha, b, p), "\t\t", pow_modulus_n(alpha, v*b, p), "\t", (pow_modulus_n(alpha, v*b, p)*42)%p, "\t", (pow_modulus_n(alpha, v*b, p)*42)%p == enc_m

def encrypt(alpha_exp_v, b, p, m):
	alpha_exp_v_b = pow_modulus_n(alpha_exp_v, b, p)
	c = (alpha_exp_v_b*m)%p

	return (alpha_exp_v, c)

def decrypt(alpha_exp_v, b, p, enc_m):
	alpha_exp_v_b = pow_modulus_n(alpha_exp_v, b, p)
	inv_alpha_exp_v_b = mulinv(alpha_exp_v_b, p)

	return (enc_m*inv_alpha_exp_v_b)%p

def sign(m, a, alpha, h, p):
	r = pow_modulus_n(alpha, h, p)
	phi_p = phi(p)
	inv_h = mulinv(h, phi_p)

	s = (((m - (a*r)%phi_p) % phi_p) * inv_h) % phi_p

	return (r, s)

def valid_signatures(m, a, alpha, p, signatures):
	res = {}

	for (r, s) in signatures:
		r_exp_s = pow_modulus_n(r, s, p)
		alpha_exp_a = pow_modulus_n(alpha, a, p)
		alpha_exp_a_r = pow_modulus_n(alpha_exp_a, r, p)
		alpha_exp_m = pow_modulus_n(alpha, m, p)

		alpha_exp_m2 = (r_exp_s*alpha_exp_a_r)%p

		res[(r, s)] = (alpha_exp_m == alpha_exp_m2)

	return res

###########################
print "Exercise: public key"
p = 251
b = 193
alpha = 120
print get_public_key(b, alpha, p)

###########################
print ""
print "Exercise: decrypt"

p = 71
alpha_exp_v = 59
enc_m = 41
b = 32
print decrypt(alpha_exp_v, b, p, enc_m)
print "comprovacio --> c: ", encrypt(alpha_exp_v, b, p, decrypt(alpha_exp_v, b, p, enc_m))


###########################
print ""
print "Exercise: sign"

#m = 128688; a = 28236; alpha = 7; h = 90725; p = 15485863
m = 45
a = 124
alpha = 60
h = 223
p = 227
print sign(m, a, alpha, h, p)
print "comprovacio -->", valid_signatures(m, a, alpha, p, [sign(m, a, alpha, h, p)])


###########################
print ""
print "Exercise: valid signatures"

#m = 128688; a = 28236; alpha = 7; h = 90725; p = 15485863; signatures = [(7635256, 11047464)]
m = 10
a = 3
alpha = 7
p = 13
signatures = [(13,4), (9,0), (8,3), (2,8), (11,5), (7,1)]

print valid_signatures(m, a, alpha, p, signatures)
