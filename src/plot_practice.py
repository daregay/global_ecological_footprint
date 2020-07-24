import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.font_manager import FontProperties
import branca.colormap as cm
import folium
import json
import argparse
plt.style.use("seaborn-darkgrid")


# functions for data cleaning
# df= pandas DataFrame

# droping columns 
def drop_col(df,index,inplace):
    return df.drop(index, inplace= inplace)

def find_NaN_values(df, col):
    "finds the NaN values in a given column"
    return df[(pd.isna(df[col])== True)]

def fillna(df, col, dic):
    '''function replaces NaN values in a col given a 
    dictionary of the values to replace it with '''
    while df[col].isnull().sum() >0:
        fillna_value={}
        for _ ,v in dic.items():
            fillna_value[col]=v
            df.fillna(fillna_value, inplace= True, limit=1)
        return df
    
def clean_column_values(df,col):
    '''cleans column values and turns them to float'''
    final_col_output= []
    for value in (df[str(col)].tolist()):
        joinstring=''
        for item in value:
              if item.isnumeric()==True or item== ".":
                    joinstring+=item
        final_col_output.append(float(joinstring))
    df[str(col)]= final_col_output
    return df

def scatter_plot_with_small_subplot (ax,color, x, y, xtitle, ytitle, title, xlim,  ylim, ax1_location):
    '''returns a scatter plot zoomed in to show the points that you want(eliminate outliers)
    and another subplot that shows all the points '''
    fig= plt.figure(edgecolor= 'black')
    ax= fig.add_subplot(111)
    ax.scatter(x,y, s= 80, c= "purple")
    ax.set_xlabel(xtitle, fontsize= 20)
    ax.set_ylabel(ytitle, fontsize= 20)
    ax.set_title(title, fontsize=22, fontweight= "bold")
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    plt.figure()
    #small subplot 
    ax1= ax.inset_axes(ax1_location)
    
    ax1.scatter(x, y, color= color, s= 40 )
    ax1.set_xlim(0,1450)
    ax1.set_ylim(0,20 )
    
    return None

def groupby_total(df,groupby_col, columns):
    "groupby a certain column and find the sum"
    return df.groupby(groupby_col).sum()[columns]


def clean_col_name(df_, replace, replace_with):
    cols= df_.columns.tolist()
    cols= [col.replace(replace,replace_with) for col in cols]
    df_.columns= cols
    return df_


def line_graphs(df_region, x_value, ylabel, title):
    "given dataframe and x value it returns a line graph with multiple plots inside it"
    fig= plt.figure()
    plt.style.use("seaborn-darkgrid")
    row= 0
    for elem in df_region.index:
        plt.figure(1,1,row+1)
        region= pd.DataFrame({ 'column':x_value, "value":df_region.iloc[row,:] })
        row+=1
        plt.plot(region["column"], region["value"], label= elem)
    plt.legend(fancybox=True, fontsize=18)
    plt.ylabel(ylabel)
    plt.title(title,fontsize=22, fontweight= "bold" )
#     matplotlib.rc('axes', xsize=12)
    size=22
    params = {
          'figure.figsize': (15,8),
          'axes.labelsize': 20,
          'axes.titlesize': 22,
          'xtick.labelsize': size*0.75,
          'ytick.labelsize': size*0.75,
          'axes.titlepad': 25}
    plt.rcParams.update(params)
    return None

dataframe= pd.read_csv('/Users/danait/documents/galvanize/capstone/global_ecological_footprint/data/countries.csv', header= 0)
countries_dataframe= dataframe.copy()
index_cols_drop=[4,7,18,24,29,30,49, 57, 60,63,70,115,120,123,128, 145,184]
inplace= True
df= countries_dataframe  
fillna_HDI_col= {'Cayman Islands': 0.888, "Côte d'Ivoire": 0.516 ,'French Guiana':0.789, 
             'Guadeloupe':0.841, "Korea, Democratic People's Republic of": 0.733, 'Martinique':0.854, 
             'Réunion':0.836 ,'Somalia':0.364}
fillna_GDP_col= {'Cayman Islands': "$81124.51",'French Guiana':"$18313", 'Guadeloupe':"$25479",
             "Korea, Democratic People's Republic of": "$1700", 'Martinique':"$30056", 
             'Réunion':"$6200" ,'Somalia':'$314.54', 'Syrian Arab Republic':'$2032.62' }
