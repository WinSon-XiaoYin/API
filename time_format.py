import datetime


def format_time(year=None, month=None, day=None, hour=None, minute=None, second=None):
    start_time = datetime.datetime(year=2014, month=10, day=6, hour=18, minute=30, second=20)
    end_time = start_time.isoformat()
    print end_time[:16]


def main():
    format_time()


if __name__ == '__main__':
    main()
