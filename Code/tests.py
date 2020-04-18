import pandas as pd
import numpy as np
import os
import re

DATA_PATH = 'C:\\Users\\Meir\\PycharmProjects\\Final_DS_Project\\Data'
PRICE_DATA_PATH = DATA_PATH + '\\Price_Paid'
INCOME_DATA_PATH = DATA_PATH + '\\Income_By_District'

data_2018 = pd.read_csv(os.path.join(PRICE_DATA_PATH, r'pp-2018.csv'), index_col='id')
data_2017 = pd.read_csv(os.path.join(PRICE_DATA_PATH, r'pp-2017.csv'), index_col='id')
data_2016 = pd.read_csv(os.path.join(PRICE_DATA_PATH, r'pp-2016.csv'), index_col='id')
data_2015 = pd.read_csv(os.path.join(PRICE_DATA_PATH, r'pp-2015.csv'), index_col='id')
data_2014 = pd.read_csv(os.path.join(PRICE_DATA_PATH, r'pp-2014.csv'), index_col='id')
data_2013 = pd.read_csv(os.path.join(PRICE_DATA_PATH, r'pp-2013.csv'), index_col='id')
data_2012 = pd.read_csv(os.path.join(PRICE_DATA_PATH, r'pp-2012.csv'), index_col='id')
data_2011 = pd.read_csv(os.path.join(PRICE_DATA_PATH, r'pp-2011.csv'), index_col='id')
data_2010 = pd.read_csv(os.path.join(PRICE_DATA_PATH, r'pp-2010.csv'), index_col='id')
data_2009 = pd.read_csv(os.path.join(PRICE_DATA_PATH, r'pp-2009.csv'), index_col='id')
data_2008 = pd.read_csv(os.path.join(PRICE_DATA_PATH, r'pp-2008.csv'), index_col='id')
data_2007 = pd.read_csv(os.path.join(PRICE_DATA_PATH, r'pp-2007.csv'), index_col='id')
data_2006 = pd.read_csv(os.path.join(PRICE_DATA_PATH, r'pp-2006.csv'), index_col='id')
data_2005 = pd.read_csv(os.path.join(PRICE_DATA_PATH, r'pp-2005.csv'), index_col='id')
data_2004 = pd.read_csv(os.path.join(PRICE_DATA_PATH, r'pp-2004.csv'), index_col='id')
data_2003 = pd.read_csv(os.path.join(PRICE_DATA_PATH, r'pp-2003.csv'), index_col='id')
data_2002 = pd.read_csv(os.path.join(PRICE_DATA_PATH, r'pp-2002.csv'), index_col='id')
data_2001 = pd.read_csv(os.path.join(PRICE_DATA_PATH, r'pp-2001.csv'), index_col='id')
data_2000 = pd.read_csv(os.path.join(PRICE_DATA_PATH, r'pp-2000.csv'), index_col='id')
data_1999 = pd.read_csv(os.path.join(PRICE_DATA_PATH, r'pp-1999.csv'), index_col='id')

file_name = 'median_income_1999-2017.csv'
sheet = 'FTE Median'

rows_to_drop = ['united kingdom', 'great britain', 'england and wales', 'england', 'wales', 'scotland',
                'northern ireland', 'north east', 'north west', 'yorkshire and the humber', 'east midlands',
                'west midlands', 'south west', 'south east', 'east']


district_changes = {'shepway': 'folkestone and hythe', 'bournemouth': 'bournemouth, christchurch and poole',
                    'christchurch': 'bournemouth, christchurch and poole', 'castle morpeth': 'northumberland',
                    'east dorset': 'dorset', 'forest heath': 'west suffolk', 'weymouth and portland': 'dorset',
                    'poole': 'bournemouth, christchurch and poole', 'purbeck': 'dorset', 'carrick': 'cornwall',
                    'st edmundsbury': 'west suffolk', 'suffolk coastal': 'east suffolk', 'bridgnorth': 'shropshire',
                    'taunton deane': 'somerset west and taunton', 'waveney': 'east suffolk', 'west dorset': 'dorset',
                    'west somerset': 'somerset west and taunton', 'south bedfordshire': 'central bedfordshire',
                    'alnwick': 'northumberland', 'berwick-upon-tweed': 'northumberland', 'west wiltshire': 'wiltshire',
                    'blyth valley': 'northumberland', 'caradon': 'cornwall', 'chester': 'cheshire west and chester',
                    'chester-le-street': 'county durham', 'congleton': 'cheshire east', 'derwentside': 'county durham',
                    'crewe and nantwich': 'cheshire east', 'durham': 'county durham', 'easington': 'county durham',
                    'ellesmere port and neston': 'cheshire west and chester', 'north shropshire': 'shropshire',
                    'north dorset': 'dorset', 'kerrier': 'cornwall', 'mid bedfordshire': 'central bedfordshire',
                    'macclesfield': 'cheshire East', 'north cornwall': 'cornwall', 'north wiltshire': 'wiltshire',
                    'oswestry': 'shropshire', 'penwith': 'cornwall', 'restormel': 'cornwall', 'salisbury': 'wiltshire',
                    'shrewsbury and atcham': 'shropshire', 'teesdale': 'county durham', 'tynedale': 'northumberland',
                    'vale Royal': 'cheshire west and chester', 'wear valley': 'county durham', 'kennet': 'wiltshire',
                    'south shropshire': 'shropshire', 'sedgefield': 'county durham', 'wansbeck': 'northumberland',
                    'kingston upon hull': 'city of kingston upon hull', 'peterborough': 'city of peterborough',
                    'derby': 'city of derby', 'westminster': 'city of westminster', 'nottingham': 'city of nottingham',
                    'bristol, city of': 'city of bristol', 'plymouth': 'city of plymouth',
                    'wrekin': 'telford and wrekin'}

