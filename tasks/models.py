from django.db import models
from django.utils.timezone import now


class Tasks(models.Model):
    subject = models.CharField(max_length=150, help_text="Тема сообщения")
    content = models.TextField(help_text="Текст сообщения")
    result = models.TextField(help_text="Результат", null=True, blank=True)
    sender = models.ForeignKey('staff.Staff', related_name='sender',
                               on_delete=models.SET_NULL, null=True, )
    addressee = models.ForeignKey('staff.Staff', related_name='addressee',
                                  on_delete=models.SET_NULL, null=True)
    send_datetime = models.DateTimeField(default=now, editable=False)
    closed = models.BooleanField()

    def __str__(self):
        return (f'<{self.subject} {self.sender}'
                f'{self.addressee} {self.send_datetime} {self.closed}'
                f'{self.content}>')

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"


class TasksArchive(models.Model):
    subject = models.CharField(max_length=150, help_text="Тема сообщения")
    content = models.TextField(help_text="Текст сообщения")
    result = models.TextField(help_text="Результат", null=True, blank=True)
    sender = models.CharField(max_length=100) # ФИО отправителя, предварительно нужно преобразовать в строку
    addressee = models.CharField(max_length=100) # ФИО получателя, предварительно нужно преобразовать в строку
    send_datetime = models.DateTimeField(help_text="Дата сообщения")
    closed = models.BooleanField()

    def __str__(self):
        return (f'<{self.subject} {self.sender} {self.addressee}'
                f'{self.send_datetime} {self.closed}>')

    class Meta:
        verbose_name = "Tasks Archive"
        verbose_name_plural = "Tasks Archive"
