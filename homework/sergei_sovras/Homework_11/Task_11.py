class Books:
    material = str
    text_exist = bool
    title = str
    author = str
    count_of_pages = int
    isnb = bool
    reserved = bool

    def __init__(self, title, author, count_of_pages, material, reserved):
        self.title = title
        self.author = author
        self.count_of_pages = count_of_pages
        self.material = material
        self.reserved = reserved

    def book_print(self):
        return (f'Название: {self.title}, Автор: {self.author}, страниц: {self.count_of_pages}, '
                f'материал: {self.material} {", зарезервирована" if self.reserved else ""}')


class WorkBooks(Books):
    subject = str
    group = str
    has_tasks = bool

    def __init__(self, title, author, count_of_pages, material, reserved, subject, group, has_tasks):
        super().__init__(title, author, count_of_pages, material, reserved)
        self.subject = subject
        self.group = group
        self.has_tasks = has_tasks

    def work_book_print(self):
        return (f'Название: {self.title}, Автор: {self.author}, страниц: {self.count_of_pages}, предмет: '
                f'{self.subject}, класс: {self.group}{", зарезервирован" if self.reserved else ""}')


first_book = Books('Идиот', 'Достоевский', 500, 'бумага', False)
second_book = Books('Второе название', 'Второй автор', 256, 'полимер', False)
third_book = Books('Третье нзвание', 'Тетий автор', 123, 'пергамент', False)
fourth_book = Books('Четвертое название', 'Четвертый автор', 54, 'папирус', False)
fiveth_book = Books('Пятое название', 'Пятый автор', 321, 'бумага', True)

print(first_book.book_print())
print(second_book.book_print())
print(third_book.book_print())
print(fourth_book.book_print())
print(fiveth_book.book_print())

first_workbook = WorkBooks('Первый учебник', 'Первый автор учебника', 324, 'бумага', False, 'математика', '3B', True)
second_workbook = WorkBooks('Второй учебник', 'Второй автор учебника', 234, 'бумага', True, 'математика', '3A', True)

print(first_workbook.work_book_print())
print(second_workbook.work_book_print())
