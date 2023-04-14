# kiểm tra dk các tháng, tháng 2 có đk đặc biệt lq đến năm nhuận, các tháng có 30 ngày, các tháng có 31 ngày
def days_in_month(month, year):
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29
        return 28
    elif month in (4, 6, 9, 11):
        return 30
    return 31

# nhập input tháng , năm
month = int(input("Enter a month (1-12): "))
year = int(input("Enter a year (YYYY): "))

# kiểm tra giá trị đã nhập vs hàm days_in_month
days = days_in_month(month, year)

print(f"There are {days} days in month {month} of year {year}.")
