class Library:
    def __init__(self):
        self.books = {}  # Инициализация словаря для хранения информации о книгах.

    def add_book(self, isbn, title, author, year):
        # Метод для добавления книги в систему. Принимает ISBN, название, автора и год выпуска.
        if isbn not in self.books:
            # Если книги с таким ISBN нет в системе, добавляем ее.
            self.books[isbn] = {'title': title, 'author': author, 'year': year, 'status': 'available'}
            print(f"Book {title} by {author} added to the library.")
        else:
            # Если книга с таким ISBN уже существует, выводим сообщение.
            print("Book with this ISBN already exists in the library.")

    def change_status(self, isbn, status):
        # Метод для изменения статуса книги. Принимает ISBN и новый статус.
        if isbn in self.books:
            # Если книга с таким ISBN найдена, обновляем ее статус.
            self.books[isbn]['status'] = status
            print(f"Status of book {self.books[isbn]['title']} changed to {status}.")
        else:
            # Если книга с таким ISBN не найдена, выводим сообщение.
            print("Book with this ISBN doesn't exist in the library.")

    def search_book(self, isbn):
        # Метод для поиска книги по ISBN. Выводит информацию о книге или сообщение, если книга не найдена.
        if isbn in self.books:
            book_info = self.books[isbn]
            print(f"ISBN: {isbn}\nTitle: {book_info['title']}\nAuthor: {book_info['author']}\nYear: {book_info['year']}\nStatus: {book_info['status']}")
        else:
            print("Book with this ISBN doesn't exist in the library.")