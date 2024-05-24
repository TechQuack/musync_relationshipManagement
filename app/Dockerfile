FROM node:21.7.0-slim

# Python installation
RUN apt update -y --fix-missing \
    && apt install python3 python3-pip python3-flask python3-jsonpickle -y \
    && pip install kafka-python --break-system-packages
# Define workdir
WORKDIR /app

# NPM Configuration
RUN npm install -g npm

# Get npm config
COPY ./package.json ./package-lock.json /app/

# Tailwind installation
RUN npm install && npm install tailwindcss@3.4.1

# Get SQLALCHEMY

RUN apt-get update && \
    apt-get install python3 python3-pip -y && \
    apt install pip python3-psycopg2 python3-sqlalchemy -y && \
    apt install python3-flask && \
    apt install python3-flask-sqlalchemy && \
    apt install python3-flask-migrate -y && \
    apt install python3-alembic
WORKDIR /app


COPY init_db.py /app

# Copy project files
COPY . /app

EXPOSE 5000