# ceremonial_counties = ['bedfordshire', 'berkshire', 'buckinghamshire', 'cambridgeshire', 'cheshire', 'cornwall',
#                        'cumberland', 'derbyshire', 'devon', 'dorset', 'durham', 'essex', 'gloucestershire',
#                        'hampshire', 'herefordshire', 'hertfordshire', 'huntingdonshire', 'kent', 'lancashire',
#                        'leicestershire', 'lincolnshire', 'middlesex', 'norfolk', 'northamptonshire',
#                        'northumberland', 'nottinghamshire', 'oxfordshire', 'rutland', 'shropshire', 'somerset',
#                        'staffordshire', 'suffolk', 'surrey', 'sussex', 'warwickshire', 'westmorland', 'wiltshire',
#                        'worcestershire', 'yorkshire']

# ceremonial_counties = ['bedfordshire', 'berkshire', 'buckinghamshire', 'cambridgeshire', 'cheshire', 'cumberland',
#                        'derbyshire', 'devon', 'durham', 'essex', 'gloucestershire', 'hampshire', 'kent',
#                        'lancashire', 'leicestershire', 'lincolnshire', 'middlesex', 'norfolk', 'northamptonshire',
#                        'nottinghamshire', 'oxfordshire', 'somerset', 'staffordshire', 'suffolk', 'surrey', 'sussex',
#                        'warwickshire', 'westmorland', 'worcestershire', 'yorkshire', 'cumbria', 'north yorkshire',
#                        'south yorkshire', 'inner london', 'outer london']


# df = pd.read_csv(io=os.path.join(DATA_PATH, file_name), sheet_name=sheet)
df = pd.read_csv(os.path.join(INCOME_DATA_PATH, file_name))

x = 2

data_years = [data_2018, data_2017, data_2016, data_2015, data_2014, data_2013, data_2012, data_2011, data_2010,
              data_2009, data_2008, data_2007, data_2006, data_2005, data_2004, data_2003, data_2002, data_2001,
              data_2000, data_1999]


income_districts = df[df.keys()[-14]].unique()[7:-35]

income_districts = [re.sub(' ua', '', income_districts[i].lower().strip()) for i in range(len(income_districts))]
income_districts = [re.sub(' mc', '', income_districts[i]) for i in range(len(income_districts))]
income_districts = [income_districts[i].split(' / ')[0] for i in range(len(income_districts))]
income_districts = [re.sub('county ', '', income_districts[i]) for i in range(len(income_districts))]

for i in range(len(income_districts)):
    if income_districts[i] in district_changes:
        income_districts[i] = district_changes[income_districts[i]]
# income_districts = [i for i in income_districts if i not in ceremonial_counties]
income_districts = [income_districts[i] for i in range(len(income_districts)) if income_districts[i] not in
                    rows_to_drop]
income_districts[income_districts.index('rhondda cynon taf')] = 'rhondda cynon taff'


for j in range(len(data_years)):
    data_districts = data_years[j][data_years[j].keys()[12]].unique()[:-1]
    # data_districts = [re.sub('city of ', '', data_districts[i].lower().strip()) for i in range(len(data_districts))]
    data_districts = [data_districts[i].lower().strip() for i in range(len(data_districts))]
    data_districts = [re.sub('county ', '', data_districts[i]) for i in range(len(data_districts))]
    data_districts = [re.sub('the ', '', data_districts[i]) for i in range(len(data_districts))]
    for i in range(len(data_districts)):
        if data_districts[i] in district_changes:
            data_districts[i] = district_changes[data_districts[i]]


    only_in_data = []
    only_in_income = []
    for i in data_districts:
        if i not in income_districts:
            only_in_data.append(i)
    for i in income_districts:
        if i not in data_districts:
            only_in_income.append(i)
    print(2018 - j)
    print(only_in_data)
    # print(len(only_in_data))
    # print(only_in_income)
    # print(len(only_in_income))

# for_now = ['wrekin', 'the vale of glamorgan', 'rhondda cynon taff', 'bristol', 'bournemouth, christchurch and poole',
#            'east suffolk', 'west suffolk', 'somerset west and taunton', 'folkestone and hythe']
# and_now = ['wrekin', 'the vale of glamorgan', 'rhondda cynon taff', 'bristol', 'london', 'bournemouth, christchurch and poole',
#            'east suffolk', 'west suffolk', 'somerset west and taunton', 'folkestone and hythe']


# for i in sorted(data_districts):
#     print(i)
# print(len(data_districts))
