import time
import string


'''
capital = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 
            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
           "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
'''
typeable = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def bruteforce(password, strvar, iterate):
    possible_characters = string.ascii_letters + string.digits
    for i in range(len(possible_characters)):
        iterate += 1
        concat = strvar + possible_characters[i]
        print(f"{concat}, {password}, {concat == password}")
        if concat == password:
            return print(f"password found on iteration {iterate}")
    
    loopit(password, strvar, iterate)

def loopit(password, strarg, iterator):
    print(iterator)
    print(strarg + " <-")
    strarg = editstring(strarg)
    print(strarg + " <-")
    bruteforce(password, strarg, iterator)


def editstring(character):
    try:
        if character == "":
            return "a"
        elif character in typeable and character != "9" and len(character) < 2:
            print(typeable[typeable.index(character) + 1])
            return typeable[typeable.index(character) + 1]
        elif character == "9":
            return "aa"
        elif len(character) > 1:
            if character[-1] == "9":
                return editstring(character[:-1]) + "a" 
            else:
                character = character[:-1] + typeable[typeable.index(character[-1]) + 1]
            return character
    except:
        print("annoyig little pesky error")

def allCharactersSame(s) :
    n = len(s)
    for i in range(0, n) :
        if s[i] != "9" :
            return False
    return True
 
def main():
    iterate = 0
    password = input("please enter a password: ")

    start = time.time()
    bruteforce(password, "", iterate)
    end = time.time() - start
    print(f"\nTime taken: {end} seconds")

main()
