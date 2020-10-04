def decrypt(msg,MORSE_CODE_DICTIONARY):
    li1=list(MORSE_CODE_DICTIONARY.keys())
    li2 = list(MORSE_CODE_DICTIONARY.values())
    dic= dict()
    for i,j in zip(li1,li2):
        dic[j]=i
    wordlist=msg.split("/")
    LetterList=list()
    DecryptedMessage=list()
    for  i in wordlist:
        Word=""
        LetterList=i.split(" ")
        for  j in LetterList:
            if j not in li2:
                DecryptedMessage.clear()
                DecryptedMessage.append('INVALID MORSE CODE!!')
                return DecryptedMessage
            Word= Word+dic[j]
        DecryptedMessage.append(Word)
        Word=""
    return DecryptedMessage

