import requests, os, logging
logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)

imageURL = ['https://f.cyberdrop.nl/ice queen (34)-aXwsMDck.jpg', 'https://f.cyberdrop.nl/ice queen (35)-voCV3aPW.jpg', 'https://f.cyberdrop.cc/ice queen (33)-BMdMsznh.jpg', 'https://f.cyberdrop.nl/ice queen (32)-ZThjDgGi.jpg', 'https://f.cyberdrop.cc/ice queen (29)-W6IbDLHI.jpg', 'https://f.cyberdrop.nl/ice queen (27)-6jSiTkj9.jpg', 'https://f.cyberdrop.nl/ice queen (30)-V4jlpnv0.jpg', 'https://f.cyberdrop.nl/ice queen (31)-U5gh4UhB.jpg', 'https://f.cyberdrop.nl/ice queen (26)-J4uv2dnE.jpg', 'https://f.cyberdrop.nl/ice queen (28)-D1YYGRm5.jpg', 'https://f.cyberdrop.nl/ice queen (21)-vkbq8CnW.jpg', 'https://f.cyberdrop.nl/ice queen (23)-Di5NJnY9.jpg', 'https://f.cyberdrop.cc/ice queen (24)-DBvEFOJc.jpg', 'https://f.cyberdrop.nl/ice queen (25)-9LQa7ee0.jpg', 'https://f.cyberdrop.nl/ice queen (19)-cqspeSKo.jpg', 'https://f.cyberdrop.cc/ice queen (16)-78GiLiJe.jpg', 'https://f.cyberdrop.nl/ice queen (22)-gWNjw832.jpg', 'https://f.cyberdrop.nl/ice queen (18)-ud7WR6jw.jpg', 'https://f.cyberdrop.nl/ice queen (20)-awR62NNM.jpg', 'https://f.cyberdrop.nl/ice queen (17)-jRoqxPZv.jpg', 'https://f.cyberdrop.cc/ice queen (12)-YvHzFzVx.jpg', 'https://f.cyberdrop.nl/ice queen (14)-EmlcUkb9.jpg', 'https://f.cyberdrop.cc/ice queen (15)-qFGVsjHv.jpg', 'https://f.cyberdrop.cc/ice queen (11)-v7ACkUQG.jpg', 'https://f.cyberdrop.nl/ice queen (6)-0oRNTWSE.jpg', 'https://f.cyberdrop.nl/ice queen (8)-anigbt24.jpg', 'https://f.cyberdrop.cc/ice queen (5)-ecGHwBZS.jpg', 'https://f.cyberdrop.cc/ice queen (9)-ICmnm2gR.jpg', 'https://f.cyberdrop.nl/ice queen (7)-giJWWCGf.jpg', 'https://f.cyberdrop.nl/ice queen (1)-ghM6PKEa.jpg']

dir = "/home/pi/Downloads/Luxlo/Test"
os.makedirs(dir, exist_ok=True)
logging.debug('Made dir')

res = requests.get(imageURL[0])
res.raise_for_status()
logging.debug('Recieved Image')

imageFile = open(os.path.join(dir, str(imageURL[0])[-10:]),'wb')
logging.debug('Saving image')

for chunk in res.iter_content(100000):
    imageFile.write(chunk)
imageFile.close()
logging.debug('Image saved')
