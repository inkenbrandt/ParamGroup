
# coding: utf-8

# In[1]:

get_ipython().magic(u'matplotlib inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from pylab import rcParams
rcParams['figure.figsize'] = 15, 10


# In[2]:

import sys
import platform
import matplotlib
print("Operating System " + platform.system() + " " + platform.release())
print("Python Version " + str(sys.version))
print("Pandas Version " + str(pd.__version__))
print("Numpy Version " + str(np.__version__))
print("Matplotlib Version " + str(matplotlib.__version__))


# In[3]:

inorganics_major_metals = ['calcium', 'dissolved calcium', 'dissolved magnesium', 'dissolved potassium', 'dissolved sodium', 
                           'magnesium', 'potassium', 'sodium', 'sodium adsorption ratio', 
                           'sodium adsorption ratio [(na)/(sq root of 1/2 ca + mg)]', 'sodium plus potassium', 
                           'sodium, percent total cations', 'total calcium', 'total magnesium', 'total potassium', 
                           'total sodium', 'percent sodium', 'hypochlorite ion']  # noqa
inorganics_major_nonmetals = ['acidity as caco3', 'alkalinity', 'alkalinity, bicarbonate as caco3', 
                              'alkalinity, carbonate as caco3', 'alkalinity, hydroxide as caco3', 
                              'alkalinity, phenolphthalein (total hydroxide+1/2 carbonate)', 'alkalinity, total', 
                              'alkalinity, total as caco3', 'bicarbonate', 'bicarbonate as caco3', 'bicarbonate as hco3', 
                              'bromide', 'carbon dioxide', 'carbonate', 'carbonate (co3)', 'carbonate as caco3', 
                              'carbonate as co3', 'chloride', 'chlorine', 'dissolved oxygen (do)', 'dissolved oxygen (field)', 
                              'dissolved oxygen saturation', 'fluoride', 'fluorine', 'gran acid neutralizing capacity',
                                      'hydrogen', 'hydrogen ion', 'hydroxide', 'inorganic carbon', 'oxygen', 'silica', 
                              'silicon', 'sulfate', 'sulfide', 'sulfur', 'total alkalinity as caco3', 'total carbon', 
                              'silica d/sio2', 't. alk/caco3', 'alkalinity as cac03', 'silica, dis. si02', 'carbon, total', 
                              'chlorine dioxide', 'chlorite', 'residual chlorine', 'hydroxide as calcium carbonate', 
                              'hydrogen sulfide', 'alkalinity, caco3 stability', 'acidity, total (caco3)', 'acidity, m.o. (caco3)', 'alkalinity, bicarbonate', 'alkalinity, carbonate', 'alkalinity, phenolphthalein', 'total chlorine', 'combined chlorine', 'perchlorate', 'free residual chlorine']  # noqa
inorganics_minor_nonmetals = ['antimony', 'argon', 'arsenate (aso43-)', 'arsenic', 'arsenite', 'boron', 'bromine', 'cyanide', 
                              'cyanides amenable to chlorination (hcn & cn)', 'dissolved arsenic', 'dissolved boron', 
                              'dissolved selenium', 'germanium', 'helium', 'iodide', 'krypton', 'neon', 'perchlorate', 
                              'selenium', 'sulfur hexafluoride', 'tellurium', 'total arsenic', 'total boron', 'total selenium', 
                              'xenon', 'chlorate', 'antimony, total', 'boron, total', 'asbestos']
inorganics_minor_metals = ['aluminum', 'barium', 'beryllium', 'bismuth', 'cadmium', 'cerium', 'cesium', 'chromium', 
                           'chromium(iii)', 'chromium(vi)', 'cobalt', 'copper', 'dissolved aluminum', 'dissolved barium', 
                           'dissolved cadmium', 'dissolved chromium', 'dissolved copper', 'dissolved iron', 'dissolved lead', 
                           'dissolved manganese', 'dissolved mercury', 'dissolved molybdenum', 'dissolved nickel', 
                           'dissolved zinc', 'dysprosium', 'erbium', 'europium', 'gadolinium', 'gallium', 'holmium', 
                           'iron', 'iron, ion (fe2+)', 'lanthanum', 'lead', 'lithium', 'lutetium', 'manganese', 'mercury', 
                           'molybdenum', 'neodymium', 'nickel', 'niobium', 'praseodymium', 'rhenium', 'rubidium', 'samarium', 
                           'scandium', 'silver', 'strontium', 'terbium', 'thallium', 'thulium', 'tin', 'titanium', 
                           'total aluminum', 'total barium', 'total cadmium', 'total chromium', 'total copper', 'total iron', 
                           'total iron-d max, dmr', 'total lead', 'total manganese', 'total mercury', 'total molybdenum', 
                           'total nickel', 'total zinc', 'tungsten', 'vanadium', 'ytterbium', 'yttrium', 'zinc', 'zirconium',
                           'iron, dissolved', 'chromium, hex, as cr', 'copper, free', 'iron, suspended', 'manganese, suspended', 
                           'beryllium, total', 'bismuth, total', 'chromium, hex', 'cobalt, total', 'lithium, total', 
                           'molybdenum, total', 'thallium, total', 'tin, total', 'titanium, total', 'vanadium, total', 
                           'lead summary', 'copper summary', 'manganese, dissolved']   # noqa
nutrient = ['ammonia', 'ammonia and ammonium', 'ammonia as n', 'ammonia as nh3', 'ammonia-nitrogen', 
            'ammonia-nitrogen as n', 'ammonium', 'ammonium as n', 'dissolved nitrate: no3', 
            'inorganic nitrogen (nitrate and nitrite)', 'inorganic nitrogen (nitrate and nitrite) as n', 
            'kjeldahl nitrogen', 'nitrate', 'nitrate as n', 'nitrate-nitrogen', 'nitrite', 'nitrite as n', 
            'nitrogen', 'orthophosphate', 'nitrogen, ammonium/ammonia ratio', 'dissolved nitrite: no2', 
            'nitrogen, mixed forms (nh3), (nh4), organic, (no2) and (no3)',
            'no2+no3 as n', 'organic nitrogen', 'ortho. phosphate', 'orthophosphate as p', 'phosphate', 
            'phosphate-phosphorus', 'phosphate-phosphorus as p', 'phosphate-phosphorus as po4', 'phosphorus', 
            'total phosphorus', 'nitrate + nitrite as n', 'phosphate, tot. dig. (as p)', 't.k.n.', 'phosphorus 0 as p', 
            'nitrogen-ammonia as (n)', 'nitrate-nitrite', 'phosphate, total', 'total kjeldahl nitrogen (in water mg/l)', 
            'phosphorus, soluble', 'phosphate, reactive', 'phosphorus, total'] 


# In[5]:

import xmltodict
infile = "C:/Users/PAULINKENBRANDT/Downloads/ResultSampleFraction/Results.xml"
#infile = "C:/Users/PAULINKENBRANDT/Downloads/ResultMeasureValuePickList/Results.xml"

with open(infile) as fd:
    # parse xml to a dictionary, encode for degree signs
    obj = xmltodict.parse(fd.read(), encoding="UTF-8", xml_attribs=True)

rows = int(obj["WQXDomainValueList"]["WQXElement"]['WQXElementName']['@rowCount'])
cols = len(obj["WQXDomainValueList"]["WQXElement"]["WQXElementRow"][0]['WQXElementRowColumn'])

head = []
f = {}
for j in range(cols):
    head.append(obj["WQXDomainValueList"]["WQXElement"]["WQXElementRow"][0]['WQXElementRowColumn'][j]['@colname'])
    rowlist= []
    for i in range(rows):
        rowlist.append(obj["WQXDomainValueList"]["WQXElement"]["WQXElementRow"][i]['WQXElementRowColumn'][j]['@value'])
        f[head[j]] = rowlist


# In[7]:

SDWISlist = pd.read_csv("E:/GitHub/ParamGroup/PARAM_MATCH.txt")
NWISlist = pd.read_table("E:/GitHub/ParamGroup/parameter_cd_query.txt",skiprows=[0,1,2,3,4,5,6,8])


# In[8]:

SDWISlist

def parMedia(x):
    if ', water, ' in x:
        media = 'water'
    elif ' soil, ' in x:
        media = 'soil'
    elif ', solids' in x:
        media = 'soil'
    elif ', rock, ' in x:
        media = 'rock'
    elif ', biota, ' in x:
        media = 'biota'
    elif ', air, ' in x:
        media = 'air'
    else:
        media = ''
    return media
        
def parSampFrac(x):
    if ', dissolved,' in x:
        sampfrac = 'Dissolved' 
    elif ', filtered' in x:
        sampfrac = 'Filtered'
    elif ', unfiltered' in x:
        sampfrac = 'Unfiltered'
    else:
        sampfrac = ''
    return sampfrac
        
SDWISlist['media'] = SDWISlist["parameter_nm"].apply(lambda x: parMedia(x), 1)
SDWISlist['sampfrac'] = SDWISlist["parameter_nm"].apply(lambda x: parSampFrac(x), 1)


# In[9]:

SDWISlist = SDWISlist[SDWISlist['media']=='water']


# In[11]:

def ListMake(df,parName,groupName):
    df["lowerNAME"] = df[parName].apply(lambda x: str(x).lower().strip(), 1)
    groups = list(df[groupName].unique())
    groupsLwr = [i.lower() for i in list(df[groupName].values)] 
    #groupsLwr = [i.lower() for i in groups]
    grpvalues = list(df['lowerNAME'].values)
    grpkeys = list(df[groupName].values)
    f = {}
    for i in range(len(groups)):
        f[groupsLwr[i]] = list(df[df[groupName]==groups[i]]['lowerNAME'])
    return f,groupsLwr, grpvalues, grpkeys


# In[12]:

parList1 = ListMake(SDWISlist, "parameter_nm", "parameter_group_nm")
parList2 = ListMake(NWISlist, "parm_nm", "group")
parList3 = ListMake(SDWISlist, "srsname", "parameter_group_nm")


# In[13]:

groupsLwr = parList1[1] + parList2[1] + parList3[1]
grpvalues = parList1[2] + parList2[2] + parList3[2]
grpkeys = parList1[3] + parList2[3] + parList3[3]


parlist = sorted(list(set(parList1[1] + parList2[1] + parList3[1])))
parlistValues = sorted(list(set(parList1[2] + parList2[2] + parList3[2])))
parlistKeys = sorted(list(set(parList1[3] + parList2[3] + parList3[3])))


# In[14]:

print(len(groupsLwr), len(grpvalues), len(grpkeys))


# In[15]:

allParameters = dict(zip(grpvalues,groupsLwr))


# In[ ]:




# In[370]:

z = parList1[0].copy()
z.update(parList2[0])
z.update(parList3[0])


# In[371]:

z


# In[353]:

biological, information, inorganics_major_metals, inorganics_major_nonmetals = [],[],[],[]
inorganics_minor_metals, inorganics_minor_nonmetals, microbiological, nutrient, = [],[],[],[]
organics_other, organics_PCBs, organics_pesticide, physical, population_community = [],[],[],[],[]
radiochemical, sediment, stable_isotopes, toxicity = [],[],[],[]

groups = [biological, information, inorganics_major_metals, inorganics_major_nonmetals, inorganics_minor_metals,
inorganics_minor_nonmetals, microbiological,
nutrient, organics_other, organics_PCBs, organics_pesticide, physical, population_community, radiochemical, 
sediment, stable_isotopes, toxicity]


# In[359]:

for i in range(len(parlist)):
    groups[i] = (z[parlist[i]])


# In[360]:

def flattenList(listToFlatten):
    a = listToFlatten
    b= [i[x] for i in a for x in range(len(i))]
    return (sorted(list(set(b))))


# In[361]:

flattened = []
for i in groups:
    i = (flattenList(i))


# In[362]:

inorganics_major_metals


# In[363]:

print(parList1[1])
print(parList2[1])


# In[46]:

SDWISmatch

