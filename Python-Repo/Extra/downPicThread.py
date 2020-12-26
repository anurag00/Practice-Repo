import bs4, requests, os, logging, threading
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
    
    f = open('links.txt','r')
    count = 0
    link=[]
    for line in f:
        count += 1
        link.append(line)
    print(count)
    f.seek(0)

    #Starting Threading
    downloadThreads = []
    for x in range(0,count,10): #10 Threads running
        for y in range(1,11):
            if (x+y) > count:
                break
            else:
                downloadThread = threading.Thread(target=CallURL,args=(str(link[x+y].strip()),dir))
                downloadThreads.append(downloadThread)
                downloadThread.start()

    #Waiting for threads to end
    for downloadThread in downloadThreads:
        downloadThread.join()

    print("Done.")
    #CallURL("https://cyberdrop.me/a/ecsg88bx",dir)
    