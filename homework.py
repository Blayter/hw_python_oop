import datetime as dt

date_now = dt.datetime.now().date()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        spent_today = 0
        for i in self.records:
            if i.date == date_now:
                spent_today += i.amount
        return spent_today

    def get_today_remained(self):
        remainder = self.limit - self.get_today_stats()
        return remainder

    def get_week_stats(self):
        week_spent = 0
        delta = dt.timedelta(days=7)
        seven_days = date_now - delta
        for i in self.records:
            if seven_days < i.date <= date_now:
                week_spent += i.amount
        return week_spent


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.date = date_now
        self.comment = comment
        if date is not None:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class CashCalculator(Calculator):
    USD_RATE = 73.00
    EURO_RATE = 85.00

    def get_today_cash_remained(self, currency):
        if currency == 'rub':
            rate = 1
            name = 'руб'
        elif currency == 'usd':
            rate = self.USD_RATE
            name = 'USD'
        elif currency == 'eur':
            rate = self.EURO_RATE
            name = 'Euro'
        else:
            return 'валюта не определена'

        remainder = round(self.get_today_remained() / rate, 2)
        if remainder > 0:
            return f'На сегодня осталось {remainder} {name}'
        elif remainder == 0:
            return 'Денег нет, держись'
        else:
            return f'Денег нет, держись: твой долг - {abs(remainder)} {name}'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories = self.get_today_remained()
        if calories <= 0:
            return 'Хватит есть!'
        else:
            return (f'Сегодня можно съесть что-нибудь ещё, но '
                    f'с общей калорийностью не более {calories} кКал')
