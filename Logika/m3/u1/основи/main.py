with open('quotes.txt', 'r', encoding='utf-8') as file:
    print(file.read())

author = input('Введення Автора:')

with open('quotes.txt', 'a', encoding='utf-8') as file:
    file.write(f'({author})')
