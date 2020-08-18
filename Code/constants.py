import pandas as pd
import numpy as np
import os
import re
from datetime import date
import pickle
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


DATA_PATH = 'C:\\Users\\Meir\\PycharmProjects\\Final_DS_Project\\Data'
ALT_DATA_PATH = 'E:\\College\\Year_4\\Semester_2\\Final_Project\\Data_Files'

PRICE_DATA_PATH = DATA_PATH + '\\Price_Paid'
PRICE_DATA_PATH_A = ALT_DATA_PATH + '\\Regular'

ORIGINAL_PRICE_DATA_PATH = PRICE_DATA_PATH + '\\Original_Parts'
ORIGINAL_PRICE_DATA_PATH_A = ALT_DATA_PATH + '\\Original'

PREPROCESSED_PRICE_DATA_PATH = PRICE_DATA_PATH + '\\Preprocessed'
PREPROCESSED_PRICE_DATA_PATH_A = ALT_DATA_PATH + '\\Preprocessed'

INCOME_DATA_PATH = DATA_PATH + '\\Income_By_District'
MEAN_INCOME_DATA_PATH = INCOME_DATA_PATH + '\\Mean'
MEDIAN_INCOME_DATA_PATH = INCOME_DATA_PATH + '\\Median'
PROSPERITY_DATA_PATH = DATA_PATH + '\\Prosperity'

MODEL_BIN_DATA_PATH = PRICE_DATA_PATH + '\\Model_Prop_Bin_Preprocessed'
MODEL_BIN_DATA_PATH_A = ALT_DATA_PATH + '\\Model_Prop_Bin_Preprocessed'
MODEL_DIS_DATA_PATH = PRICE_DATA_PATH + '\\Model_Prop_Dis_Preprocessed'
MODEL_DIS_DATA_PATH_A = ALT_DATA_PATH + '\\Model_Prop_Dis_Preprocessed'

MODEL_BIN_TRAIN_A = ALT_DATA_PATH + '\\Model_Prop_Bin_Train'
MODEL_BIN_TEST_A = ALT_DATA_PATH + '\\Model_Prop_Bin_Test'
MODEL_DIS_TRAIN_A = ALT_DATA_PATH + '\\Model_Prop_Dis_Train'
MODEL_DIS_TEST_A = ALT_DATA_PATH + '\\Model_Prop_Dis_Test'

MODEL_BIN_COMB_A = ALT_DATA_PATH + '\\Model_Prop_Bin_Combined'
MODEL_DIS_COMB_A = ALT_DATA_PATH + '\\Model_Prop_Dis_Combined'


district_changes = {'shepway': 'folkestone and hythe', 'bournemouth': 'bournemouth, christchurch and poole',
                    'christchurch': 'bournemouth, christchurch and poole', 'castle morpeth': 'northumberland',
                    'east dorset': 'dorset', 'forest heath': 'west suffolk', 'weymouth and portland': 'dorset',
                    'poole': 'bournemouth, christchurch and poole', 'purbeck': 'dorset', 'north dorset': 'dorset',
                    'st edmundsbury': 'west suffolk', 'suffolk coastal': 'east suffolk', 'bridgnorth': 'shropshire',
                    'taunton deane': 'somerset west and taunton', 'waveney': 'east suffolk', 'west dorset': 'dorset',
                    'west somerset': 'somerset west and taunton', 'south bedfordshire': 'central bedfordshire',
                    'alnwick': 'northumberland', 'berwick-upon-tweed': 'northumberland', 'west wiltshire': 'wiltshire',
                    'blyth valley': 'northumberland', 'caradon': 'cornwall', 'chester': 'cheshire west and chester',
                    'chester-le-street': 'county durham', 'congleton': 'cheshire east', 'derwentside': 'county durham',
                    'crewe and nantwich': 'cheshire east', 'durham': 'county durham', 'easington': 'county durham',
                    'ellesmere port and neston': 'cheshire west and chester', 'north shropshire': 'shropshire',
                    "st mary's": 'isles of scilly', 'kerrier': 'cornwall', 'mid bedfordshire': 'central bedfordshire',
                    'macclesfield': 'cheshire east', 'north cornwall': 'cornwall', 'north wiltshire': 'wiltshire',
                    'oswestry': 'shropshire', 'penwith': 'cornwall', 'restormel': 'cornwall', 'salisbury': 'wiltshire',
                    'shrewsbury and atcham': 'shropshire', 'teesdale': 'county durham', 'tynedale': 'northumberland',
                    'vale royal': 'cheshire west and chester', 'wear valley': 'county durham', 'kennet': 'wiltshire',
                    'south shropshire': 'shropshire', 'sedgefield': 'county durham', 'wansbeck': 'northumberland',
                    'kingston upon hull': 'city of kingston upon hull', 'peterborough': 'city of peterborough',
                    'derby': 'city of derby', 'westminster': 'city of westminster', 'nottingham': 'city of nottingham',
                    'bristol, city of': 'city of bristol', 'bristol': 'city of bristol', 'plymouth': 'city of plymouth',
                    'wrekin': 'telford and wrekin', 'north bedfordshire': 'bedford', 'newcastle': 'newcastle upon tyne',
                    'east yorkshire': 'east riding of yorkshire', 'aberystwyth': 'ceredigion', 'brecon': 'powys',
                    'bangor and holyhead': 'gwynedd', 'cardigan': 'ceredigion', 'tywyn and dolgellau': 'gwynedd',
                    'haverfordwest and milford haven': 'pembrokeshire', 'llandrindod wells and builth wells': 'powys',
                    'llanelli': 'carmarthenshire', 'newtown and welshpool': 'powys', 'rhyl': 'denbighshire',
                    'pwllheli and porthmadog': 'gwynedd', 'pembroke and tenby': 'pembrokeshire', 'colwyn bay': 'conwy',
                    'south bucks': 'buckinghamshire', 'aylesbury vale': 'buckinghamshire', 'wycombe': 'buckinghamshire',
                    'east': 'east of england', 'kingston upon hull, city of': 'city of kingston upon hull',
                    'vale of glamorgan': 'the vale of glamorgan', 'rhondda cynon taf': 'rhondda cynon taff',
                    "st martin's": 'isles of scilly', 'kings lynn and west norfolk': "king's lynn and west norfolk",
                    'herefordshire, county of': 'herefordshire', 'carrick': 'cornwall', 'chiltern': 'buckinghamshire'}

