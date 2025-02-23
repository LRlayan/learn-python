from bs4 import BeautifulSoup as bs

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie&quot; class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie&quot; class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie&quot; class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = bs(html_doc,'html.parser')
print(soup.title) #<title>The Dormouse's story</title>
print(soup.title.contents,type(soup.title.contents)) #["The Dormouse's story"] <class 'list'>

print(soup.p)
print("Contents : ",soup.p.b.contents)
print(soup.a)
print(soup.a['id'])
p_tag = soup.find('p')
print(p_tag)
print(soup.find(id='link1'))
print(soup.find_all('p'))


