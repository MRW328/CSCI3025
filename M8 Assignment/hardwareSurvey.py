import pandas as pd
import matplotlib.pyplot as pp
import numpy

#this program reads computer hardware surveys from Steam
#and analyzes the dats to answer 2 analysis questions:
#When did ATI have the highest market share? and 
#WHat is the current distribution of video graphic cards by vendor?

#creats dataframe of Steam survey data 
myData = pd.read_csv('shs.csv')
print("dataframe head: \n\n", myData.head())
print('################################')
print("dataframe shape: \n\n", myData.shape) #row and column count
print('################################')
print("dataframe data types: \n\n", myData.dtypes)
print('################################')



#change date from string to datetime
myData['date'] = pd.to_datetime(myData['date'])
#filter by video card description
myData = myData[myData['category'] == 'Video Card Description'] 
#remove NaN from dataframe
myData = myData.dropna(subset=['name'] ) 
#removes any blank names, though after testing there was none found
myData = myData[myData['name'] != ''] 

print(myData.duplicated().sum()) #check for duplicates


#each condition checks if the name contains the specified string
#if no condition matches, the vendor is labeled as 'Unknown'
conditions = [
    myData['name'].str.contains('NVIDIA', case=False),
    myData['name'].str.contains('ATI|AMD', case=False),
    myData['name'].str.contains('Intel', case=False)
]

vendors = ['NVIDIA', 'AMD', 'Intel']
myData['vendor'] = numpy.select(conditions, vendors, default='Unknown')
print(myData['vendor'].value_counts())


#groups the data by date and vendor, then sum the percentage column
#to get total market share per vendor for each month
vendorShare = myData.groupby(['date', 'vendor'])['percentage'].sum().reset_index()

#print(vendorShare.head(10))

#filters vendorShare to just NVIDIA and AMD rows
nvidia = vendorShare[vendorShare['vendor'] == 'NVIDIA']
amd = vendorShare[vendorShare['vendor'] == 'AMD']

#finds the average market share for each vendor across all months
nvidiaAvg = nvidia['percentage'].mean()
amdAvg = amd['percentage'].mean()

#calculates NVIDIA's average lead over AMD
print(f"NVIDIA average share: {nvidiaAvg:.2%}")
print(f"AMD average share: {amdAvg:.2%}")
print(f"NVIDIA's average lead: {nvidiaAvg - amdAvg:.2%}")

#finds the month where AMD had its highest market share
amdPeak = amd.loc[amd['percentage'].idxmax()]

print(f"AMD's peak market share: {amdPeak['percentage']:.2%}")
print(f"Date: {amdPeak['date']}")

#plots NVIDIA and AMD market share over time as a line chart
pp.figure(figsize=(12, 6)) 
pp.plot(nvidia['date'], nvidia['percentage'], label='NVIDIA')
pp.plot(amd['date'], amd['percentage'], label='AMD')

pp.title('NVIDIA vs AMD GPU Market Share on Steam (2008-2026)')
pp.xlabel('Date')
pp.ylabel('Market Share')
pp.legend()
pp.tight_layout()


#gets the most recent month's data for each vendor
latestMonth = vendorShare[vendorShare['date'] == vendorShare['date'].max()]

#creates a bar chart of current vendor market share
pp.figure(figsize=(8, 5))
pp.bar(latestMonth['vendor'], latestMonth['percentage'])

pp.title('GPU Vendor Market Share on Steam - March 2026')
pp.xlabel('Vendor')
pp.ylabel('Market Share')
pp.tight_layout()


pp.show()
