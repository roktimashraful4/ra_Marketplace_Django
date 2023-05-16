$(function(e){
  'use strict'

	//world map
	if ($('#world-map-gdp').length ){

		$('#world-map-gdp').vectorMap({
			map: 'world_en',
			backgroundColor: null,
			color: '#6964f7',
			hoverOpacity: 0.7,
			selectedColor: '#ec296b',
			enableZoom: true,
			showTooltip: true,
			values: sample_data,
			scaleColors: ['#ec296b', '#4801ff'],
			normalizeFunction: 'polynomial'
		});

	}


	jQuery('#usa-map').vectorMap({
		map: 'usa_en',
		backgroundColor: null,
		color: '#6964f7',
		enableZoom: true,
		showTooltip: true,
		selectedColor: null,
		hoverColor: null,
		colors: {
			mo: '#2980b9',
			fl: '#27ae60',
			or: '#8e44ad'
		},
		onRegionClick: function(event, code, region){
			event.preventDefault();
		}
	});
	
	jQuery('#german').vectorMap({
		map: 'germany_en',
		backgroundColor: null,
		color: '#6964f7',
		hoverOpacity: 0.7,
		enableZoom: false,
		showTooltip: false
	});
	
	jQuery('#russia').vectorMap({
			map : 'russia_en',
			backgroundColor: null,
			color: '#6964f7',
			hoverOpacity: 0.7,
			selectedColor: '#ec296b',
			enableZoom: true,
			showTooltip: true,
			values: sample_data,
		});
	

});