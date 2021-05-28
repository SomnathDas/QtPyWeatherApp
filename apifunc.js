const options = {
        // Required: API key
        key: "", // REPLACE WITH YOUR KEY !!!

        // Put additional console output
        verbose: true,

        // Optional: Initial state of the map
        lat: 50.4,
        lon: 14.3,
        zoom: 5,
};

// Initialize Windy API
windyInit(options, windyAPI => {
    // windyAPI is ready, and contain 'map', 'store',
    // 'picker' and other usefull stuff

    const { map } = windyAPI;
    // .map is instance of Leaflet map
    let myData = JSON.parse(data)
    console.log(data)
    L.popup()
        .setLatLng()
        .setContent('Hello World') 
        .openOn(map);
});