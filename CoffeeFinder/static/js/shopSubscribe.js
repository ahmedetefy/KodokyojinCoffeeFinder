




  var myLatlng = new google.maps.LatLng(-25.363882,131.044922); //initial map center
  var map 
  var marker
  var markersArray = [];
 

function initialize() {
    var mapOptions = {
  zoom: 4,
  center: myLatlng
  }
  
   
  map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

  

  google.maps.event.addListener(map, 'click', function(event) {
   //adds a marker at the place of the click
        placeMarker(event.latLng);
        document.getElementById('lat').value = event.latLng.lat();
        document.getElementById("long").value = event.latLng.lng();
        
    });

  // Create the search box and link it to the UI element.
  var input = /** @type {HTMLInputElement} */(
      document.getElementById('pac-input'));
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
  var searchBox = new google.maps.places.SearchBox(
    /** @type {HTMLInputElement} */(input));

  //adds a listener to respond to user search result
  google.maps.event.addListener(searchBox, 'places_changed', function() {

      //now we should get all the places, detect which place that the user selects and collect data about it
      var places = searchBox.getPlaces();
      var bounds = new google.maps.LatLngBounds();
      for (var i = 0, place; place = places[i]; i++) {
           var image = {
            url: place.icon,
            size: new google.maps.Size(71, 71),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(17, 34),
            scaledSize: new google.maps.Size(25, 25)
            };

          
      
            //sets the bounds of the selected place to be viewd
            bounds.extend(place.geometry.location);
        }
        //go to the selected place.
       map.fitBounds(bounds);
    });
  

  // Bias the SearchBox results towards places that are within the bounds of the
  // current map's viewport.
 
}


    //adds a marker on the passed location
  function placeMarker(location) {
    
       //loops on any existing markers and deletes it
   for (var i=0; i<markersArray.length; i++){
        if( map.getBounds().contains(markersArray[i].getPosition()) ){
        markersArray[i].setMap(null);
       }
     }
   
   //creates a new marker object and places it on the map
      marker = new google.maps.Marker({
      position: location,
      map: map,
      title:"Hello World!"
      });
     markersArray.push(marker); 

      var infowindow = new google.maps.InfoWindow({ // Info window on marker saying it belongs to the user
      content:"You Are Here"
     });

     infowindow.open(map,marker); // Opening the info window above the marker on the map

     //calls on the function that gets the address
    reverseGecoding(location);

     
    }
 
 //this function takes a latlng location as an input and requests the detailed address
 //from maps API
  function reverseGecoding(location){
      var lat = location.lat();
      var lng = location.lng();
      var xmlHttp = null;
    
    
    //initialize request and send it
    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "https://maps.googleapis.com/maps/api/geocode/json?latlng="+lat+","+lng+"&key={{APIkey}}", false );
    xmlHttp.send( null );
   
    //calls a function to process the response that was received from the request
    ProcessRequest(xmlHttp.responseText);

     
    
    
    
  }

  //takes as an input a JSON object containing location details
  function ProcessRequest(response) {
    //parse json object to a dictionary
    var json_data = JSON.parse(response);
    
    //get the formatted address from the dictionary
   var lol = json_data.results[0]['formatted_address'];

   //splits the string into fields and store it in an array
   var add = lol.split(',');
    window.document.getElementById("street").value = "add[0]";
    window.document.getElementById("area").value = add[2];
    document.getElementById("city").value = add[3];
    document.getElementById("country").value = add[4];
    //document.getElementById("demo").
    //response;
  }

 
  
    google.maps.event.addDomListener(window, 'load', initialize);
 
