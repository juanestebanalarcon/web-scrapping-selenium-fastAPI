from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from googletrans import Translator
from time import sleep

def getHTMLContent(fileName:str):
    # Load HTML file into BeautifulSoup
    with open(f'../HTML_Transform/{fileName}.html', 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        # Extract text from HTML using the get_text() method
        text = soup.get_text()
        return text
def startSelenium(website:str,websiteName:str):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # Set up the webdriver
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    counter = 0
    sleep(2)
    # Navigate to the webpage to scrape
    driver.get(website)
    print(f'Loading wbesite: {website}')
    sleep(3)
    # Get the HTML document
    print(f'Getting page source \n')
    html_content =  driver.page_source
    # Write the HTML content to a file
    print(f'Homepage name: {websiteName}')
    sleep(2)
    with open(f'./HTML_Transform/{websiteName}.html', 'w') as file:
        soup = BeautifulSoup(html_content, 'html.parser')
        print(f'Writting html source of {websiteName} \n')
        file.write(str(soup))
    sleep(2)
    print(f'Getting websites from {websiteName} using <a> tags...')
    sleep(2)
    # navigate to other pages on the website
    links = driver.find_elements(By.CSS_SELECTOR,'a')
    print(f"Getting websites from {websiteName} using <a> tags... [DONE]")
    sleep(2)
    for link in links:
        href = link.get_attribute('href')
        print(f'Fetching website {href}...')
        sleep(1)
        driver.get(href)
        sleep(3)
        print("Getting page source of each page on the website")
        # get the page source of each page
        page_content = driver.page_source
        sleep(2)
        print(f"Saving Page content: {href}...")
        with open(f'./HTML_Transform/_{counter}_.html', 'w') as file:
            soup = BeautifulSoup(page_content, 'html.parser')
            file.write(str(soup))
        sleep(3)
        print(f"Saving Page content: {link}...[DONE]")
        ++counter
    #Close the webdriver
    driver.quit()


def htmlTranslate(websiteName:str):
    # Initialize the translator
    translator = Translator(service_urls=['translate.google.com'])
    # Load HTML file into BeautifulSoup
    with open(f'./HTML_Transform/{websiteName}.html', 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
    htmlToTransform = soup.get_text()
    translatedHtml = translator.translate(htmlToTransform,src='en',dest='hi')
    for element in soup.find_all(text=True):
        if element.parent.name not in ['style', 'script', 'head', 'title', 'meta','body','html','footer']:
            element.replace_with(translatedHtml.text)
    # Write the translated HTML to a new file
    with open(f'./templates_hindi/{websiteName}.html', 'w') as file:
        file.write(str(soup))
    return str(soup)
