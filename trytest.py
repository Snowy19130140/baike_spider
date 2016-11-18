#encoding:utf-8

class Person(object):
    __score = 90
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_grade(self):
        return self.__score

p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print p1.get_grade()
print p2.get_grade()
print p3.get_grade()


def func(passline):
    def cmp(val):
        if val >= passline:
            print('%d pass' %val)
        else:
            print('%d failed' % val)
    return cmp

f_100 = func(60)
f_150 = func(90)
f_100(89)
f_150(89)



def dec(func):
    def in_dec(*args):
        print('in dec args =', args)
        if len(args) == 0:
            return 0
        for val in args:
            if not isinstance(val, int):
                return 0
        return func(*args)
    print('call dec')
    return in_dec

@dec
def my_sum(*args):

    print('in my_sum')
    return sum(args)

def my_average(*args):
    return sum(args)/len(args)

print(my_sum(1,2,3,4,5))

'''
my_sum = dec(my_sum)

my_average = dec(my_average)


print(my_sum(1,2,3,4,5))
print(my_sum(1,2,3,4,5,'6'))
print(my_average(1,2,3,4,5))
print(my_average())
'''








import urllib2
import cookielib

url = 'http://www.baidu.com'
print 'First:'
resp1 = urllib2.urlopen(url)
print resp1.getcode()
print len(resp1.read())

print 'Second:'
request = urllib2.Request(url)
request.add_header('user-agent', 'Mozilla/5.0')
resp2 = urllib2.urlopen(request)
print resp2.getcode()
print len(resp2.read())

print 'Third:'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
resp3 = urllib2.urlopen(url)
print resp3.getcode()
print cj
print len(resp3.read())


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
print '打印所有链接：'
links = soup.find_all('a')
for link in links:
    print link.name, link['href'], link.get_text()

node = soup.find('a', href="http://example.com/lacie")
print node.name, node['href'], node.get_text()

print '正则匹配输出：'
link_node = soup.find('a', href=re.compile(r'ill'))
print link_node.name, link_node['href'], link_node.get_text()

print '打印p段落文字：'
p_nodes = soup.find_all('p', class_="title")
for p_node in p_nodes:
    print p_node.name, p_node.get_text()
