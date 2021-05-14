"""Small fastapi app served by the RPI controlling the FPGA.

Author: Romain Fayat, May 2021
"""
from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import Optional
from pathlib import Path
# from .clock import Clock_Handler

# Initialize the app
app = FastAPI()
templates = Jinja2Templates(directory="rpi_clock/templates/")

@app.get("/")
async def home(request: Request):
    "Home page for starting and stopping the clock"
    return templates.TemplateResponse("menu.html", context={"request": request})

@app.get("/start")
async def start():
    "Start the fpga clock"
    return RedirectResponse("/")

@app.get("/stop")
async def stop():
    "Stop the fpga clock"
    return RedirectResponse("/")
