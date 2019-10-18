import facebook
import urllib3
import json
import pprint

token = ''

graph_api = facebook.GraphAPI(access_token=token, version="3.1")

# Obtendo dados do próprio usuário
me = graph_api.get_object('me')

pprint.pprint(me, indent = 4)