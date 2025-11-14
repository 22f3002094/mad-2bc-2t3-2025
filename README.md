# Quizmaster
## By: Himanshu Saini
### 23f3002094 | Modern Application Development – II | IIT Madras
## Project Overview
This project is from the Modern Application Development - II course which is offered by IITM BS Degree during the Diploma in Programming. It is a multi-user app that acts as an exam preparation site for multiple courses. The platform provides both practice and exam modes for students to test their knowledge across various subjects and allows admins to create, manage, and analyse the quiz.

**🔗 Demo URL**:  
**👤 Demo User Login**: `himanshu@gmail.com` | **🔐 Password**: `pass`  
**👤 Demo Admin Login**: `admin@parksmart.com` | **🔐 Password**: `pass`

## Technologies used:
### Frontend:
- Vue 3 CLI - JavaScript framework for building user interfaces
- Bootstrap 5 - CSS framework for responsive design
- Chart.js - JavaScript library for data visualization
- Vue Router - Navigation management

  
### Backend:
- Flask - Python web framework
- Flask-SQLAlchemy - ORM for database interaction
- Flask-Security-too - Authentication handling
- Flask-Caching - Response caching

### Task Processing:
- Celery - Distributed task queue
- Redis - Message broker for Celery and caching  

## Setup Instructions:
Open the Project Folder:
```sh
cd Quizmaster_bootcamp/
``` 

### Backend
Open the Backend Folder:
```sh
cd backend/
``` 
1. Create and activate a virtual environment:
    ```sh
    python3 -m venv .myenv
    source .myenv/bin/activate  
    ```
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the backend server:
    ```sh
    python app.py
    ```
4. Run MailHog
    ```sh
    MailHog
    ```
5. Run Redis
    ```sh
    redis-server
    ```
    * if this gives error
        ```sh
        sudo systemctl stop redis
        sudo lsof -i :6379
        sudo kill -9 <pid>
        ```    
6. Run the Celery worker:
    ```sh
    celery -A app.celery worker --loglevel INFO
    ```
7. Run the Celery beat worker:
    ```sh
    celery -A app.celery beat --loglevel INFO
    ```    
8. Open the App:
    ```sh
    http://127.0.0.1:5000
    ```

### frontend
```sh
cd frontend/
``` 

1. Install All Required Packages:
```
npm install
```
2. Start the Vue Development Server:
### Compiles and hot-reloads for development
```
npm run serve
```
