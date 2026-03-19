import requests
import re
from bs4 import BeautifulSoup

chapName = "GEN" #input("Enter Chapter name (e.g Gẹnẹsisi): ")
check = 2 #int(input("Enter total number: "))
startNum = 1


url = f"https://www.bible.com/bible/911/{chapName}.{startNum}.BMYO"

response = requests.get(url)
if response.status_code == 200:
  htmlContent = BeautifulSoup(response.text, 'html.parser')
  spans = htmlContent.select('span.ChapterContent-module__cat7xG__content')
  
  with open('yorubaWord.txt', 'r', encoding="utf-8") as file:
    existing_words = set(line.strip() for line in file if line.strip())
  with open('yorubaWord.txt', 'a', encoding="utf-8") as file:
    for span in spans:
      texts = span.get_text(strip=True)
      words = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿẸỌṢẹọṣ̀́]+", texts)
    
      for word in words:
        if word != "Search":
          if word not in existing_words:
            file.write(word)
            print(word)
            existing_words.add(word)
else:
  print(f"Not able to Retrieve {chapName} @ {startNum}")