#drop rows with many null columns 
clean1= drop_col(df,index_cols_drop,inplace)
    
#fill NaN values for the HDI column
clean2= fillna(clean1, "HDI", fillna_HDI_col)
    
#fill NaN values for GDP per Capita column
clean3= fillna(clean2, 'GDP per Capita',fillna_GDP_col )
    
#cleans the $ sign or other elements from columns
clean4= clean_column_values(clean3,'GDP per Capita')

df3= clean4.copy()



#scatter plot of ecological footprint as population and GDP increase 2 plots 
# fig= plt.figure(figsize=( 17,15), edgecolor= 'black')
 
# ax1= fig.add_subplot(2,1,1)
# ax1.scatter(df3['Population (millions)'],df3["Total Ecological Footprint"], color= "gray")
# ax1.set_xlabel("Population (millions)", fontsize= 20)
# ax1.set_ylabel("Total Ecological Footprint", fontsize= 20)
# ax1.set_title("Ecologial Footprint as Population Increases", fontsize=18, fontweight= "bold")
# ax1.set_xlim(0,150)
# ax1.set_ylim(0,16
# plt.figure()
# ax1a= ax1.inset_axes([0.6, 0.55, 0.40, .45]) 
# ax1a.scatter(df3['Population (millions)'],df3["Total Ecological Footprint"])




# ax2=fig.add_subplot(2,1,2)
# ax2.scatter(df3['GDP per Capita'],df3["Total Ecological Footprint"], color= "red")
# ax2.set_xlabel("GDP per Capita", fontsize= 20)
# ax2.set_ylabel("Total Ecological Footprint", fontsize= 20)
# ax2.set_title("Ecologial Footprint as GDP Increases", fontsize=18, fontweight= "bold")
# ax2.set_xlim(200,60000)
# ax2.set_ylim(-.50,16.5)
# plt.figure()
# ax2a= ax2.inset_axes([0.6, 0.65, 0.40, .35])
# plt.savefig('Compare_GDP_VS_population_increases_footprint.png', bbox_inches='tight') 
# ax2a.scatter(df3['GDP per Capita'],df3["Total Ecological Footprint"])
# plt.tight_layout()

 # plots
 #scatter plot of ecological footprint as population increases     
df= clean4.copy()
color= "gray"
x= df['Population (millions)']
y= df["Total Ecological Footprint"]
xtitle= "Population (millions)"
ytitle= "Total Ecological Footprint"
title= "Ecologial Footprint as population increases"
xlim= (0,150)
ax1_location= [0.6, 0.55, 0.40, .45]
ylim=(-.50,16.5) 
ax="ax" 
scatter1= scatter_plot_with_small_subplot(ax,color, x, y, xtitle, ytitle, title, xlim,  ylim,  ax1_location)
print(scatter1)    

    #scatter plot of ecological footprint as GDP increases
x= df['GDP per Capita']
y= df["Total Ecological Footprint"]
xtitle= "GDP per Capita"
ytitle= "Total Ecological Footprint"
title= "Ecologial Footprint as GDP increases"
xlim= (200,60000)
ylim= (-.50,16.5) 
ax1_location= [0.6, 0.65, 0.40, .35]
scatter2= scatter_plot_with_small_subplot(ax,color, x, y, xtitle, ytitle, title, xlim,  ylim,     ax1_location)
print(scatter2)
    
    
    #biocapacity as population increases
x= df['Population (millions)']
y= df["Biocapacity Deficit or Reserve"]
xtitle= "Population (millions)"
ytitle= "Biocapacity Deficit or Reserve"
title= "Biocapacity as Population Increases"
xlim= (0,100)
ax1_location= [0.6, 0.65, 0.40, .35]
ylim= (-5,5) 
scatter3= scatter_plot_with_small_subplot(ax,color, x, y, xtitle, ytitle, title,xlim, ylim, ax1_location)
print(scatter3)   

    #biocapacity as GDP increases
x= df['GDP per Capita']
y= df["Biocapacity Deficit or Reserve"]
xtitle= "GDP per Capita"
ytitle= "Biocapacity Deficit or Reserve"
title= "Deficit or Reserve as GDP Increases"
xlim= (200,6000)
ax1_location= [0.6, 0.65, 0.40, .35]
ylim= (-5,5) 
scatter4 = scatter_plot_with_small_subplot(ax,color, x, y, xtitle, ytitle, title, xlim,         ylim, ax1_location) 
print(scatter4)   
plt.show()