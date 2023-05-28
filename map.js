var map = L.map('map');
var coordenadas = {
    lat1: 0,
    lng1: 0,
    lat2: 0,
    lng2: 0
}
var animando = false
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

$('body').height(window.innerHeight+'px')

function getUrlParameter(name) {
    name = name.replace(/[[]/, '\\[').replace(/[\]]/, '\\]');
    var regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
    var results = regex.exec(location.search);
    return results === null ? '' : decodeURIComponent(results[1].replace(/\+/g, ' '));
}

var lat1 = (getUrlParameter('lat1')?parseFloat(getUrlParameter('lat1')):25.721647034182975),
lng1 = (getUrlParameter('lng1')?parseFloat(getUrlParameter('lng1')):-100.33862172891841),
lat2 = (getUrlParameter('lat2')?parseFloat(getUrlParameter('lat2')):25.725277870746236),
lng2 = (getUrlParameter('lng2')?parseFloat(getUrlParameter('lng2')):-100.31354186611351)

L.Routing.control({ 
    waypoints: [ 
       L.latLng(lat1, lng1), 
       L.latLng(lat2, lng2) ] 
    }).addTo(map);

$(window).on('resize', () => {
    $('body').height(window.innerHeight+'px')    
})

$('#input-salida').on('propertychange input', ()=>{
    console.log(1)
    $.ajax({
        url: 'https://geocode.search.hereapi.com/v1/geocode',
        data: {
          apiKey: 'jkoxzZckultxUMnycgyCKwuWFHu6k3o9ezmyjrLaZig',
          q: $('#input-salida').val()+' Nuevo León, México',
          limit: 1
        }
      }).done(function(data) {  
        console.log(data)
        //$('#menu-salida>.item-dropdown').remove()
        data.items.forEach(e => {
            coordenadas.lat1 = e.position.lat
            coordenadas.lng1 = e.position.lng
        });
      });
    
})

$('#input-destino').on('propertychange input', ()=>{
    console.log(1)
    $.ajax({
        url: 'https://geocode.search.hereapi.com/v1/geocode',
        data: {
          apiKey: 'jkoxzZckultxUMnycgyCKwuWFHu6k3o9ezmyjrLaZig',
          q: $('#input-destino').val()+' Nuevo León, México',
          limit: 1
        }
      }).done(function(data) {  
        console.log(data)
        //$('#menu-salida>.item-dropdown').remove()
        data.items.forEach(e => {
            coordenadas.lat2 = e.position.lat
            coordenadas.lng2 = e.position.lng
        });
      });
    
})

$('#search').click(()=>{
    window.location.href = 'index.html?lat1='+coordenadas.lat1+'&lng1='+coordenadas.lng1+'&lat2='+coordenadas.lat2+'&lng2='+coordenadas.lng2
})