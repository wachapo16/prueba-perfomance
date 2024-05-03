from datetime import date, timedelta

class DateGenerator:
    @staticmethod
    def generate_future_date():
        today = date.today()
        future_date = today + timedelta(days=5)
        if future_date.weekday() in [5, 6]:
            future_date += timedelta(days=(7 - future_date.weekday()))
        return future_date.strftime("%Y-%m-%d")
