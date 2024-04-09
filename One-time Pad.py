import random
# Encode and decode modes
Mode = 0
while Mode != "E" and Mode != "D":
    Mode = input("Enter 'E' for encoding, 'D' for decoding: ")

# Encoding
# Enter string
if Mode == "E":
    PlainText = input("Enter message to encode, without spaces: ")
    PlainList = [i for i in PlainText]
    Bin = []
    # Write string as binary
    for i in range(len(PlainList)):
        # Lowercase 97-122
        Bin.append(bin(ord(PlainList[i])))
    print(Bin)
# Generate random key of correct length and print key for use decoding
    KeyList = []
    EncodedBin = []
    for i in range(len(PlainList)):
        TempKey = ['0', 'b']
        TempBin = [Bin[i][0], Bin[i][1]]
        for k in range(2, 9):
            key = random.randint(0, 1)
            TempKey.append(str(key))
            # Add together string and key, if it gives a 2 map that back to a 0
            IndividualBin = [j for j in Bin[i]]
            while len(IndividualBin) < 9:
                IndividualBin.insert(2, "0")
            print(IndividualBin)
            if int(IndividualBin[k]) + key != 2:
                TempBin.append(int(IndividualBin[k]) + key)
            else:
                TempBin.append(0)
            TempBin[k] = str(TempBin[k])
        EncodedBin.append(chr(int("".join(TempBin), 2)))
        KeyList.append("".join(TempKey))

    # Output encoded + keys
    print("Encoded text:", EncodedBin)
    print("Keys:", KeyList)

# Decoding
if Mode == "D":
    # String already in code
    ToDecodeBin = []
    DecodeKeys = []
    NumChar = int(input("How many characters to decode? "))
    for i in range(NumChar):
        print("If hexadecimal remove the backslash")
        ToDecodeBin.append(str(input("Input character: ")))
        # Input key used to encode, was output in the encoding part
        DecodeKeys.append(input("Input associated key, of the form 0b1111111: "))
    for i in range(NumChar):
        if ToDecodeBin[i] == "x00":
            ToDecodeBin[i] = '0b0000000'
        elif ToDecodeBin[i] == "x01":
            ToDecodeBin[i] = '0b0000001'
        elif ToDecodeBin[i] == "x02":
            ToDecodeBin[i] = '0b0000010'
        elif ToDecodeBin[i] == "x03":
            ToDecodeBin[i] = '0b0000011'
        elif ToDecodeBin[i] == "x04":
            ToDecodeBin[i] = '0b0000100'
        elif ToDecodeBin[i] == "x05":
            ToDecodeBin[i] = '0b0000101'
        elif ToDecodeBin[i] == "x06":
            ToDecodeBin[i] = '0b0000110'
        elif ToDecodeBin[i] == "x07":
            ToDecodeBin[i] = '0b0000111'
        elif ToDecodeBin[i] == "x08":
            ToDecodeBin[i] = '0b0001000'
        elif ToDecodeBin[i] == "x09":
            ToDecodeBin[i] = '0b0001001'
        elif ToDecodeBin[i] == "x0a":
            ToDecodeBin[i] = '0b0001010'
        elif ToDecodeBin[i] == "x0b":
            ToDecodeBin[i] = '0b0001011'
        elif ToDecodeBin[i] == "x0c":
            ToDecodeBin[i] = '0b0001100'
        elif ToDecodeBin[i] == "x0d":
            ToDecodeBin[i] = '0b0001101'
        elif ToDecodeBin[i] == "x0e":
            ToDecodeBin[i] = '0b0001110'
        elif ToDecodeBin[i] == "x0f":
            ToDecodeBin[i] = '0b0001111'
        elif ToDecodeBin[i] == "x10":
            ToDecodeBin[i] = '0b0010000'
        elif ToDecodeBin[i] == "x11":
            ToDecodeBin[i] = '0b0010001'
        elif ToDecodeBin[i] == "x12":
            ToDecodeBin[i] = '0b0010010'
        elif ToDecodeBin[i] == "x13":
            ToDecodeBin[i] = '0b0010011'
        elif ToDecodeBin[i] == "x14":
            ToDecodeBin[i] = '0b0010100'
        elif ToDecodeBin[i] == "x15":
            ToDecodeBin[i] = '0b0010101'
        elif ToDecodeBin[i] == "x16":
            ToDecodeBin[i] = '0b0010110'
        elif ToDecodeBin[i] == "x17":
            ToDecodeBin[i] = '0b0010111'
        elif ToDecodeBin[i] == "x18":
            ToDecodeBin[i] = '0b0011000'
        elif ToDecodeBin[i] == "x19":
            ToDecodeBin[i] = '0b0011001'
        elif ToDecodeBin[i] == "x1a":
            ToDecodeBin[i] = '0b0011010'
        elif ToDecodeBin[i] == "x1b":
            ToDecodeBin[i] = '0b0011011'
        elif ToDecodeBin[i] == "x1c":
            ToDecodeBin[i] = '0b0011100'
        elif ToDecodeBin[i] == "x1d":
            ToDecodeBin[i] = '0b0011101'
        elif ToDecodeBin[i] == "x1e":
            ToDecodeBin[i] = '0b0011110'
        elif ToDecodeBin[i] == "x1f":
            ToDecodeBin[i] = '0b0011111'
        elif ToDecodeBin[i] == "x20":
            ToDecodeBin[i] = '0b0100000'
        elif ToDecodeBin[i] == "x7f":
            ToDecodeBin[i] = '0b1111111'
        else:
            ToDecodeBin[i] = bin(ord(ToDecodeBin[i]))
# Add together xor
    Decoded = []
    for i in range(NumChar):
        IndividualBin = [j for j in ToDecodeBin[i]]
        while len(IndividualBin) < 9:
            IndividualBin.insert(2, "0")
        IndividualKey = [j for j in DecodeKeys[i]]
        TempBin = [ToDecodeBin[i][0], ToDecodeBin[i][1]]
        for k in range(2, 9):
            if int(IndividualBin[k]) + int(IndividualKey[k]) != 2:
                TempBin.append(int(IndividualBin[k]) + int(IndividualKey[k]))
            else:
                TempBin.append(0)
            TempBin[k] = str(TempBin[k])
        # Convert to letters from ASCII
        Decoded.append(chr(int("".join(TempBin), 2)))

# Output
    print("".join(Decoded))
