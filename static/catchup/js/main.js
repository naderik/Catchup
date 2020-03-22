document.getElementById("mylocation").onclick = function () {
  var startPos;
  var geoOptions = {
    timeout: 10 * 1000
  }

  var geoSuccess = function (position) {
    startPos = position;
    userLat = startPos.coords.latitude;
    userLng = startPos.coords.longitude;
    
    map = new google.maps.Map(document.getElementById('map'), {
      zoom: 16,
      center: new google.maps.LatLng(userLat, userLng),
      mapTypeId: 'roadmap',
      //disableDefaultUI: true,
      fullscreenControl: true,
      scaleControl: false,
      zoomControl: false,
      streetViewControl: false
    });
    var marker = new google.maps.Marker({
      position: new google.maps.LatLng(userLat, userLng),
      map: map,
    });
  };
  var geoError = function (error) {
    console.log('Error occurred. Error code: ' + error.code);
  };

  navigator.geolocation.getCurrentPosition(geoSuccess, geoError, geoOptions);
};