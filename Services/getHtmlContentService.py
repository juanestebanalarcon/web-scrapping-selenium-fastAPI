from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from deep_translator import MyMemoryTranslator
from time import sleep
import os
import requests

def getHTMLContent(fileName:str):
    # Load HTML file into BeautifulSoup
    with open(f'./HTML_Transform/{fileName}.html', 'r') as file:
        html = file.read()
        soup = BeautifulSoup(html, 'html.parser')
    return soup
def saveHtmlContent(fileName:str,html_content):
    with open(f'./HTML_Transform/{fileName}.html', 'w') as file:
            soup = BeautifulSoup(html_content, 'html.parser')
            print(f'Writting html source of {fileName} \n')
            file.write(str(soup))
def startSelenium(website:str,websiteName:str,tagName:str,pageName:str,case_:int):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # Set up the webdriver
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    counter = 0
    sleep(2)
    if case_ == 1:
        html = getHTMLContent(websiteName)
        soup = BeautifulSoup(html, 'html.parser')
        # Find the <ul> list you want to extract href values from
        ul_list = soup.find('ul', {'class': tagName})
        # Create an empty list to store the href values
        href_list = []
        links = []
        # Loop through all <a> tags in the <ul> list and extract the href values
        print('Extracting href values')
        for a_tag in ul_list.find_all('a'):
            href = a_tag.get('href')
            href_list.append(href)
        sleep(2)
        print('Extracting href values and joining them with a new link')
        for href in href_list:
            links.append(str.join(website,href))
        sleep(2)
        for link in links:
            print(f'Getting page source of {link}')
            sleep(2)
            driver.get(link)
            sleep(3)
            pageSource = driver.page_source
            sleep(3)
            print(f'Saving page source of {link}')
            saveHtmlContent(href.split('/','_',pageSource))
            sleep(3)
        print('Getting all page sources of link list [DONE]')
    else:   
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
        saveHtmlContent(websiteName,html_content)
        sleep(2)
    #Close the webdriver
    driver.quit()


def htmlTranslate(websiteName:str):
    translated = MyMemoryTranslator(source='en',target='hi').translate_file(f'./HTML_Transform/{websiteName}.html')
    saveHtmlContent('prueba',translated)

def download_site(url, folder_name,fileName:str):
    # Create folder to store downloaded content
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Send request to get HTML content of the page
    response = requests.get(url)
    
    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Download all linked resources (e.g. images, CSS, JavaScript)
    for link in soup.find_all('link'):
        link_href = link.get('href')
        if link_href and not link_href.startswith('http'):
            download_resource(url + link_href, folder_name)
    
    for script in soup.find_all('script'):
        script_src = script.get('src')
        if script_src and not script_src.startswith('http'):
            download_resource(url + script_src, folder_name)
    
    for img in soup.find_all('img'):
        img_src = img.get('src')
        if img_src and not img_src.startswith('http'):
            download_resource(url + img_src, folder_name)
    
    # Save HTML content to a file
    with open(os.path.join(folder_name, f'{fileName}.html'), 'wb') as file:
        file.write(response.content)

def download_resource(url, folder_name):
    # Send request to get content of the resource
    response = requests.get(url)
    
    # Save content to a file
    file_path = os.path.join(folder_name, url.split('/')[-1])
    with open(file_path, 'wb') as file:
        file.write(response.content)
