#!/usr/bin/env python3
#
#  reporting tool that prints out reports (in plain text)

import psycopg2

# Database name
DBNAME = "news"

# Query 1 :  The most popular three articles of all time
query1 = "SELECT * FROM popular_article_view LIMIT 3;"
# Title for query 1
title1 = "\n1:What are the most popular three articles of all time? \n "

# Query 2: The most popular article authors of all time
query2 = ("SELECT au.name , count(*) as views \n"
          "FROM articles a , log l , authors au \n"
          "WHERE a.slug = substring(l.path,10) and au.id = a.author\n"
          "GROUP BY 1 \n"
          "order by 2 desc ;")
# Title for query 2
title2 = "\n2. Who are the most popular article authors of all time? \n"

# Query 3 :  On which days did more than 1% of requests lead to errors
query3 = ("SELECT to_char(errortime, 'Mon DD, YYYY') , error_percent \n"
          "FROM error_log_view WHERE error_percent > 1 ;")
# Title for query 2
title3 = "\n3. On which days did more than 1% of requests lead to errors?  \n"


def get_query(query):
    """
    Connects to the database and executes the query
    Args:
        Query to be executes
        Returns:
        Results from the 'database', most recent first.
    """
    db = psycopg2.connect(dbname=DBNAME)
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result


def format_output(raw_data):
    """
      Formats the raw data
      Args:
        query_result in array format
      Returns:
       Formatted result in form of string.
    """
    for i in range(len(raw_data)):
        print(raw_data[i][0] + ' -- ' + str(raw_data[i][1]) + ' views')


def format_query3(raw_data):
    """
      Formats the raw data
      Args:
        query_result in array format
      Returns:
       Formatted result in form of string.
    """
    for i in range(len(raw_data)):
        print(str(raw_data[i][0]) + ' -- ' + str(raw_data[i][1]) + ' %')


# execute the script
if __name__ == '__main__':
    query_result1 = get_query(query1)
    query_result2 = get_query(query2)
    query_result3 = get_query(query3)

    # print formatted data
    print(title1)
    format_output(query_result1)
    print(title2)
    format_output(query_result2)
    print(title3)
    format_query3(query_result3)
