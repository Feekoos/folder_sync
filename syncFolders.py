from dirsync import sync

options = ''

folders = {
r'c:\Users\Filip\AppData\Local\Programs\Python\Python37\Scripts\win': r'd:\Python\Scripts_win',

}

print(len(folders))

for x, y in folders.items():
	source = x
	destination = y
	sync(source, destination, 'sync', ctime=True, twoway=True, create=True, purge=True)
