#! python3

import os, bs4, requests, logging, re
logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

def downloadImages():
    first = True  # exception for first comic name
    downloadFinish = 0 # total images downloaded
    downloadUnfinished = 0   # number of times couldn't find image
    url = 'https://xkcd.com'  #starting url
    os.makedirs(r'F:/xkcd', exist_ok=True)
    while not url.endswith('#'):
        logging.debug("Start of while loop")
        #Download the page
        res = requests.get(url)
        tempRes = res
        res.raise_for_status()
        # try:
        #     res.raise_for_status()
        # except Exception as ex:
        #     print("Exception Occured: " + ex.value)         
        soup = bs4.BeautifulSoup(res.text,'html.parser')

        #Find the URL of the comic image
        comicElem = soup.select('#comic > img')
        if comicElem == []:
            print("Couldn't Find Comic")
            downloadUnfinished += 1
        else:
            try:
                #logging.debug(comicElem[0].get('src'))
                comicUrl = "https:" + comicElem[0].get('src')
                #downloading image
                print("Downloading image %s..." %(comicElem[0].get('alt')))
                res = requests.get(comicUrl)
                res.raise_for_status()
                downloadFinish += 1
            except requests.exceptions.MissingSchema:
                #skpping this comic
                prevLink = soup.select('a[rel="prev"]')[0]
                logging.debug("Previous link (skipped comic) " + str(prevLink))
                url = "https://xkcd.com" + prevLink.get('href')
                continue

        #Save the image to F:/xkcd
        logging.debug("Saving the file")
        if first:
            #add file number from plain text written on the site
            textRegex = re.compile(r'Permanent link to this comic: https://xkcd.com/(\d\d\d\d)')
            mo = textRegex.findall(tempRes.text)
            logging.debug(textRegex)
            imageFile = open(os.path.join("F:\\xkcd", mo[0] + '-' + os.path.basename(comicUrl)),'wb')
            #imageFile = open(os.path.join("F:\\xkcd", os.path.basename(comicUrl)),'wb')
            first = False
        else:
            imageFile = open(os.path.join("F:\\xkcd", prevLink.get('href').strip('/') + '-' + os.path.basename(comicUrl)),'wb')
        #imageFile = open(os.path.join("F:\\xkcd", os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

        #Get the Prev Button's url.
        prevLink = soup.select('a[rel="prev"]')[0]
        logging.debug("Previous link " + str(prevLink))
        url = "https://xkcd.com" + prevLink.get(('href'))

        print("Done")
    print("Finished = " + str(downloadFinish) + ", Couldn't find = " + str(downloadUnfinished))

if __name__ == "__main__":
    '''
    download all the images from xkcd
    '''
    downloadImages()