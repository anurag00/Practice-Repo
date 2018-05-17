import requests
res = requests.get(r'https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)
res.raise_for_status() # raises an exception if error occurs


print('length = '+str(len(res.text)))
print(res.text[:100])

playFile = open(r'G:\Anurag\RomeoAndJuliet.txt','wb')
for chunk in res.iter_content(50000):
    print(playFile.write(chunk))
playFile.close()