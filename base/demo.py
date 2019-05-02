import json
import requests


class RunMain():
    #def __init__(self, url, method, data=None):
        #self.res = self.run_main(url, method, data=None)

    def send_get(self, url, data):
        res = requests.get(url=url, data=data).json()
        return json.dumps(res, indent=2, sort_keys=True)

    def send_post(self, url, data):
        res = requests.post(url=url, data=data).json()
        return json.dumps(res, indent=2, sort_keys=True)

    def run_main(self, url, method, data=None):
        res = None
        if method == 'POST':
            res = self.send_post(url, data)
        else:
            res = self.send_get(url, data)
        return res


if __name__ == '__main__':
    url = 'http://coding.imooc.com/api/cate'
    data = {'secrect': '8c12a788038a2671b5e0a8a6dc30673d',
            'timestamp': '1530084524251',
            'token': '755ce48a29737df0287a029c7ede5fe5',
            'uid': '5409699'
            }
    rm = RunMain()
    print(rm.run_main(url, 'POST', data))
