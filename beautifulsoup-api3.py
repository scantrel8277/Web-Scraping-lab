table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"

table_bs = BeautifulSoup(table, 'html5lib')

table_rows=table_bs.find_all('tr')
table_rows

first_row =table_rows[0]
first_row

print(type(first_row))

first_row.td

for i,row in enumerate(table_rows):
    print("row",i,"is",row)

for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)

list_input=table_bs .find_all(name=["tr", "td"])
list_input

table_bs.find_all(id="flight")

list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
list_input

table_bs.find_all(href=True)

table_bs.find_all(href=False)

soup.find_all(id="boldest")

table_bs.find_all(string="Florida")
