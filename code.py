import traceback
from decorator import send_error_to_email_decorator


@send_error_to_email_decorator
def error():
    a = 1/0
    print(a)


error()
