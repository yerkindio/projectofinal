function iniciarMap(){
    var coord = {lat:-33.3633205, lng:-70.678306};
    var map = new google.maps.Map(document.getElementById('map'),{
        zoom: 10,
        center: coord
    });
    var marker = new google.maps.Marker({
        position: coord,
        map: map
    });
}