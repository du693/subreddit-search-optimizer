from bs4 import BeautifulSoup as bs
import requests
import re
import sqlite3

def input_stream(subreddit):
    subredditSearch = subreddit.replace(' ', '+')
    googleURL = f"https://www.google.com/search?q={subredditSearch}+subreddit"
    return googleURL

def get_subreddit(URL):
    page=requests.get(URL)
    soup=bs(page.content, "html.parser")
    subreddit=str(soup.find('a', {'href':re.compile('^/url\?q=https:\/\/www\.reddit\.com\/')}))
    subreddit=str(re.search(r'https://www.reddit.com/r/.*?\/', subreddit)[0])
    return subreddit



# def sql(strURL):
#     db=sqlite3.connect('subreddits.sqlite')
#     cur=db.cursor()
#     cur.execute('drop table if exists subreddit')
#     cur.execute('create table subreddit (subreddit text)')
#     cur.execute('insert into subreddit(subreddit) values (?);', (strURL,))
#     db.commit()
#     return None

# def get_db_connection():
#     conn = sqlite3.connect('subreddits.sqlite')
#     return conn

# conn=get_db_connection()
# print(str(conn.execute('SELECT * FROM subreddit').fetchall()))



