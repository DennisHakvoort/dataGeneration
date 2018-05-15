import datetime
import random
import string
from datetime import timedelta


def generate_alpha_string(length):
    return ''.join([random.choice(string.ascii_letters) for x in range(length)])

def generate_alpha_numeric_string(length):
    return ''.join([random.choice(string.ascii_letters+string.digits) for x in range(length)])

def generate_random_date(min, max):
    min = datetime.strptime(min '%m/%d/%Y %I:%M %p')
    max = datetime.strptime(max, '%m/%d/%Y %I:%M %p')
    delta = max - min
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return min + timedelta(seconds=random_second)


for x in range(100):
    # print(generate_alpha_string(random.randrange(3, 19)))
    print(generate_random_date('1/1/2008 1:30 PM', '1/1/2009 4:50 AM'))