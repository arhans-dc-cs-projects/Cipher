def messageValidity(inputString): 
  functionOutput = all(x.isalpha() or x.isspace() for x in userMessage)
  return functionOutput

def shiftValidity(inputString):
  functionOutput = str(shiftAmount).isdigit()
  return functionOutput

def atbash(userMessage):
  alphabet = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm,', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
  atbash = ['Z', 'z', 'Y', 'y', 'X', 'x', 'W', 'w', 'V', 'v', 'U', 'u', 'T', 't', 'S', 's', 'R', 'r', 'Q', 'q', 'P', 'p', 'O', 'o', 'N', 'n', 'M', 'm', 'L', 'l', 'K', 'k', 'J', 'j', 'I', 'i', 'H', 'h', 'G', 'g', 'F', 'f', 'E', 'e', 'D', 'd', 'C', 'c', 'B', 'b', 'A', 'a']
  atbashOutput = ""
  for i in range(len(userMessage)):
    if userMessage[i] != ' ':
        for x in range(len(alphabet)):
            if userMessage[i] == alphabet[x]:
                atbashOutput = atbashOutput + atbash[x]
    elif userMessage[i] == ' ':
        atbashOutput = atbashOutput + " "
  return(atbashOutput)


def encryptCaesar(userMessage, shiftAmount):
  cipherText = ""
  for i in range(0, len(userMessage)):
    letterInOrder = ord(userMessage[i])
    shiftedLetter = letterInOrder + shiftAmount
    if userMessage[i] == " ":
      cipherText = cipherText + " "
    elif shiftedLetter > 122 or shiftedLetter >= 91 and shiftedLetter <= 116 and letterInOrder >= 65 and letterInOrder <= 90:
      shiftedLetter = shiftedLetter - 26
    cipherText = cipherText + chr(shiftedLetter)
  return cipherText

def noSymbols(encryptedCaesar):
  refined = ""
  for i in range(0, len(encryptedCaesar)):
    if encryptedCaesar[i].isalpha() == True:
      refined = refined + encryptedCaesar[i]
    elif encryptedCaesar[i] == " ":
      refined = refined + " "
  return refined

def decryptCaesar(userMessage, shiftAmount):
  decrypted = ""
  for i in range(0, len(userMessage)):
    letterInOrder = ord(userMessage[i])
    removeShift = letterInOrder - shiftAmount
    if letterInOrder <= 90 and userMessage[i] != " ":
      if removeShift >= ord("A"):
        shiftAmount = shiftAmount + chr(removeShift)
      else:
        decrypted = decrypted + chr(removeShift + 26)
    elif userMessage[i] == " ":
      decrypted = decrypted + userMessage[i]
    else:
      if removeShift >= ord("a"):
        decrypted = decrypted + chr(removeShift)
      else:
        decrypted = decrypted + chr(removeShift + 26)
  return decrypted

userMessage = input("Enter the message you want to encrypt or decrypt: ")

while True:
  if messageValidity(userMessage) is False:
    userMessage = input("Invalid; your message should only contain letters: ")
    continue
  elif messageValidity(userMessage) is True:
    break

userCipher = input("The 'atbash' or 'caesar' cipher? ")

while True:
  if userCipher == "caesar" or userCipher == "atbash":
    break
  elif str(userCipher) != "C" or str(userCipher) != "A":
    userCipher = input("Invalid; 'atbash' or 'caesar' cipher: ")

if userCipher == "caesar":
    userMode = input("'E' to encrypt this message or 'D' to decrypt this message: ")
    while True:
        if userMode == "E" or userMode == "D":
            break
        elif str(userMode) != "E" or str(userMode) != "D":
            userMode = input("Invalid; 'E' for encrypt, 'D' for decrypt: ")

    shiftAmount = input("Enter the shift: ")
    while True:
        if shiftValidity(shiftAmount) == True:
            shiftAmount = int(shiftAmount) % 26
            break
        elif shiftValidity(shiftAmount) == False:
            shiftAmount = input("Invalid; enter the shift: ")
            continue
        
    if userMode == "D":
            decryptedCaesar = decryptCaesar(userMessage, shiftAmount)
            decryptedCaesar = noSymbols(decryptedCaesar)
            print("Encrypted message:", '"'+decryptedCaesar+'"')
            userExport = input("Export result to file? ")
            while True:
              if userExport == "yes" or userExport == "no":
                if userExport =="no":
                  print("Finished")
                  quit()
                if userExport=="yes":
                  with open('cipher.txt', 'w') as exportReadFile:
                      exportReadFile.write(decryptedCaesar)
                      continue

    if userMode == "E":
            encryptedCaesar = encryptCaesar(userMessage, shiftAmount)
            encryptedCaesar = noSymbols(encryptedCaesar)
            print("Encrypted message:", '"'+encryptedCaesar+'"')
            userExport = input("Export result to a file? ")
            while True:
              if userExport == "yes" or userExport == "no":
                if userExport =="no":
                  print("Finished")
                  quit()
                if userExport=="yes":
                  with open('cipher.txt', 'w') as exportReadFile:
                      exportReadFile.write(encryptedCaesar)
                      continue
                              


if userCipher == "atbash":
            print("Encrypted message:", atbash(userMessage))
            userExport = input("Export result to file? ")
            while True:
              if userExport == "yes" or userExport == "no":
                if userExport =="no":
                  print("Finished")
                  quit()
                if userExport=="yes":
                  with open('cipher.txt', 'w') as exportReadFile:
                      exportReadFile.write(atbash(userMessage))
                      continue
