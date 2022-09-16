var width = 700,
      height = 700,
      start = -0.025,
      end = 2.3,
      numSpirals = 2
      margin = {top:300,bottom:50,left:150,right:500};

    var theta = function(r) {
      return numSpirals * Math.PI * r;
    };

    // used to assign nodes color by group
    var color = d3.scaleOrdinal(d3.schemeCategory10);

    var r = d3.min([width, height]) / 2 - 110;

    var radius = d3.scaleLinear()
      .domain([start, end])
      .range([20, r]);

    var svg = d3.select("#chart").append("svg")
      .attr("width", width + margin.right + margin.left)
      .attr("height", height + margin.left + margin.right)
      .append("g")
      .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

    var points = d3.range(start, end + 0.001, (end - start) / 1000);

    var spiral = d3.radialLine()
      .curve(d3.curveCardinal)
      .angle(theta)
      .radius(radius);

    var path = svg.append("path")
      .datum(points)
      .attr("id", "spiral")
      .attr("d", spiral)
      .style("fill", "none")
      .style("stroke", "white");

    var spiralLength = path.node().getTotalLength(),
        N = 65,
        barWidth = (spiralLength / N) - 1;
    var someData = [{date: 1958, value: 11}, {date: 1959, value: 11}, {date: 1960, value: 58}, {date: 1961, value: 13}, {date: 1962, value: 3}, {date: 1963, value: 22}, {date: 1964, value: 13}, {date: 1965, value: 24}, {date: 1966, value: 19}, {date: 1967, value: 30}, {date: 1968, value: 73}, {date: 1969, value: 73}, {date: 1970, value: 21}, {date: 1971, value: 39}, {date: 1972, value: 64}, {date: 1973, value: 28}, {date: 1974, value: 54}, {date: 1975, value: 37}, {date: 1976, value: 25}, {date: 1977, value: 30}, {date: 1978, value: 61}, {date: 1979, value: 73}, {date: 1980, value: 83}, {date: 1981, value: 36}, {date: 1982, value: 40}, {date: 1983, value: 51}, {date: 1984, value: 42}, {date: 1985, value: 85}, {date: 1986, value: 68}, {date: 1987, value: 60}, {date: 1988, value: 78}, {date: 1989, value: 50}, {date: 1990, value: 30}, {date: 1991, value: 82}, {date: 1992, value: 46}, {date: 1993, value: 43}, {date: 1994, value: 83}, {date: 1995, value: 37}, {date: 1996, value: 66}, {date: 1997, value: 134}, {date: 1998, value: 134}, {date: 1999, value: 163}, {date: 2000, value: 178}, {date: 2001, value: 175}, {date: 2002, value: 240}, {date: 2003, value: 453}, {date: 2004, value: 545}, {date: 2005, value: 561}, {date: 2006, value: 496}, {date: 2007, value: 547}, {date: 2008, value: 453}, {date: 2009, value: 493}, {date: 2010, value: 514}, {date: 2011, value: 491}, {date: 2012, value: 531}, {date: 2013, value: 528}, {date: 2014, value: 494}, {date: 2015, value: 540}, {date: 2016, value: 547}, {date: 2017, value: 591}, {date: 2018, value: 551}, {date: 2019, value: 531}, {date: 2020, value: 822}, {date: 2021, value: 918}, {date: 2022, value: 2530}];
   /* for (var i = 0; i < N; i++) {
      var currentDate = new Date();
      currentDate.setDate(currentDate.getDate() + i);
      someData.push({
        date: currentDate,
        value: Math.random(),
        group: currentDate.getMonth()
      });
    } */

    var timeScale = d3.scaleTime()
      .domain(d3.extent(someData, function(d){
        return d.date;
      }))
      .range([0, spiralLength]);
    
    // yScale for the bar height
    var yScale = d3.scaleLinear()
      .domain([0, d3.max(someData, function(d){
        return d.value;
      })])
      .range([0, (r / numSpirals) + 500]);

    svg.selectAll("rect")
      .data(someData)
      .enter()
      .append("rect")
      .attr("x", function(d,i){
        
        var linePer = timeScale(d.date),
            posOnLine = path.node().getPointAtLength(linePer),
            angleOnLine = path.node().getPointAtLength(linePer - barWidth);
      
        d.linePer = linePer; // % distance are on the spiral
        d.x = posOnLine.x; // x postion on the spiral
        d.y = posOnLine.y; // y position on the spiral
        
        d.a = (Math.atan2(angleOnLine.y, angleOnLine.x) * 180 / Math.PI) - 90; //angle at the spiral position

        return d.x;
      })
      .attr("y", function(d){
        return d.y;
      })
      .attr("width", function(d){
        return barWidth;
      })
      .attr("height", function(d){
        return yScale(d.value);
      })
      .style("fill", function(d){return color((d.date)%3);})
      .style("stroke", "none")
      .attr("transform", function(d){
        return "rotate(" + d.a + "," + d.x  + "," + d.y + ")"; // rotate the bar
      });
    
    // add date labels
    var tF = d3.timeFormat("%b %Y"),
        firstInMonth = {};

    svg.selectAll("text")
      .data(someData)
      .enter()
      .append("text")
      .attr("dy", 10)
      .style("text-anchor", "start")
      .style("font", "10px arial")
      .append("textPath")
      // only add for the first of each month
      .filter(function(d){
        var sd = d.date;
        if (sd){
          sd % 4 ==0;
          return true;
        }
        return false;
      })
      .text(function(d){
        return (d.date+1);
      }) 

      // place text along spiral
      .attr("xlink:href", "#spiral")
      .style("fill", "grey")
      .attr("startOffset", function(d){
        return ((d.linePer / spiralLength) * 100) + "%";
      })


    var tooltip = d3.select("#chart")
    .append('div')
    .attr('class', 'tooltip');

    tooltip.append('div')
    .attr('class', 'date');
    tooltip.append('div')
    .attr('class', 'value');

    svg.selectAll("rect")
    .on('mouseover', function(d) {

        tooltip.select('.date').html("Year: <b>" + d.date + "</b>");
        tooltip.select('.value').html("Literature: <b>" + d.value + "<b>");

        d3.select(this)
        .style("fill","#FFFFFF")
        .style("stroke","#000000")
        .style("stroke-width","2px");

        tooltip.style('display', 'block');
        tooltip.style('opacity',2);

    })
    .on('mousemove', function(d) {
        tooltip.style('top', (d3.event.layerY + 10) + 'px')
        .style('left', (d3.event.layerX - 25) + 'px');
    })
    .on('mouseout', function(d) {
        d3.selectAll("rect")
        .style("fill", function(d){return color((d.date)%3);})
        .style("stroke", "none")

        tooltip.style('display', 'none');
        tooltip.style('opacity',0);
    });