""" 
This is a crawler program using beautifulsoup.
It crawls the website "https://sport050.nl/sportaanbieders/alle-aanbieders/"
and fetches all the sport suppliers in the city of Groningen. It outputs 
a csv-file with the url;phone-number;email-address of all the suppliers it can find.
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

class Crawler:
    def __init__(self):
        print ('fetch urls')
        self.url = "https://sport050.nl/sportaanbieders/alle-aanbieders/"
        self.s = self.open_url(url=self.url)
        self.reflist = self.read_hrefs(self.s)

        print ('getting sub-urls')
        self.sub_urls = [s for s in filter(lambda x: '<a href="/sportaanbieders' in str(x), self.reflist)]
        self.sub_urls = self.sub_urls[3:]

       
        self.pointer = -1

    

    def __next__(self):
        self.pointer += 1
        if self.pointer == len(self.sub_urls):
            raise StopIteration
        return self.crawl_site()

    def hack_ssl(self):
        """ ignores the certificate errors"""
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return ctx


    def open_url(self, url):
        """ reads url file as a big string and cleans the html file to make it
            more readable. input: url, output: soup object
        """
        ctx = self.hack_ssl()
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        return soup


    def read_hrefs(self, soup):
        """ get from soup object a list of anchor tags,
            get the href keys and and prints them. Input: soup object
        """
        reflist = []
        tags = soup('a')
        for tag in tags:
            reflist.append(tag)
        return reflist

    def read_li(self, soup):
        lilist = []
        tags = soup('li')
        for tag in tags:
            lilist.append(tag)
        return lilist

    def get_phone(self, info):
        reg = r"(?:(?:00|\+)?[0-9]{4})?(?:[ .-][0-9]{3}){1,5}"
        phone = [s for s in filter(lambda x: 'Telefoon' in str(x), info)]
        try:
            phone = str(phone[0])
        except:
            phone = [s for s in filter(lambda x: re.findall(reg, str(x)), info)]
            try:
                phone = str(phone[0])
            except:
                phone = ""   
        return phone.replace('Facebook', '').replace('Telefoon:', '')

    def get_email(self, soup):
        try: 
            email = [s for s in filter(lambda x: '@' in str(x), soup)]
            email = str(email[0])[4:-5]
            bs = BeautifulSoup(email, features="html.parser")
            email = bs.find('a').attrs['href'].replace('mailto:', '')
        except:
            email = ""
        return email

    def remove_html_tags(self, text):
        """Remove html tags from a string"""
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    def fetch_sidebar(self, soup):
        """ reads html file as a big string and cleans the html file to make it
            more readable. input: html, output: tables
        """
        sidebar = soup.findAll(attrs={'class': 'sidebar'})
        return sidebar[0]

    def extract(self, url):
        text = str(url)
        text = text[26:].split('"')[0] + "/"
        return text


    
    def crawl_site(self):
    
        for index, sub in enumerate(self.sub_urls):
            if index == self.pointer:
                try:
                    sub = self.extract(sub)
                    site = self.url[:-16] + sub
                    soup = self.open_url(site)    
                    info = self.fetch_sidebar(soup)
                    info = self.read_li(info)
                    phone = self.get_phone(info)
                    phone = self.remove_html_tags(phone).strip()
                    email = self.get_email(info)
                    email = self.remove_html_tags(email).replace("/","")
                    
                    
                    return(f'{site} ; {phone} ; {email}')
                except Exception as e:
                    print (e)
                    exit()
                break
    