# !usr/bin/env python

# Logs Analysis Project

# Import postgresql library
import psycopg2

DBNAME = "news"


def connect(query):
	# Connect to database
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # Execute queries
    c.execute(query)
    # Fetch results
    return c.fetchall()
    db.close()

# Create Views for Question 2 and Question 3 as instructed on the README file.

# Question 1. What are the most popular three articles of all time?
query1 = """SELECT title, COUNT(log.id) AS views
            FROM articles, log
            WHERE log.path = CONCAT('/article/', articles.slug)
            GROUP BY articles.title
            ORDER BY views desc
            LIMIT 3;"""


def top_three_articles(query):
    results = connect(query)
    print('\n Displaying the most popular articles of all time:\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' views')
        print(" ")

# Question 2. Who are the most popular article authors of all time?
query2 = """SELECT name, sum(article_views.views) AS views
            FROM article_authors, article_views
            WHERE article_authors.title = article_views.title
            GROUP BY name
            ORDER BY views desc;"""


def top_authors(query):
    results = connect(query)
    print('\n Displaying the most popular authors of all time:\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' views')
        print(" ")

# Question 3. On which days did more than 1% of requests lead to errors?
query3 = """SELECT errorlogs.date, (100.0*errorcount/logcount) as percent
            FROM logs, errorlogs
            WHERE logs.date = errorlogs.date
            AND errorcount > logcount/100;"""


def error_percentage(query):
    results = connect(query)
    print('\n The days when more than 1% of requests lead to error:\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' %' + ' errors')
        print(" ")

# Print results
top_three_articles(query1)
top_authors(query2)
error_percentage(query3)
