import datetime
import re
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, TakeFirst, MapCompose

def extract_ip_address(string):
    regex = re.compile("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}")
    match = regex.search(string)
    if match: 
        return match.group()
    else:
        return ''

def extract_numbers(string):
    regex = re.compile("(?P<id>[0-9]+)")
    match = regex.search(string)
    if match:
        return match.groups()[0]
    else:
        return None

def strip_start_date(s):
    return s.replace('Start Date ', '')

def to_datetime_long(s):
    try:
        dt = datetime.datetime.strptime(s, '%b %d %Y, %I:%M %p')
    except ValueError:
        today = datetime.date.today()
        now = datetime.datetime.now()
        # We lose the time here.
        if 'Yesterday' in s:
            yesterday = today - datetime.timedelta(days=1)
            time = datetime.datetime.strptime(s, 'Yesterday, %I:%M %p').time()
            dt = datetime.datetime.combine(yesterday, time)
        elif 'Today' in s:
            time = datetime.datetime.strptime(s, 'Today, %I:%M %p').time()
            dt = datetime.datetime.combine(today, time)
        elif 'minute' in s:
            min_str = s.split(" ")[0]
            if re.match("^[0-9]+$",min_str):
                m = int(min_str)
            elif min_str == "One":
                m = 1
            else:
                raise Exception("Could not parse '%s' as time" % (s,))
            dt = now - datetime.timedelta(minutes=m)
        else:
            raise Exception("Could not parse '%s' as time" % (s,))
    return dt

def to_datetime_short(s):
    try:
        return datetime.datetime.strptime(s, '%B %d, %Y')
    except ValueError:
        return None

def to_int(s):
    non_decimal = re.compile(r'[^\d]+')
    return non_decimal.sub('', s)


class ForumLoader(XPathItemLoader):
    default_output_processor = TakeFirst()

    zeta_id_in = MapCompose(unicode.strip, extract_numbers)


class ThreadLoader(XPathItemLoader):
    default_output_processor = TakeFirst()

    zeta_id_in = MapCompose(unicode.strip, extract_numbers)
    user_in = MapCompose(unicode.strip)
    replies_in = MapCompose(unicode.strip, to_int)
    views_in = MapCompose(unicode.strip, to_int)
    date_posted_in = MapCompose(unicode.strip, strip_start_date, to_datetime_long)


class PostLoader(XPathItemLoader):
    default_output_processor = TakeFirst()

    zeta_id_in = MapCompose(unicode.strip, extract_numbers)
    ip_address_in = MapCompose(unicode.strip, extract_ip_address)
    date_posted_in = MapCompose(unicode.strip, to_datetime_long)


class RawPostLoader(XPathItemLoader):
    default_output_processor = TakeFirst()

    zeta_id_in = MapCompose(unicode.strip, extract_numbers)


class UserLoader(XPathItemLoader):
    default_output_processor = TakeFirst()

    zeta_id_in = MapCompose(unicode.strip, extract_numbers)
    member_number_in = MapCompose(unicode.strip, extract_numbers)
    post_count_in = MapCompose(unicode.strip, to_int)
    signature_in = Join()
    date_birthday_in = MapCompose(unicode.strip, to_datetime_short)
    date_joined_in = MapCompose(unicode.strip, to_datetime_short)


class UserGroupLoader(XPathItemLoader):
    default_output_processor = TakeFirst()
