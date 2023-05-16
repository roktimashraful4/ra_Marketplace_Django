$(function(e){
  'use strict'
 /* chartjs (#sales-status) */
 

	var myCanvas = document.getElementById("sales-status");
	myCanvas.height="355";
    var myChart = new Chart( myCanvas, {
		type: 'line',
		data: {
			labels: ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021'],
			datasets: [{
				label: 'Course Visit',
				data: [100, 210, 180, 354,  270, 140, 220, 356, 256, 350, 280, 230, 410],
				backgroundColor: 'rgba(105, 100, 247, .1)',
				borderWidth: 2,
				borderColor: '#6964f7',
				hoverBorderColor: '#6964f7',
				borderDash: [6,3],
			}, {

			    label: 'Course Sale',
				data: [200, 330, 150, 170, 380, 250, 180, 435, 375, 238, 354, 454, 230,],
				backgroundColor: 'rgba(105, 100, 247, .05)',
				borderWidth: 2,
				borderColor: 'rgba(105, 100, 247, 0.15) ',
				hoverBorderColor: 'rgba(105, 100, 247, 0.15) ',
			}
		  ]
		},
		options: {
			responsive: true,
			maintainAspectRatio: false,
			layout: {
				padding: {
					left: 0,
					right: 0,
					top: 0,
					bottom: 0
				}
			},
			tooltips: {
				enabled: false,
			},
			scales: {
				yAxes: [{
					gridLines: {
						display: true,
						drawBorder: true,
						zeroLineColor: 'rgba(142, 156, 173,0.1)',
						color: "rgba(142, 156, 173,0.1)",
					},
					scaleLabel: {
						display: true,
					},
					ticks: {
						beginAtZero: true,
						stepSize: 100,
						max: 500,
						fontColor: "#8492a6",
						fontFamily: 'Poppins',
					},
				}],
				xAxes: [{
					ticks: {
						beginAtZero: true,
						fontColor: "#8492a6",
						fontFamily: 'Poppins',
					},
					gridLines: {
						color: "rgba(142, 156, 173,0.1)",
						display: true
					},

				}]
			},
			legend: {
				display: false
			},
			elements: {
				point: {
					radius: 0
				},
				line: {
					tension: 0.3
				}
			}
		}
	});


});
$('.data-table-example').DataTable();
