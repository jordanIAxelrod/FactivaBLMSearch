from bs4 import BeautifulSoup
import datetime as dt
import re
import pandas as pd
import matplotlib.pyplot as plt


def extract_dates(date_string: str) -> dt.date:
    """
    Takes a string from factiva containing a date and extracts it into a datetime.date obj
    :param date_string: string containing a date
    :return dt.date: date in the string
    """
    date_string = str(date_string)
    year = re.search(r'\d{4}(?!\swords)', date_string)[0]
    try:
        day = re.search(r'\s\d{2}\s(?!words)', date_string)[0]
    except IndexError:
        day = re.search(r'\s\d\s(?!words)', date_string)[0]
    except TypeError:
        day = re.search(r'\s\d\s(?!words)', date_string)[0]

    print(day)
    month_dict = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'may': 5,
        'jun': 6,
        'jul': 7,
        'aug': 8,
        'sep': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12
    }
    month = [
        month
        for (month, fil) in zip(
            month_dict.values(),
            [month in date_string.lower() for month in month_dict.keys()]
        )
        if fil
    ][0]
    return dt.date(
        year=int(year),
        day=int(day),
        month=month
    )


def read_dates(url: str) -> list:
    """
    Reads from the file and returns all the dates
    :param url:
    :return dates: list of dates in the file
    """
    with open(url, "r", encoding='utf8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        date_strings = soup.find_all(class_='leadFields')
        dates = [extract_dates(date_str) for date_str in date_strings]
        return dates


def plot_fig(data: pd.Series) -> None:
    """
    Given a Series, plot the values vs the index
    :param data: contains the data you'd like to plot
    :return:
    """
    fig, ax = plt.subplots()
    ax.scatter(data.index, data.values)
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of BLM Articles')
    plt.savefig('Daily articles.png')


def main(url: str) -> None:
    """
    Reads The dates from all leadField and saves a plot of the
    dates of the articles, saves the data in a csv.
    :param url: path to the file
    :return: None
    """
    date_list = []
    split_url = url.split('.')
    fact = split_url[-2]
    for i in range(1, 13):
        split_url[-2] = fact + str(i)
        new_url = '.'.join(split_url)

        date_list.extend(read_dates(new_url))

    date_series = pd.Series(date_list)

    counts = date_series.value_counts()
    plot_fig(counts)

    counts.to_csv('Dates of Articles BLM.csv')
    print(counts)


if __name__ == '__main__':
    main(r"Factiva Search Results\Factiva.html")
