# Global Ecological Footprint and Biocapacity

## Introduction

Ecological Footprint measures the ecological resources that a given population uses (demand side).  Biocapacity represents an ecosystem’s capacity to provide natural resources and absorb waste generated by a given population(supply-side). 
- They are measured by considering a region’s supply capacity and demand in these categories: croplands, grazing lands for animal products, forested areas to produce wood products, marine areas for fisheries, built-up land for housing and infrastructure, and forested land needed to absorb carbon dioxide emissions from energy consumption.
- Both the Ecological Footprint and biocapacity are expressed in global hectares(gha),which measures productive surface area. 
- A region is considered ecologically deficit when the footprint exceeds its biocapacity (they relay on trade, or liquidate their resources i.e. overfishing).
- It’s considered to have an ecological reserve when it's biocapacity exceeds its footprint. 


![Ecological Footprint image](images/footprint-labeled-crop.jpg)



### Motivating Questions 

* Which countries/regions are ecologically deficit?
* Which countries/regions have ecological reserves?
* Is population growth correlated to a higher ecological footprint?
* How about the relationship between GDP per capita and the countries ecological footprint?



## Dataset 

I found the countries.csv data from Kaggle. The dataset was from 2016 and was updated 3 years ago.  It was originally provided by the Global Footprint Network. 

* sums five categories to track a country's ecological footprint: cropland footprint, grazing footprint, fish footprint, built-up (or urban) land, and carbon demand on land.
* sums five categories to track a country's biocapacity: cropland land, grazing land, fishing water, forest area, and urban land.
* the ecological footprint was subtracted from the biocapacity to determined if a country is ecologially deficit or has reserves. 
* 21 columns of data with a mixture of floats and strings
* 188 rows (188 countries)
* filling null values and conversion of column datatype was needed.
* I also deleted some countries with a lot of missing data. The final cleaned dataset contained 171 countries. 

* I also obtained another world.countries dataset from Kaggle to create the heatmaps using geographical coardinates. 

## Data Source 
* https://www.kaggle.com/footprintnetwork/ecological-footprint

sources used to fill NaN values
* https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_capita#References
* https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index


## Exploratory Data Aanlysis

### Biocapacity and Ecological Footprint by Country

Question: Which countries/regions are ecologically deficit?have reserve? 
* To arrange the scaling and help visualize the data better by country I eliminated these 3 oulier countries from the  maps below. 
![outlier_countries](images/outlier_countries.png)

First I want to look at a country's Biocapacity level per person. This maps shows the total Biocapacity of a country per person.  
![map heat of biocapacity](images/Biocap.png)

Many of the countries have really low Biocapacity level, they fall within the ranges of 0 to 4 global hectors. The rest have ranges of 4 to 18. Gabon's Biocapacity is between 22 to 26. The three outlier country's Biocapacity is ranged from 66- 111 gha. 


The map below shows the Ecological Footprint of a country per person. 
![map heat of ecological footprint](images/EcoFP.png)
Many countries in North America have a high Ecological Footprint compared to other regions. Countries in Africa have the lowest Ecological Footprint. 

Many of the countries Ecological Footprint is in the range of 0 to 11 global hectors. Some limited countries such as Luxembourg have footprints as high as 16gha. 
* The countries with Ecological Footprint that range from 11 to 16gha are too small to see on the map without zooming. 

Map of countries with Biocapacity Deficits or Reservs
* deficit or reserve = Biocapacity - Ecological Footprint 

![map heat of deficit or reserve](images/bioDEFres.png)

Many countries have reservs that range from 0 to 5. Followed by a number of countries who are experiencing Biocapacity deficit that range from -1 to -8. 

- It seems that Latin America has the hightest number of countries whose Biocapacity is greater than its population’s Ecological Footprint. Let's look indepth at each of the categorical measurements by region.  




![graph regional biocapacity](images/"region_biocapacity".png)

This graph sums the biocapacity in each of the productive surface areas per region. Since this is per region the three outlier countries are included. 

- One reason Latine America has the highest number of countries who have Biocapacity reserve is due to it's large forest land per person. 
- Latine America also has the largest fishing capacity. 

![graph of regional ecological footprint](images/total_regional_footprint.png)
- Most of the regions Ecological footprint comes from carbon emissions. They all peak at carbon. 
- The Europian Union has the biggest Ecologial Footprint and carbon emissions, even though it's biocapacity is not very high. 

![graph of reg def res](images/region_biocap_vs_ecology_demand.png)
- 4 regions are below zero. 
- Most of the countries in the regions of Middle East/Central Asia, European Union, Northern/Easern Europe,European Union, Asian-Pacific have exceeded the regions biocapacity and are ecologically deficit. 

Latin America's high Biocapacity reserve or Biological capacity doesn't necessarly mean that it has the highest productive surface area out of all the regions. It means it has the highest productive surface area per person. So does population increase lead to an increase in Ecological Footprint? Is there another factor that yields stronger correlation? 

## Population vs. GDP per capita 

![ecofootprint_vs_pop_gdp](images/test3.png)
Since most of the countries have a population of 150 million, the graph is plotted to reflect those countries. The subplot inside includes all the countries in the dataset. The same with the GDP per capita, countries who have GDP up to 20000 are reflected in the graph, with all the countries included in the subplot. 

* There is no strong trend that is observed for the Ecological Footprint as the population increases. 

* For GDP however, there is a trend forming. The Ecological Footprint gradually increases as the GDP increases. The subplot also clearly reflects this positive correlation. 





![def_or_res_vs_pop_gdp](images/test2.png)

A very small trend is observed for the Biocapacity deficit or reserve as population increases. It seems countries that have larger than 50 million people are mostly in the Biocapacity deficit side. 
* However, whats interesting about this graph is that most countries have less than 25 million people. And more than half of these countries are located on the Biocapacity deficit side than the reserve. 
* If population increase was strongly correlated to ecological footprint, I believe more of these countries would have biocapacity reserve. 

For the second graph a stronger correlation is reflected. There is a visible trend of more biocapacity deficit countries as the GDP increases. 


## Conclusion 
A table of top ten biocapacity deficit countries 
![top deficit countries](images/topten_def.png)

A table of top ten biocapacity reserve countries
![top deficit countries](images/topten_res.png)











