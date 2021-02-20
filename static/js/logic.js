
// states Map map object
var myMap = L.map("map", {
    center: [38, -96],
    zoom: 5
});

// Adding tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    tileSize: 512,
    zoomOffset: -1,
    id: "mapbox/light-v9",
    accessToken: API_KEY
}).addTo(myMap);


var object = [];

//all feature function 
function all_features(jsonData) {
    geojson = L.choropleth(jsonData, {
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
                    layer = event.target;
                    layer.bindTooltip("<h1>" + feature.properties.NAME + "</h1>" + "<hr></hr>" + "<h2>" + feature.properties.ACRES + "</h2").openTooltip();
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
    return geoJson
}

//state acre info
d3.json("raw_data/acres_stateLevelGeo.json", function (data) {
    object.push(all_features(data))
})
d3.json("raw_data/countyLevelGeo.json", function (county_data) {
    object.push(all_features(county_data))
})
// d3.json("raw_data/countyLevelGeo.json", function(county_map){
//     L.geoJson(county_map).addTo(myMap)
// })
var overlayMaps = {
    State: object[0],
    County: object[1]
};

L.control.layers(overlayMaps, {
    collapsed: false
}).addTo(myMap);

var legend = L.control({ position: "bottomright" });
//legend 
legend.onAdd = function () {
    var div = L.DomUtil.create("div", "info legend");
    var limits = geojson.options.limits;
    var colors = geojson.options.colors;
    var labels = [];

    var legendInfo = "<h1>State Total Acres</h1>" +
        "<div class=\"labels\">" +
        "<div class=\"min\"> Min: " + limits[0] + "</div>" +
        "<div class=\"max\"> Max: " + limits[limits.length - 1] + "</div>" +
        "</div>";
    div.innerHTML = legendInfo;

    limits.forEach(function (limit, index) {
        labels.push("<li style=\"background-color: " + colors[index] + "\"> </li>")

    });
    div.innerHTML += "<ul>" + labels.join("") + "</ul>";

    return div;

};
legend.addTo(myMap);