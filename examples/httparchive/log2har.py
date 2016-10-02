import csv
import sys

from har import HAR, HARPage, HAREntry


def read_log(filename):
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            parsed = (row[0], float(row[1]), float(row[2]))
            yield parsed


def get_page_start_time(filename):
    """The timestamp of the last row will be the earliest timestamp,
    so use that as the page start time.

    """
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            continue

    _, page_start_time, _ = row
    return float(page_start_time)


def main(argv=None):
    if argv is None:
        argv = sys.argv

    try:
        filename = sys.argv[1]
    except:
        return 1

    pageref = 'page_id_0'
    page_start_time = get_page_start_time(filename)

    har = HAR()

    page = HARPage(pageref, 'Title for page_id_0', page_start_time)
    har.add_page(page)

    for line in read_log(filename):
        (name, start_time, duration) = line
        entry = HAREntry(name, pageref, start_time, duration)
        har.add_entry(entry)

    print(har.json())

if __name__ == '__main__':
    sys.exit(main())
