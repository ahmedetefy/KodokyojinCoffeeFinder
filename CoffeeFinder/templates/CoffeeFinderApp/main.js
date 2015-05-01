        var lat;
        var long;
        var coords;
        alert("hello");
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

        function myFunction() {
          if(navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
            var pos = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
            window.alert("Your location will be added automatically as the delivery address");
            reverseGecoding(pos);
            }, function() {
              handleNoGeolocation(true);
            }, {enableHighAccuracy: true});
          } else {
            // Browser doesn't support Geolocation
            handleNoGeolocation(false);
          }
        }
        function ProcessRequest(response) {
          //parse json object to a dictionary
          var json_data = JSON.parse(response);
            
          //get the formatted address from the dictionary
          var address = json_data.results[0]['formatted_address'];
          document.getElementById("order-address").value = address.toString();
        }
        function handleNoGeolocation(errorFlag) {
          if (errorFlag) {
            var content = 'Error: The Geolocation service failed.';
          } else {
            var content = 'Error: Your browser doesn\'t support geolocation.';
          }
        }