if __name__ == "__main__":
    pass

def flip(word):
    rtn = []
    for i in word:
        if i.upper() == i:
            rtn.append(i.lower())
        else:
            rtn.append(i.upper())
    return ''.join(rtn)

def mock(string):
    string = string.lower()
    rtn = ""
    letter_count = 1
    for char in string:
        even = (letter_count%2 == 0)
        if even:
            rtn += char.upper()
        else:
            rtn += char

        if char != " ":
            letter_count +=1    
    return rtn

def mock2(string):
    rtn = ''
    letter_count = 1
    string = string.lower()
    for char in string:
        if letter_count%2==0:
            rtn += flip(char)
        else:
            rtn += char
        if char != " ":
            letter_count += 1
    return rtn

def oldflip(word, end_on_flip):
    rtn = ''
    count = 1
    for char in word:
        if end_on_flip and count == 1:
            rtn += char
        elif count%2==0:
            rtn += flip(char)
            if count == len(word):
                end_on_flip = True
        else:
            rtn += char
            if count == len(word):
                end_on_flip = False
        count += 1
    return (rtn, end_on_flip)

def wordflip(word, end_on_flip):
    rtn = ''
    flipped = end_on_flip
    for letter in word:
        if not flipped:
            letter = flip(letter)
        flipped = not flipped

            # exceptions
        # if letter == 'I':
        #     print(f"word is {word}")
        #     letter = letter.lower()
        #     flipped = False
        # if letter == 'l':
        #     letter = letter.upper()
        

        rtn += letter

    # if 'I' in word or 'l' in word:
    #     rtn = flip(word)
    # if 'l' in word:
    #     rtn = wordflip(word, flipped)
    return (rtn, flipped)
        


def mock3(string):
    rtn = []
    words = string.split(' ')
    words = [word.lower() for word in words]
    print(words)
    end_on_flip = True
    for word in words:
        flipped, end_on_flip = wordflip(word, end_on_flip)
        if 'l' or 'I' in flipped:
            flipped, end_on_flip = wordflip(word, not end_on_flip)
        rtn.append(flipped)
    return " ".join(rtn)
        

# test1 = "What a neat program"
# answer = "wHaT a NeAt PrOgRaM"

# print(mock(test1))
# print(mock(test1) == answer)
# print("-"*10)
# print(mock2(test1))
# print(mock2(test1) == answer)

# # next 
# test3 = "ryan I do not like this rule"
# answer3 = "rYaN i Do NoT LiKe tHiS RuLe"
# print("-"*10)
# print(mock3(test3))
# print(mock3(test3) == answer3)
