from datetime import datetime


def add_years(date, years):
    '''
    helper function to preform datetime calculations
    :param date: datetime
    :param years: int
    :return: datetime
    '''
    try:
        return date.replace(year=date.year + years).replace(tzinfo=None)
    except ValueError:
        return (
            date +
            (
                datetime.date(date.year + years, 1, 1) -
                datetime.date(date.year, 1, 1)
            )
        ).replace(tzinfo=None)
