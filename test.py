locations = ['/data/mybackup/data/fil1',
            '/data/mybackup/data/fil2',
            '/data/mybackup/data/fil3',
            '/data/mybackup/song/fil1',
            '/data/mybackup/song/fil2',
            '/data/mybackup/song/fil3',
            '/data/archive/song/fil1',
            '/data/archive/song/fil2',
            '/data/archive/song/fil3',
            '/data/archive/data/fil1',
            '/local/archive/data/fil2',
            '/local/archive/data/fil3',
            '/ebboks/wordpress/fil1',
            '/ebooks/wordpress/fil2',
            '/ebooks/wordpress/fil3']

excludes = [  '/data/archive/', '/data' , '/ebooks/'   ]
locs = []
for location in locations:
    for exclude in excludes:
    # print('exclude: ',exclude)
        if not location.startswith(exclude):
            locs.append(location)
print(location)



    #   print(location)
[location for location in locations if not location.startswith(tuple(excludes))]
