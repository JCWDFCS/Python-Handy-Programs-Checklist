filename = 'movie.txt'

def add_movie(movies):
    movie = input('Movie: ')
    year = input('Year:')
    movie = []
    movies.append(movie)
    movies.append(year)
    write_movies(movies)
    print(movie[0] + ' was added.\n')



def write_movies(movies):
    with open(filename, 'w') as file:
        for movie in movies:
            line = '|'.join(movie)
            file.write(line + '\n')

def read_movies():
    movies = []
    with open(filename) as file:
        for row in file:
            row = row.replace('\n', '')
            movie = row.split('|')
            movies.append(movie)
    return movies

def list_movies(movies):
    for i in range(len(movies)):
        movie = movies[i]
        print(str(i+1) + ". " + movie)
    print()



def delete_movie(movies):
    while True:
        try:
            index = int(input('Number: '))
        except ValueError:
            print('Invalid integer,please try again.')
            continue
        if number < 1 or number > len(movies):
            print("There's no movie with that number, please try again.")
        else:
            break
    movie = movies.pop(index - 1)
    write_movies(movies)
    print(movie + ' was deleted. \n')

def display_menu():
    print("The Movie List Program")
    print()
    print('COMMAND MENU')
    print('List - List all the movies')
    print('Add -  Add a movie')
    print('del -  Delete a movie')
    print('Exit - Exit program')

def main():
    display_menu()
    movies = read_movies()
    while True:
        command = input('Command: ')
        if command == 'list':
            list_movies(movies)
        elif command == 'add':
            add_movie(movies)
        elif command == 'del':
            delete_movie(movies)
        elif command == 'exit':
            break
            print('Bye!')
        else:
            print('Not a valid command, try again.')


if __name__ == "__main__":
    main()
