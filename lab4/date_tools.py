from datetime import datetime
from dateutil.relativedelta import relativedelta
from rich import print


def show_date():
    today = datetime.now()
    future = today + relativedelta(days=7)
    print(f"Сьогодні: {today:%d.%m.%Y}")
    print(f"Через 7 днів: {future:%d.%m.%Y}")