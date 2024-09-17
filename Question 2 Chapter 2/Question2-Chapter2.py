#Function that seperates the input string and splits it up between numbers and letters.
def separate_string(s):
    
    numbers = ''.join(c for c in s if c.isdigit())
    letters = ''.join(c for c in s if c.isalpha())
    return numbers, letters

#Function that converts the substrings obtained from the above function into ASCII list values.
def substring_converter(numbers, letters):
    
    ascii_numbers = [int(n) for n in numbers if int(n) % 2 == 0]
    ascii_letters = [ord(c) for c in letters if c.isupper()]
    return ascii_numbers, ascii_letters

#Function that decyrypts the encrypted string.
def text_decrypter(ciphertext, shift):
    
    decrypted = []
    for char in ciphertext:
        if char.isalpha():
            shift_value = 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') - shift) % shift_value + ord('a'))
            elif char.isupper():
                new_char = chr((ord(char) - ord('A') - shift) % shift_value + ord('A'))
            decrypted.append(new_char)
        else:
            decrypted.append(char)
    return ''.join(decrypted)

#Encoded string saved under a variable.
s_shift_key = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQ NG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYY QBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"

#Extracts digits and letters from the variable string.
numbers, letters = separate_string(s_shift_key)

#Converts the digits and numbers into ASCII values.
ascii_numbers, ascii_letters = substring_converter(numbers, letters)

#This loops through all '26' letters, checks if the decrypted text contains the word "the". Once it correctly loops it will then print out the decrypted text once it finds readable words.
for shift in range(1, 26):
    decrypted = text_decrypter(s_shift_key, shift)
    if "the" in decrypted.lower():
        print(f"Shift {shift}: {decrypted}")
        break
