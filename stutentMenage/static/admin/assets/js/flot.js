/*---- placeholder1----*/
$(function(e) {
		var sin = [], cos = [];
		for (var i = 0; i < 14; i += 0.1) {
			sin.push([i, Math.sin(i)]);
			cos.push([i, Math.cos(i)]);
		}

		plot = $.plot("#placeholder1", [
			{ data: sin },
			{ data: cos}

		], {
			series: {
				lines: {
					show: true
				}
			},
			 lines: {
				show: true,
				fill: true,
				fillColor: { colors: [{ opacity: 0.7 }, { opacity: 0.7}] }
			},
			crosshair: {
				mode: "x"
			},
			grid: {
				hoverable: false,
				autoHighlight: false,
				borderColor: "#e3edfc",
				verticalLines:false,
				horizontalLines:false
			},
			colors: ['#6964f7', '#ef5050'],
			yaxis: {
				min: -1.2,
				max: 1.2,
				tickLength: 0
			},
			xaxis: {
			  tickLength: 0
			}
		});
		/*---- placeholder2----*/

		var sin = [],
			cos = [];

		for (var i = 0; i < 14; i += 0.5) {
			sin.push([i, Math.sin(i)]);
			cos.push([i, Math.cos(i)]);
		}

		var plot = $.plot("#placeholder2", [
			{ data: sin, label: "data1"},
			{ data: cos, label: "data2"}
		], {
			series: {
				lines: {
					show: true
				},
				points: {
					show: true
				}
			},
			grid: {
				hoverable: true,
				clickable: true,
				borderColor: "#e3edfc",
				verticalLines:false,
				horizontalLines:false
			},
			colors: ['#6964f7', '#ef5050'],
			yaxis: {
				min: -1.2,
				max: 1.2,
				tickLength: 0
			},
			xaxis: {
			  tickLength: 0
			}
		});

		/*---- flotBar2----*/

		$.plot('#flotBar2', [{
			data: [
				[0, 10],
				[2, 15],
				[4, 25],
				[6, 22],
				[8, 18],
				[10, 27],
				[12, 34],
				[14, 35],
				[16, 48],
			],
			bars: {
				show: true,
				lineWidth: 0,
				fillColor: '#6964f7',
				barWidth: .8
			}
		}, {
			data: [
				[1, 8],
				[3, 10],
				[5, 24],
				[7, 17],
				[9, 23],
				[11, 24],
				[13, 30],
				[15, 16]
			],
			bars: {
				show: true,
				lineWidth: 0,
				fillColor: '#ef5d5d',
				barWidth: .8
			}
		}], {
			grid: {
				borderWidth: 1,
				borderColor: 'rgb(223,224,239)'
			},
			yaxis: {
				tickColor: 'rgb(223,224,239)',
				font: {
					color: '#77778e',
					size: 10
				}
			},
			xaxis: {
				tickColor: 'rgb(223,224,239)',
				font: {
					color: '#77778e',
					size: 10
				}
			}
		});
		var newCust = [
			[0, 10],
			[1, 15],
			[2, 25],
			[3, 22],
			[4, 18],
			[5, 27],
			[6, 34],
		];
		var retCust = [
			[0, 8],
			[1, 17],
			[2, 28],
			[3, 20],
			[4, 16],
			[5, 24],
			[6, 36]
		];

		/*---- placeholder4----*/

		// We use an inline data source in the example, usually data would
		// be fetched from a server

		var data = [],
			totalPoints = 300;

		function getRandomData() {

			if (data.length > 0)
				data = data.slice(1);

			// Do a random walk

			while (data.length < totalPoints) {

				var prev = data.length > 0 ? data[data.length - 1] : 50,
					y = prev + Math.random() * 10 - 5;

				if (y < 0) {
					y = 0;
				} else if (y > 100) {
					y = 100;
				}

				data.push(y);
			}

			var res = [];
			for (var i = 0; i < data.length; ++i) {
				res.push([i, data[i]])
			}

			return res;
		}

		var updateInterval = 30;
		$("#updateInterval").val(updateInterval).change(function () {
			var v = $(this).val();
			if (v && !isNaN(+v)) {
				updateInterval = +v;
				if (updateInterval < 1) {
					updateInterval = 1;
				} else if (updateInterval > 2000) {
					updateInterval = 2000;
				}
				$(this).val("" + updateInterval);
			}
		});

		var plot = $.plot("#placeholder4", [ getRandomData() ], {
			series: {
				shadowSize: 0	// Drawing is faster without shadows
			},
			grid: {
				borderColor: "#e3edfc",
			},
			colors: ["#6964f7"],
			yaxis: {
				min: 0,
				max: 100,
				tickLength: 0
			},
			xaxis: {
				tickLength: 0,
				show: false
			}
		});

		function update() {
			plot.setData([getRandomData()]);
			plot.draw();
			setTimeout(update, updateInterval);
		}

		update();

/*---- placeholder5----*/

		var d1 = [];
		for (var i = 0; i < 14; i += 0.5) {
			d1.push([i, Math.sin(i)]);
		}

		var d2 = [[0, 3], [4, 8], [8, 5], [9, 13]];

		var d3 = [];
		for (var i = 0; i < 14; i += 0.5) {
			d3.push([i, Math.cos(i)]);
		}

		var d4 = [];
		for (var i = 0; i < 14; i += 0.1) {
			d4.push([i, Math.sqrt(i * 10)]);
		}

		var d5 = [];
		for (var i = 0; i < 14; i += 0.5) {
			d5.push([i, Math.sqrt(i)]);
		}

		var d6 = [];
		for (var i = 0; i < 14; i += 0.5 + Math.random()) {
			d6.push([i, Math.sqrt(2*i + Math.sin(i) + 5)]);
		}

		$.plot("#placeholder5", [{

			data: d1,
			lines: { show: true, fill: true }
		}, {
			data: d2,
			bars: { show: true }
		}, {
			data: d3,
			points: { show: true }
		}, {
			data: d4,
			lines: { show: true }
		}, {
			data: d5,
			lines: { show: true },
			points: { show: true }
		}, {
			data: d6,
			lines: { show: true, steps: true }
		}]);
		
		/*---- placeholder6----*/

		var d1 = [];
		for (var i = 0; i <= 10; i += 1) {
			d1.push([i, parseInt(Math.random() * 30)]);
		}

		var d2 = [];
		for (var i = 0; i <= 10; i += 1) {
			d2.push([i, parseInt(Math.random() * 30)]);
		}

		var d3 = [];
		for (var i = 0; i <= 10; i += 1) {
			d3.push([i, parseInt(Math.random() * 30)]);
		}

		var stack = 0,
			bars = true,
			lines = false,
			steps = false;

		function plotWithOptions() {
			$.plot("#placeholder6", [ d1, d2, d3 ], {
				series: {

					stack: stack,
					lines: {
						show: lines,
						fill: true,
						steps: steps
					},
					bars: {
						show: bars,
						barWidth: 0.6
					}
				},
				grid: {
					borderColor: "#e3edfc",
				},
				colors: ['#6964f7', '#ef5050'],
				yaxis: {
					tickLength: 0
				},
				xaxis: {
					tickLength: 0,
					show: false
				}
			});
		}

		plotWithOptions();
		
		
		$(".stackControls button").click(function (e) {
			e.preventDefault();
			stack = $(this).text() == "With stacking" ? true : null;
			plotWithOptions();
		});

		$(".graphControls button").click(function (e) {
			e.preventDefault();
			bars = $(this).text().indexOf("Bars") != -1;
			lines = $(this).text().indexOf("Lines") != -1;
			steps = $(this).text().indexOf("steps") != -1;
			plotWithOptions();
		});


	});
	$(function() {
		var data = [],
			series = Math.floor(Math.random() * 4) + 3;

		for (var i = 0; i < series; i++) {
			data[i] = {
				label: "Series" + (i + 1),
				data: Math.floor(Math.random() * 100) + 1
			}
		}

		var placeholder = $("#placeholder");

		$("#example-1").click(function() {

			placeholder.unbind();

			$("#title").text("Default pie chart");
			$("#description").text("The default pie chart with no options set.");

			$.plot(placeholder, data, {
				series: {
					pie: {
						show: true
					}

				},
				colors: ['#6964f7', '#ef5050', '#5e5baa', '#21cb95', '#f44336'],

			});

		});

		$("#example-2").click(function() {

			placeholder.unbind();

			$("#title").text("Default without legend");
			$("#description").text("The default pie chart when the legend is disabled. Since the labels would normally be outside the container, the chart is resized to fit.");

			$.plot(placeholder, data, {
				series: {
					pie: {
						show: true
					}
				},
				colors: ['#6964f7', '#ef5050', '#5e5baa', '#21cb95', '#f44336'],
				legend: {
					show: false
				}
			});

		});

		$("#example-3").click(function() {

			placeholder.unbind();

			$("#title").text("Custom Label Formatter");
			$("#description").text("Added a semi-transparent background to the labels and a custom labelFormatter function.");

			$.plot(placeholder, data, {
				series: {
					pie: {
						show: true,
						radius: 1,
						label: {
							show: true,
							radius: 1,
							formatter: labelFormatter,
							background: {
								opacity: 0.8
							}
						}
					}
				},
				colors: ['#6964f7', '#ef5050', '#5e5baa', '#21cb95', '#f44336'],
				legend: {
					show: false
				}
			});
		});

		$("#example-4").click(function() {

			placeholder.unbind();

			$("#title").text("Label Radius");
			$("#description").text("Slightly more transparent label backgrounds and adjusted the radius values to place them within the pie.");

			$.plot(placeholder, data, {
				series: {
					pie: {
						show: true,
						radius: 1,
						label: {
							show: true,
							radius: 3/4,
							formatter: labelFormatter,
							background: {
								opacity: 0.5
							}
						}
					}
				},
				colors: ['#6964f7', '#ef5050', '#5e5baa', '#21cb95', '#f44336'],
				legend: {
					show: false
				}
			});
		});

		$("#example-5").click(function() {

			placeholder.unbind();

			$("#title").text("Label Styles #1");
			$("#description").text("Semi-transparent, black-colored label background.");

			$.plot(placeholder, data, {
				series: {
					pie: {
						show: true,
						radius: 1,
						label: {
							show: true,
							radius: 3/4,
							formatter: labelFormatter,
							background: {
								opacity: 0.5,
								color: "#000"
							}
						}
					}
				},
				colors: ['#6964f7', '#ef5050', '#5e5baa', '#21cb95', '#f44336'],
				legend: {
					show: false
				}
			});
		});

		$("#example-6").click(function() {

			placeholder.unbind();

			$("#title").text("Label Styles #2");
			$("#description").text("Semi-transparent, black-colored label background placed at pie edge.");

			$.plot(placeholder, data, {
				series: {
					pie: {
						show: true,
						radius: 3/4,
						label: {
							show: true,
							radius: 3/4,
							formatter: labelFormatter,
							background: {
								opacity: 0.5,
								color: "#000"
							}
						}
					}
				},
				colors: ['#6964f7', '#ef5050', '#5e5baa', '#21cb95', '#f44336'],
				legend: {
					show: false
				}
			});

		});

		$("#example-7").click(function() {

			placeholder.unbind();

			$("#title").text("Hidden Labels");
			$("#description").text("Labels can be hidden if the slice is less than a given percentage of the pie (10% in this case).");

			$.plot(placeholder, data, {
				series: {
					pie: {
						show: true,
						radius: 1,
						label: {
							show: true,
							radius: 2/3,
							formatter: labelFormatter,
							threshold: 0.1
						}
					}
				},
				colors: ['#6964f7', '#ef5050', '#5e5baa', '#21cb95', '#f44336'],
				legend: {
					show: false
				}
			});

		});

		$("#example-8").click(function() {

			placeholder.unbind();

			$("#title").text("Combined Slice");
			$("#description").text("Multiple slices less than a given percentage (5% in this case) of the pie can be combined into a single, larger slice.");

			$.plot(placeholder, data, {
				series: {
					pie: {
						show: true,
						combine: {
							color: "#999",
							threshold: 0.05
						}
					}
				},
				colors: ['#6964f7', '#ef5050', '#5e5baa', '#21cb95', '#f44336'],
				legend: {
					show: false
				}
			});

		});

		$("#example-9").click(function() {

			placeholder.unbind();

			$("#title").text("Rectangular Pie");
			$("#description").text("The radius can also be set to a specific size (even larger than the container itself).");

			$.plot(placeholder, data, {
				series: {
					pie: {
						show: true,
						radius: 500,
						label: {
							show: true,
							formatter: labelFormatter,
							threshold: 0.1
						}
					}
				},
				colors: ['#6964f7', '#ef5050', '#5e5baa', '#21cb95', '#f44336'],
				legend: {
					show: false
				}
			});

		});

		$("#example-10").click(function() {

			placeholder.unbind();

			$("#title").text("Tilted Pie");
			$("#description").text("The pie can be tilted at an angle.");

			$.plot(placeholder, data, {
				series: {
					pie: {
						show: true,
						radius: 1,
						tilt: 0.5,
						label: {
							show: true,
							radius: 1,
							formatter: labelFormatter,
							background: {
								opacity: 0.8
							}
						},
						combine: {
							color: "#999",
							threshold: 0.1
						}
					}
				},
				colors: ['#6964f7', '#ef5050', '#5e5baa', '#21cb95', '#f44336'],
				legend: {
					show: false
				}
			});

		});

		$("#example-11").click(function() {

			placeholder.unbind();

			$("#title").text("Donut Hole");
			$("#description").text("A donut hole can be added.");

			$.plot(placeholder, data, {
				series: {
					pie: {
						innerRadius: 0.5,
						show: true
					}
				}
			});


		});
		$("#example-1").click();

	});

	// A custom label formatter used by several of the plots

	function labelFormatter(label, series) {
		return "<div style='font-size:8pt; text-align:center; padding:2px; color:white;'>" + label + "<br/>" + Math.round(series.percent) + "%</div>";
	}

	//

	function setCode(lines) {
		$("#code").text(lines.join("\n"));
	}