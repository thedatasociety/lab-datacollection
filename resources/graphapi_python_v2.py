import facebook
import urllib3
import json
import pprint

token = ''

graph_api = facebook.GraphAPI(access_token=token, version="3.1")

# Obtendo amigos
me = graph_api.get_object('me')
my_friends = graph_api.get_connections(me['id'], 'friends')['summary']
pprint.pprint(my_friends)
