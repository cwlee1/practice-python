dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}

a = {1: 'hi'}
a = { 'a': [1,2,3]}

a = {1: 'a'}
a[2] = 'b'
a

a['name'] = 'pey'
a[3] = [1,2,3]
del a[1]
a

grade = {'pey': 10, 'julliet': 99}
grade['pey']
grade['julliet']

a = {1:'a', 2:'b'}
a[1]
a[2]

a = {1:'a', 2:'b'}
a['a']
a['b']

dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
dic['name']
dic['phone']
dic['birth']

a = {1:'a', 1:'b'}
a

a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
a.keys()

for k in a.keys():
    print(k)


list(a.keys())
a.values()
a.items()
a.clear()
a

a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
a.get('name')
a.get('phone')

a.get('foo', 'bar')

a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
'name' in a
'email' in a
