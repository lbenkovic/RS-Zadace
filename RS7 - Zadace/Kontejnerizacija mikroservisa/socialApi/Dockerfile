FROM python:3.11-slim
WORKDIR /app
COPY . /app/
RUN pip install fastapi uvicorn
EXPOSE 3500
CMD ["uvicorn", "socialApi:app", "--host", "0.0.0.0", "--port", "3500"]