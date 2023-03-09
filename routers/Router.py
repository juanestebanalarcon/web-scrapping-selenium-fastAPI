from fastapi import APIRouter, File,UploadFile,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

#Create a new router instance
router=APIRouter(prefix="/api",tags=["Scrapper"],responses={404:{"description":"Not found"}})

#Create endpoints:
@router.get("/translateToHindi")
async def translateHTML(file:UploadFile=File()):
    pass


