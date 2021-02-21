// global scope vars
var myMap;
//var layerToggle = false;

// some helper functions
function numWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function toTitleCase(str) {
    return str.replace(
      /\w\S*/g,
      function(txt) {
        return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
      }
    );
}

// load the things
var overlays = [];
d3.json("/state_geo", function (data) {
    overlays.push(all_features(data));
})
d3.json("/county_geo", function (county_data) {
    overlays.push(all_features(county_data, county = true));
    createMap(overlays);
})

// Mapping business
function createMap(overlays){
    // Adding tile layer
    var light = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
        tileSize: 512,
        zoomOffset: -1,
        id: "mapbox/light-v9",
        accessToken: API_KEY
    });
    var outdoors = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "outdoors-v10",
    accessToken: API_KEY
    });
    // baseMaps object to hold our base layer(s)
    var baseMaps = {
        "Light Map": light,
        Outdoors : outdoors
    };
    // overlay object to hold our geoJSON features
    var overlayMaps = {
        State : overlays[0],
        County : overlays[1]
    };

    myMap = L.map("map", {
        center: [38, -96],
        zoom: 4,
        layers: [outdoors, overlayMaps.State]
    });
    
    L.control.layers(baseMaps, overlayMaps, {
        collapsed: false
        }).addTo(myMap);
    
    var legend = makeLegend(overlayMaps.State);
    legend.addTo(myMap);
}
//all feature function 
function all_features(jsonData, county = false) {
    var geojson = L.choropleth(jsonData, {
        valueProperty: "ACRES",
        scale: ["#2ef659", "#005d73"],
        steps: 6,
        mode: "q",
        style: {
            color: "#fff",
            weight: 1,
            fillOpacity: 0.7
        },

        onEachFeature: function (feature, layer) {
            layer.on({
                mouseover: function (event) {
                    var label = feature.properties.NAME;
                    if (county){
                        label +=  " (" + toTitleCase(feature.properties['STATE NAME']) + ")";
                    };
                    layer = event.target;
                    layer.bindTooltip("<h4 style='text-align: center;'>" + label + "</h4>" + "" + "<p>Total Ag Acres: " + numWithCommas(feature.properties.ACRES) + "</p").openTooltip();
                    layer.setStyle({
                        fillOpacity: 0.3
                    });

                },
                mouseout: function (event) {
                    layer = event.target;
                    layer.setStyle({
                        fillOpacity: 0.7
                    });
                },
                click: function (event) {
                    myMap.fitBounds(event.target.getBounds());
                }

            });
        }

    });
    return geojson
}

function makeLegend(geojson){
    var legend = L.control({ position: "bottomright" });

    legend.onAdd = function () {
        var div = L.DomUtil.create("div", "info legend");
        var limits = geojson.options.limits;
        var colors = geojson.options.colors;
        var labels = [];

        var legendInfo = "<h3 style = 'text-align: center;'>Total Ag Acres</h3>";
            //"<div class=\"labels\">" +
            //"<div class=\"min\"> Min: " + limits[0] + "</div>" +
            //"<div class=\"max\"> Max: " + limits[limits.length - 1] + "</div>" +
            //"</div>"
        div.innerHTML = legendInfo;

        limits.forEach(function (limit, index) {
            labels.push("<li style=\"background-color: " + colors[index] + "\"> </li>")

        });
        div.innerHTML += "<ul>" + labels.join("") + "</ul>";

        return div;

    };
    return legend;
}