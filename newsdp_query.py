#!/usr/bin/env python2

import psycopg2
# database name
conn = psycopg2.connect(database="news")


def get_top_articles(conn):
    """Return the most popular three articles of all time"""
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


def get_top_article_authors(conn):
    """Return  the most popular article authors of all time """
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


def get_top_day_requests(conn):
    """Return days did more than 1% of requests lead to errors """
    c = conn.cursor()
    c.execute("""SELECT  error_date, error_percent
                FROM log_error_view
                WHERE error_percent > 1
                ORDER BY error_date DESC""")
    days_request_result = c.fetchall()
    print "3 : On which days did more than 1% of requests lead to errors?", "\n"  # NOQA
    for row in days_request_result:
        print row[0], "-", row[1], "%", " errors"

get_top_articles(conn)
print"===================================================", "\n"
get_top_article_authors(conn)
print"===================================================", "\n"
get_top_day_requests(conn)
