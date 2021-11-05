import requests
from tqdm import tqdm
import pandas as pd
df_shp = pd.read_csv('in.csv')
shp = df_shp['shp_id'].unique()
with open('out.txt', 'w') as f:
	f.write('shipment_id' +  '\t' + 'value'+ '\t' + 'auth_method'+ '\n')
	for i in tqdm(shp):
		try:
			req_shp = requests.get("https://internal-api.mercadolibre.com/mercadoenvios/deliveries-scoring/shipments/"+str(i)+"/safety-method", headers = {"X-Client-Id":"4749098811397999"}).json() 
			value = req_shp['value']
			auth_method = req_shp['auth-method']
			f.write(str(i)  + '\t' + str(value) + '\t' + str(auth_method) +'\n')
		except Exception as e:
			print ('Error para el user input '+ str(i) + ' del tipo: ' + str(e))