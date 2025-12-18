!pip install bs4
!pip install requests pandas html5lib 

from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

soup = BeautifulSoup(html, 'html5lib')

print(soup.prettify())

tag_object=soup.title
print("tag object:",tag_object)

print("tag object type:",type(tag_object))

tag_object=soup.h3
tag_object

tag_child =tag_object.b
tag_child

parent_tag=tag_child.parent
parent_tag

tag_object # identical to above statement

tag_object.parent

sibling_1=tag_object.next_sibling
sibling_1

sibling_2=sibling_1.next_sibling
sibling_2

sibling_3=sibling_2.next_sibling
sibling_3

tag_child['id']

tag_child.attrs

tag_child.get('id')

tag_string=tag_child.string
tag_string

type(tag_string)

unicode_string = str(tag_string) # convert to Python string object
unicode_string


