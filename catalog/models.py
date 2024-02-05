from django.db import models


# Жанры книг
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text=" Введите жанр книги", verbose_name="Жанр книги")

    def __str__(self):
        return self.name


# Язык книги
class Language(models.Model):
    name = models.CharField(max_length=20, help_text=" Введите язык книги", verbose_name="Язык книги")

    def __str__(self):
        return self.name


# Издательство
class Publisher(models.Model):
    name = models.CharField(max_length=100, help_text=" Введите наименование издательства", verbose_name="Издательство")

    def __str__(self):
        return self.name


# Авторы
class Author(models.Model):
    first_name = models.CharField(max_length=200, help_text=" Введите имя автора", verbose_name="Имя автора")
    last_name = models.CharField(max_length=100, help_text=" Введите фамилию автора", verbose_name="Фамилия автора")
    date_of_birth = models.DateField(help_text="Введите дата рождения", verbose_name="Дата рождения",
                                     null=True, blank=True)
    about = models.TextField(help_text="Введите сведения об авторе", verbose_name="Сведения об авторе")
    photo = models.ImageField(upload_to="images", help_text="Загрузите фото автора", verbose_name="Фото автора",
                              null=True, blank=True)

    def __str__(self):
        return self.last_name


class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Введите название книги",
                             verbose_name="Название книги")
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, help_text="Выберите жанр для книги",
                              verbose_name="Жанр книги", null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE, help_text="Выберите язык книги",
                                 verbose_name="Язык книги", null=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, help_text="Выберите издательство",
                                  verbose_name="Издательство", null=True)
    year = models.CharField(max_length=4, help_text="Введите год издания",
                            verbose_name="Год издания")
    author = models.ManyToManyField('Author', help_text="Выберите автора (авторов) книги",
                                    verbose_name="Автор (авторы книги")
    summary = models.TextField(max_length=1000, help_text="Введите краткое описание книги",
                               verbose_name="Аннотация книги")
    isbn = models.CharField(max_length=13, help_text="Должно содержать 13 символов",
                            verbose_name="ISBN книги")
    price = models.DecimalField(decimal_places=2, max_digits=7, help_text="Введите цену книги",
                                verbose_name="Цена (руб.)")
    photo = models.ImageField(upload_to="images", help_text="Загрузите изображение обложки",
                              verbose_name="Изображение обложки")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse ('book_detail', args=[str(self.id)])
        pass


# состояние экземпляра книги
class Status(models.Model):
    name = models.CharField(max_length=20, help_text="Введите статус экземпляра книги",
                            verbose_name="Статус экземпляра книги")

    def __str__(self):
        return self.name


# экземпляр книги
class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    inv_nom = models.CharField(max_length=20, null=True, help_text="Введите инвентарный номер экземпляра",
                               verbose_name="Инвентарный номер")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, help_text="Изменить состояние экземпляра",
                               verbose_name="Статус экземпляра книги")
    due_back = models.DateField(null=True, help_text="Введите конец срока статуса",
                                verbose_name="Дата окончания статуса")

    # Метаданные
    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return f'{self.inv_nom}, {self.book}, {self.status}'
