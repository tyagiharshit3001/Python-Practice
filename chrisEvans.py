book = {}
book["tom"] = {
    'name': "tomus",
    'address': 'cartoon network',
    'mobile': 52546546
}
book['bob'] = {
    'name': 'doggy',
    'address': 'CN',
    'mobile': 6556565
}
import json
s = json.dumps(book)
with open("d://CHEEKO BOYEE/book.txt","w") as f :
    f.write(s)
