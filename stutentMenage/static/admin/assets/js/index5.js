( function ( $ ) {
	/* line chart */
	
	
	var myCanvas = document.getElementById("lineChart");
	myCanvas.height="150";

	var myCanvasContext = myCanvas.getContext("2d");
	var gradientStroke1 = myCanvasContext.createLinearGradient(0, 0, 0, 380);
	gradientStroke1.addColorStop(0, 'rgba(105, 100, 247, 1)');
	
	var gradientStroke2 = myCanvasContext.createLinearGradient(0, 0, 0, 280);
	gradientStroke2.addColorStop(0, 'rgba(239, 80, 80, 1)');
	
    var myChart = new Chart( myCanvas, {
		type: 'bar',
		data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            type: 'bar',
            datasets: [ {
				label: 'In Progress',
				data: [50, 70, 30, 120, 40, 141, 60],
				backgroundColor: gradientStroke1,
				borderColor: '#6964f7',
				pointBackgroundColor:'#6964f7',
				pointHoverBackgroundColor:gradientStroke1,
				pointBorderColor :'#6964f7',
				pointHoverBorderColor :gradientStroke1,
				borderWidth: 2,
				borderRadius: 5,
            }, {
				label: "Completed",
				data: [30, 50, 70, 40, 80, 79, 50],
				backgroundColor: gradientStroke2,
				borderColor: '#ef5050',
				pointBackgroundColor:'#ef5050',
				pointHoverBackgroundColor:gradientStroke2,
				pointBorderColor :'#ef5050',
				pointHoverBorderColor :gradientStroke2,
				borderWidth: 2,
				borderRadius: 5,
			}
			]
        },
		options: {
			responsive: true,
			maintainAspectRatio: true,
			tooltips: {
				mode: 'index',
				titleFontSize: 12,
				titleFontColor: '#000',
				bodyFontColor: '#000',
				backgroundColor: '#fff',
				cornerRadius: 3,
				intersect: false,
			},
			legend: {
				display: true,
				labels: {
					usePointStyle: false,
				},
			},
			scales: {
				xAxes: [{
					barPercentage: 0.6,
					ticks: {
						fontColor: "#605e7e",
					 },
					display: true,
					gridLines: {
						display: true,
						color:'rgba(96, 94, 126, 0.1)',
						drawBorder: false
					},
					scaleLabel: {
						display: false,
						labelString: 'Month',
						fontColor: 'transparent'
					}
				}],
				yAxes: [{
					ticks: {
						fontColor: "#605e7e",
					 },
					display: true,
					gridLines: {
						display: true,
						color:'rgba(96, 94, 126, 0.1)',
						drawBorder: false
					},
					scaleLabel: {
						display: false,
						labelString: 'sales',
						fontColor: 'transparent'
					}
				}]
			},
			title: {
				display: false,
				text: 'Normal Legend'
			}
		}
	});
	/* line chart end */
	
	$(".sparkline22").sparkline([2, 4, 3, 4, 7, 5, 4, 3, 5, 6, 2, 4, 3, 4, 5, 4, 5, 4, 3, 4, 6], {
		type: 'line',
		height: '100',
		width: '300',
		lineColor: '#6964f7',
		fillColor: 'rgba(105, 100, 247, 0.1)',
		lineWidth: 1,
		spotColor: '#6964f7',
		minSpotColor: '#6964f7'
	});
	/* sparkline_bar end */
} )( jQuery );	

$('.data-table-example').DataTable();
