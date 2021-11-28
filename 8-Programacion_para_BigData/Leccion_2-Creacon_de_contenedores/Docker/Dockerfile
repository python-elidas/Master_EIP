FROM python:3.8
RUN pip install fastapi uvicorn
EXPOSE 80
COPY ./app /app
CMD ["uvicorn", "app.Leccion_2-Docker:app", "--host", "0.0.0.0", "--port", "80"]
