from django.db import models
from django.db.models.fields import DateField, EmailField
from phonenumber_field.modelfields import PhoneNumberField


class Staff(models.Model):
    last_name = models.CharField(max_length=20, help_text="Введите фамилию")
    first_name = models.CharField(max_length=20, help_text="Введите имя")
    middle_name = models.CharField(max_length=20, help_text="Введите отчество")
    rank = models.ForeignKey('Rank', on_delete=models.SET_NULL, null=True)
    telegram_nickname = models.CharField(max_length=20,
                                         help_text="Введите никнейм Telegram",
                                         unique=True)
    phone_number = PhoneNumberField(max_length=14, region=None,
                                    help_text="Введите номер телефона",
                                    unique=True)
    personal_email = EmailField(max_length=50,
                                help_text="Введите персональный email",
                                unique=True)
    work_email = EmailField(max_length=50, help_text="Введите рабочий email",
                            unique=True)
    employment_date = DateField(help_text="Введите дату приёма на работу")
    date_of_birth = DateField(help_text="Введите дату рождения")

    def __str__(self):
        return f'{self.last_name} {self.first_name}, {self.rank}'

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"


class Rank(models.Model):
    rank = models.CharField(max_length=20, help_text="Введите должность")

    def __str__(self):
        return f'{self.rank}'

    class Meta:
        verbose_name = "Rank"
        verbose_name_plural = "Rank"


class StaffArchive(models.Model):
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    rank = models.CharField(max_length=20)
    telegram_nickname = models.CharField(max_length=20, unique=True)
    phone_number = PhoneNumberField(max_length=14, region=None)
    personal_email = EmailField(max_length=50, unique=True)
    work_email = EmailField(max_length=50, unique=True)
    employment_date = DateField()
    date_of_birth = DateField()
    date_of_dismissal = DateField()

    def __str__(self):
        return f'{self.last_name} {self.first_name}, {self.rank}'

    class Meta:
        verbose_name = "Staff Archive"
        verbose_name_plural = "Staff Archive"
