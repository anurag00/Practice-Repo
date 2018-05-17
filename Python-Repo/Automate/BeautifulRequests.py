import requests, bs4

def getAmazonPrice(producturl):
    res = requests.get(producturl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    elems = soup.select('#priceblock_ourprice')
    return elems[0].text.strip()

if __name__ == "__main__":
    price = getAmazonPrice('https://www.amazon.in/gp/product/B073JYVKNX/ref=ox_sc_sfl_title_1?ie=UTF8&psc=1&smid=A14CZOWI0VEHLG')
    print('Price is Rupees ' + price)