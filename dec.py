from datetime import datetime
from habr import scrap_main_page
from fake_useragent import UserAgent
from pprint import pprint

def logger(filename: str):
    def logger_(func):
        def new_func(*args, **kwargs):
            time = datetime.now().strftime('%d.%m.%y %H:%M:%S')
            name = func.__name__
            result = func(*args, **kwargs)
            string_to_append = f'Function {name} run at {time} with args {args} {kwargs}. Function return {result};\n'
            with open(f'{filename}', 'a') as file:
                file.write(string_to_append)
            return result
        return new_func
    return logger_


decorator = logger('log.txt')
decorated_scrap_main_page = decorator(scrap_main_page)
pprint(decorated_scrap_main_page(UserAgent().google))
