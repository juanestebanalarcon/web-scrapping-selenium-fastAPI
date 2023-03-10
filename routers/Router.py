from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests
from pydantic import BaseModel, Field
from Services import getHtmlContentService as service
#Create a new router instance
router=APIRouter(prefix="/api",tags=["Scrapper"],responses={404:{"description":"Not found"}})
templates= Jinja2Templates(directory="templates_hindi")

class SeleniumBody(BaseModel):
    website:str
    websiteName:str
    tagName:str
    pageName:str
    case_:int

#Create endpoints:
@router.get("/getPageContent")
async def translateHTML(url:SeleniumBody):
    service.startSelenium(url.website,url.websiteName,url.tagName,url.pageName,url.case_)
    return {"message": "Scrapping complete"}
@router.get("/onlyTranslate")
async def translateToHindi(url:SeleniumBody):
    response = service.htmlTranslate(url.websiteName)
    return {"message": "Translation complete","response": response}
#Rendering HTML Content:
@router.get('/downloadSite')
def downloadSite(url:SeleniumBody):
    service.download_site(url.website,url.websiteName,url.pageName)
    return {'message':'Successfully downloaded'}