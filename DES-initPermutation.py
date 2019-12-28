initialPermMatrix = [
    58, 50, 42, 34, 26, 18, 10, 2, 
	60, 52, 44, 36, 28, 20, 12, 4,
	62, 54, 46, 38, 30, 22, 14, 6,
	64, 56, 48, 40, 32, 24, 16, 8,
	57, 49, 41, 33, 25, 17, 9, 1,
	59, 51, 43, 35, 27, 19, 11, 3,
	61, 53, 45, 37, 29, 21, 13, 5,
	63, 55, 47, 39, 31, 23, 15, 7
]

expansionMatrix = [
    32,  1,   2,   3,   4,   5,
    4,   5,   6,   7,   8,   9,
    8,   9,   10,  11,  12,  13,
    12,  13,  14,  15,  16,  17,
    16,  17,  18,  19,  20,  21,
    20,  21,  22,  23,  24,  25,
    24,  25,  26,  27,  28,  29,
    28,  29,  30,  31,  32,  1
]

permutationMatrix = [
    16,  7,   20,  21,  29,  12,  28,  17,
    1,   15,  23,  26,  5,   18,  31,  10,
    2,   8,   24,  14,  32,  27,  3,   9,
    19,  13,  30,  6,   22,  11,  4,   25
]

pc1Matrix = [
    57,  49,  41,  33,  25,  17,  9,
    1,   58,  50,  42,  34,  26,  18,
    10,  2,   59,  51,  43,  35,  27,
    19,  11,  3,   60,  52,  44,  36,
    63,  55,  47,  39,  31,  23,  15,
    7,   62,  54,  46,  38,  30,  22,
    14,  6,   61,  53,  45,  37,  29,
    21,  13,  5,   28,  20,  12,  4
]

pc2Matrix = [
    14,  17,  11,  24,  1,   5,
    3,   28,  15,  6,   21,  10,
    23,  19,  12,  4,   26,  8,
    16,  7,   27,  20,  13,  2,
    41,  52,  31,  37,  47,  55,
    30,  40,  51,  45,  33,  48,
    44,  49,  39,  56,  34,  53,
    46,  42,  50,  36,  29,  32
]

rotationsDC = [ 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1 ]

sBoxes = [
    [
        [14,  4,   13,  1,   2,   15,  11,  8,   3,   10,  6,   12,  5,   9,   0,   7],
        [0,   15,  7,   4,   14,  2,   13,  1,   10,  6,   12,  11,  9,   5,   3,   8],
        [4,   1,   14,  8,   13,  6,   2,   11,  15,  12,  9,   7,   3,   10,  5,   0],
        [15,  12,  8,   2,   4,   9,   1,   7,   5,   11,  3,   14,  10,  0,   6,   13]
    ],
    [
        [15, 1,  8,  14, 6,  11, 3,  4,  9,  7,  2,  13, 12, 0,  5,  10],
        [3,  13, 4,  7,  15, 2,  8,  14, 12, 0,  1,  10, 6,  9,  11, 5],
        [0,  14, 7,  11, 10, 4,  13, 1,  5,  8,  12, 6,  9,  3,  2,  15],
        [13, 8,  10, 1,  3,  15, 4,  2,  11, 6,  7,  12, 0,  5,  14, 9]
    ],
    [
        [10, 0,  9,  14, 6,  3,  15, 5,  1,  13, 12, 7,  11, 4,  2,  8],
        [13, 7,  0,  9,  3,  4,  6,  10, 2,  8,  5,  14, 12, 11, 15, 1],
        [13, 6,  4,  9,  8,  15, 3,  0,  11, 1,  2,  12, 5,  10, 14, 7],
        [1,  10, 13, 0,  6,  9,  8,  7,  4,  15, 14, 3,  11, 5,  2,  12]
    ],
    [
        [7,  13, 14, 3,  0,  6,  9,  10, 1,  2,  8,  5,  11, 12, 4,  15],
        [13, 8,  11, 5,  6,  15, 0,  3,  4,  7,  2,  12, 1,  10, 14, 9],
        [10, 6,  9,  0,  12, 11, 7,  13, 15, 1,  3,  14, 5,  2,  8,  4],
        [3,  15, 0,  6,  10, 1,  13, 8,  9,  4,  5,  11, 12, 7,  2,  14]
    ],
    [
        [2,  12, 4,  1,  7,  10, 11, 6,  8,  5,  3,  15, 13, 0,  14, 9],
        [14, 11, 2,  12, 4,  7,  13, 1,  5,  0,  15, 10, 3,  9,  8,  6],
        [4,  2,  1,  11, 10, 13, 7,  8,  15, 9,  12, 5,  6,  3,  0,  14],
        [11, 8,  12, 7,  1,  14, 2,  13, 6,  15, 0,  9,  10, 4,  5,  3]
    ],
    [
        [12,    1,  10, 15, 9,  2,  6,  8,  0,  13, 3,  4,  14, 7,  5,  11],
        [10, 15, 4,  2,  7,  12, 9,  5,  6,  1,  13, 14, 0,  11, 3,  8],
        [9,  14, 15, 5,  2,  8,  12, 3,  7,  0,  4,  10, 1,  13, 11, 6],
        [4,  3,  2,  12, 9,  5,  15, 10, 11, 14, 1,  7,  6,  0,  8,  13]
    ],
    [
        [4,  11, 2,  14, 15, 0,  8,  13, 3,  12, 9,  7,  5,  10, 6,  1],
        [13, 0,  11, 7,  4,  9,  1,  10, 14, 3,  5,  12, 2,  15, 8,  6],
        [1,  4,  11, 13, 12, 3,  7,  14, 10, 15, 6,  8,  0,  5,  9,  2],
        [6,  11, 13, 8,  1,  4,  10, 7,  9,  5,  0,  15, 14, 2,  3,  12]
    ],
    [
        [13, 2,  8,  4,  6,  15, 11, 1,  10, 9,  3,  14, 5,  0,  12, 7],
        [1,  15, 13, 8,  10, 3,  7,  4,  12, 5,  6,  11, 0,  14, 9,  2],
        [7,  11, 4,  1,  9,  12, 14, 2,  0,  6,  10, 13, 15, 3,  5,  8],
        [2,  1,  14, 7,  4,  10, 8,  13, 15, 12, 9,  0,  3,  5,  6,  11]
    ]
]

