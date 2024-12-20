# Social Media

This project was developed as part of a course at the Faculty of Technical Sciences in Novi Sad, for the subject Distributed Computer Systems.

Social Media is a full-stack application designed for connecting users. It features secure user authentication, post sharing, and admin functionality. This project demonstrates how to build and deploy a Dockerized full-stack application with Flask, Angular, MySQL, and Docker.

## Built using

- &nbsp;<img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg" align="center" width="28" height="28"/> <a href="https://flask.palletsprojects.com">Flask</a>
- &nbsp;<img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/Angular_full_color_logo.svg" align="center" width="28" height="28"/> <a href="https://angular.io">Angular</a>
- &nbsp;<img src="https://www.vectorlogo.zone/logos/mysql/mysql-icon.svg" align="center" width="28" height="28"/> <a href="https://www.mysql.com">MySQL</a>
- &nbsp;<img src="https://www.vectorlogo.zone/logos/docker/docker-icon.svg" align="center" width="28" height="28"/> <a href="https://www.docker.com">Docker</a>

## Installation:

To run this project, make sure you have the following installed:
  - Node.js: [Download and install Node.js](https://nodejs.org/)
  - Python: [Download and install Python](https://www.python.org/)
  - MySQL: [Download and install MySQL](https://dev.mysql.com/downloads/)
  - MySQL Workbench: [Download and install MySQL Workbench](https://dev.mysql.com/downloads/workbench/)
  - Docker Desktop: [Download and install Docker Desktop](https://www.docker.com/products/docker-desktop/)

After installing these dependencies, follow the setup instructions to get the project running.
  
## How to run:

<details>
  <summary>Running with Docker</summary>

  The easiest way to run the application is by using Docker

1. **Clone the project**:

   Clone the repository and navigate to the Project_DRS_Social_Media project directory:

   ```bash
   git clone https://github.com/Acile067/Project_DRS_Social_Media.git
   cd Project_DRS_Social_Media/backend
   ```

2. **Build docker image (backend)**:

   ```bash
   docker build -t my-python-app .
   ```

3. **Build docker image (frontend)**:

   ```bash
   cd ..
   cd frontend/DRS_frontend
   docker build -t angular-app .
   ```

4. **Create docker network**:

   ```bash
   docker network create my_network
   ```

5. **Run docker containers**:

   ```bash
   docker run --name mysql_db --network my_network -e MYSQL_ROOT_PASSWORD=MySQLPassword1 -e MYSQL_DATABASE=appDB -p 3307:3306 -d mysql:8.0
   docker run --name python_app --network my_network -p 5000:5000 -d my-python-app
   docker run --name angular_app --network my_network -p 4200:4200 -d angular-app
   ```
   
6. **Migrate tables**:

   Before migrating the tables, you need to connect to the database and create the `appDB` database.

   Create a new connection in MySQL Workbench using the following settings:  

    - **Port**: 3307  
    - **Password**: MySQLPassword1 

   **Create the `appDB` manually then type**

    ```bash
    docker exec -it python_app /bin/bash
    flask --app app.app db init
    flask --app app.app db migrate
    flask --app app.app db upgrade
    ```
   
7. **Add admin in db**:  

    Fill in a row in the table to create an admin with the following values:  
    - **isAdmin**: yes  
    - **isNewUser**: no  
    - **RejectedPostCount**: 0
    - **Email**: x@x  
    - Fill in the remaining fields as desired (fields must not be null).
      
</details>

<details>
  <summary>Running Locally</summary>

  Alternatively, you can run the project locally.
  
1. **Clone the project**:

   Clone the repository and navigate to the Project_DRS_Social_Media project directory:

   ```bash
   git clone https://github.com/Acile067/Project_DRS_Social_Media.git
   cd Project_DRS_Social_Media/
   ```

2. **Run frontend**:

   You must have Angular installed globally to run the `ng serve` command.

   To install Angular globally, use the following command:
  
   ```bash
   npm install -g @angular/cli
   ```

   ```bash
   cd frontend/DRS_frontend
   npm i
   ng serve
   ```
   
    If `ng serve` does not work, try running:

    ```bash
    npm run ng serve
    ```

3. **Create database**:

   Create a local database on port 3306 with the password `MySQLPassword1`. You can use a different password, but it is important to remember it.
   
   **Create the `appDB` manually**.

4. **Run backend**:

   Navigate to the `backend` folder.

   ```bash
   py -m venv .venv
   ```

   or 

   ```bash
   python -m venv .venv
   ```

   or 

   ```bash
   python3 -m venv .venv
   ```

   It depends on the version of Python you have.

   ---

   ```bash
   cd .venv/bin
   ```

   or

   ```bash
   cd .venv/Scripts
   ```

   ---

   ```bash
   ./activate
   cd ../../
   ```

   Replace the following line:

    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:MySQLPassword1@mysql_db:3306/appDB'
    ```

    with this one:

    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:MySQLPassword1@127.0.0.1/appDB'
    ```

    It is important to set the correct password (`MySQLPassword1`).

    This change can be made in the `app.py` file.

    ---

   ```bash
   pip3 install -r requirements.txt
   cd app
   flask db migrate
   flask db upgrade
   ```

   **RUN `run.py`**
   
   ```bash
   cd ..
   py ./run.py
   ```      

5. **Add admin in db**:  

    Fill in a row in the table to create an admin with the following values:  
    - **isAdmin**: yes  
    - **isNewUser**: no  
    - **RejectedPostCount**: 0
    - **Email**: x@x  
    - Fill in the remaining fields as desired (fields must not be null).
   
</details>

---

# Common Issues:

Q1: What if I encounter an error during table migration?

A1: Ensure the database appDB is created and the password in app.py matches the MySQL credentials.

Q2: The migrations folder is causing issues

A2: Feel free to delete it, as well as the alembic_version table in the database, and try running the migration again.  

  
