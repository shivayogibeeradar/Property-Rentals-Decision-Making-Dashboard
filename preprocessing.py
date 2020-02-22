import tqdm
from tqdm._tqdm_notebook import tqdm_notebook
from googlegeocoder import GoogleGeocoder
from pygeocoder import Geocoder

def impute_zip(df):
	geocoder=Geocoder('your-api-key')
	tqdm_notebook().pandas()
	df.loc[df["zipcode"].isnull(),"zipcode"]=df[df["zipcode"].isnull()].progress_apply(lambda row: geocoder.reverse_geocode(row['latitude'],row['longitude'])[0].postal_code,axis=1)
	return(df)

def zipcode_check(df):
	df=df[df["zipcode"].notnull()]
	df1=df.drop(df[df.zipcode.str.len() > 5].index)
	df1["zipcode"]=df1["zipcode"].astype(int)
	return(df1)
def citysubset(df,city):
	df=df[df["City"]=="New York"].reset_index(drop=True)
	return(df)
