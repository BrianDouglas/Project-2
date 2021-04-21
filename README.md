# agData-website

## Overview
  A website that aggregates data from the USDA to visualize how agricultural land is distributed across the US. An interactive map is provided to see the amount of agricultural land there is at the state and county levels. Charts are used to explore county data for each state and an info panel shows the types of usages in each county. Additionally, API end points are provided to query state and county data in JSON format.
  
## Features
### Interactive Map
  * Mapbox and leaflet are used to create an interactive choropleth map. The map has two layers representing state and county level choropleths. States and counties can be clicked on to zoom that map to that area
  * **Future development:** When a state is clicked on the county layer should be toggled on. When zoomed out sufficiently the state layer should be toggled on.

### Data Analysis
  * Plotly and d3 are used to create the charts to inspect state level agriculture usage. States can be selected from the drop down and the total agriculture usage for each county will be layed out on the bar chart. This chart can be sorted alphabetically, or numerically in ascending or descending order.
  * Another dropdown can be used to select a particular county in the selected state. This then populates an info box that will show a breakdown of the types of agricultural usages in that county.
  * **Future development:** Effort will be made to make the chart interactive. Selecting a state from the map should select that state for the data analysis section. Furthermore, counties should be able to be selected from the plot. These two features would remove the need for 2 dropdown menus and the sort can be integrated into the plot

### API Endpoints
  * Appending /api to the homepage will show how to use the API. 
  * To retrieve data on all counties in a state simply append /api/<state_name>
  * To retrieve data for only a specific county append /api/<state_name>/<county_name>

## Performance considerations
  * The county level geojson file is quite large. Because it is a layer added to the map on creation the map will not display until the entire file has been processed. 
    * Will consider not loading county level data until the layer is selected. Possible to only add county data when it's associated state is selected also.
