var initialize = function() {
 
 
 var image = {url: 'http://simoneicardidevelarea.altervista.org/temp/map-logo.png'};// CAMBIARE CON PATH DI PROD

 
//MAP1 HK
  // fornisce latitudine e longitudine
  var latlng1 = new google.maps.LatLng(22.30821,114.22491);
  // imposta le opzioni di visualizzazione
  var options1 = { zoom: 13,
                  center: latlng1,
                  mapTypeId: google.maps.MapTypeId.ROADMAP,
				 panControl: false,
				zoomControl: false,
				scaleControl: false
                };
                 
  // crea l'oggetto map1
  var map1 = new google.maps.Map(document.getElementById('map1'), options1);
  
  
  
  var marker = new google.maps.Marker({ position: latlng1,
                                      map: map1, 
                                      title: 'Hong Kong Main office',
									  icon: image
									  });

 
//MAP2 Shangai
  // fornisce latitudine e longitudine
  var latlng2 = new google.maps.LatLng(31.30760, 121.51861);
  // imposta le opzioni di visualizzazione
  var options2 = { zoom: 13,
                  center: latlng2,
                  mapTypeId: google.maps.MapTypeId.ROADMAP,
				 panControl: false,
				zoomControl: false,
				scaleControl: false
                };
                 
  // crea l'oggetto map2
  var map2 = new google.maps.Map(document.getElementById('map2'), options2);  
  
  var marker = new google.maps.Marker({ position: latlng2,
                                      map: map2, 
                                      title: 'Shanghai office',
									  icon: image
									  });
 
 
 
//MAP3 USA
  // fornisce latitudine e longitudine
  var latlng3 = new google.maps.LatLng(40.75532,-73.99329);
  // imposta le opzioni di visualizzazione
  var options3 = { zoom: 13,
                  center: latlng3,
                  mapTypeId: google.maps.MapTypeId.ROADMAP,
				 panControl: false,
				zoomControl: false,
				scaleControl: false
                };
                 
  // crea l'oggetto map1
  var map3 = new google.maps.Map(document.getElementById('map3'), options3);
  
  var marker = new google.maps.Marker({ position: latlng3,
                                      map: map3, 
                                      title: 'Tollegno 1900 USA Inc.',
									  icon: image
									  });
									  
									  
//MAP3 Japan
  // fornisce latitudine e longitudine
  var latlng4 = new google.maps.LatLng(34.67657, 135.50210);
  // imposta le opzioni di visualizzazione
  var options4 = { zoom: 13,
                  center: latlng4,
                  mapTypeId: google.maps.MapTypeId.ROADMAP,
				 panControl: false,
				zoomControl: false,
				scaleControl: false
                };
                 
  // crea l'oggetto map1
  var map4 = new google.maps.Map(document.getElementById('map4'), options4);
  
  var marker = new google.maps.Marker({ position: latlng4,
                                      map: map4, 
                                      title: 'Tollegno 1900  Japan Inc.',
									  icon: image
									  });
  
}
 
window.onload = initialize;