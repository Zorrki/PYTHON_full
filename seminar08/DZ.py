def main():
    isStop = 10
    while isStop != 0:
        print(f'1. Добавить контакт. \n2. Открыть телефонную книгу. \n3. Найти контакт. \n4. Копировать контакт. \n5. Удалить контакт \n0. Выход')
        isStop = int(input('Введите номер нужной операции: '))
        if isStop == 0:
            return False
        elif isStop == 1:
            add_contact()
        elif isStop == 2:
            open_phonebook()
        elif isStop == 3:
            find_contact()
        elif isStop == 4:
            copy_contact()
        elif isStop == 5:
            delete_contact()
        elif isStop not in [0,5]:
            print('Обратите внимание на номера элементов меню!')
        input('Нажмите Enter для продолжения ')
    
def add_contact():
    s_name = input('Введите фамилию: ')
    name = input('Введите имя: ')
    m_name = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    contact = {'Фамилия': s_name, 'Имя': name, 'Отчество': m_name, 'Телефон': phone}
    with open('phonebook.txt', 'a', encoding='utf-8') as data:
        for value in contact.values():
            data.write(f'{value}     ' )
        data.write('\n')

def open_phonebook():
    header = ["Фамилия", "Имя", "Отчество", "Номер телефона"]
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        print("\t".join(header))
        print(*data.readlines())

def find_contact():
    header = ["Фамилия", "Имя", "Отчество", "Номер телефона"]
    desired = input('Кого ищем? ')
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        print("\t".join(header))
        for value in data.readlines():
            if desired in value:
                print(*value)
            
def copy_contact():
    header = ["Фамилия", "Имя", "Отчество", "Номер телефона"]
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        print("\t".join(header))
        baza = list(enumerate(data.readlines()))
        print(*baza, sep='\n')
    copied = int(input('Введите порядковый номер копируемого контакта: '))
    for value in baza:
        if value[0] == copied:
            file_name = str(value[1].split(" ", 1)[:1])
            with open(f'{file_name}.txt', 'a', encoding='utf-8') as data:
                data.write("\t\t".join(header) +'\n')
                data.write(value[1])
                data.write('\n')

def delete_contact():
    header = ["Фамилия", "Имя", "Отчество", "Номер телефона"]
    baza = []
    with open('phonebook.txt', 'r+', encoding='utf-8') as data:
        print("\t".join(header))
        baza = list(enumerate(data.readlines()))
        print(*baza, sep='\n')
    del_cont = int(input('Введите порядковый номер удаляемого контакта: '))
    baza.pop(del_cont)
    with open('phonebook.txt', 'w', encoding='utf-8') as data:
        for str1 in baza:
            data.write(str1[1])
        data.write('\n')


main()