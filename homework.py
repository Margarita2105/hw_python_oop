import datetime as dt


in_seven_days = dt.date.today() - dt.timedelta(7)


class Calculator:
    gts_amount = 0
    ws_amount = 0

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        for rec in self.records:
            if rec.date == dt.date.today():
                self.gts_amount += rec.amount
        return self.gts_amount

    def get_week_stats(self):
        in_seven_days = dt.date.today() - dt.timedelta(7)
        for rec in self.records:
            if rec.date >= in_seven_days:
                self.ws_amount += rec.amount
        return self.ws_amount


class CaloriesCalculator(Calculator):

    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        self.lim = self.limit - self.get_today_stats()
        if self.lim <= 0:
            self.answer = 'Хватит есть!'
        else:
            self.answer = 'Сегодня можно съесть что-нибудь ещё,' \
                          ' но с общей калорийностью не более '\
                          f'{self.lim}' ' кКал'
        return self.answer


class CashCalculator(Calculator):
    USD_RATE = 60.0
    EURO_RATE = 70.0

    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        self.currency = currency
        self.lim = self.limit - self.get_today_stats()
        cur = {'usd': 60.0, 'eur': 70.0, 'rub': 1}
        cur1 = {'usd': 'USD', 'eur': 'Euro', 'rub': 'руб'}
        if self.lim == 0:
            self.answer = 'Денег нет, держись'
        elif self.lim < 0:
            self.c = round(self.lim / cur[currency], 2)
            self.answer = 'Денег нет, держись: твой долг - ' \
                          '' f'{- float(self.c)} {cur1[currency]}'
        else:
            if currency == 'usd':
                us = round(self.lim / self.USD_RATE, 2)
                self.answer = f'На сегодня осталось {us} USD'
            elif currency == 'eur':
                eu = round(self.lim / self.EURO_RATE, 2)
                self.answer = f'На сегодня осталось {eu} Euro'
            else:
                self.answer = f'На сегодня осталось {float(self.lim)} руб'
        return self.answer


class Record:
    def __init__(self, amount, comment, date=dt.date.today()):
        self.amount = amount
        self.comment = comment
        self.date = date
        if isinstance(self.date, str):
            dn = dt.datetime.strptime(date, "%d.%m.%Y")
            self.date = dn.date()

cash_calculator = CashCalculator(1000)
# дата в параметрах не указана,
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment="кофе"))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
print(cash_calculator.get_today_cash_remained("rub"))
c = Calculator(1000)
c.add_record(Record(145, 'fg'))
c.add_record(Record(300, 'fg'))
c.add_record(Record(3000, 'fg', '4.3.2020'))
c1 = c.get_today_stats()
print(c1)
print(1000 - c1)
