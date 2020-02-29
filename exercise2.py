import requests
import pandas as pd

response = requests.get('https://haveibeenpwned.woventeams.com/api/v3/breachedaccount/test@example.com?truncateResponse=false')
if response.status_code == 200:
    raw_data = response.json()
    df = pd.DataFrame.from_dict(raw_data, orient='columns')
    print(df.head(5))
    print(df.tail(5))
else:
    print('An error occurred while attempting to retrieve data from the API.')
