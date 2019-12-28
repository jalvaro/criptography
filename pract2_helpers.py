#########################################################################################
# 
# STUDENT HELPERS
#
# You can create your own functions in this area
#
#########################################################################################
import numpy as np
import itertools
from collections import Counter

def xor(a, b):
    return (a + b) % 2
    
def xor_sequences(xs, ys):
    zs = []
    for i in range(len(xs)):
        zs.append(xor(xs[i], ys[i]))
    return zs
    
def hex_xor_char_list_with_char(char_list, c):
    bit_matrix = map(from_string_to_bit_array, char_list)
    bit_c = from_string_to_bit_array(c)
    xor_bit_matrix = map(lambda x: xor_sequences(x, bit_c), bit_matrix)
    xor_hex_matrix = map(from_bit_array_to_hex_array, xor_bit_matrix)
    xor_hex_list = map(lambda x: x.upper(), flatten(xor_hex_matrix))
    return xor_hex_list
    
def hex_xor_hex_string_with_hex_string(str1, str2):
    if len(str1) < len(str2):
        str2 = str2[:len(str1)]
    elif len(str1) > len(str2):
        str1 = str1[:len(str2)]
        
    bit_array1 = from_hex_string_to_bit_array(str1)
    bit_array2 = from_hex_string_to_bit_array(str2)
    
    xor_bit_array = xor_sequences(bit_array1, bit_array2)
    xor_hex_array = from_bit_array_to_hex_array(xor_bit_array)
    return map(lambda x: x.upper(), xor_hex_array)

def create_polynomial(bits, ones_position):
    polynomial = np.zeros(bits)
    for x in ones_position:
        polynomial[x] = 1
    
    return polynomial
    
def lfsr(polynomial, initial_state, output_bits):
    aux = initial_state
    result = []
    
    for i in range(output_bits):
        res = np.dot(aux, polynomial) % 2
        aux = aux[1:]
        aux.append(res)
        result.append(res)
        
    return result
    
def from_string_to_bit_array(msg):
    array_hex_str = [elem.encode("hex") for elem in msg]
    return flatten(map(lambda x: from_hex_string_to_bit_array(x), array_hex_str))
    
def bitfield(n, padding):
    digits = bin(n)[2:].zfill(padding)
    return [int(digit) for digit in digits]

def flatten(array):
    result = []
    for ar in array:
        for a in ar:
            result.append(a)
    return result

def from_hex_string_to_bit_array(msg):
    a = map(lambda x: int(x, 16), group_in_n(msg, 2))
    return from_int_array_to_bit_array(a, 8)

def from_int_array_to_bit_array(int_array, padding):
    b = map(lambda x: bitfield(x, padding), int_array)
    return flatten(b)
    
def group_in_n(sth, n):
    e = []
    sub = ""
    for x in sth:
        sub = sub + str(x)
        if len(sub) == n:
            e.append(sub)
            sub = ""
    return e

def from_bit_array_to_hex_array(bit_array):
    e = group_in_n(bit_array, 8)
    return map(lambda x: hex(int(x, 2))[2:].zfill(2), e)
   
def from_bit_array_to_string_array(bit_array):
    hex_array = from_bit_array_to_hex_array(bit_array)
    return map(lambda x: chr(int(x, 16)), hex_array)
    
def get_n_words_bigger_or_equal_than(words, n):
    count = 0
    for w in words:
        if len(w) >= n:
            count = count + 1
    return count
    
def counter_oks(zero_space, zeros_combinations, combs, i, j):
    count = 0
    for k in range(len(combs)):
        comb = combs[k]
        if (comb[0] == i or comb[0] == j or comb[1] == i or comb[1] == j) and zero_space in zeros_combinations[k]:
            count = count + 1
    return count

def is_special_zero_space_case(zero_space, zeros_combinations, combs, i, j, ciphertexts):
    n_words = 2*(get_n_words_bigger_or_equal_than(ciphertexts, zero_space)-2)
    return (counter_oks(zero_space, zeros_combinations, combs, i, j) == n_words)           # 2 equal