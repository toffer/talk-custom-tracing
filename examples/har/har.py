import datetime
import json

from utc import UTC


def isoformat(timestamp):
    dt = datetime.datetime.fromtimestamp(timestamp)
    dt = dt.replace(tzinfo=UTC())
    return dt.isoformat()


class HAR(object):

    def __init__(self):
        self.creator = {'name': 'har.py', 'version': '0.1'}
        self.pages = []
        self.entries = []
        self.comment = ''

    def add_page(self, page):
        self.pages.append(page)

    def add_entry(self, entry):
        self.entries.append(entry)

    def _sorted_entries(self):
        return sorted(self.entries, key=lambda x: x.timestamp)

    def asdict(self):
        return {
            'log': {
                'version': '1.2',
                'creator': self.creator,
                'pages': [p.asdict() for p in self.pages],
                'entries': [e.asdict() for e in self._sorted_entries()],
                'comment': self.comment,
            }
        }

    def json(self):
        return json.dumps(self.asdict())


class HARPage(object):

    def __init__(self, page_id, title, timestamp, timings=None):
        self.page_id = page_id
        self.title = title
        self.timestamp = timestamp

        if timings is None:
            timings = {'onContentLoad': -1, 'onLoad': -1}
        self.timings = timings

    def asdict(self):
        return {
            'id': self.page_id,
            'title': self.title,
            'startedDateTime': isoformat(self.timestamp),
            'pageTimings': self.timings,
        }


class HAREntry(object):

    def __init__(self, name, page_ref, timestamp, duration):
        self.name = name
        self.page_ref = page_ref
        self.timestamp = timestamp
        self.duration = duration

        self.request = self._make_request()
        self.response = self._make_response()
        self.timings = self._make_timings()

        self.started_date_time = isoformat(self.timestamp)

    def _make_request(self):
        return {
            "method": 'FUNC',
            "url": self.name,
            "httpVersion": "HTTP/1.1",
            "cookies": [],
            "headers": [],
            "queryString" : [],
            "postData" : {'mimeType': 'text/plain'},
            "headersSize" : -1,
            "bodySize" : -1,
            "comment" : ""
        }

    def _make_response(self):
        return {
            "status": 200,
            "statusText": "OK",
            "httpVersion": "HTTP/1.1",
            "cookies": [],
            "headers": [],
            "content": {'size': 1, 'mimeType': 'text/plain'},
            "redirectURL": "",
            "headersSize" : -1,
            "bodySize" : -1,
            "comment" : ""
        }

    def _make_timings(self):
        return {
            "blocked": 0,
            "dns": 0,
            "connect": 0,
            "send": 0,
            "wait": self.duration,
            "receive": 0,
            "ssl": 0,
            "comment": "",
        }

    def asdict(self):
        return {
            "pageref": self.page_ref,
            "startedDateTime": self.started_date_time,
            "time": self.duration,
            "request": self.request,
            "response": self.response,
            "cache": {},
            "timings": self.timings,
        }

if __name__ == '__main__':

    # Dummy times one second apart
    page_start_time = datetime.datetime.now(UTC())
    entry_ts_1 = page_start_time + datetime.timedelta(0, 1)
    entry_ts_2 = entry_ts_1 + datetime.timedelta(0, 1)

    har = HAR()

    hp = HARPage('id_0', 'Page Title for id_0', page_start_time.timestamp())
    har.add_page(hp)

    e1 = HAREntry('entry_1', 'id_0', entry_ts_1.timestamp(), 940)
    e2 = HAREntry('entry_2', 'id_0', entry_ts_2.timestamp(), 550)
    har.add_entry(e1)
    har.add_entry(e2)

    print(har.json())
