var mymap = L.map('mapid').setView([51.505, -0.09], 2);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiYWxsZXhpbyIsImEiOiJja21xMGcwbHYxNmV3Mm5wZWd2NnQ2eHhmIn0.kTfXbeTPkVVzpmgFVGX2qQ'
}).addTo(mymap);
{location_pings}