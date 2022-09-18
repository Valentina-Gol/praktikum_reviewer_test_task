import datetime as dt


class Record:
    """
        1) Нужно добавить docstrings.
    """
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        # 2) Нужно корректно оформить перенос строк.
        self.date = (
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date()
        )
        self.comment = comment


class Calculator:
    """
        3) Нужно добавить docstrings.
    """
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        """
            4) Нужно добавить docstrings и описать входные и выходные данные.
        """
        self.records.append(record)

    def get_today_stats(self):
        """
            5) Нужно добавить docstrings и описать входные и выходные данные.
        """
        today_stats = 0
        # 6) Название переменных должно соответствовать snake_case стилю, в
        # соответствии с ним название переменно1 Record должно принять вид
        # record.
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                # 7) Можно использовать оператор += для улучшения читаемости
                # кода.
                today_stats = today_stats + Record.amount
        return today_stats

    def get_week_stats(self):
        """
            8) Нужно добавить docstrings и описать выходные данные.
        """
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            # 9) Разницу дат лучше вынести в отдельную переменную, чтобы
            # условие ниже стало более коротким и читаемым.
            if (
                (today - record.date).days < 7 and
                (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    """
        10) Нужно добавить docstrings.
    """
    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        """
            11) Осталось обернуть комментарий к методу в docstrings и добавить
            выходные данные, и будет отлично.
        """
        # 12) Лучше переименовать переменную 'x' в соответствии с её смыслом,
        # чтобы потом самому не запутаться.
        x = self.limit - self.get_today_stats()
        if x > 0:
            # 13) Не нужно использовать back-слеши для переноса.
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        # 14) else ниже можно удалить, потому что в условии выше происходит
        # return
        else:
            # 15) скобки излишни, необходимо их удалить и добавить пробел.
            return('Хватит есть!')


class CashCalculator(Calculator):
    """
        16) Нужно добавить docstrings.
    """
    # 17) Объявить переменную типа float можно с использованием точки.
    # Например, 60.0.
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.

    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        """
            18. Нужно добавить docstrings и описать входные и выходные данные.
        """
        # 19) И переменные USD_RATE и EURO_RATE лучше перевести в нижний
        # регистр.
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        # 20) Чтобы в дальнейшем не запутаться, лучше использовать одну и ту же
        # переменную для проверки в if. В данном случае значения currency_type
        # и currency совпадают, но лучше было бы заменить переменную currency
        # на currency_type в первом сравнении в if для единообразия, чтобы в
        # дальнейшем не запутаться.
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            # 21) Тут небольшая опечатка, нужно поставить одинарное =, иначе
            # строчка ниже не будет иметь никакого эффекта и cash_remained не
            # поменяется.
            cash_remained == 1.00
            currency_type = 'руб'
        # 22) Лучше будет завести переменную, в которую мы будем присваивать
        # сообщения из блока if-else, а потом один раз вернуть её из return.
        if cash_remained > 0:
            return (
                # 23) В f-строках должна применяться только подстановка
                # переменных, и не должно быть логических операций, лучше
                # изменить значение cash_remained до вызова оператора return.
                f'На сегодня осталось {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'Денег нет, держись'
        elif cash_remained < 0:
            # 24) Не нужно использовать back-слеши для переноса.
            return 'Денег нет, держись:' \
                   ' твой долг - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)

    #  25) Так как в данном случае мы не меняем поведение метода при
    #  переопределении, то функция ниже излишня, можно её удалить.
    def get_week_stats(self):
        super().get_week_stats()

# P.S. Задача выполнена в целом хорошо, осталось немного подучить как правильно
# оформлять код.