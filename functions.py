from note import Note
import datetime

def append_string(string):
    print('Чтобы сохранить и выйти, нажмите Enter на пустой строке')
    buffer = []
    buffer.append(string)
    while True:
        line = input()
        if not line:
            break
        buffer.append(line)
    return '\n'.join(buffer)

def input_text():
    print('Чтобы сохранить и выйти, нажмите Enter на пустой строке')
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    return '\n'.join(lines)

def input_date():
    date_str = input("Введите дату в формате dd.mm.yyyy: ")
    try:
        day_str, month_str, year_str = date_str.split('.')
        day = int(day_str)
        month = int(month_str)
        year = int(year_str)
        return datetime.date(year, month, day)
    except (ValueError, TypeError):
        return None

def get_id(notes):
    max_id = 0
    for note in notes:
        if note.id > max_id:
            max_id = note.id
    return max_id+1

def get_notes_by_date_range(start_date, end_date, notes):

    matching_notes = []
    for note in notes:
        if start_date <= note.created_at <= end_date:
            matching_notes.append(note)
    return matching_notes

def add_note(main_id,notes):
    print("введите заголовок")
    title = input()
    print("введите заметку")
    body = input_text()
    note = Note(main_id, title, body)
    notes.append(note)

def date_filter(notes):
    date=input_date()
    if (date):
        filtred_notes = []
        for note in notes:
            getdate=note.get_created()
            if (getdate == date):
                filtred_notes.append(note)
        return filtred_notes

def open_note(id,notes):
    note = next((n for n in notes if int(n.get_id()) == int(id)), None)
    if note:
        print(note.show_note())
        return note
    else: 
        print('Заметка не найдена')
        return None

def change_note_title(note:Note):
        new_title = input('Введите новый заголовок заметки: ')
        note.change_title(new_title)
        print('Заголовок заметки обновлен')

def change_note_body(note:Note):
        text=input_text()
        note.change_body(text)

def apend_note_body(note:Note):
        text=append_string(note.get_body())
        note.change_body(text)
