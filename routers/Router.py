from fastapi import APIRouter, File,UploadFile,Request
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

#Create endpoints:
@router.get("/translateToHindi")
async def translateHTML(url:SeleniumBody):
    await service.startSelenium(url.website,url.websiteName)
    await service.htmlTranslate(url.websiteName)
    return {"message": "Translation complete"}
@router.get("/onlyTranslate")
async def translateToHindi(url:SeleniumBody):
    await service.htmlTranslate(url.websiteName)
    return {"message": "Translation complete"}
#Rendering HTML Content:
