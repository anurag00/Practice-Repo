import requests
from bs4 import BeautifulSoup

try:
    response = requests.get('https://in.ericssonremoteaccess2.com/sessions')
    print("Response available")
except requests.exceptions.RequestException as e:
    print(e)  # Print the specific error message
    print("Failed")
    exit(1)
    
soup = BeautifulSoup(response.content, 'html.parser')
titles = [element.text.strip() for element in soup.find_all("tbody")]
          
# 2. Find all elements with class "fc-content"
fc_content_elements = soup.find_all("td")

# 3. Extract and append "fd-time" and "fd-title" for each element
extracted_data = []
for element in fc_content_elements:
    print(element)
    extracted_data.append(element)
    #fd_time = element.find("span", class_="fc-time").text.strip()
    #fd_title = element.find("span", class_="fc-title").text.strip()
    #extracted_data.append((fd_time, fd_title))

# 4. Print or use the extracted data as needed
print(extracted_data)

# Optional: Write to a new file
with open("main.txt", "w") as file:
    for time, title in extracted_data:
        file.write(f"{time}_{title}\n")
