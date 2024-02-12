with open('movies.txt' ,'w') as file:
    file.write('\n')

def populate_list(movie_file):
    movie_list = ['Lethal Weapon 1\n', 'Jurrasic Park\n', 'Spider_-Man\n']
    with open('movies.txt', 'r') as file:
        for line in file:
            movie_list.append(line.strip())
            return movie_list

def displaymenu():
    print('Welcome To The Movie Guide!!!!')
    print('list --> Lists all movies.')
    print('add --> Add a movie.')
    print('delete --> Delete a movie.')
    print('exit --> Close Movie Guide')

def display_titles(movie_list):
    print('\nmovie titles')
    for idx, title in enumerate(movie_list, start=1):
        print(f'{idx}, {title}')

def add_title(movie_list, title, file_name):
    movie_list.append(title)
    with open(file_name, 'a') as file:
        file.write(title + '\n')
    print(f"\n'{title}' has been added to the list.")

def delete_title(movie_list, index, file_name):
    if 1 <= index <= len(movie_list):
        deleted_title = movie_list.pop(index - 1)
        with open(file_name, 'w') as file:
            file.write('\n'.join(movie_list))
            print(f"\n'{deleted_title}' has been deleted from the list.")
    else:
        print('\nInvalid number. No movie was deleted.')

def main():
    movie_file = 'movies.txt'
    movie_list = populate_list(movie_file)
    while True:
        displaymenu()
        choice = input('Enter your choice: ')
        if choice == 'list':
            display_titles(movie_list)
        elif choice == 'add':
            new_title = input('Enter the new movie title: ')
            add_title(movie_list, new_title, movie_file)
            display_titles(movie_list)
        elif choice == 'delete':
            display_titles(movie_list)
            index = int(input('Enter the number of the movie title to delete: '))
            delete_title(movie_list, index, movie_file)
            display_titles(movie_list)
        elif choice == 'exit':
            print('Exiting the program.')
            break
        else:
            print('Invalid command. Please choose a valid option.')
if __name__ == "__main__":
    main()