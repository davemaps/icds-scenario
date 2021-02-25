# icds-scenario

Data Viz Scenario for ICDS

Find multimedia to use:

- Nigerian flag
- stock footage of vaccination clinic?
- stock footage of locales when zooming to data for a specific place

(scroll to overview of new map, then keep scrolling to zoom to specific places)

## Visualizations – scrollytelling site

### Actual cluster data

#### Charts with national data

Stacked bars by age or connected scatter plot (multi-series)?

#### Data driven circles map

Circle size by number of individuals in the cluster
Change color by rate of seroprevalence
Slider to filter by age
Pop-up with same stacked bars as above
Geocoder search to zoom to location

### Predict outcomes for an individual

Our first attempt to generalize the clusters across a wider area

#### Voronoi

Cut up country into slices by cluster
Bivariate choropleth, or same colors as circles map?
Slider to filter by age
Pop-up with same chart(s) as above
Geocoder search to zoom to location

This could be useful for entering an individual’s location and quickly finding statistics from the nearest cluster.
But of course just as land does not vote (a common problem with election maps), land does not catch disease, so this method is not the best for communicating information about the population.

#### Gridded pop. data coded by voronoi cluster

Using gridded population data, we can more accurately represent where people exist with/without seroprevalence.
This is likely the best visualization when communicating broadly to the public.

### Targeting vaccination campaigns

Assume that age does not affect susceptibility differently by location

#### Choropleth by political boundaries

Then, use existing political boundaries for vaccination campaigns
Calculate cluster data stats by population within political boundaries
Slider to filter by age
Pop-up with same chart(s) as above
Geocoder search to zoom to location

#### Rankings of states/locales most in need of vaccination

update with age range filter

## Tools Used

All open source, cross-platform tools

- VS Code
- QGIS to explore data spatially
- Python with Pandas
- Visidata
- csv2geojson

These tools make the process reproducible and scriptable, so that the visualizations could automatically be updated when new data is available.

### Proof of concept for targeting 3 vaccines

## Timeline

### Monday

Explore data and make plan, starting with envisioned final product

### Tuesday

Write script to clean and convert data

### Wednesday

Code the maps and discover gridded population data by age (YAY!)

## Data

- Original sample data
- Cleaned sample data with generated seroB, seroC data
- [GRID3 Nigeria National Population Estimates](https://grid3.gov.ng/dataset/national-population-estimates/resources)

## References

- [Python venv](https://python.land/virtual-environments/virtualenv)
- [Running a simple Python http server](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/set_up_a_local_testing_server)
- [Getting Mapbox labels above features](https://docs.mapbox.com/mapbox-gl-js/example/geojson-layer-in-stack/)
