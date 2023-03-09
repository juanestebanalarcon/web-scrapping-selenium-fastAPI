from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

def getHTMLContent(fileName:str):
    # Load HTML file into BeautifulSoup
    with open(f'../HTML_Transform/{fileName}.html', 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        # Extract text from HTML using the get_text() method
        text = soup.get_text()
        return text
def startSelenium(website:str,websiteName:str):
    # Set up the webdriver
    driver = webdriver.Chrome()
    # Navigate to the webpage to scrape
    driver.get(website)
    # Get the HTML document
    html_content =  driver.page_source
    #Close the webdriver
    driver.quit()
    # Write the HTML content to a file
    with open(f'../HTML_Transform/{websiteName}.html', 'w') as file:
        file.write(html_content)
    
async def htmlTranslate(websiteName:str):
    # Load HTML file into BeautifulSoup
    with open(f'../HTML_Transform/{websiteName}.html', 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
    # Extract text from HTML using the get_text() method
    text = soup.get_text()
    # Translate the text from English to Hindi using MyMemory API
    url = 'https://api.mymemory.translated.net/get?q=' + text + '&langpair=en|hi'
    response = await requests.get(url)
    translation = response.json()['responseData']['translatedText']
    # Replace the English text with the translated Hindi text in the HTML
    for string in soup.stripped_strings:
        if string in text:
            string.replace_with(translation)
    # Write the translated HTML to a new file
    with open(f'../templates_hindi/{websiteName}.html', 'w') as file:
        file.write(str(soup))
