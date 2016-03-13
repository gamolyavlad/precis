from handlers.indexHandler import indexHandler
from handlers.searchTextHendler import searchTextHendler

url_patterns = [
    (r"/", indexHandler),
    (r"/searchText/?(?P<text>[^\/]+)?/",searchTextHendler)
]
