# Launch the app
firefox http://127.0.0.1:5000/ &
uvicorn rpi_clock.app:app --reload --port 5000 --host 127.0.0.1;
