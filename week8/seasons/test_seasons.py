import seasons as s
from datetime import date


def test_date_format():
    s.valid_date_format("2022-12-29") == True
    s.valid_date_format("2020-1-2") == False
    s.valid_date_format("1900-9-13") == False
    s.valid_date_format("1000-01-20") == True
    s.valid_date_format("1950-01-29") == True
    s.valid_date_format("2000-7-11") == False
    s.valid_date_format("2000-07-11") == True


def test_existing_date():
    today = date.today()
    one_year_later_today = today.replace(year=today.year + 1).isoformat()
    one_day_later_today = today.replace(day=today.day + 1).isoformat()

    s.date_existed("2022-12-29") == True
    s.date_existed("1910-02-24") == True
    s.date_existed("2000-11-10") == True
    s.date_existed(one_year_later_today) == False
    s.date_existed(one_day_later_today) == False


def test_verbose_minutes():
    today = date.today()
    one_year_before_today = today.replace(year=today.year - 1).isoformat()
    two_years_before_today = today.replace(year=today.year - 2).isoformat()
    five_years_before_today = today.replace(year=today.year - 5).isoformat()

    s.age_as_minutes(
        one_year_before_today
    ) == "Five hundred twenty-five thousand, six hundred minutes"
    s.age_as_minutes(
        two_years_before_today
    ) == "One million, fifty-one thousand, two hundred minutes"
    s.age_as_minutes(
        five_years_before_today
    ) == "Two million, six hundred twenty-eight thousand minutes"
