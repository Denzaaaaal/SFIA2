import urllib3

def test_home():
    http = urllib3.PoolManager()
    r = http.request('GET', "http://worker/")
    assert r.status == 500
