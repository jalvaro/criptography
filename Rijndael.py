import textwrap

iterationMatrix = [
	[10, 10, 14],
	[12, 12, 14],
	[14, 14, 14]
]

def numberOfIterations(k, b):
	nKeykBits = len(k)*4
	nBlockBits = len(b)*4

	nKey32BitWords = nKeykBits / 32
	nBlock32BitWords = nBlockBits / 32

	equivalences = {
		4: 0,
		6: 1,
		8: 2
	}

	return iterationMatrix[equivalences[nKey32BitWords]][equivalences[nBlock32BitWords]]

def groupInNCols(array, nCols):
    e = []
    sub = []

    for x in array:
        sub.append(x)

        if len(sub) == nCols:
            e.append(sub)
            sub = []

    return e

def fromStringArrayToString(stringArray):
    g = ""

    for x in stringArray:
        g = g + x + " "

    return g

def addRoundKey(k0, msg):
	k0Array = textwrap.wrap(k0, 2)
	msgArray = textwrap.wrap(msg, 2)

	res = []
	for i in range(len(k0Array)):
		res.append(hex(int(msgArray[i], 16) ^ int(k0Array[i], 16))[2:].zfill(2))

	return zip(*groupInNCols(res, 4))

def ROTL8(x,shift) : 
        return 0xff & ( ( (x) << (shift) ) | ( (x) >> (8 - (shift) ) ) )

def initialize_aes_sbox() :
        sbox = [None] * 256
        p = q = 1
        firstTime = True

        # loop invariant: p * q == 1 in the Galois field
        while p != 1 or firstTime : # To simulate a do/while loop
                # multiply p by 2
                p = p ^ (p << 1) ^ (0x1B if p & 0x80 else 0)
                p = p & 0xff

                # divide q by 2
                q ^= q << 1
                q ^= q << 2
                q ^= q << 4
                q ^= 0x09 if q & 0x80 else 0
                q = q & 0xff

                # compute the affine transformation
                xformed = q ^ ROTL8(q, 1) ^ ROTL8(q, 2) ^ ROTL8(q, 3) ^ ROTL8(q, 4)

                sbox[p] = xformed ^ 0x63
                firstTime = False

        # 0 is a special case since it has no inverse
        sbox[0] = 0x63

        return sbox

def ByteSub(stateStr):
	array = stateStr.split(' ')
	sMatrix = groupInNCols(initialize_aes_sbox(), 16)

	return map(lambda x: hex(sMatrix[int(x[0], 16)][int(x[1], 16)])[2:].zfill(2), array)

##################################

print(numberOfIterations("66508A14EE9CEE96C4FB5DEFC15588D6", "CD63EDC7085338ACEB4DED3E29D0D817"))

print("------")

key5 = "D6CFC43EA609BB75705F61F611307ED2"
msg5 = "1ECEA05838DB7F8078EB562A3FD067E5"
res = addRoundKey(key5, msg5)
print(res)
print(fromStringArrayToString(res[0]))

print("------")

print(fromStringArrayToString(ByteSub("2d 58 d0 65")))

