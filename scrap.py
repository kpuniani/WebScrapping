'''
Created on Jan 21, 2018

@author: karan
'''
import urllib.request
from bs4 import BeautifulSoup
import pymysql



def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata =BeautifulSoup(thepage,"html.parser")
    return soupdata
db = pymysql.connect("localhost","<username>","<password>","<dbname>")
cursor = db.cursor()
upcomingeventsaved =""
soup=make_soup("http://www.lapl.org/whats-on/calendar")
for record in soup.findAll("tr",{"class":["even","odd"]}):
    count=0;
    upcomingevent=""
    for data in record.findAll('td',{"class":["views-field views-field-field-event-branch"]}):
        upcomingevent=upcomingevent+" "+data.text
        count=0
    if len(upcomingevent)!=0:
        upcomingeventsaved=upcomingeventsaved+upcomingevent[1:]
        result=upcomingeventsaved
        sql = ('insert into <tablename> values ("%s","%s")' % (count,result))  
        cursor.execute(sql)
        db.commit()



