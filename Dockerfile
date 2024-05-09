# Dockerfile

FROM python:3.12

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

# Expose the port your Django app runs on
EXPOSE 8000

CMD ["gunicorn", "social_network.wsgi:application", "--bind", "0.0.0.0:8000"]