def start():
    print('\n *** Список работников организации*** \n' +
        '-------------------------------------\n' +
        'введите 1,2,3,4 или 5:\n' +
        '1 для показа работников\n' +
        '2 для добавления нового работника\n' +
        '3 для поиска работника\n' +
        '4 для удаления работника\n' +
        '5 для выхода\n')
    choice = input('введите число от 1 до 5: ')
    return choice

def print_message(data):
    print(data)

def insert_data(message):
    return input(message)


