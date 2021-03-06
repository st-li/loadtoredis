import redis
import json
import pandas as pd

if __name__ == '__main__':
    conn = redis.Redis('127.0.0.1', 6379)
    origin_list = pd.read_csv('pure_chn_link.csv', header=None)
    for index, row in origin_list.iterrows():
        key, value = row
        result = conn.hget('rg_chinese', key)
        if not result:
            conn.hset('rg_chinese', key, value)