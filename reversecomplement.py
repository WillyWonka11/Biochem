s = input("Input your strand: ")
slow = s.lower()
print("Your strand is : " + s)

def base_converter(strand):
    for letter in range(0,len(strand)):
        nstrand = strand.replace("a","w").replace("c","x").replace("g","y").replace("t","z")
    return nstrand

def complementer(strand):
    for letter in range(0,len(strand)):
        nstrand = strand.replace("w","t").replace("x","g").replace("y","c").replace("z","a")
    return nstrand

converted = base_converter(slow)
print(converted.upper())
complemented = complementer(converted)
print(complemented.upper())


def reverser():
    return complemented[::-1]

creversed = reverser()
print("Your reversed complimented strand: " + creversed.upper())

