alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def flip(word):
    # usage: one char
    rtn = []
    for i in word:
        if i.upper() == i:
            rtn.append(i.lower())
        else:
            rtn.append(i.upper())
    return ''.join(rtn)

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
        if letter in alphabet:
            flipped = not flipped
        if letter == 'I' or letter == 'l':
            letter = flip(letter)
            flipped = not flipped
        rtn += letter

    return (rtn, flipped)

def mock(string):
    rtn = []
    words = string.lower().split(' ')
    end_on_flip = True
    for word in words:
        flipped, end_on_flip = wordflip(word, end_on_flip)
        # if 'l' or 'I' in flipped:
        #     flipped, end_on_flip = wordflip(word, not end_on_flip)
        rtn.append(flipped)
    return " ".join(rtn)

    """iLLinOiS"""
    """
    TiP
    """

if __name__ == "__main__":
    print(flip("rYaN sUcKs DoNkeY dOnG"))
