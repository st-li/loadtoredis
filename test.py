import redis

if __name__ == '__main__':
    conn = redis.Redis('127.0.0.1', 6379)
    all_urls = conn.hgetall('rg_chinese')
    all_urls.values()
    a = all_urls.values()
    keys = all_urls.keys()
    print 'There are %d records in Redis' % len(keys)
    for i in range(10):
        print a[i]