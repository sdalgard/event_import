
import pandas as pd
from eventregistry import *

def panda_to_jsonfile(pd, file_name):
    pd.to_json(path_or_buf=file_name, orient='records', date_format='iso', date_unit='s')        
    

# query and downloaded data    
er = EventRegistry(apiKey = 'd584d800-b401-4452-8e69-db670203bf94')

romeLocationUri = "http://en.wikipedia.org/wiki/Rome"
milanLocationUri = "http://en.wikipedia.org/wiki/Milan"
cq = ComplexEventQuery(
    CombinedQuery.AND(
        [
            CombinedQuery.OR(
                [
                    BaseQuery(locationUri = romeLocationUri),
                    BaseQuery(locationUri = milanLocationUri)
                ]
            ),
            BaseQuery(dateStart = "2018-01-01", 
                      dateEnd = "2018-02-28",
                      lang = "eng"),
            BaseQuery(minArticlesInEvent = 400)
        ]
    )
)
#q = QueryEvents.initWithComplexQuery(cq)
#q.setRequestedResult(RequestEventsInfo())
#res = self.er.execQuery(q)
count = 0
art_arr = []
iter = QueryEventsIter.initWithComplexQuery(cq)
for art in iter.execQuery(er):
    art_arr.append(art)
    count += 1
    if count > 20:
        break
panda = pd.Series(art_arr)    
panda_to_jsonfile(panda, 'event_rome_milan_date.json')




