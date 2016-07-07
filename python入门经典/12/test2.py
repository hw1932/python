def assert0():
    broken_int = 0
    try:
        assert type(broken_int)==type(''),'broken_int is broken'
    except AssertionError:
        print('handle the error here')

if __name__ == '__main__':
    assert0()