class MyError(Exception):
    ...

class OtherError(Exception):
    ...

def raise_an_exception():
    exception_ = MyError('a', 'b', 'c')
    exception_.add_note('Look the note 1')
    exception_.add_note('you miss that')
    raise exception_
try: 
    raise_an_exception()

except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OtherError("I'm gonna raise again")
    exception_.add_note('Another note')
    exception_.__notes__ += error.__notes__.copy()
    raise exception_ from error