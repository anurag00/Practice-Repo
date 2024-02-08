from bs4 import BeautifulSoup

# Path to your downloaded HTML file
html_file = "PAGE1.HTML"

# Open the file and parse it with BeautifulSoup
with open(html_file, "r") as f:
    soup = BeautifulSoup(f, "html.parser")

# Find the table containing the session list
#table = soup.find("table", class_="table table-hover session-list mb-0")
table = soup.find_all("div", style="max-width: 300px; word-break: break-all;")

#next_td = table.find_next_sibling("td")
#print(next_td.get_text(strip=True))

rows = []
session_date=[]
session_time=[]
for div in table:
    header_div = div.find("div")  # Find the first nested div within each div
    
    temp = div.find_next("td")    #find the date and time
    session_date.append(temp.find_next("td"))
    temp = temp.find_next("td")
    session_time.append(temp.find_next("td"))
    #print(session_date[-1].text.strip(),session_time[-1].text.strip())
    
    if header_div:      #find session id
        row = header_div.text.strip()
        rows.append(row)

anchor_tag = soup.find_all("a", target="_blank")

links_session = []      #collecting links
for x in anchor_tag:
    links_session.append(x.get("href"))

session_string = "https://in.ericssonremoteaccess2.com"
session_outputs = [session_string+links for links in links_session if "session" in links]

#print(session_outputs)

converted_times = []
for time in session_time:
    time = time.text.strip()
    time = time.replace(':',' ')
    # Extract hour, minute, and period
    hour, minute, period = time.split()

    # Convert period to single characters
    if period == "am":
        period = "a"
    elif period == "pm":
        period = "p"
    if int(hour) < 10:
        hour = hour[1:]
    # Combine and append converted time
    converted_time = f"{hour}:{minute}{period}"
    converted_times.append(converted_time)

#print(converted_times)

fixed_date = [links.text.strip() for links in session_date]

# rows = session id
# fixed_date
# converted_time
# session_outputs = links


x = len(rows)
for i in range(x):
    print(f"{converted_times[i]} {rows[i]}_{fixed_date[i]}_{session_outputs[i]}")

# Optional: Write to a new file
with open("UPDATE.txt", "w") as file:
    for i in range(x):
        file.write(f"{converted_times[i]} {rows[i]}_{fixed_date[i]}_{session_outputs[i]}\n")





