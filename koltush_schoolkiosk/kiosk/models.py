from django.db import models
from django.urls import reverse


class Raspisanie_Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    raspisanie_post_1monday = models.FileField(upload_to="raspisanie_post/%Y/1monday/",
                                               verbose_name='Файл с расписанием на понедельник')
    raspisanie_post_2tuesday = models.FileField(upload_to="raspisanie_post/%Y/2tuesday/",
                                                verbose_name='Файл с расписанием на вторник')
    raspisanie_post_3wednesday = models.FileField(upload_to="raspisanie_post/%Y/3wednesday/",
                                                  verbose_name='Файл с расписанием на среду')
    raspisanie_post_4thursday = models.FileField(upload_to="raspisanie_post/%Y/4thursday/",
                                                 verbose_name='Файл с расписанием на четверг')
    raspisanie_post_5friday = models.FileField(upload_to="raspisanie_post/%Y/5friday/",
                                               verbose_name='Файл с расписанием на пятницу')
    raspisanie_post_6saturday = models.FileField(upload_to="raspisanie_post/%Y/6saturday/",
                                                 verbose_name='Файл с расписанием на субботу', blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Постоянное расписание 5-11 классы'
        verbose_name_plural = 'Постоянное расписание 5-11 классы'
        ordering = ['id']


class Raspisanie_New(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    raspisanie_new = models.FileField(upload_to="raspisanie_new/%Y/%m/%d/",
                                      verbose_name='Файл с измененным расписанием')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('raspisanie_new', kwargs={'rasp_new_slug': self.slug})

    class Meta:
        verbose_name = 'Измененное расписание(временное) 5-11 классы'
        verbose_name_plural = 'Измененное расписание(временное) 5-11 классы'
        ordering = ['id']


class Raspisanie_Calls(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    raspisanie_calls = models.FileField(upload_to='raspisanie_calls/%Y/%m/%d/',
                                        verbose_name='Файл с расписанием звонков')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Расписание звонков'
        verbose_name_plural = 'Расписание звонков'
        ordering = ['id']
