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

# Preview

![PREVIEW](https://github.com/Kool-Cool/dump-/blob/main/ezgif.com-gif-maker.gif)
