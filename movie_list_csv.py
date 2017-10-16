import csv
# a file in the current directory
filename = 'movies.csv'



def write_movies(movies):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file) #transfer to the object of writer
        writer.writerows(movies) #object


def read_movies():
    movies = []
    with open(filename, newline=None) as file:
        reader = csv.reader(file) #transfer to the object of reader
        ## readline(), read, readlines() are not its methods.
        # print('%s' %reader)
        # line = reader.readline()
        # print(line)
        for row in reader:
            movies.append(row)
    # print('%r' %movies)
    return movies


def list_movies(movies):
    for i in range(len(movies)):
        movie = movies[i]
        print("%s.%s (%s)" %(str(i+1), movie[0], movie[1]))
        
def add_movie(movies):
    name = input('Name:')
    year = input('Year:')
    movie = []
    movie.append(name)
    movie.append(year)
    movies.append(movie)
    write_movies(movies)
    print(name + ' was added.\n')

def delete_movie(movies):
    index = int(input('Number: '))
    movie = movies.pop(index - 1)
    write_movies(movies)
    print(movie[0] + ' was deleted. \n')


def display_menu():
    print('The movie list program.')
    print()
    print('COMMAND MENU')
    print('list - List all movies')
    print('add  - Add a movie')
    print('del  - Delete a movie')
    print('exit - Exit program')
    print()

def main():
    display_menu()
    movies = read_movies()
    while True:
        command = input('Command: ')
        if command.lower() == 'list':
            list_movies(movies)
        elif command.lower() == 'add':
            add_movie(movies)
        elif command.lower() == 'del':
            delete_movie(movies)
        elif command.lower() == 'exit':
            break
        else:
            print('Not a valid command. Please try again. \n')
    print('Bye...')





if __name__ == '__main__':
    main()
