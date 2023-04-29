import interface
import functions
import saveloder
from  note import Note

notes = []
main_id = 1

def start():
    # mainmenu=(" 1 - Открыть файл;  2 - Сохранить в файл;  3 - Добавить заметку; 4 - Открыть заметку по ИД; 5 - Фильтр ; 6 - Вывести весь список 7 удалить q - выход\n")
    global notes
    global main_id
    while (True):

        print(interface.mainmenu)
        n= input("введите команду: ")
        if n == "q":
            break

        elif n == "1":
            notes = saveloder.read_notes()
            main_id = functions.get_id(notes)

        elif n == "2":
            saveloder.save_notes(notes)

        elif n == "3":
            functions.add_note(main_id,notes)
            main_id = main_id+1

        elif n == "4":
            id=input("введите ID: ")
            note=functions.open_note(id,notes)
            if note: submenu(note)

        elif n == "5":
            list=functions.date_filter(notes)
            if (list): interface.show_list(list)
            else: print("список пуст")

        elif n == "6":
            interface.show_list(notes)

        elif n == "7":
            id=input("введите ID: ")
            functions.delete_note(id,notes)
        else: print("неизвестная команда")

def submenu(note):
    # submenu=("1 - Изменить заголовок; 2 - Дописать заметку; 3 - Ввести новый текст 4-просмотр q - возврат")
    while (True):
        print(interface.submenu)
        n = input("введите команду: ")
        if n == "q":
            break
        if n == "1":
            functions.change_note_title(note)
        elif n == "2":
            functions.apend_note_body(note)
        elif n == "3":
            functions.change_note_body(note)
        elif n == "4":
            print(note.show_note())
