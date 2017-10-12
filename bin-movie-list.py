import pickle
# a file in the current directory
filename = 'movies.bin'

def main():
    displayMenu()
    movies = readMovies()
    while True:
        command = input('Command: ')
        if command.lower() == 'list':
            listMovies(movies)
        elif command.lower() == 'add':
            addMovie(movies)
        elif command.lower() == 'del':
            deleteMovie(movies)
        elif command.lower() == 'exit':
            break
        else:
            print('Not a valid command. Please try again. \n')
    print('Bye...')


def writeMovies(movies):
    with open(filename, 'wb') as file:
        pickle.dump(movies, file)


def readMovies():
    movies = []
    with open(filename, 'rb') as file:
        movies = pickle.load(file)
    return movies


def listMovies(movies):
    for i in range(len(movies)):
        movie = movies[i]
        print("%s.%s (%s)" %(str(i+1), movie[0], movie[1]))
        print()

def addMovie(movies):
    name = input('Name:')
    year = input('Year:')
    movie = []
    movie.append(name)
    movie.append(year)
    movies.append(movie)
    writeMovies(movies)
    print(name + ' was added.\n')

def deleteMovie(movies):
    index = int(input('Number: '))
    movie = movies.pop(index - 1)
    writeMovies(movies)
    print(movie[0] + ' was deleted. \n')


def displayMenu():
    print('The movie list program.')
    print()
    print('COMMAND MENU')
    print('list - List all movies')
    print('add  - Add a movie')
    print('del  - Delete a movie')
    print('exit - Exit program')
    print()





if __name__ == '__main__':
    main()
