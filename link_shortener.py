#!/usr/bin/python
import requests
import sys

bitly_shorten_api = 'https://api-ssl.bitly.com/v3/shorten?access_token={0}&longUrl={1}'
bitly_expand_api = 'https://api-ssl.bitly.com/v3/expand?access_token={0}&shortUrl={1}'
bitly_clicks_api = 'https://api-ssl.bitly.com/v3/link/clicks?access_token={0}&link={1}'
auth = '18d3fe31091ee0fe3547b4ec251b766700e9553e'

def shorten_url(url_to_short): 
    response = requests.get(bitly_shorten_api.format(auth, url_to_short))
    if response.status_code != 200:
        print 'unable to create short link for : {}'.format(link_to_short)
        return None
    else:
        json = response.json()
        return json['data']['url']

def expand_url(url_to_expand):
    response = requests.get(bitly_expand_api.format(auth, url_to_expand))
    if response.status_code != 200:
        print 'unable to expand link : {0}'.url_to_expand
    else:
        json = response.json()
        return json['data']['expand'][0]['long_url']

def url_clicks(url):
    response = requests.get(bitly_clicks_api.format(auth, url))
    if response.status_code != 200:
        print 'unable to find clicks info about: {0}'.format(url)
        return None
    else:
        json = response.json();
        return json['data']['link_clicks']



def build_query():
    size = len(sys.argv)
    link = sys.argv[size - 1]
    if link.startswith('-'):
        return None, None
    args = sys.argv[1:]
    opt = []
    for arg in args:
        if str(arg).startswith('-'):
            cmd_ops = arg[1:]
            for i in range(len(cmd_ops)):
                opt.append(cmd_ops[i])
    return opt, link

def perform_opration(opt, link):
    if opt == None or len(opt) == 0 or link == None or len(link) == 0:
        print 'invalid command opt: {0} , link: {1}'.format(opt, link)
        return
    for op in opt:
        if op == 's':
            print 'Link shorted: {0}'.format(shorten_url(link))
        elif op == 'e':
            print 'Expanded link: {0}'.format(expand_url(link))
        elif op == 'c':
            print 'Number of clicks: {0}'.format(url_clicks(link))
        elif op == 'x':
            print 'x'

if __name__ == '__main__':
    opt, link = build_query()
    perform_opration(opt, link)