jQuery(document).ready(function($) {
	
	$('.open_gallery').magnificPopup({
		items: [
		  {
			src: 'http://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Peter_%26_Paul_fortress_in_SPB_03.jpg/800px-Peter_%26_Paul_fortress_in_SPB_03.jpg',
			title: 'Peter & Paul fortress in SPB'
		  },
		  {
			src: 'http://www.simoneicardi.com/wp-content/uploads/2013/07/gea_logo.jpg',
			title: 'image number 2'
		  },
		  {
			src: 'http://www.simoneicardi.com/wp-content/uploads/2013/08/domopak0.jpg',
			title: 'image number 3'
		  }/*,
		  {
			src: '#my-popup', // CSS selector of an element on page that should be used as a popup
			type: 'inline'
		  }*/
		],
		gallery: {
		  enabled: true
		},
		type: 'image', // this is a default type
		
		
			 // Delay in milliseconds before popup is removed
	  removalDelay: 300,
	
	  // Class that is added to popup wrapper and background
	  // make it unique to apply your CSS animations just to this exact popup
	  mainClass: 'mfp-fade'
		
	});

});