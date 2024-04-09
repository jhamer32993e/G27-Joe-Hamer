# Encode or decode function?
Function = input("Encode? Enter 'Y', otherwise will be decoding: ")
if Function == "Y":
    PlainText = str(input("Input the message to be encoded: "))
    PlainList = [char for char in PlainText]
    EncryptList = []
    # Lowercase letters have ord 97-122
    # Uppercase letters have ord 65-90
    # Can edit shift here to be a random number for more security but the below decoder will cycle through anyway
    # Caesar cipher is traditionally a shift of three though
    for i in range(len(PlainList)):
        # Lowercase encoding
        if 119 < ord(PlainList[i]) < 123:
            EncryptList.append(chr(ord(PlainList[i])-23))
        elif 96 < ord(PlainList[i]) < 120:
            EncryptList.append(chr(ord(PlainList[i])+3))
        # Uppercase encoding
        elif 87 < ord(PlainList[i]) < 91:
            EncryptList.append(chr(ord(PlainList[i])-23))
        elif 64 < ord(PlainList[i]) < 88:
            EncryptList.append(chr(ord(PlainList[i]) + 3))
        # If not letters, I'm choosing to not encode them
        else:
            EncryptList.append(PlainList[i])
    print("".join(EncryptList))

# Decryption
else:
    ToDecode = input("Enter text to decode, without punctuation and lowercase: ")
    # Becomes overly complicated to pick out the appropriate ranges to use punctuation,
    # and generally Caesar cipher tables do not consider punctuation
    ListToDecode = [i for i in ToDecode]

    for j in range(26):
        DecodedList = []
        for i in range(len(ToDecode)):
            if ord(ListToDecode[i]) < 97 or ord(ListToDecode[i]) > 122:
                DecodedList.append(ListToDecode[i])
            elif 96 < ord(ListToDecode[i]) + j < 123 or 64 < ord(ListToDecode[i]) +j < 91:
                DecodedList.append(chr(ord(ListToDecode[i]) + j))
            else:
                DecodedList.append(chr(ord(ListToDecode[i]) - 26 + j))
        print("".join(DecodedList))
    print("Scan through to find the string that makes sense")
