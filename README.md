## Logs Analysis Project - Udacity Full Stack Web Developer Nanodegree

#### DESCRIPTION
For this project, my task was to create a reporting tool that prints out reports( in plain text) based on the data in the given database. This reporting tool is a Python program using the `psycopg2` module to connect to the database.

#### QUESTIONS
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

#### CREATE THE FOLLOWING VIEWS FOR QUESTION 2 AND QUESTION 3:

##### Views for Question 2
    CREATE VIEW article_authors AS
    SELECT title, name
    FROM articles, authors
    WHERE articles.authors = authors,id;
----
    CREATE VIEW articles_views AS
    SELECT title, count(log.id) as views
    FROM articles, log
    WHERE log.path = CONCAT('/article/', articles.slug)
    GROUP BY articles.title
    ORDER BY views desc;

##### Views for Question 3
    CREATE VIEW logs AS
    SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as LogCount
    FROM log
    GROUP BY Date;
----    
    CREATE VIEW errorlogs AS
    SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as ErrorCount
    FROM log
    WHERE STATUS = '404 NOT FOUND'
    GROUP BY Date


#### RUNNING THE PROGRAM
1. To get started, you'll need to have virtual machine running on your computer. You need Vagrant and Virtual box to install and manage your virtual machine. Use `vagrant up` to bring the virtual machine online and `vagrant ssh` to login.

2. Download the data provided by Udacity [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). This file should be inside the Vagrant folder.

3. Load the database using `psql -d news -f newsdata.sql`. 

4. Connect to the database using `psql -d news`.

5. Create the Views given above. Exit `psql`.

6. Now execute the Python file - `python Logs_Analysis.py`.







