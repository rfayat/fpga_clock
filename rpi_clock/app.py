"""Small fastapi app served by the RPI controlling the FPGA.

Author: Romain Fayat, May 2021
"""
from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import Optional
from pathlib import Path
from .clock import Clock_Handler

# Initialize the app
app = FastAPI()
templates = Jinja2Templates(directory="rpi_clock/templates/")
clock_handler = Clock_Handler(verbose=True)

@app.get("/")
async def home(request: Request):
    "Home page for starting and stopping the clock"
    enable_state = clock_handler.enable_state
    context = {"request": request, "enable_state": enable_state}
    return templates.TemplateResponse("menu.html", context=context)

@app.get("/start")
async def start():
    "Start the fpga clock"
    clock_handler.enable()
    return RedirectResponse("/")

@app.get("/stop")
async def stop():
    "Stop the fpga clock"
    clock_handler.disable()
    clock_handler.reset()
    return RedirectResponse("/")
