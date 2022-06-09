# Own modules
import my_module
my_module.add(5, 5)
my_module.sustract(10, 5)

# Third party modules
from colorama import Fore, Style, init
init(convert=True)
print(Fore.RED + 'Hello World')

# Python modules
# import datetime # https://docs.python.org/3/library/datetime.html
from datetime import timedelta, date

print(date.today()) # 2022-06-09
print(timedelta(minutes=70)) # 1:10:00