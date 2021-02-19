//string holding path to json file
source_file = "/raw_data/cleaned_agdata.json"
//d3.json() makes a promise to do something after the file is retrieved.
//that's why we use the .then() to add a function to do something with
//the data once we've received it.
d3.json(source_file).then(data => {
    console.log(data["ALABAMA"]);
    states = [];
    for (var state in data){
        states.push(state);
    }
    console.log(states);

    counties = []
    for (var county in data["ALABAMA"]){
        counties.push(county);
    }
    console.log(counties);
});

//Note: You won't be able to read the file unless you're using a localhost
//server via go live or python or the like. It's a security thing.