####################################

def bitfield(n, padding):
    digits = bin(n)[2:].zfill(padding)
    return [int(digit) for digit in digits]

def flatten(array):
    result = []

    for ar in array:
        for a in ar:
            result.append(a)

    return result

def fromStringToBitArray(msg):
    a = map(lambda x: int(x, 16), msg.split(' '))
    return fromIntArrayToBitArray(a, 8)

def fromIntArrayToBitArray(intArray, padding):
    b = map(lambda x: bitfield(x, padding), intArray)

    return flatten(b)

def permuteBitArray(bitArray, matrix):
    return map(lambda x: bitArray[x-1], matrix)

def groupInNBits(bitArray, n):
    e = []
    sub = ""

    for x in bitArray:
        sub = sub + str(x)

        if len(sub) == n:
            e.append(sub)
            sub = ""

    return e

def fromBitArrayToHexArray(bitArray):
    e = groupInNBits(bitArray, 8)

    f = map(lambda x: hex(int(x, 2)), e)

    return f

def fromHexArrayToString(hexArray):
    g = ""

    for x in hexArray:
        g = g + x[2:].zfill(2) + " "

    return g

def transform(msg, matrix):
    bitArray = fromStringToBitArray(msg)

    bitArrayTransformed = permuteBitArray(bitArray, matrix)

    hexArray = fromBitArrayToHexArray(bitArrayTransformed)

    return fromHexArrayToString(hexArray)

def initialPermutation(msg):
    return transform(msg, initialPermMatrix)

def l(bitArrayD):
    bitArrayTransformed = permuteBitArray(bitArrayD, expansionMatrix)

    return bitArrayTransformed

def sumBits(xs, ys):
    if len(xs) != len(ys):
        print("Different lengths!!!")

    zs = []
    for i in range(len(xs)):
        #zs.append(xs[i] | ys[i])
        zs.append((xs[i] + ys[i]) % 2)

    return zs

def s(grouped6Bits, i):
    rowBitArray = str(grouped6Bits[0]) + str(grouped6Bits[5])
    colBitArray = str(grouped6Bits[1]) + str(grouped6Bits[2]) + str(grouped6Bits[3]) + str(grouped6Bits[4])

    row = int(rowBitArray, 2)
    col = int(colBitArray, 2)

    return sBoxes[i][row][col]

def f(arrayBitsD, arrayBitsK):
    array48bitsD = l(arrayBitsD)

    arraySumDK = sumBits(array48bitsD, arrayBitsK)

    grouped6BitsArray = groupInNBits(arraySumDK, 6)

    intArray = []
    for i in range(len(grouped6BitsArray)):
        intArray.append(s(grouped6BitsArray[i], i))

    bitArray = fromIntArrayToBitArray(intArray, 4)

    bitArrayTransformed = permuteBitArray(bitArray, permutationMatrix)

    return bitArrayTransformed

def iteration(e, d, k):
    arrayBitsE = fromStringToBitArray(e)
    arrayBitsD = fromStringToBitArray(d)
    arrayBitsK = fromStringToBitArray(k)

    resF = f(arrayBitsD, arrayBitsK)

    sumBitsArray = sumBits(arrayBitsE, resF)

    hexArray = fromBitArrayToHexArray(sumBitsArray)

    return fromHexArrayToString(hexArray)

def rotateArray(array, positions):
    positions = positions % len(array)
    return array[positions:] + array[:positions]

def subkey(k, iter):
    arrayBitsK = fromStringToBitArray(k)

    p1BitArray = permuteBitArray(arrayBitsK, pc1Matrix)

    fBitArray = rotateArray(p1BitArray[:28], rotationsDC[iter - 1])
    gBitArray = rotateArray(p1BitArray[28:], rotationsDC[iter - 1])

    p2BitArray = permuteBitArray(fBitArray + gBitArray, pc2Matrix)

    hexArray = fromBitArrayToHexArray(p2BitArray)

    return fromHexArrayToString(hexArray)

#######################

m1 = "4E 43 45 4F 46 47 4F 44"
m2 = "00 00 92 49"


#print(initialPermutation("4E 43 45 4F 46 47 4F 44"))

#print(iteration("FF 45 C1 AB", "00 00 1A 05", "A0 92 42 A6 52 0C"))

#print(iteration("BF 11 A6 BC", "00 FE 02 10", "B0 92 42 15 17 A1"))

print(subkey("46 45 49 53 54 45 4C 21", 1))





