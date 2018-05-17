import webbrowser, bs4, requests, sys

def searchWord(word):
    '''
    open first 5 search results in google
    return : none
    '''
    res = requests.get("https://www.google.com/search?q=" + word)
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    elem = soup.select(".r a")
    numOpen = min(5,len(elem))
    for x in range(numOpen):
        webbrowser.open("https://www.google.com" + elem[x].get('href'))


if __name__ == "__main__":
    '''
    open chrome window for first 5 google search results
    takes commandline arguments
    '''
    if len(sys.argv) > 1:
        searchWord(' '.join(sys.argv[1:]))
    else:
        print("Enter a word or string of words to search =>", end=' ')
        word = input()
        searchWord(word)