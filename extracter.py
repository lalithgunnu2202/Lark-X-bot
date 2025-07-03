import requests
from bs4 import BeautifulSoup

# to find number of jounals present in website
url = "https://lark-blog.onrender.com/personal/journals/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

target_div = soup.find("div", class_="journal-list")

if target_div:
    anchor_tags = target_div.find_all("a")
    num = int(len(anchor_tags)/2)
else:
    print("Target div not found")

# to view and read journal info
url = f"https://lark-blog.onrender.com/personal/view_journal/{num}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    sections = soup.find_all("div", class_="journal-section")
    n=1
    for section in sections:
        title_tag = section.find('h2')
        content_tag = section.find('p')
        title = title_tag.text.strip() if title_tag else "No Title"
        content = content_tag.text.strip()
        with open(f"journal_{n}.txt","w") as f:
            f.write(title +":"+content)
        n=n+1
    print("files created")
        

else:
    print(f"Failed to fetch page. Status Code: {response.status_code}")
