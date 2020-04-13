import urllib3

def test_home():
    http = urllib3.PoolManager()
    r = http.request('GET', "http://worker-node/")
    assert r.status == 200
