def guess():
    import random
    print("What is you name fine sir?")
    name = input()
    print("Hello {0}, Welcom to the number guessing game".format(name))
    num = random.randint(1,10)
    print("I have selected a number range(1,10), please try and guess it?:)")
    attempt = 0
    numPredict = 0
    winFlag = False  #winning condition
    while (attempt < 5):  # Should have used [for attempt in range(5)]
        attempt += 1
        try:
            print("Attempt # {0}: Your Number => ".format(attempt),end=" ")
            numGuess = int(input())
        except ValueError as err:
            print("Error detected :{0} (Exiting game)".format(err))
            break
        if numGuess == num:
            print("Great job. Completed in {0} attempt(s)".format(attempt))
            winFlag = True
            break
        if attempt == 1:
            print("A good place to start as any")
            numPredict = numGuess
            continue
        if abs((num - numPredict)) > abs((num - numGuess)):
            print("Hotter")
        if abs((num - numPredict)) < abs((num - numGuess)):
            print("Colder")
        if abs((num - numPredict)) == abs((num - numGuess)):
            print("Luke warm!")
        numPredict = numGuess #replacing value for next turn
    if winFlag is False:
        print("Sorry {0}, looks like you couldn't guess the number {1} :(".format(name,num))


if __name__ == "__main__":
    guess()