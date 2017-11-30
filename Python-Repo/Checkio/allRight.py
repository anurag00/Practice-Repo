def left_join(phrases):
    """
        Join strings and replace "right" to "left"

        Could have used replace
        ",".join(phrases).replace("right", "left")
    """
    string = ""
    firstWord = True
    for word in phrases:
        if len(word) < 5:
            if firstWord:
                string += word
                firstWord = False
            else:
                string += "," + word
        else:
            print(word)
            correctWord = list('right')
            print(correctWord)
            leftCorrect = False
            hasRight = False
            length = len(word)
            newWord = list(word)
            for x in range(length - 4):
                if leftCorrect:
                    leftCorrect = False
                    continue
                print(newWord[x:(x+5)])
                if newWord[x:(x+5)] == correctWord:
                    newWord = newWord[:x] + list('left') + newWord[(x+5):]
                    leftCorrect = True
            word = ''.join(newWord)
            if firstWord:
                string += word
                firstWord = False
            else:
                string += "," + word
    print(string)        
    return string

if __name__ == '__main__':
    left_join(("brightness wright",))
"""
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
"""
