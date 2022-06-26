import json
from urllib.error import URLError
from urllib.request import Request, urlopen


def getMoveTitles(substr: str, results = []):
    base_url = f"https://jsonmock.hackerrank.com/api/movies/search?Title={substr}"
    req = Request(base_url)
    try:
        resp = urlopen(req)
    except URLError as e:
        print(f"Error occured: {e}")
    else:
        json_data = json.loads(resp.read())
        main_data = json_data.get('data')
        current_page = int(json_data.get('page'))
        num_pages = int(json_data.get('total_pages'))
    
    for i in range(len(main_data)):
        results.append(main_data[i]['Title'])
    return getMoveTitles(substr, )

_substr = str(input())

res = getMoveTitles(_substr)
for res_cur in res:
    print(f"{res_cur}")
