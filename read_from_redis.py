import pandas as pd
import redis
import hashlib

if __name__ == '__main__':
    conn = redis.Redis('127.0.0.1', 6379)
    all_urls = conn.hgetall('rg_chinese')
    f = open('urls_left', 'a+')
    for url in all_urls.values():
        key = hashlib.sha256(url).hexdigest()
        str = key + ',' + url + '\n'
        f.write(str)
    f.close()
