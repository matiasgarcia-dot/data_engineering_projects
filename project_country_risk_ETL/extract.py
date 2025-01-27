import pandas as pd
import requests

url= "https://api.argentinadatos.com/v1/finanzas/indices/riesgo-pais"

req= requests.get(url)

if req.status_code==200:
    print("Good Request")
    data= req.json()
       
else:
    print("Error Request")

df = pd.DataFrame(data)
print(df.head())  
    