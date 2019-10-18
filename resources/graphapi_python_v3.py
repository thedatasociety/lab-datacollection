import facebook
import urllib3
import json
import pprint

token = ''

graph_api = facebook.GraphAPI(access_token=token, version="3.1")

# Obtendo os meus likes
me = graph_api.get_object('me')
my_likes = graph_api.get_connections(me['id'], 'likes')
pprint.pprint(my_likes)
while 'paging' in my_likes.keys() and 'next' in my_likes['paging'].keys():
    try:
        http = urllib3.PoolManager()
        my_likes = http.request('GET', my_likes['paging']['next'])
        my_likes = json.loads(my_likes.data)
        pprint.pprint(my_likes)
    except Exception as ex:
        pprint.pprint(ex)
        break