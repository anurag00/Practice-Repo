import bs4, requests, os, logging, time
logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)

def CallURL(url, dir):

    try:
        res = requests.get(url)
        res.raise_for_status()
    except:
        return
    soup = bs4.BeautifulSoup(res.text,"html.parser")

    ###Finding file name
    folderName = url
    for link in soup.find_all('meta'):
        if link.get('property') == "og:title":
            folderName = link.get('content')
    print(folderName)
    folderName = folderName[7:-15]
    dir += folderName
    os.makedirs(dir, exist_ok=True)
    logging.debug('Made dir')

    #print(soup.img)
    listFind = ['image']
    for link in soup.find_all('a'):
        if link.get('class') == listFind:
            print(link.get('href')+" -- "+link.get('title'))
            ###Downloading the image
            try:
                res = requests.get(link.get('href'))
                res.raise_for_status()
            except:
                logging.debug('Image not found')
                continue
            logging.debug('Recieved Image')

            imageFile = open(os.path.join(dir, link.get('title')),'wb')
            logging.debug('Saving image')

            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
            logging.debug('Image saved')
            

if __name__ == "__main__":
    dir = "G:\\Luxlo\\"
    CallURL("https://cyberdrop.me/a/ecsg88bx",dir)
    