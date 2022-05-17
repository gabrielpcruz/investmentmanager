import requests


class Searcher:
    def __init__(self, url):
        self.url = url

        self.hearders = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

    def search(self, path_url):
        url = self.url + path_url

        return requests.get(url, self.hearders)
