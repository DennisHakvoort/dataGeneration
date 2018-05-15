import random
import string
from datetime import datetime
from datetime import timedelta


def generate_alpha_string(length):
    return ''.join([random.choice(string.ascii_letters) for x in range(length)])

def generate_alpha_numeric_string(length):
    return ''.join([random.choice(string.ascii_letters+string.digits) for x in range(length)])

def generate_random_date(min, max):
    delta = max - min
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return min + timedelta(seconds=random_second)


# for x in range(100):
#     print(generate_random_date(datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p'), datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')))