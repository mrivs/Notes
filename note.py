# Здеcь описан класс Заметка (Note)
from datetime import datetime


class Note:

    def __init__(self, id, title, body, created_at=None, updated_at=None):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def __repr__(self):
        return f" ID: {self.id} Cоздана: {self.created_at.date()} Изменена: {self.updated_at.date()} Заголовок: {self.title}"

    def update(self):
        self.updated_at = datetime.now()

    def change_title(self, line):
        if line:
            self.title = line
        self.update()

    def change_body(self, text):
        self.body = text
        self.update()

    def get_body(self):
        return self.body

    def get_title(self):
        return self.title

    def get_created(self):
        return self.created_at.date()

    def get_id(self):
        return self.id

    def show_note(self):
        return f" === {self.title} ===\n{self.body}\n ===================="
