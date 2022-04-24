import lxml.html
from urllib.request import urlopen

tree = lxml.html.parse('full_book_list.html')
type(tree)

html = tree.getroot()
type(html)

