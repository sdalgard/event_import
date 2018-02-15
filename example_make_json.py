
import pandas as pd
from eventregistry import *

def panda_to_jsonfile(pd, file_name):
    pd.to_json(path_or_buf=file_name, orient='records', date_format='iso', date_unit='s')        
    

# query and downloaded data    
er = EventRegistry(apiKey = 'd584d800-b401-4452-8e69-db670203bf94')


count = 0
art_arr = []
iter = QueryEventsIter(conceptUri = er.getConceptUri("Star Wars"))
for art in iter.execQuery(er, lang = "eng"):
    art_arr.append(art)
    count += 1
    if count > 10:
        break
panda = pd.Series(art_arr)    
panda_to_jsonfile(panda, 'event_star_wars.json')


count = 0
art_arr = []
iter = QueryEventArticlesIter("eng-2940883")
for art in iter.execQuery(er, lang = "eng"):
    art_arr.append(art)
    count += 1
    if count > 10:
        break
panda = pd.Series(art_arr)    
panda_to_jsonfile(panda, 'event_2940883.json')



q = QueryArticlesIter(conceptUri = er.getConceptUri("Rome"))

count = 0
art_arr = []
for art in q.execQuery(er, sortBy = "date"):
    art_arr.append(art)
    count += 1
    if count > 10:
        break
    
panda = pd.Series(art_arr)    
panda_to_jsonfile(panda, 'article_rome.json')


q = GetTrendingConcepts(source = "news", count = 10)
trend_arr =  er.execQuery(q)
panda = pd.Series(trend_arr)    
panda_to_jsonfile(panda, 'trend_news.json')