dist_reg_map = {'adur': 'south east', 'allerdale': 'north west', 'amber valley': 'east midlands', 'arun': 'south east',
                'ashfield': 'east midlands', 'babergh': 'east of england', 'barking and dagenham': 'london',
                'barnet': 'london', 'barnsley': 'yorkshire and the humber', 'basildon': 'east of england',
                'basingstoke and deane': 'south east', 'bassetlaw': 'east midlands',
                'bath and north east somerset': 'south west', 'bexley': 'london', 'blaby': 'east midlands',
                'blackburn with darwen': 'north west', 'blackpool': 'north west', 'blaenau gwent': 'wales',
                'bolsover': 'east midlands', 'bolton': 'north west', 'boston': 'east midlands',
                'bracknell forest': 'south east', 'braintree': 'east of england', 'breckland': 'east of england',
                'brent': 'london', 'brentwood': 'east of england', 'brighton and hove': 'south east',
                'broadland': 'east of england', 'bromley': 'london', 'bromsgrove': 'west midlands',
                'broxbourne': 'east of england', 'broxtowe': 'east midlands', 'buckinghamshire': 'south east',
                'burnley': 'north west', 'bury': 'north west', 'caerphilly': 'wales',
                'calderdale': 'yorkshire and the humber', 'camden': 'london', 'cannock chase': 'west midlands',
                'castle point': 'east of england', 'central bedfordshire': 'east of england', 'ceredigion': 'wales',
                'charnwood': 'east midlands', 'cherwell': 'south east', 'cheshire east': 'north west',
                'chesterfield': 'east midlands', 'chichester': 'south east', 'chorley': 'north west',
                'city of kingston upon hull': 'yorkshire and the humber', 'city of london': 'london',
                'city of westminster': 'london', 'colchester': 'east of england', 'conwy': 'wales',
                'copeland': 'north west', 'corby': 'east midlands', 'cornwall': 'south west', 'cotswold': 'south west',
                'county durham': 'north east', 'craven': 'yorkshire and the humber', 'croydon': 'london',
                'dacorum': 'east of england', 'darlington': 'north east', 'dartford': 'south east',
                'daventry': 'east midlands', 'denbighshire': 'wales', 'derbyshire dales': 'east midlands',
                'dorset': 'south west', 'dover': 'south east', 'ealing': 'london',
                'east cambridgeshire': 'east of england', 'east devon': 'south west', 'east hampshire': 'south east',
                'east hertfordshire': 'east of england', 'east lindsey': 'east midlands',
                'east northamptonshire': 'east midlands', 'east riding of yorkshire': 'yorkshire and the humber',
                'east staffordshire': 'west midlands', 'east suffolk': 'east of england', 'eastleigh': 'south east',
                'eden': 'north west', 'elmbridge': 'south east', 'enfield': 'london',
                'epping forest': 'east of england', 'epsom and ewell': 'south east', 'erewash': 'east midlands',
                'fareham': 'south east', 'fenland': 'east of england', 'flintshire': 'wales',
                'folkestone and hythe': 'south east', 'forest of dean': 'south west', 'fylde': 'north west',
                'gateshead': 'north east', 'gedling': 'east midlands', 'gloucester': 'south west',
                'gosport': 'south east', 'gravesham': 'south east', 'great yarmouth': 'east of england',
                'greenwich': 'london', 'guildford': 'south east', 'hackney': 'london',
                'halton': 'north west', 'hambleton': 'yorkshire and the humber', 'hammersmith and fulham': 'london',
                'harborough': 'east midlands', 'haringey': 'london', 'harlow': 'east of england', 'harrow': 'london',
                'hart': 'south east', 'hastings': 'south east', 'havant': 'south east', 'havering': 'london',
                'herefordshire': 'west midlands', 'hertsmere': 'east of england', 'high peak': 'east midlands',
                'hillingdon': 'london', 'hinckley and bosworth': 'east midlands', 'horsham': 'south east',
                'hounslow': 'london', 'huntingdonshire': 'east of england', 'hyndburn': 'north west',
                'isle of anglesey': 'wales', 'isles of scilly': 'south west', 'islington': 'london',
                'kensington and chelsea': 'london', 'kettering': 'east midlands',
                "king's lynn and west norfolk": 'east of england', 'kingston upon thames': 'london',
                'kirklees': 'yorkshire and the humber', 'knowsley': 'north west', 'lambeth': 'london',
                'lancaster': 'north west', 'lewes': 'south east', 'lewisham': 'london', 'lichfield': 'west midlands',
                'maidstone': 'south east', 'maldon': 'east of england', 'malvern hills': 'west midlands',
                'medway': 'south east', 'melton': 'east midlands', 'mendip': 'south west', 'merthyr tydfil': 'wales',
                'merton': 'london', 'mid devon': 'south west', 'mid suffolk': 'east of england',
                'mid sussex': 'south east', 'middlesbrough': 'yorkshire and the humber', 'mole valley': 'south east',
                'monmouthshire': 'wales', 'neath port talbot': 'wales', 'new forest': 'south east',
                'newark and sherwood': 'east midlands', 'newcastle-under-lyme': 'west midlands', 'newham': 'london',
                'north devon': 'south west', 'north east derbyshire': 'east midlands',
                'north east lincolnshire': 'yorkshire and the humber', 'north hertfordshire': 'east of england',
                'north kesteven': 'east midlands', 'north lincolnshire': 'yorkshire and the humber',
                'north norfolk': 'east of england', 'north somerset': 'south west', 'north tyneside': 'north east',
                'north warwickshire': 'west midlands', 'north west leicestershire': 'east midlands',
                'northumberland': 'north east', 'nuneaton and bedworth': 'west midlands',
                'oadby and wigston': 'east midlands', 'oldham': 'north west', 'pembrokeshire': 'wales',
                'pendle': 'north west', 'reading': 'south east', 'redbridge': 'london',
                'redcar and cleveland': 'yorkshire and the humber', 'redditch': 'west midlands',
                'reigate and banstead': 'south east', 'rhondda cynon taff': 'wales', 'ribble valley': 'north west',
                'richmond upon thames': 'london', 'richmondshire': 'yorkshire and the humber', 'rochdale': 'north west',
                'rochford': 'east of england', 'rossendale': 'north west', 'rother': 'south east',
                'rotherham': 'yorkshire and the humber', 'rugby': 'west midlands', 'runnymede': 'south east',
                'rushcliffe': 'east midlands', 'rushmoor': 'south east', 'rutland': 'east midlands',
                'ryedale': 'yorkshire and the humber', "st martin's": 'south west', "st mary's": 'south west',
                'salford': 'north west', 'sandwell': 'west midlands', 'scarborough': 'yorkshire and the humber',
                'sedgemoor': 'south west', 'sefton': 'north west', 'selby': 'yorkshire and the humber',
                'sevenoaks': 'south east', 'slough': 'south east', 'solihull': 'west midlands',
                'somerset west and taunton': 'south west', 'south cambridgeshire': 'east of england',
                'south derbyshire': 'east midlands', 'south gloucestershire': 'south west', 'south hams': 'south west',
                'south holland': 'east midlands', 'south kesteven': 'east midlands', 'south lakeland': 'north west',
                'south norfolk': 'east of england', 'south northamptonshire': 'east midlands',
                'south oxfordshire': 'south east', 'south ribble': 'north west', 'south somerset': 'south west',
                'south staffordshire': 'west midlands', 'south tyneside': 'north east', 'southampton': 'south east',
                'southend-on-sea': 'east of england', 'southwark': 'london', 'spelthorne': 'south east',
                'st albans': 'east of england', 'st helens': 'north west', 'staffordshire moorlands': 'west midlands',
                'stevenage': 'east of england', 'stockport': 'north west', 'stockton-on-tees': 'north east',
                'stratford-on-avon': 'west midlands', 'stroud': 'south west', 'surrey heath': 'south east',
                'sutton': 'london', 'swale': 'south east', 'tameside': 'north west', 'tamworth': 'west midlands',
                'tandridge': 'south east', 'teignbridge': 'south west', 'telford and wrekin': 'west midlands',
                'tendring': 'east of england', 'test valley': 'south east', 'tewkesbury': 'south west',
                'thanet': 'south east', 'the vale of glamorgan': 'wales', 'three rivers': 'east of england',
                'thurrock': 'east of england', 'tonbridge and malling': 'south east', 'torbay': 'south west',
                'torfaen': 'wales', 'torridge': 'south west', 'tower hamlets': 'london', 'trafford': 'north west',
                'tunbridge wells': 'south east', 'uttlesford': 'east of england', 'vale of white horse': 'south east',
                'wakefield': 'yorkshire and the humber', 'waltham forest': 'london', 'wandsworth': 'london',
                'warrington': 'north west', 'warwick': 'west midlands', 'watford': 'east of england',
                'waverley': 'south east', 'wealden': 'south east', 'wellingborough': 'east midlands',
                'welwyn hatfield': 'east of england', 'west berkshire': 'south east', 'west devon': 'south west',
                'west lancashire': 'north west', 'west lindsey': 'east midlands', 'west oxfordshire': 'south east',
                'west suffolk': 'east of england', 'wigan': 'north west', 'winchester': 'south east',
                'windsor and maidenhead': 'south east', 'wirral': 'north west', 'woking': 'south east',
                'wokingham': 'south east', 'worcester': 'west midlands', 'worthing': 'south east',
                'wychavon': 'west midlands', 'wyre': 'north west', 'wyre forest': 'west midlands'}

