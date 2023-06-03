import requests
from bs4 import BeautifulSoup

def is_valid_input(ans):
    if ans.lower() == "q":
        return True
    elif ans.isdigit():
        return True
    else:
        return False

    
def parse(page=1): 
    url = f"https://news.ycombinator.com/?p={page}"
    r = requests.get(url, timeout=20)
    soup = BeautifulSoup(r.content, "html.parser")
    content = soup.find('table').find_all('span', class_="titleline")
    for i in content:
        title = i.text
        link = i.find('a').get('href')
        print(f"###########\n{title}: \n{link} \n###########\n")


while True:
    ans = str(input("Enter [x] number to show news from other page (q to quit): "))
    if not is_valid_input(ans):
        print("Invalid Input")
        continue
    elif ans.lower() == "q":
        break
    elif is_valid_input(ans):
        parse(ans)
        continue