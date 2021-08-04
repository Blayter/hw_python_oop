import datetime as dt

DATE_FORMAT = '%d.%m.%Y'
# Единственное, что пока пришло в голову, хотя почитав
# про now и today особой разницы не увидел
date_now = dt.date.today()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, new_record):
        self.records.append(new_record)

    def get_today_stats(self):
        spent_today = 0
        for record in self.records:
            if record.date == date_now:
                spent_today += record.amount
        return spent_today

    def get_today_remained(self):
        remainder = self.limit - self.get_today_stats()
        return remainder

    def get_week_stats(self):
        week_spent = 0
        delta = dt.timedelta(days=7)
        seven_days = date_now - delta
        for record in self.records:
            if seven_days < record.date <= date_now:
                week_spent += record.amount
        return week_spent


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is not None:
            self.date = dt.datetime.strptime(date, DATE_FORMAT).date()
        else:
            self.date = date_now


class CashCalculator(Calculator):
    USD_RATE = 73.00
    EURO_RATE = 85.00

    def get_today_cash_remained(self, currency):
        currency_list = {
            'usd': (self.USD_RATE, 'USD'),
            'eur': (self.EURO_RATE, 'Euro'),
            'rub': (1, 'руб')
        }

        if currency not in currency_list:
            return 'валюта не определена'

        rate, name = currency_list[currency]

        remainder = round(self.get_today_remained() / rate, 2)
        module_reminder = abs(remainder)
        # Про guard block пока не очень понял, перечитаю на свежую голову
        if remainder == 0:
            return 'Денег нет, держись'
        elif remainder > 0:
            return f'На сегодня осталось {remainder} {name}'
        else:
            return f'Денег нет, держись: твой долг - {module_reminder} {name}'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories = self.get_today_remained()
        if calories <= 0:
            return 'Хватит есть!'
        # Получается в else нет смысла, достаточно return
        return ('Сегодня можно съесть что-нибудь ещё, но '
                f'с общей калорийностью не более {calories} кКал')
