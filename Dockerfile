FROM python:3.11-slim
LABEL authors="VS-CDR"

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

EXPOSE 8000
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]