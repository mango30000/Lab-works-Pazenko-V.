class Book:
    title = '"Хроники заводной птицы"'
    author = 'Харуки Мураками'
    year = '1994'
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        print("Название книги:",self.title,'Автор:', self.author,'Год издания:',self.year)

book = Book('Три мушкетёра',"Александр Дюма", 1844)
print('Название главной книги:{}'.format(book.__class__.title))
print('Автор главной книги:{}'.format(book.__class__.author))
print('Год издания главной книги:{}'.format(book.__class__.year))
book.get_info()




