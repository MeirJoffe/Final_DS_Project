from Code.constants import *

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
df = pd.read_csv(os.path.join(MEDIAN_INCOME_DATA_PATH, file_name))

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


# total = 0
# dds = []
# for j in range(len(data_years[:1])):
#     print(len(data_years[j]))
#     total += len(data_years[j])
#     data_districts = data_years[j][data_years[j].keys()[12]].unique()[:-1]
#     # data_districts = [re.sub('city of ', '', data_districts[i].lower().strip()) for i in range(len(data_districts))]
#     data_districts = [data_districts[i].lower().strip() for i in range(len(data_districts))]
#     data_districts = [re.sub('county ', '', data_districts[i]) for i in range(len(data_districts))]
#     data_districts = [re.sub('the ', '', data_districts[i]) for i in range(len(data_districts))]
#     dds = data_districts
#     for i in range(len(data_districts)):
#         if data_districts[i] in district_changes:
#             data_districts[i] = district_changes[data_districts[i]]
#
#
#     only_in_data = []
#     only_in_income = []
#     for i in data_districts:
#         if i not in income_districts:
#             only_in_data.append(i)
#     for i in income_districts:
#         if i not in data_districts:
#             only_in_income.append(i)
#     print(2018 - j)
#     print(only_in_data)
#     # print(len(only_in_data))
#     # print(only_in_income)
#     # print(len(only_in_income))
#
# # for_now = ['wrekin', 'the vale of glamorgan', 'rhondda cynon taff', 'bristol', 'bournemouth, christchurch and poole',
# #            'east suffolk', 'west suffolk', 'somerset west and taunton', 'folkestone and hythe']
# # and_now = ['wrekin', 'the vale of glamorgan', 'rhondda cynon taff', 'bristol', 'london', 'bournemouth, christchurch and poole',
# #            'east suffolk', 'west suffolk', 'somerset west and taunton', 'folkestone and hythe']
#
#
# # for i in sorted(data_districts):
# #     print(i)
# # print(len(data_districts))
#
# # print(total)
#
#
# districts_england = ["Adur	website	63,869	District		West Sussex",
# "Allerdale	website	97,527	Borough		Cumbria",
# "Amber Valley	website	126,678	Borough		Derbyshire",
# "Arun	website	159,827	District		West Sussex",
# "Ashfield	website	127,151	District		Nottinghamshire",
# "Ashford	website	129,281	Borough		Kent",
# "Babergh	website	91,401	District		Suffolk",
# "Barking and Dagenham	website	211,998	London Borough	London borough	Greater London",
# "Barnet	website	392,140	London Borough	London borough	Greater London",
# "Barnsley	website	245,199	Metropolitan Borough	Metropolitan borough	South Yorkshire",
# "Barrow-in-Furness	website	67,137	Borough		Cumbria",
# "Basildon	website	185,862	Borough		Essex",
# "Basingstoke and Deane	website	175,729	Borough		Hampshire",
# "Bassetlaw	website	116,839	District		Nottinghamshire",
# "Bath and North East Somerset	website	192,106		Unitary authority	Somerset",
# "Bedford	website	171,623	Borough	Unitary authority	Bedfordshire",
# "Bexley	website	247,258	London Borough	London borough	Greater London",
# "Birmingham	website	1,141,374	City (1889)	Metropolitan borough	West Midlands",
# "Blaby	website	100,421	District		Leicestershire",
# "Blackburn with Darwen	website	148,942	Borough	Unitary authority	Lancashire",
# "Blackpool	website	139,305	Borough	Unitary authority	Lancashire",
# "Bolsover	website	79,530	District		Derbyshire",
# "Bolton	website	285,372	Metropolitan Borough	Metropolitan borough	Greater Manchester",
# "Boston	website	69,366	Borough		Lincolnshire",
# "Bournemouth, Christchurch and Poole	website	395,784	Borough	Unitary authority	Dorset",
# "Bracknell Forest	website	121,676	Borough	Unitary authority	Berkshire",
# "Bradford	website	537,173	City (1897)	Metropolitan borough	West Yorkshire",
# "Braintree	website	151,561	District		Essex",
# "Breckland	website	139,329	District		Norfolk",
# "Brent	website	330,795	London Borough	London borough	Greater London",
# "Brentwood	website	76,550	Borough		Essex",
# "Brighton and Hove	website	290,395	City (2000)	Unitary authority	East Sussex",
# "Bristol	website	463,405	City (1542)	Unitary authority	Bristol",
# "Broadland	website	129,464	District		Norfolk",
# "Bromley	website	331,096	London Borough	London borough	Greater London",
# "Bromsgrove	website	96,876	District		Worcestershire",
# "Broxbourne	website	96,800	Borough		Hertfordshire",
# "Broxtowe	website	113,272	Borough		Nottinghamshire",
# "Buckinghamshire	website			Unitary authority	Buckinghamshire",
# "Burnley	website	88,527	Borough		Lancashire",
# "Bury	website	190,108	Metropolitan Borough	Metropolitan borough	Greater Manchester",
# "Calderdale	website	210,082	Metropolitan Borough	Metropolitan borough	West Yorkshire",
# "Cambridge	website	125,758	City (1951)		Cambridgeshire",
# "Camden	website	262,226	London Borough	London borough	Greater London",
# "Cannock Chase	website	100,109	District		Staffordshire",
# "Canterbury	website	164,553	City (TI)		Kent",
# "Carlisle	website	108,387	City (TI)		Cumbria",
# "Castle Point	website	90,070	Borough		Essex",
# "Central Bedfordshire	website	283,606		Unitary authority	Bedfordshire",
# "Charnwood	website	182,643	Borough		Leicestershire",
# "Chelmsford	website	177,079	City (2012)		Essex",
# "Cheltenham	website	117,090	Borough		Gloucestershire",
# "Cherwell	website	149,161	District		Oxfordshire",
# "Cheshire East	website	380,790		Unitary authority	Cheshire",
# "Cheshire West and Chester	website	340,502		Unitary authority	Cheshire",
# "Chesterfield	website	104,628	Borough		Derbyshire",
# "Chichester	website	120,750	District		West Sussex",
# "Chorley	website	116,821	Borough		Lancashire",
# "Colchester	website	192,523	Borough		Essex",
# "Copeland	website	68,424	Borough		Cumbria",
# "Corby	website	70,827	Borough		Northamptonshire",
# "Cornwall	website	565,968		Unitary authority	Cornwall",
# "Cotswold	website	89,022	District		Gloucestershire",
# "Coventry	website	366,785	City (1345)	Metropolitan borough	West Midlands",
# "Craven	website	56,832	District		North Yorkshire",
# "Crawley	website	112,448	Borough		West Sussex",
# "Croydon	website	385,346	London Borough	London borough	Greater London",
# "Dacorum	website	154,280	Borough		Hertfordshire",
# "Darlington	website	106,566	Borough	Unitary authority	County Durham",
# "Dartford	website	109,709	Borough		Kent",
# "Daventry	website	84,484	District		Northamptonshire",
# "Derby	website	257,174	City (1977)	Unitary authority	Derbyshire",
# "Derbyshire Dales	website	71,977	District		Derbyshire",
# "Doncaster	website	310,542	Metropolitan Borough	Metropolitan borough	South Yorkshire",
# "Dorset	website	376,484		Unitary authority	Dorset",
# "Dover	website	116,969	District		Kent",
# "Dudley	website	320,626	Metropolitan Borough	Metropolitan borough	West Midlands",
# "County Durham	website	526,980		Unitary authority	County Durham",
# "Ealing	website	341,982	London Borough	London borough	Greater London",
# "East Cambridgeshire	website	89,362	District		Cambridgeshire",
# "East Devon	website	144,317	District		Devon",
# "East Hampshire	website	120,681	District		Hampshire",
# "East Hertfordshire	website	148,105	District		Hertfordshire",
# "East Lindsey	website	140,741	District		Lincolnshire",
# "East Northamptonshire	website	93,906	District		Northamptonshire",
# "East Riding of Yorkshire	website	339,614		Unitary authority	East Riding of Yorkshire",
# "East Staffordshire	website	118,574	Borough		Staffordshire",
# "East Suffolk	website	248,249	District		Suffolk",
# "Eastbourne	website	103,160	Borough		East Sussex",
# "Eastleigh	website	131,819	Borough		Hampshire",
# "Eden	website	52,881	District		Cumbria",
# "Elmbridge	website	136,626	Borough		Surrey",
# "Enfield	website	333,869	London Borough	London borough	Greater London",
# "Epping Forest	website	131,137	District		Essex",
# "Epsom and Ewell	website	79,928	Borough		Surrey",
# "Erewash	website	115,490	Borough		Derbyshire",
# "Exeter	website	130,428	City (TI)		Devon",
# "Fareham	website	116,339	Borough		Hampshire",
# "Fenland	website	101,491	District		Cambridgeshire",
# "Folkestone and Hythe	website	112,578	District		Kent",
# "Forest of Dean	website	86,543	District		Gloucestershire",
# "Fylde	website	79,770	Borough		Lancashire",
# "Gateshead	website	202,508	Metropolitan Borough	Metropolitan borough	Tyne and Wear",
# "Gedling	website	117,786	Borough		Nottinghamshire",
# "Gloucester	website	129,285	City (1541)		Gloucestershire",
# "Gosport	website	85,283	Borough		Hampshire",
# "Gravesham	website	106,385	Borough		Kent",
# "Great Yarmouth	website	99,370	Borough		Norfolk",
# "Greenwich	website	286,186	Royal Borough	London Borough	Greater London",
# "Guildford	website	147,889	Borough		Surrey",
# "Hackney	website	279,665	London Borough	London borough	Greater London",
# "Halton	website	128,432	Borough	Unitary authority	Cheshire",
# "Hambleton	website	91,134	District		North Yorkshire",
# "Hammersmith and Fulham	website	185,426	London Borough	London borough	Greater London",
# "Harborough	website	92,499	District		Leicestershire",
# "Haringey	website	270,624	London Borough	London borough	Greater London",
# "Harlow	website	86,594	District		Essex",
# "Harrogate	website	160,533	District		North Yorkshire",
# "Harrow	website	250,149	London Borough	London borough	Greater London",
# "Hart	website	96,293	District		Hampshire",
# "Hartlepool	website	93,242	Borough	Unitary authority	County Durham",
# "Hastings	website	92,855	Borough		East Sussex",
# "Havant	website	125,813	Borough		Hampshire",
# "Havering	website	257,810	London Borough	London borough	Greater London",
# "Herefordshire	website	192,107		Unitary authority	Herefordshire",
# "Hertsmere	website	104,205	Borough		Hertfordshire",
# "High Peak	website	92,221	Borough		Derbyshire",
# "Hillingdon	website	304,824	London Borough	London borough	Greater London",
# "Hinckley and Bosworth	website	112,423	Borough		Leicestershire",
# "Horsham	website	142,217	District		West Sussex",
# "Hounslow	website	270,782	London Borough	London borough	Greater London",
# "Kingston upon Hull	website	260,645	City (1299)	Unitary authority	East Riding of Yorkshire",
# "Huntingdonshire	website	177,352	District		Cambridgeshire",
# "Hyndburn	website	80,815	Borough		Lancashire",
# "Ipswich	website	137,532	Borough		Suffolk",
# "Isle of Wight	website	141,538		Unitary authority	Isle of Wight",
# "Isles of Scilly	website	2,242		Sui generis	Cornwall",
# "Islington	website	239,142	London Borough	London borough	Greater London",
# "Kensington and Chelsea	website	156,197	Royal borough	London Borough	Greater London",
# "Kettering	website	101,266	Borough		Northamptonshire",
# "King's Lynn and West Norfolk	website	151,811	Borough		Norfolk",
# "Kingston upon Thames	website	175,470	Royal Borough	London Borough	Greater London",
# "Kirklees	website	438,727	Metropolitan Borough	Metropolitan borough	West Yorkshire",
# "Knowsley	website	149,571	Metropolitan Borough	Metropolitan borough	Merseyside",
# "Lambeth	website	325,917	London Borough	London borough	Greater London",
# "Lancaster	website	144,246	City (1937)		Lancashire",
# "Leeds	website	789,194	City (1895)	Metropolitan borough	West Yorkshire",
# "Leicester	website	355,218	City (1919)	Unitary authority	Leicestershire",
# "Lewes	website	102,744	District		East Sussex",
# "Lewisham	website	303,536	London Borough	London borough	Greater London",
# "Lichfield	website	103,965	District		Staffordshire",
# "Lincoln	website	99,039	City (TI)		Lincolnshire",
# "Liverpool	website	494,814	City (1880)	Metropolitan borough	Merseyside",
# "City of London	website	8,706	City (TI)	Sui generis	City of London",
# "Luton	website	214,109	Borough	Unitary authority	Bedfordshire",
# "Maidstone	website	169,955	Borough		Kent",
# "Maldon	website	64,425	District		Essex",
# "Malvern Hills	website	78,113	District		Worcestershire",
# "Manchester	website	547,627	City (1853)	Metropolitan borough	Greater Manchester",
# "Mansfield	website	108,841	District		Nottinghamshire",
# "Medway	website	277,855	Borough	Unitary authority	Kent",
# "Melton	website	51,100	Borough		Leicestershire",
# "Mendip	website	114,881	District		Somerset",
# "Merton	website	206,186	London Borough	London borough	Greater London",
# "Mid Devon	website	81,695	District		Devon",
# "Mid Suffolk	website	102,493	District		Suffolk",
# "Mid Sussex	website	149,716	District		West Sussex",
# "Middlesbrough	website	140,545	Borough	Unitary authority	North Yorkshire",
# "Milton Keynes	website	268,607	Borough	Unitary authority	Buckinghamshire",
# "Mole Valley	website	87,253	District		Surrey",
# "Newark and Sherwood	website	121,566	District		Nottinghamshire",
# "Newcastle-under-Lyme	website	129,490	Borough		Staffordshire",
# "Newcastle upon Tyne	website	300,196	City (1882)	Metropolitan borough	Tyne and Wear",
# "New Forest	website	179,753	District		Hampshire",
# "Newham	website	352,005	London Borough	London borough	Greater London",
# "North Devon	website	96,110	District		Devon",
# "North East Derbyshire	website	101,125	District		Derbyshire",
# "North East Lincolnshire	website	159,821	Borough	Unitary authority	Lincolnshire",
# "North Hertfordshire	website	133,214	District		Hertfordshire",
# "North Kesteven	website	115,985	District		Lincolnshire",
# "North Lincolnshire	website	172,005	Borough	Unitary authority	Lincolnshire",
# "North Norfolk	website	104,552	District		Norfolk",
# "North Somerset	website	213,919		Unitary authority	Somerset",
# "North Tyneside	website	205,985	Metropolitan Borough	Metropolitan borough	Tyne and Wear",
# "North Warwickshire	website	64,850	Borough		Warwickshire",
# "North West Leicestershire	website	102,126	District		Leicestershire",
# "Northampton	website	225,146	Borough		Northamptonshire",
# "Northumberland	website	320,274		Unitary authority	Northumberland",
# "Norwich	website	141,137	City (1195)		Norfolk",
# "Nottingham	website	331,069	City (1897)	Unitary authority	Nottinghamshire",
# "Nuneaton and Bedworth	website	128,902	Borough		Warwickshire",
# "Oadby and Wigston	website	57,056	Borough		Leicestershire",
# "Oldham	website	235,623	Metropolitan Borough	Metropolitan borough	Greater Manchester",
# "Oxford	website	154,327	City (1542)		Oxfordshire",
# "Pendle	website	91,405	Borough		Lancashire",
# "Peterborough	website	201,041	City (1541)	Unitary authority	Cambridgeshire",
# "Plymouth	website	263,100	City (1928)	Unitary authority	Devon",
# "Portsmouth	website	215,133	City (1926)	Unitary authority	Hampshire",
# "Preston	website	141,818	City (2002)		Lancashire",
# "Reading	website	163,203	Borough	Unitary authority	Berkshire",
# "Redbridge	website	303,858	London Borough	London borough	Greater London",
# "Redcar and Cleveland	website	136,718	Borough	Unitary authority	North Yorkshire",
# "Redditch	website	84,989	Borough		Worcestershire",
# "Reigate and Banstead	website	147,757	Borough		Surrey",
# "Ribble Valley	website	60,057	Borough		Lancashire",
# "Richmond upon Thames	website	196,904	London Borough	London borough	Greater London",
# "Richmondshire	website	53,244	District		North Yorkshire",
# "Rochdale	website	220,001	Metropolitan Borough	Metropolitan borough	Greater Manchester",
# "Rochford	website	86,981	District		Essex",
# "Rossendale	website	70,895	Borough		Lancashire",
# "Rother	website	95,656	District		East Sussex",
# "Rotherham	website	264,671	Metropolitan Borough	Metropolitan borough	South Yorkshire",
# "Rugby	website	107,194	Borough		Warwickshire",
# "Runnymede	website	88,000	Borough		Surrey",
# "Rushcliffe	website	117,671	Borough		Nottinghamshire",
# "Rushmoor	website	95,142	Borough		Hampshire",
# "Rutland	website	39,697		Unitary authority	Rutland",
# "Ryedale	website	54,920	District		North Yorkshire",
# "St Albans	website	147,373	City (1877)		Hertfordshire",
# "St Helens	website	180,049	Metropolitan Borough	Metropolitan borough	Merseyside",
# "Salford	website	254,408	City (1926)	Metropolitan borough	Greater Manchester",
# "Sandwell	website	327,378	Metropolitan Borough	Metropolitan borough	West Midlands",
# "Scarborough	website	108,736	Borough		North Yorkshire",
# "Sedgemoor	website	122,791	District		Somerset",
# "Sefton	website	275,396	Metropolitan Borough	Metropolitan borough	Merseyside",
# "Selby	website	89,106	District		North Yorkshire",
# "Sevenoaks	website	120,293	District		Kent",
# "Sheffield	website	582,506	City (1893)	Metropolitan borough	South Yorkshire",
# "Shropshire	website	320,274		Unitary authority	Shropshire",
# "Slough	website	149,112	Borough	Unitary authority	Berkshire",
# "Solihull	website	214,909	Metropolitan Borough	Metropolitan borough	West Midlands",
# "Somerset West and Taunton	website	153,866	District		Somerset",
# "South Cambridgeshire	website	157,519	District		Cambridgeshire",
# "South Derbyshire	website	104,493	District		Derbyshire",
# "South Gloucestershire	website	282,644		Unitary authority	Gloucestershire",
# "South Hams	website	86,221	District		Devon",
# "South Holland	website	93,980	District		Lincolnshire",
# "South Kesteven	website	141,853	District		Lincolnshire",
# "South Lakeland	website	104,532	District		Cumbria",
# "South Norfolk	website	138,017	District		Norfolk",
# "South Northamptonshire	website	92,515	District		Northamptonshire",
# "South Oxfordshire	website	140,504	District		Oxfordshire",
# "South Ribble	website	110,527	Borough		Lancashire",
# "South Somerset	website	167,861	District		Somerset",
# "South Staffordshire	website	112,126	District		Staffordshire",
# "South Tyneside	website	150,265	Metropolitan Borough	Metropolitan borough	Tyne and Wear",
# "Southampton	website	252,796	City (1964)	Unitary authority	Hampshire",
# "Southend-on-Sea	website	182,463	Borough	Unitary authority	Essex",
# "Southwark	website	317,256	London Borough	London borough	Greater London",
# "Spelthorne	website	99,334	Borough		Surrey",
# "Stafford	website	135,880	Borough		Staffordshire",
# "Staffordshire Moorlands	website	98,397	District		Staffordshire",
# "Stevenage	website	87,754	Borough		Hertfordshire",
# "Stockport	website	291,775	Metropolitan Borough	Metropolitan borough	Greater Manchester",
# "Stockton-on-Tees	website	197,213	Borough	Unitary authority	County Durham and North Yorkshire",
# "Stoke-on-Trent	website	255,833	City (1925)	Unitary authority	Staffordshire",
# "Stratford-on-Avon	website	127,580	District		Warwickshire",
# "Stroud	website	119,019	District		Gloucestershire",
# "Sunderland	website	277,417	City (1992)	Metropolitan borough	Tyne and Wear",
# "Surrey Heath	website	88,874	Borough		Surrey",
# "Sutton	website	204,525	London Borough	London borough	Greater London",
# "Swale	website	148,519	Borough		Kent",
# "Swindon	website	221,996	Borough	Unitary authority	Wiltshire",
# "Tameside	website	225,197	Metropolitan Borough	Metropolitan borough	Greater Manchester",
# "Tamworth	website	76,678	Borough		Staffordshire",
# "Tandridge	website	87,496	District		Surrey",
# "Teignbridge	website	132,844	District		Devon",
# "Telford and Wrekin	website	177,799	Borough	Unitary authority	Shropshire",
# "Tendring	website	145,803	District		Essex",
# "Test Valley	website	125,169	Borough		Hampshire",
# "Tewkesbury	website	92,599	Borough		Gloucestershire",
# "Thanet	website	141,819	District		Kent",
# "Three Rivers	website	93,045	District		Hertfordshire",
# "Thurrock	website	172,525	Borough	Unitary authority	Essex",
# "Tonbridge and Malling	website	130,508	Borough		Kent",
# "Torbay	website	135,780	Borough	Unitary authority	Devon",
# "Torridge	website	68,143	District		Devon",
# "Tower Hamlets	website	317,705	London Borough	London borough	Greater London",
# "Trafford	website	236,370	Metropolitan Borough	Metropolitan borough	Greater Manchester",
# "Tunbridge Wells	website	118,054	Borough		Kent",
# "Uttlesford	website	89,179	District		Essex",
# "Vale of White Horse	website	133,732	District		Oxfordshire",
# "Wakefield	website	345,038	City (1888)	Metropolitan borough	West Yorkshire",
# "Walsall	website	283,378	Metropolitan Borough	Metropolitan borough	West Midlands",
# "Waltham Forest	website	276,700	London Borough	London borough	Greater London",
# "Wandsworth	website	326,474	London Borough	London borough	Greater London",
# "Warrington	website	209,547	Borough	Unitary authority	Cheshire",
# "Warwick	website	142,484	District		Warwickshire",
# "Watford	website	96,767	Borough		Hertfordshire",
# "Waverley	website	125,610	Borough		Surrey",
# "Wealden	website	160,175	District		East Sussex",
# "Wellingborough	website	79,478	Borough		Northamptonshire",
# "Welwyn Hatfield	website	122,746	District		Hertfordshire",
# "West Berkshire	website	158,527		Unitary authority	Berkshire",
# "West Devon	website	55,528	Borough		Devon",
# "West Lancashire	website	113,949	District		Lancashire",
# "West Lindsey	website	94,869	District		Lincolnshire",
# "Westminster	website	255,324	City (1540)	London Borough	Greater London",
# "West Oxfordshire	website	109,800	District		Oxfordshire",
# "West Suffolk	website	178,881	District		Suffolk",
# "Wigan	website	326,088	Metropolitan Borough	Metropolitan borough	Greater Manchester",
# "Wiltshire	website	498,064		Unitary authority	Wiltshire",
# "Winchester	website	124,295	City (TI)		Hampshire",
# "Windsor and Maidenhead	website	150,906	Royal borough	Unitary authority	Berkshire",
# "Wirral	website	323,235	Metropolitan Borough	Metropolitan borough	Merseyside",
# "Woking	website	101,167	Borough		Surrey",
# "Wokingham	website	167,979	Borough	Unitary authority	Berkshire",
# "Wolverhampton	website	262,008	City (2000)	Metropolitan borough	West Midlands",
# "Worcester	website	101,891	City (1189)		Worcestershire",
# "Worthing	website	110,025	Borough		West Sussex",
# "Wychavon	website	127,340	District		Worcestershire",
# "Wyre	website	111,223	Borough		Lancashire",
# "Wyre Forest	website	101,062	District		Worcestershire",
# "York website	209,893	City (TI)	Unitary authority	North Yorkshire"]
#
# districts_wales = ["Aberconwy	Borough	Clwyd	149,738 acres (605.97 km2)	49,730	54,100	Llandudno	Conwy",
# "	Alyn and Deeside	District	Clwyd	38,104 acres (154.20 km2)	68,280	74,500	Hawarden	Flintshire",
# "	Anglesey - Ynys Môn	Borough	Gwynedd	176,638 acres (714.83 km2)	62,020	69,300	Llangefni	Isle of Anglesey",
# "	Arfon	Borough	Gwynedd	101,207 acres (409.57 km2)	53,640	56,100	Bangor	Gwynedd",
# "	Blaenau Gwent	Borough	Gwent	31,318 acres (126.74 km2)	84,080	76,900	Ebbw Vale	Blaenau Gwent, Monmouthshire",
# "	Brecknock	Borough	Powys	443,382 acres (1,794.30 km2)	37,120	41,500	Brecon	Powys",
# "	Cardiff	City	South Glamorgan	29,633 acres (119.92 km2)	285,760	295,600	Cardiff	Cardiff",
# "	Carmarthen	District	Dyfed	291,192 acres (1,178.41 km2)	49,910	56,200	Carmarthen	Carmarthenshire",
# "	Ceredigion	District	Dyfed	443,182 acres (1,793.49 km2)	55,430	67,900	Aberystwyth	Ceredigion",
# "	Colwyn	Borough	Clwyd	136,566 acres (552.66 km2)	45,990	56,400	Colwyn Bay	Conwy, Denbighshire",
# "	Cynon Valley	Borough	Mid Glamorgan	44,639 acres (180.65 km2)	69,630	65,600	Aberdare	Rhondda Cynon Taf",
# "	Delyn	Borough	Clwyd	6,870 acres (27.8 km2)	59,440	69,700	Flint	Flintshire",
# "	Dinefwr	Borough	Dyfed	239,868 acres (970.71 km2)	36,140	38,700	Llandeilo	Carmarthenshire",
# "	Dwyfor	District	Gwynedd	152,753 acres (618.17 km2)	25,870	27,300	Pwllheli	Gwynedd",
# "	Glyndŵr	District	Clwyd	238,686 acres (965.93 km2)	38,450	42,000	Ruthin	Denbighshire, Powys, Wrexham",
# "	Islwyn	Borough	Gwent	24,362 acres (98.59 km2)	66,140	67,200	Blackwood	Caerphilly",
# "	Llanelli	Borough	Dyfed	57,737 acres (233.65 km2)	76,720	74,600	Llanelli	Carmarthenshire",
# "	Lliw Valley	Borough	West Glamorgan	52,818 acres (213.75 km2)	57,460	64,200	Penllergaer	Neath Port Talbot, Swansea",
# "	Meirionnydd	District	Gwynedd	374,912 acres (1,517.22 km2)	30,830	32,900	Dolgellau	Gwynedd",
# "	Merthyr Tydfil	Borough	Mid Glamorgan	27,584 acres (111.63 km2)	61,490	60,100	Merthyr Tydfil	Merthyr Tydfil",
# "	Monmouth	District Borough from 1988	Gwent	203,438 acres (823.28 km2)	66,090	76,700	Pontypoola	Monmouthshire",
# "Montgomeryshire 1986	District	Powys	510,109 acres (2,064.34 km2)	43,580	53,700	Welshpool	Powys",
# "	Neath	Borough	West Glamorgan	50,971 acres (206.27 km2)	66,150	66,300	Neath	Neath Port Talbot",
# "	Newport	Borough	Gwent	49,558 acres (200.55 km2)	135,910	137,200	Newport	Newport",
# "	Ogwr	Borough	Mid Glamorgan	70,444 acres (285.08 km2)	126,570	134,200	Bridgend	Bridgend, Vale of Glamorgan",
# "	Port Talbot on 1 January 1986[4]	Borough	West Glamorgan	37,371 acres (151.24 km2)	58,580	51,100	Port Talbot	Neath Port Talbot",
# "	Preseli Pembrokeshire on 1 April 1987[5]	District	Dyfed	258,075 acres (1,044.39 km2)	61,700	71,200	Haverfordwest	Pembrokeshire",
# "Radnorshire on 8 May 1989[6]	District	Powys	301,165 acres (1,218.77 km2)	18,670	24,000	Llandrindod Wells	Powys",
# "	Rhondda	Borough	Mid Glamorgan	23,882 acres (96.65 km2)	87,710	79,300	Pentre	Rhondda Cynon Taf",
# "	Rhuddlan	Borough	Clwyd	26,860 acres (108.7 km2)	49,920	55,000	Rhyl	Denbighshire",
# "	Rhymney Valley	District	Mid Glamorgan	43,522 acres (176.13 km2)	103,800	104,000	Hengoed	Caerphilly",
# "	South Pembrokeshire	District	Dyfed	134,640 acres (544.9 km2)	37,060	42,700	Pembroke Dock	Pembrokeshire",
# "	Swansea	City	West Glamorgan	60,504 acres (244.85 km2)	190,370	189,400	Swansea	Swansea",
# "	Taff-Ely	Borough	Mid Glamorgan	41,632 acres (168.48 km2)	86,880	99,700	Pontypridd	Cardiff, Rhondda Cynon Taf",
# "	Torfaen	Borough	Gwent	31,258 acres (126.50 km2)	88,870	91,300	Pontypool	Torfaen",
# "	Vale of Glamorgan	Borough	South Glamorgan	73,198 acres (296.22 km2)	106,490	114,800	Barry	Vale of Glamorgan",
# "	Wrexham Maelor	Borough	Clwyd	90,569 acres (366.52 km2)	106,800	117,200	Wrexham	Wrexham"]
#
#
# # d_e = [i.split('website')[0].replace('city of ', '').strip().lower() for i in districts_england]
# # d_w = [i.split('Borough')[0].split('District')[0].split('City')[0].split(' on ')[0].strip().lower() for i in
# #        districts_wales]
# #
# # print(d_e)
# # print(d_w)
# # print(len(d_e))
# # print(len(d_w))
# # print(len(dds))
# # one = []
# # two = []
# # three = []
# # for j in dds:
# #     if j not in d_e and j not in d_w:
# #         one.append(j)
# # for k in d_e:
# #     if k not in dds:
# #         two.append(k)
# # for l in d_w:
# #     if l not in dds:
# #         three.append(l)
# #
# # print(one)
# # print(two)
# # print(three)


x = 2
