$(function(e){
  'use strict'


  var chartdata = [
    {
      name: 'Total Visits',
      type: 'bar',
      data: [10, 15, 9, 18, 10, 15, 22, 18, 10, 15, 22, 18],
      barMaxWidth: 12,
      itemStyle: {
        emphasis: {
            barBorderRadius: [50, 50]
        },
        normal: {
            barBorderRadius: [50, 50, 0 ,0 ]
        }
    }
    },
    {
      name: 'Total Joined',
      type: 'bar',
      data: [10, 14, 10, 15, 9, 25, 16, 15, 9, 25, 16,25],
      barMaxWidth: 12,
      itemStyle: {
        emphasis: {
            barBorderRadius: [50, 50]
        },
        normal: {
            barBorderRadius: [50, 50, 0 ,0 ]
        }
    }
    }
  ];

  var chart = document.getElementById('echart1');
  var barChart = echarts.init(chart);

  var option = {
    grid: {
      top: '6',
      right: '0',
      bottom: '20',
      left: '25',
    },
    xAxis: {
      data: [ 'Jan', 'Feb' , 'Mar', 'Apr' ,'May', 'Jun' , 'Jul' , 'Aug' ,'Sep' ,'Oct' ,'Nov' ,'Dec'],
      axisLine: {
        lineStyle: {
          color: 'rgba(227, 237, 252,0.5)'
        }
      },
      axisLabel: {
        fontSize: 12,
        color: '#9e9db5'
      }
    },
	tooltip: {
		show: true,
		showContent: true,
		alwaysShowContent: true,
		triggerOn: 'mousemove',
		trigger: 'axis',
		axisPointer:
		{
			label: {
				show: false,
			}
		}

	},
    yAxis: {
      splitLine: {
        lineStyle: {
          color: 'rgba(227, 237, 252,0.5)'
        }
      },
      axisLine: {
        lineStyle: {
          color: 'rgba(227, 237, 252,0.5)'
        }
      },
      axisLabel: {
        fontSize: 10,
        color: '#a7b4c9'
      }
    },
    series: chartdata,
    color:[ '#6964f7 ', '#ef5050 ',],
	barMaxWidth: 10
	
  };

  barChart.setOption(option);


});
/*----- Employees ------*/
var options = {
  series: [25, 25,15,20,15],
  chart: {
    height:320,
    type: 'donut',
  },
  dataLabels: {
    enabled: false
  },
  legend: {
    show: true,
    position:'bottom',
    margin:{
      top:50,
    }
   
  },
   stroke: {
    show: true,
    lineCap: "round",
    width:0
  },
  plotOptions: {
  pie: {
    donut: {
      size: '80%',
      background: 'transparent',
      labels: {
        show: true,
        name: {
          show: true,
          fontSize: '29px',
          color:'#6c6f9a',
          offsetY: -10
        },
        value: {
          show: true,
          fontSize: '26px',
          color: undefined,
          offsetY: 16,
          formatter: function (val) {
            return val + "%"
          }
        },
        total: {
          show: true,
          showAlways: false,
          label: 'Total',
          fontSize: '22px',
          fontWeight: 600,
          color: '#373d3f',
          }

      }
    }
  }
  },
  responsive: [{
    options: {
      legend: {
        show: true,
      }
    }
  }],
  labels: ["IE","Chrome" ,"Opera" ,"Firefox" ,"Edge"],
  colors: ['#02c3ee', '#425bd6','#ffe15b', '#ff1a1a', '#21c44c'],
};
var chart = new ApexCharts(document.querySelector("#browser"), options);
chart.render();


$('.data-table-example').DataTable();



