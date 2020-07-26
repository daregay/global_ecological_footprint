import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.font_manager import FontProperties
df3= clean4.copy()


#  scatter plot of ecological footprint as population and GDP increase returns 2 plots 
fig= plt.figure(figsize=( 17,15), edgecolor= 'black')
 
ax1= fig.add_subplot(2,1,1)
ax1.scatter(df3['Population (millions)'],df3["Total Ecological Footprint"], color= "gray")
ax1.set_xlabel("Population (millions)", fontsize= 20)
ax1.set_ylabel("Total Ecological Footprint", fontsize= 20)
ax1.set_title("Ecologial Footprint as Population Increases", fontsize=18, fontweight= "bold")
ax1.set_xlim(0,150)
ax1.set_ylim(0,16

ax1a= ax1.inset_axes([0.6, 0.55, 0.40, .45]) 
ax1a.scatter(df3['Population (millions)'],df3["Total Ecological Footprint"])




ax2=fig.add_subplot(2,1,2)
ax2.scatter(df3['GDP per Capita'],df3["Total Ecological Footprint"], color= "red")
ax2.set_xlabel("GDP per Capita", fontsize= 20)
ax2.set_ylabel("Total Ecological Footprint", fontsize= 20)
ax2.set_title("Ecologial Footprint as GDP Increases", fontsize=18, fontweight= "bold")
ax2.set_xlim(200,60000)
ax2.set_ylim(-.50,16.5)
plt.figure()
ax2a= ax2.inset_axes([0.6, 0.65, 0.40, .35])
plt.savefig('Compare_GDP_VS_population_increases_footprint.png', bbox_inches='tight') 
ax2a.scatter(df3['GDP per Capita'],df3["Total Ecological Footprint"])
plt.tight_layout()



# plots line graph of total regional ecological footprint of each categories 
'''creates random colors: matplotlib.colors.rgb_to_hsv(np.random.random(size=3))'''
fig= plt.figure()
plt.style.use("seaborn-darkgrid")
row= 0
for elem in df_region.index:
    plt.figure(1,1,row+1)
    
    
    
    region= pd.DataFrame({ 'column':clean_col_name(df_region, "Footprint", "").columns, "value":df_region.iloc[row,:]})
    row+=1
    plt.plot(region["column"], region["value"], label= elem)
    size=22
    plt.ylabel('Ecological footprint by category')
    plt.title('Total Regional Ecological Footprint',fontsize=22, fontweight= "bold" )
    params = {
          'figure.figsize': (15,8),
          'axes.labelsize': 20,
          'axes.titlesize': 22,
          'xtick.labelsize': size*0.75,
          'ytick.labelsize': size*0.75,
          'axes.titlepad': 25}
    plt.rcParams.update(params)
plt.legend(fancybox=True, fontsize=17)

# plot notes for folium heatmap 
'''Notes: first have file of the long and lat of the map you want to plot.
your data/what you want to plot must have feature id that matchs the long_lat file'''
# Import libraries
import json
import pandas as pd
import folium
 
# Initialize the map:
m = folium.Map( location=[37, -102],zoom_start=2)
m.fit_bounds([[52.193636, -2.221575], [52.636878, -1.139759]])
# Add the color for the chloropleth:
m.choropleth(
 geo_data=state_geo,
 # geo_data : the dataset containing the longitude and latitude of countries 
 name='choropleth',
 data=state_data,
 # the dataset/dataframe of what you are trying to plot 
 columns=['code_that_match_feature.id', 'col_to_plot'],
 # a column from your data set that matchs the state_geo feature_id (key_on)
 key_on='feature.id',

 fill_color='RdYlGn',
 # choose range of colors 
 nan_fill_color= "white",
 fill_opacity=0.7,
 line_opacity=0.2,
 legend_name='Title'
)
folium.LayerControl().add_to(m)
 
# Save to html
#m.save('name.html')







