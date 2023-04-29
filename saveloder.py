import csv
from datetime import datetime
from note import Note

def read_notes():
    try:
        notes=[]
        file_path = input("введите Enter или имя своего файла: ")
        if (file_path == ""):
            file_path = "myfile.csv"
        with open(file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')
            for row in reader:
                note = Note(int(row['Id']), row['Title'], row['Body'],
                            datetime.strptime(
                                row['Created At'], '%Y-%m-%d %H:%M:%S.%f'),
                            datetime.strptime(row['Updated At'], '%Y-%m-%d %H:%M:%S.%f') if row['Updated At'] else None)
                notes.append(note)
        return notes
    
    except FileNotFoundError:
        print('Файл не найден')
        return []
    except:
        print('Ошибка чтения файла')
        return []

def save_notes(notes):
    file_path = input("введите Enter или имя своего файла : ")
    if (file_path == ""):
        file_path = "myfile.csv"
    with open(file_path, mode='w', newline='') as csv_file:
        fieldnames = ['Id', 'Title', 'Body', 'Created At', 'Updated At']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames,delimiter=';')
        writer.writeheader()
        for note in notes:
            writer.writerow({'Id': note.id, 'Title': note.title, 'Body': note.body,
                             'Created At': note.created_at, 'Updated At': note.updated_at})
            
