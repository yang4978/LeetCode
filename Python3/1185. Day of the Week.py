class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

        total = day + sum(month_days[:month-1]) + int(month>2 and ((year%4==0 and year%100!=0) or year%400==0)) + sum(1 if ((i%4==0 and i%100!=0) or i%400==0) else 0 for i in range(1971,year)) + (year-1971)*365

        return weekday[(total+4)%7]
