# FSND-Logs-Analysis





### CREATE THE FOLLOWING VIEWS FOR QUESTION 2 AND QUESTION 3:

#### QUESTION 2
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

#### QUESTION 3
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


