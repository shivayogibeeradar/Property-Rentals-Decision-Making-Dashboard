def rate(df,n):
	null_series = df.isnull().sum() # The number of missing values from each column in your dataframe
	full_col_series = null_series[null_series == 0] # Will keep only the columns with no missing values

	df1 = df[full_col_series.index]
	b=df1.iloc[:,df1.shape[1]-1]
	a=df1.iloc[:,df1.columns.get_loc("SizeRank")+1]
	rate=(b-a)/(a*n)
	return(rate)
def roi_equity(df,n):
    return(((((1+df["rate"]))**n)*df["sell_price"]-df["sell_price"])/df["sell_price"])

def roi(df,n):
      return(((df["annual_rent"])*n+(((1+df["rate"]))**n)*df["sell_price"]-df["sell_price"])/df["sell_price"])