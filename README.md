# AI_Web_Arrow

## How I have started this project step by step

* created Git Repo with the name AI_Wen _Arrow

# Backend (Django + PostgreSQL)

##  1. Virtual Environment and activate it:
    Create Virtual environment and activate it

    ``` bash
        python -m venv .venv
        .venv\Scripts\activate
    ```

##  3. Install Dependencies
    Install Dependencies

    ``` bash
        pip install django 
        pip install djangorestframework 
        pip install psycopg2-binary 
        pip install django-cors-headers
    ```

## 2. Generate the requirements file after any dependency install

    ``` bash
        pip freeze > requirements.txt
    ``` 

## 3. Update your project 
    ``` bash
        pip install -r requirements.txt
    ```

##  4. Create Project

    ``` bash
        django-admin startproject ai_code
        cd ai_code
        python manage.py startapp interview_api

    ```

## 5. Create Apps
    ``` bash
        python manage.py startapp blog
        python manage.py startapp contact
        python python manage.py startapp interview apps/interview     
        # This will create app in folder                                             
    ```

## Python run migrations

    ``` bash
        python manage.py makemigrations
        python manage.py migrate
    ```

    to run miration for single app

    ``` bash
        python manage.py makemigrations appname
    ```

## Python start server
    python manage.py migrate

    ``` bash
        python manage.py runserver
    ```

# PostgreSQL Configuration

## 1.Create Database
    In PostgreSQL:

    ``` sql
        CREATE DATABASE ai_code_hack_db; 
    ```

## 2. Configure PostgreSQL
    Update settings.py

    ``` python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'ai_code_hack_db', // Database Name
                'USER': 'postgres',
                'PASSWORD': 'Pass@123',
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }
    ```

# Frontend (Angular)
##  1. Setup Angular Project
    ``` typescript
        ng new AI_Frontend
    ```