# @author juanestebanalarcon - Backend Developer
from fastapi import FastAPI
from routers import Router
# Initialize the API:
app = FastAPI(title="Web Scraper", description="Web scraper using FastAPI and Selenium, developed by Juan Esteban Alarcón Miranda")
app.include_router(Router.router)
