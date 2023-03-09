from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the webdriver
driver = webdriver.Chrome()

def getHTMLContent(fileName:str):
    # Load HTML file into BeautifulSoup
    with open(f'../HTML_Transform/{fileName}.html', 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        # Extract text from HTML using the get_text() method
        text = soup.get_text()
        return text
def startSelenium(website:str):
    # Navigate to the webpage to scrape
    driver.get(website)
    # Get the HTML document
    html_content = driver.page_source
    #Close the webdriver
    driver.close()
    
def saveHTMLFile(html_content:str,websiteName:str):
    # Write the HTML content to a file
    with open(f'../HTML_Transform/{websiteName}.html', 'w') as file:
        file.write(html_content)
    
    