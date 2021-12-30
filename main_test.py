import main


def test():
    results = main.extract_dates(" 08:00 AM 23 dec 2019")
    boolean = 2019 == results.year
    if boolean:
        print('Test passed', results.year)
    boolean = 23 == results.day
    if boolean:
        print('test passed', results.day)

    boolean = 12 == results.month
    if boolean:
        print('test passed', results.month)


if __name__ == '__main__':
    test()
