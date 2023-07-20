# Flask Job Board App

![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

This project is open for contributions from anyone who is interested. If you want to contribute, please check the GitHub issues page and pick an issue that you can work on. You can also create a new issue if you have an idea or a suggestion. Please follow the code of conduct and the contribution guidelines when submitting your pull requests.

To contribute, please follow these steps:

- Fork this repository and clone it to your local machine.
- Create a new branch with a descriptive name for your changes.
- Make your changes and commit them with clear and concise messages.
- Push your branch to your forked repository and create a pull request to the main branch of this repository.
- Wait for feedback and approval from the maintainers.

Please make sure to follow the code style and conventions of this project, and to test your changes before submitting them.



# Flask WebAPP
It contains 

- JOB listing
- Form by which one can apply to job
- Acknowledgedment Page After form Submission
- API for data 

# DataBase
  DataBase is made using **[MySQL](https://www.mysql.com/products/workbench/)** and stored at **[PlanetSclae](https://planetscale.com/docs)**

```
CREATE TABLE jobs(
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(250) NOT NULL,
    location VARCHAR(250) NOT NULL,
    salary INT,
    currency VARCHAR(10),
    responsibilities VARCHAR(2000),
    requirements TEXT,
    PRIMARY KEY (id)
);

create table applications (
	id INT not null auto_increment,
	job_id int not null,
	full_name varchar(250) not null,
	email varchar(250) not null,
	linkedin_url varchar(2000),
	work_experience varchar(2000),
	resume_url varchar(500),
	created_at timestamp default current_timestamp,
	updated_at timestamp default current_timestamp on update current_timestamp,
	primary key (id)
);
```




This documentation provides an overview of the Flask Job Board web application. The application serves both HTML pages and API endpoints to list and view job listings. The app also allows users to apply to specific job listings and store their application data.

## Table of Contents

1. [Introduction](#introduction)
2. [Routes](#routes)
3. [Database](#database)
4. [Usage](#usage)
5. [API Endpoints](#api-endpoints)
6. [Contributing](#contributing)
7. [License](#license)

## 1. Introduction

The Flask Job Board web application is designed to list job postings, provide detailed information about individual jobs, and allow users to apply to specific jobs. It combines HTML routes for user-friendly pages and API routes to serve job data in JSON format.

## 2. Routes

### Home Route

- **URL**: `/`
- **Description**: Displays the home page with a list of all available job listings.
- **Method**: GET

### Job Page Route

- **URL**: `/job/<id>`
- **Description**: Displays detailed information about a specific job listing.
- **Method**: GET

### Apply to Job Route

- **URL**: `/job/<id>/apply`
- **Description**: Allows users to apply to a specific job by submitting their application data.
- **Method**: POST

## 3. Database

The application uses a database to store job listings and user job applications. The `database.py` file contains the necessary functions to interact with the database, including loading job listings, retrieving individual job details, and adding job applications.

## 4. Usage

1. Clone the repository from GitHub:
```
git clone https://github.com/your-username/flask-job-board.git
```



2. Navigate to the project directory:
```
cd flask-job-board
```



3. Install the required dependencies:
```
pip install Flask
```



4. Run the application:
```
python app.py
```

5. Open your web browser and navigate to `http://localhost:5000/` to access the Job Board app.

## 5. API Endpoints

### List All Jobs

- **URL**: `/api/jobs`
- **Description**: Returns a JSON array containing all job listings.
- **Method**: GET

### Show Job Details

- **URL**: `/api/job/<id>`
- **Description**: Returns a JSON object containing detailed information about a specific job listing.
- **Method**: GET

## 6. Contributing

Contributions to the Flask Job Board web application are welcome. If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request on GitHub.

## 7. License

The Flask Job Board web application is open-source software released under the [MIT License](LICENSE).

---
This concludes the documentation for the Flask Job Board web application. Thank you for using our Job Board app! 📝🏢

# Preview

![PREVIEW](https://github.com/Kool-Cool/dump-/blob/main/ezgif.com-gif-maker.gif)
