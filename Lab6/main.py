from decorator import add_prefix
from function import get_text


@add_prefix
def result():
    return get_text()


print(result())
