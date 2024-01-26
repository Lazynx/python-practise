from datetime import datetime, timedelta
from time import sleep

# ex_1
print(datetime.now() - timedelta(days=5))

# ex_2
print(f"Today: {datetime.today()}, yesterday: {datetime.today() - timedelta(days=1)}, tomorrow:"
      f" {datetime.today() - timedelta(days=1)}")

# ex_3
print(f"{datetime.today()}, without microseconds: {datetime.today().replace(microsecond=0)}")

# ex_4
date_1 = datetime.now()
sleep(2)
date_2 = datetime.now()
print((date_2 - date_1).seconds)
