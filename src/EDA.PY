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

def group_by(df, colum):
    "groups by certain colum"
    return df.groupby("colum")

def groupby_sum(df, groupcol, lst_col):
    "groups by groupcol and includes certain columns returns new data frame"
    return df.groupby(groupcol).sum()[lst_col]

def sort_dataframe(df, col, ascending= True):
    "return sorted dataframe by the given column"
    return df.sort_values([col], ascending= [False])

def reginal_biocapacity(df_region, title, ytitle):
    '''takes a dataframe, cleans the columns and uses the columns as lables on the x-axis
    and plots the rows at each axis
    '''
    fig= plt.figure(figsize= (10,8))
    plt.style.use("seaborn-darkgrid")
    row= 0
    for elem in df_region.index:
        plt.figure(1,1,row+1)
        region= pd.DataFrame({ 'column':clean_col_name(df_region, "Footprint", "").columns, "value":df_region.iloc[row,:]})
        row+=1
        plt.plot(region["column"], region["value"], label= elem)
    plt.legend(fancybox=True, fontsize=18)
    plt.ylabel(ytitle)
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



def heat_map():
    state_geo = country_geo
    state_data = data
 
    # Initialize the map:
    m = folium.Map( location=[37, -102],zoom_start=2)
    m.fit_bounds([[52.193636, -2.221575], [52.636878, -1.139759]])
    # Add the color for the chloropleth:
    m.choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=['CountryCode', 'Biocapacity Deficit or Reserve'],
    key_on='feature.id',
    fill_color='RdYlGn',
    nan_fill_color= "white",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Biocapacity Deficit or Reserve'
folium.LayerControl().add_to(m)
    return None

def subset_dataframe(df, columns):
    '''return the columns you want in a dataframe'''
    return df[[columns]]

def sort_values(df,columns,colum_sort, ascend= True):
    "returns df given df, columns to sort by, columns it want returned "
    return subset_dataframe(df, columns).sort_values([colum_sort],ascend= True)

def join_df(df1, df2, set_index, on, how):
    '''returns joined dataframs with th index specified, on certain column, and how you want to join it '''
    return df2.join(df1.set_index(set_index, on=on, how=how))

        
        
if __name__ == "__main__":

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
    countries_dataframe= drop_col(df,index_cols_drop,inplace)
    
    #fill NaN values for the HDI column
    countries_dataframe= fillna(df, "HDI", fillna_HDI_col)
    
    #fill NaN values for GDP per Capita column
    countries_dataframe= fillna(df, 'GDP per Capita',fillna_GDP_col )
    
    #cleans the $ sign or other elements from columns
    countries_dataframe= clean_column_values(df,'GDP per Capita')
    
    # plots
    
    #scatter plot of ecological footprint as population increases     
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
    scatter_plot_with_small_subplot(ax,color, x, y, xtitle, ytitle, title, xlim,  ylim,  ax1_location)
    

    #scatter plot of ecological footprint as GDP increases
    x= df['GDP per Capita']
    y= df["Total Ecological Footprint"]
    xtitle= "GDP per Capita"
    ytitle= "Total Ecological Footprint"
    title= "Ecologial Footprint as GDP increases"
    xlim= (200,60000)
    ylim= (-.50,16.5) 
    ax1_location= [0.6, 0.65, 0.40, .35]
    scatter_plot_with_small_subplot(ax,color, x, y, xtitle, ytitle, title, xlim,  ylim,     ax1_location)
    
    
    #biocapacity as population increases
    x= df['Population (millions)']
    y= df["Biocapacity Deficit or Reserve"]
    xtitle= "Population (millions)"
    ytitle= "Biocapacity Deficit or Reserve"
    title= "Biocapacity as Population Increases"
    xlim= (0,100)
    ax1_location= [0.6, 0.65, 0.40, .35]
    ylim= (-5,5) 
    scatter_plot_with_small_subplot(ax,color, x, y, xtitle, ytitle, title,xlim,           ylim, ax1_location)
    
    #biocapacity as GDP increases
    x= df['GDP per Capita']
    y= df["Biocapacity Deficit or Reserve"]
    xtitle= "GDP per Capita"
    ytitle= "Biocapacity Deficit or Reserve"
    title= "Deficit or Reserve as GDP Increases"
    xlim= (200,6000)
    ax1_location= [0.6, 0.65, 0.40, .35]
    ylim= (-5,5) 
    scatter_plot_with_small_subplot(ax,color, x, y, xtitle, ytitle, title, xlim,         ylim, ax1_location) 
    
    
    # #group dataframes 
    
    # #regionally grouped dataframe for ecologial footprint
    columns= ["Cropland Footprint", "Grazing Footprint", "Forest Footprint", "Carbon Footprint", "Fish Footprint", "Total  Ecological Footprint"]
    Regional_ecofootprint= groupby_total(countries_dataframe, "Region",columns)
    
    #clean the Regionally grouped column names
    region_ecofootprint= clean_col_name(Regional_ecofootprint, "Footprint", "")
    
    #regionally grouped dataframe for biocapcity 
    columns=["Cropland", "Grazing Land", "Forest Land", "Fishing Water", "Urban Land", "Total     Biocapacity"]
    regional_biocap=groupby_total(countries_dataframe, "Region",columns)
    
    #regionally grouped dataframe for ecological footprint, biocapacity, and  deficit or reserve 
    columns= ["Total Biocapacity",'Total Ecological Footprint','Biocapacity Deficit or Reserve']
    regional_bio_eco=groupby_total(countries_dataframe, "Region",columns) 
    
    
    # #graph line plots
    
    # #line graph of total regional biocapacity for each categorie 
    # line_graphs(regional_biocap,regional_biocap.columns, 'Biocapacity by category',       'Total Regional Biocapacity' )

    # #line graph of total regional ecological footprint for eat categorie
    # line_graphs(region_ecofootprint,region_ecofootprint.columns, 'Ecological footprint by category', 'Total Regional Ecological Footprint' )
    
    # #line graph of ecological footprint, biocapacity, and regional biocapacity deficient or reserv
    # line_graphs(regional_bio_eco,regional_bio_eco.columns, 'global hectares per person', "Reginal Biocapacity vs. Ecological Demand" )
    # plt.show()


