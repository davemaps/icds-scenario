# icds-scenario

Data Viz Scenario for ICDS

# Visualizations – scrollytelling site

## Actual cluster data

### Charts with national data

Stacked bars by age or connected scatter plot (multi-series)?

### Data driven circles map

Circle size by number of individuals in the cluster
Change color by rate of seroprevalence
Slider to filter by age
Pop-up with same stacked bars as above
Geocoder search to zoom to location

## Predict outcomes for an individual

Our first attempt to generalize the clusters across a wider area

### Voronoi

Cut up country into slices by cluster
Bivariate choropleth, or same colors as circles map?
Slider to filter by age
Pop-up with same chart(s) as above
Geocoder search to zoom to location

### Gridded pop. data coded by voronoi cluster

TK - more info needed here

## Targeting vaccination campaigns

Assume that age does not affect susceptibility differently by location

### Choropleth by political boundaries

Calculate cluster data stats by population within political boundaries
Slider to filter by age
Pop-up with same chart(s) as above
Geocoder search to zoom to location

# Tools Used

All open source, cross-platform tools

-VS Code
-QGIS to explore data spatially
-Python with Pandas
-Visidata
-csv2geojson

## Proof of concept for targeting 3 vaccines

# Data

-Sample data
-Generated seroB, seroC data
-GRID3 Nigeria National Population Estimates

# References

-[Python venv](https://python.land/virtual-environments/virtualenv)
-[Running a simple Python http server](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/set_up_a_local_testing_server)