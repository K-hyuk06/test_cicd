FROM python:3.8.17-slim
RUN apt update -y
WORKDIR /app
COPY app.py /app
RUN pip install pytest
ENTRYPOINT ["pytest","/app/test_app.py"]