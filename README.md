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
