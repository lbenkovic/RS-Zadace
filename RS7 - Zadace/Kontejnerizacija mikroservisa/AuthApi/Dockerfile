FROM python:3.11-slim
WORKDIR /app
COPY authApi.py /app/
RUN pip install aiohttp
EXPOSE 9000
CMD ["python", "authApi.py"]
