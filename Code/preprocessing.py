import pandas as pd
import numpy as np
import os
import re


DATA_PATH = 'C:\\Users\\Meir\\PycharmProjects\\Final_DS_Project\\Data'
PRICE_DATA_PATH = DATA_PATH + '\\Price_Paid'
ORIGINAL_PRICE_DATA_PATH = DATA_PATH + '\\Price_Paid\\Original_Parts'
INCOME_DATA_PATH = DATA_PATH + '\\Income_By_District'

price_paid_headers = ['tid', 'price', 'date', 'postcode', 'property_type', 'old_new', 'duration', 'paon', 'saon',
                      'street', 'locality', 'city', 'district', 'county', 'ppd_type', 'status']


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


def combine_parts(file_1, file_2):
    df_1 = pd.read_csv(os.path.join(ORIGINAL_PRICE_DATA_PATH, file_1), index_col='Unnamed: 0')
    df_2 = pd.read_csv(os.path.join(ORIGINAL_PRICE_DATA_PATH, file_2), index_col='Unnamed: 0')
    new_df = pd.concat([df_1, df_2], ignore_index=True)
    new_df.index.rename('id', inplace=True)
    new_df.to_csv(os.path.join(PRICE_DATA_PATH, file_1[:-10] + '.csv'))


def add_headers(file_name, path, headers):
    df = pd.read_csv(os.path.join(path, file_name), header=None)
    df.columns = headers
    df.to_csv(os.path.join(path, file_name))


def fix_index_col(file_name):
    df = pd.read_csv(os.path.join(PRICE_DATA_PATH, file_name), index_col='Unnamed: 0')
    df.index.rename('id', inplace=True)
    df.to_csv(os.path.join(PRICE_DATA_PATH, file_name))


# add_headers('pp-2018.csv', PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2017.csv', PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2016.csv', PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2015.csv', PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2014.csv', PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2013.csv', PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2012-part1.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2012-part2.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2011-part1.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2010-part1.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2010-part2.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2009-part1.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2009-part2.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2008-part1.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2008-part2.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2007-part1.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2006-part1.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2006-part2.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2005-part1.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2005-part2.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2004-part1.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2004-part2.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2003-part1.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2003-part2.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2002-part1.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2002-part2.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2001-part1.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2001-part2.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2000-part1.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-2000-part2.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-1999-part1.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
# add_headers('pp-1999-part2.csv', ORIGINAL_PRICE_DATA_PATH, price_paid_headers)


# combine_parts('pp-2012-part1.csv', 'pp-2012-part2.csv')
# combine_parts('pp-2011-part1.csv', 'pp-2011-part2.csv')
# combine_parts('pp-2010-part1.csv', 'pp-2010-part2.csv')
# combine_parts('pp-2009-part1.csv', 'pp-2009-part2.csv')
# combine_parts('pp-2008-part1.csv', 'pp-2008-part2.csv')
# combine_parts('pp-2007-part1.csv', 'pp-2007-part2.csv')
# combine_parts('pp-2006-part1.csv', 'pp-2006-part2.csv')
# combine_parts('pp-2005-part1.csv', 'pp-2005-part2.csv')
# combine_parts('pp-2004-part1.csv', 'pp-2004-part2.csv')
# combine_parts('pp-2003-part1.csv', 'pp-2003-part2.csv')
# combine_parts('pp-2002-part1.csv', 'pp-2002-part2.csv')
# combine_parts('pp-2001-part1.csv', 'pp-2001-part2.csv')
# combine_parts('pp-2000-part1.csv', 'pp-2000-part2.csv')
# combine_parts('pp-1999-part1.csv', 'pp-1999-part2.csv')


# fix_index_col('pp-2018.csv')
# fix_index_col('pp-2017.csv')
# fix_index_col('pp-2016.csv')
# fix_index_col('pp-2015.csv')
# fix_index_col('pp-2014.csv')
# fix_index_col('pp-2013.csv')
