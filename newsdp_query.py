import psycopg2
# database name
DBName = "news"

"""Defin a function to Return the most popular three articles of all time"""


def get_articles_Q1():
    conn = psycopg2.connect(database=DBName)
    c = conn.cursor()
    c.execute("""SELECT articles.title,count(log.path) AS views
                 FROM articles JOIN log ON log.path
                 LIKE CONCAT('%', articles.slug, '%')
                 WHERE log.status = '200 OK' AND log.path !='/'
                 GROUP BY articles.title
                 ORDER BY views DESC
                 LIMIT 3""")
    articles_results = c.fetchall()
    print"1. What are the most popular three articles of all time? ", "\n"
    for row in articles_results:
        print '"', row[0], '"- ', row[1], " views"

"""Defin a function to Return  the most popular article authors of all time """


def get_article_authors_Q2():
    conn = psycopg2.connect(database=DBName)
    c = conn.cursor()
    c.execute("""SELECT authors.name, count(log.id) AS views
                 FROM authors, log, articles
                 WHERE log.path LIKE CONCAT('%', articles.slug, '%')
                 AND status='200 OK' AND path !='/'
                 AND articles.author = authors.id
                 GROUP BY authors.name
                 ORDER BY views DESC""")
    authors_reuslt = c.fetchall()
    print "2 : Who are the most popular article authors of all time?", "\n"
    for row in authors_reuslt:
        print row[0], "-", row[1], " views"

"""Defin a function to return days did more than 1% of requests lead to errors """  # NOQA


def get_day_requests_Q3():
    conn = psycopg2.connect(database=DBName)
    c = conn.cursor()
    c.execute("""SELECT  error_date, error_percent
                FROM log_error_view
                WHERE error_percent > 1
                ORDER BY error_date DESC """)
    days_request_result = c.fetchall()
    print "3 : On which days did more than 1% of requests lead to errors?", "\n"  # NOQA
    for row in days_request_result:
        print row[0], "-", row[1], "%", " errors"

''' call the functions to view the results'''
get_articles_Q1()
print"===================================================", "\n"
get_article_authors_Q2()
print"===================================================", "\n"
get_day_requests_Q3()
