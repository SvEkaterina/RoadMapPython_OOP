from functools import total_ordering
 

@total_ordering
class CustomString(str):
    def __new__(cls, string):
        return str.__new__(cls, string)


    def __init__(self, string):
        self.string = string
    

    def __gt__(self, other):
        return len(self) > len(other)


    def __lt__(self, other):
        return len(self) < len(other)


    def __ge__(self, other):
        return len(self) >= len(other)


    def __le__(self, other):
        return len(self) <= len(other)


    def __eq__(self, other):
        return len(self) == len(other)


def test_string_comparation():
    short_latin_str = CustomString("Apples")
    short_kiril_str = CustomString("Яблоко")
    long_str = CustomString("Hello my name is Python")
    simple_str = "simple"

    print("Start test_string_comparation...")
    assert (short_latin_str == short_kiril_str)

    assert (short_latin_str < long_str)
    assert (short_latin_str <= long_str)
    assert (long_str > short_latin_str)
    assert (long_str >= short_latin_str)

    assert (short_kiril_str < long_str)
    assert (short_kiril_str <= long_str)
    assert (long_str > short_kiril_str)
    assert (long_str >= short_kiril_str)

    assert (not short_kiril_str > simple_str)
    assert (short_kiril_str == simple_str)

    print('OK')


if __name__ == "__main__":
    test_string_comparation()
