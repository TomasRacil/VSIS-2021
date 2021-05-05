from functools import wraps


def decorated(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        kwargs['text'] = "HelloWorld"
        if args[0]:
            f(*args, **kwargs)
        else:
            print("False")

    return wrapper


@decorated
def HelloWorld(test, text="pepa"):
    print(text)


HelloWorld(True, text="pepa")
