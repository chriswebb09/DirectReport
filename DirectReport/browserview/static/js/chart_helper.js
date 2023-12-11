
function showGraphics(data) {
    const newData = data
    const stringData = JSON.stringify(newData['broad_categories']);
    const values = Object.keys(newData['broad_categories']).map(function (key) {
        return [key, Number(newData['broad_categories'][key])]
    });

    const chartWidth = 400
    const chartHeight = 300
    const padding = 35
    var data = values
    const heightScalingFactor = chartHeight / 67
    var container = d3.select('#map-container')
        .append('svg')
        .attr('width', chartWidth)
        .attr('height', chartHeight)

    var svg = d3.select("svg")
    var groups = svg.selectAll(".groups")
        .data(data)
        .enter()
        .append("g")
        .attr("class", "gbar");

    groups.append("rect")
        .attr('x', function (value, index) {
            if (index === 0) {
                return 0
            } else {
                return (index * (chartWidth / data.length))
            }
        })
        .attr('y', function (value, index) {
            return (chartHeight - 18) - (value[1] * 20)
        })
        .attr("width", function (value, index) {
            return (chartWidth / data.length) - padding
        })
        .attr("height", function (value, index) {
            return value[1] * 20
        })
        .attr("fill", "teal");

    groups.append("text")
        .attr('x', function (value, index) {
            if (index == 0) {
                return 0
            } else {
                return (index * (chartWidth / data.length))
            }

        })
        .attr('y', function (value, index) {
            return (chartHeight + 5)
        })
        .attr("dy", "-1em")
        .style("font-size", "11px")
        .style("text-anchor", "center")
        .text(function (value, index) {
            return value[0].split("_")[0].slice(0, 8)
        })
}
function getMax(collection) {
    var max = 0
    collection.forEach(function (element) {
        max = element > max ? element : max
    })
    return max
}

  // function wrap(text, width) {
  //       text.each(function() {
  //           let text = d3.select(this),
  //               words = text.text().split(/\s+/).reverse(),
  //               word,
  //               line = [],
  //               lineNumber = 0,
  //               lineHeight = 1.1, // ems
  //               x = text.attr("x"),
  //               y = text.attr("y"),
  //               dy = 1.1,
  //               tspan = text.text(null).append("tspan").attr("x", x).attr("y", y).attr("dy", dy + "em");
  //           while (word = words.pop()) {
  //               line.push(word);
  //               tspan.text(line.join(" "));
  //               if (tspan.node().getComputedTextLength() > width) {
  //                   line.pop();
  //                   tspan.text(line.join(" "));
  //                   line = [word];
  //                   tspan = text.append("tspan").attr("x", x).attr("y", y).attr("dy", ++lineNumber * lineHeight + dy + "em").text(word);
  //               }
  //           }
  //       });
  //   }