reg_dist_map = {}

county_changes = {'cleveland': 'north yorkshire', 'durham': 'county durham', 'south gloucestershire': 'gloucestershire',
                  'north somerset': 'somerset', 'bath and north east somerset': 'somerset', 'avon': 'city of bristol',
                  'cheshire east': 'cheshire', 'cheshire west and chester': 'cheshire', 'bedford': 'bedfordshire',
                  'rhondda cynon taff': 'rhondda cynon taf', 'city of derby': 'derbyshire', 'wokingham': 'berkshire',
                  'city of nottingham': 'nottinghamshire', 'southampton': 'hampshire', 'city of plymouth': 'devon',
                  'city of kingston upon hull': 'east riding of yorkshire', 'slough': 'berkshire', 'poole': 'dorset',
                  'hartlepool': 'county durham', 'portsmouth': 'hampshire', 'north lincolnshire': 'lincolnshire',
                  'southend-on-sea': 'essex', 'the vale of glamorgan': 'vale of glamorgan', 'halton': 'cheshire',
                  'warrington': 'cheshire', 'stockton-on-tees': 'county durham', 'brighton and hove': 'east sussex',
                  'darlington': 'county durham', 'bracknell forest': 'berkshire', 'milton keynes': 'buckinghamshire',
                  'wrekin': 'shropshire', 'windsor and maidenhead': 'berkshire', 'stoke-on-trent': 'staffordshire',
                  'west berkshire': 'berkshire', 'medway': 'kent', 'luton': 'bedfordshire', 'blackpool': 'lancashire',
                  'reading': 'berkshire', 'leicester': 'leicestershire', 'middlesbrough': 'north yorkshire',
                  'torbay': 'devon', 'central bedfordshire': 'bedfordshire', 'north east lincolnshire': 'lincolnshire',
                  'swindon': 'wiltshire', 'bournemouth, christchurch and poole': 'dorset', 'york': 'north yorkshire',
                  'isles of scilly': 'cornwall', 'bournemouth': 'dorset', 'city of peterborough': 'cambridgeshire',
                  'thurrock': 'essex', 'blackburn with darwen': 'lancashire', 'redcar and cleveland': 'north yorkshire'}

regions_of_england = ['north east', 'north west', 'yorkshire and the humber', 'west midlands', 'east midlands',
                      'east of england', 'london', 'south east', 'south west']

regions = regions_of_england
regions.append('wales')
