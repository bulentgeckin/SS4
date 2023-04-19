from datetime import date

if __name__ == '__main__':
    today = date.today()
    print(today)  # today: 2021-12-01
    print(today.year)  # 2021
    print(today.month)  # 04
    print(today.day)  # 01

    birth_date = date(2000, 4, 3)
    print(birth_date)  # 2023-03-04
    print(birth_date.year)  # 2000


    #  https://www.w3schools.com/python/python_datetime.asp#:~:text=A%20date%20in%20Python%20is,with%20dates%20as%20date%20objects.
    print(birth_date.strftime("%A"))  # Monday
    print(birth_date.strftime("%a"))  # Mon
    print(birth_date.strftime("%B"))  # April
    print(birth_date.strftime("%b"))  # Apr

    print(today - birth_date)
