def main():
    isStop = 10
    while isStop != 0:
        print(f'1. Добавление нового контакта \n2. Открыть телефонную книгу \n3. Поиск контакта \n4. Копирование контакта \n5. Удаление контакта \n0. Выход')
        isStop = int(input('Номер операции: '))
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
            print('ОШИБКА! Укажите корректный номер операции!')
        input('\nДля продолжения нажмите клавишу Enter...')
    
def add_contact():
    s_name = input('Фамилия: ')
    name = input('Имя: ')
    m_name = input('Отчество: ')
    phone = input('Телефон: ')
    contact = {'Фамилия': s_name, 'Имя': name, 'Отчество': m_name, 'Телефон': phone}
    with open('phonebook.txt', 'a', encoding='utf-8') as data:
        for value in contact.values():
            data.write(f'{value}     ' )
        data.write('\n')

def open_phonebook():
    header = ["Фамилия", "Имя", "Отчество", "Номер телефона"]
    data_lines = []
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            data_lines.append(line.strip().split())
    column_widths = [max(len(str(row[i])) for row in data_lines) for i in range(len(header))]
    for i, head in enumerate(header):
        print(f"{head:<{column_widths[i]}}", end="\t")
    print()
    for row in data_lines:
        for i, item in enumerate(row):
            print(f"{item:<{column_widths[i]}}", end="\t")
        print()  # Переход на новую строку после печати строки данных

def find_contact():
    header = ["Фамилия", "Имя", "Отчество", "Телефон"]
    desired = input('Укажите данные для поиска контака: ')
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        print("\t".join(header))
        for value in data.readlines():
            if desired in value:
                print(*value)
            
def copy_contact():
    header = ["Фамилия", "Имя", "Отчество", "Телефон"]
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
    header = ["Фамилия", "Имя", "Отчество", "Телефон"]
    baza = []
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        print("\t".join(header))
        baza = list(enumerate(data.readlines()))
        print(*baza, sep='\n')
    del_cont = int(input('Введите порядковый номер удаляемого контакта: '))
    baza.pop(del_cont)
    with open('phonebook.txt', 'w', encoding='utf-8') as data:
        for str1 in baza:
            # Записываем контакт в файл без завершающего символа новой строки, если это последний контакт
            if str1 == baza[-1]:
                data.write(str1[1].rstrip('\n'))
            else:
                data.write(str1[1])
        data.write('\n')

main()