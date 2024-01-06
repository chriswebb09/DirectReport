

function sortOnKeys(dict) {

    var sorted = [];
    for(var key in dict) {
        sorted[sorted.length] = key;
    }
    sorted.sort();

    var tempDict = {};
    for(var i = 0; i < sorted.length; i++) {
        tempDict[sorted[i]] = dict[sorted[i]];
    }

    return tempDict;
}


function showAllGraphics(data, divTag, divTag2, divTag3) {
    showGraphics(data,  divTag);
    showGraphics2(data, divTag2);
    showGraphics3(data, divTag3);
}
function showGraphics(data, divtag) {

    const newData = data
    const dict = sortOnKeys(newData['pull_requests']);
    const stringData = JSON.stringify(dict);

    const values = Object.keys(dict).map(function (key) {
        return [key, Number(newData['pull_requests'][key])]
    });

    const chartWidth = 350
    const chartHeight = 300
    const padding = 20

    var data = values
    const heightScalingFactor = chartHeight / 67

    var container = d3.select(divtag)
        .append('svg')
        .attr('width', chartWidth)
        .attr('height', chartHeight)

    var svg = d3.select(divtag).select("svg")
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
            return (chartHeight - 30) - (value[1] * 5)
        })
        .attr("width", function (value, index) {
            return (chartWidth / data.length) - padding
        })
        .attr("height", function (value, index) {
            return value[1] * 5
        })
        .attr("fill", "blueviolet");

    groups.append("text")
        .attr('x', function (value, index) {
            if (index == 0) {
                return 0
            } else {
                return (index * (chartWidth / data.length))
            }

        })
        .attr('y', function (value, index) {
            return (chartHeight - 8)
        })
        .attr("dy", "-1em")
        .style("font-size", "10px")
        .style("text-anchor", "center")
        .text(function (value, index) {
            print(value[0].split("_")[0].slice(0, 8))
            return value[0].split("_")[0].slice(0, 8)
        })
}

function showGraphics2(data, divtag) {

    const newData = data
    const stringData = JSON.stringify(newData['commit_nums']);

    const values = Object.keys(newData['commit_nums']).map(function (key) {
        return [key, Number(newData['commit_nums'][key])]
    });

    const chartWidth = 350
    const chartHeight = 300
    const padding = 20

    var data = values
    const heightScalingFactor = chartHeight / 67

    var container = d3.select(divtag)
        .append('svg')
        .attr('width', chartWidth)
        .attr('height', chartHeight)

    var svg = d3.select(divtag).select("svg")
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
            return (chartHeight - 30) - (value[1] * 10)
        })
        .attr("width", function (value, index) {
            return (chartWidth / data.length) - padding
        })
        .attr("height", function (value, index) {
            // console.log(value[1] * 20)
            return (value[1] * 10) - 5
        })
        .attr("fill", "steelblue");

    groups.append("text")
        .attr('x', function (value, index) {
            if (index == 0) {
                return 0
            } else {
                return (index * (chartWidth / data.length))
            }

        })
        .attr('y', function (value, index) {
            return (chartHeight - 8)
        })
        .attr("dy", ".35em")
        .style("font-size", "8px")
        .style("text-anchor", "center")
        .text(function (value, index) {
            return value[0].slice(0, 8)
        })
        .call(wrap, 5);
}






function showGraphics3(data, divtag) {

    const newData = data

    const stringData = JSON.stringify(newData['broad_categories']);

    const values = Object.keys(newData['broad_categories']).map(function (key) {
        return [key, Number(newData['broad_categories'][key])]
    });

    const chartWidth = 350
    const chartHeight = 300
    const padding = 20

    var data = values
    const heightScalingFactor = chartHeight / 67

    var container = d3.select(divtag)
        .append('svg')
        .attr('width', chartWidth)
        .attr('height', chartHeight)


    var svg = d3.select(divtag).select("svg")
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
                return (index * (chartWidth / data.length)) + padding
            }
        })
        .attr('y', function (value, index) {
            return (chartHeight - 30) - (value[1] * 10)
        })
        .attr("width", function (value, index) {
            return (chartWidth / data.length) - padding
        })
        .attr("height", function (value, index) {
            return value[1] * 10
        })
        .attr("fill", "teal");

    groups.append("text")
        .attr('x', function (value, index) {
            if (index == 0) {
                return 0
            } else {
                return (index * (chartWidth / data.length) + padding)
            }

        })
        .attr('y', function (value, index) {
            return (chartHeight + 8)
        })
        .attr("dy", "-1em")
        .style("font-size", "8px")
        .style("text-anchor", "center")
        .text(function (value, index) {
            return value[0].split("_")[0].slice(0, 6) + ' ' + value[0].split("_")[1]
        }).call(wrap, 5);

}


function chart4(data) {

    const newData = data

    const stringData = JSON.stringify(newData['broad_categories']);

    const values = Object.keys(newData['broad_categories']).map(function (key) {
        return [key, Number(newData['broad_categories'][key])]
    });

    const width = 928;
    const height = Math.min(width, 500);

    // Create the color scale.
    const color = d3.scaleOrdinal()
        .domain(data.map(d => d.name))
        .range(d3.quantize(t => d3.interpolateSpectral(t * 0.8 + 0.1), data.length).reverse())

    // Create the pie layout and arc generator.
    const pie = d3.pie()
        .sort(null)
        .value(d => d.value);

    const arc = d3.arc()
        .innerRadius(0)
        .outerRadius(Math.min(width, height) / 2 - 1);

    const labelRadius = arc.outerRadius()() * 0.8;

    // A separate arc generator for labels.
    const arcLabel = d3.arc()
        .innerRadius(labelRadius)
        .outerRadius(labelRadius);

    const arcs = pie(data);

    // Create the SVG container.
    const svg = d3.create("svg")
        .attr("width", width)
        .attr("height", height)
        .attr("viewBox", [-width / 2, -height / 2, width, height])
        .attr("style", "max-width: 100%; height: auto; font: 10px sans-serif;");

    // Add a sector path for each value.
    svg.append("g")
        .attr("stroke", "white")
        .selectAll()
        .data(arcs)
        .join("path")
        .attr("fill", d => color(d.data.name))
        .attr("d", arc)
        .append("title")
        .text(d => `${d.data.name}: ${d.data.value.toLocaleString("en-US")}`);

    // Create a new arc generator to place a label close to the edge.
    // The label shows the value if there is enough room.
    svg.append("g")
        .attr("text-anchor", "middle")
        .selectAll()
        .data(arcs)
        .join("text")
        .attr("transform", d => `translate(${arcLabel.centroid(d)})`)
        .call(text => text.append("tspan")
            .attr("y", "-0.4em")
            .attr("font-weight", "bold")
            .text(d => d.data.name))
        .call(text => text.filter(d => (d.endAngle - d.startAngle) > 0.25).append("tspan")
            .attr("x", 0)
            .attr("y", "0.7em")
            .attr("fill-opacity", 0.7)
            .text(d => d.data.value.toLocaleString("en-US")));
    return svg.node();
}
function getMax(collection) {
    var max = 0
    collection.forEach(function (element) {
        max = element > max ? element : max
    })
    return max
}

function wrap(text, width) {
    text.each(function() {
        var text = d3.select(this),
            words = text.text().split(/\s+/).reverse(),
            word,
            line = [],
            lineNumber = 0,
            y = text.attr("y"),
            xValue = text.attr("x"),
            dy = parseFloat(text.attr("dy")),
            lineHeight = 1.1, // ems
            tspan = text.text(null).append("tspan").attr("x", function(d) {
                return xValue
            }).attr("y", y).attr("dy", dy + "em");
        while (word = words.pop()) {
            line.push(word);
            tspan.text(line.join(" "));
            var textWidth = tspan.node().getComputedTextLength();
            if (tspan.node().getComputedTextLength() > width) {
                line.pop();
                tspan.text(line.join(" "));
                line = [word];
                ++lineNumber;
                tspan = text.append("tspan").attr("x", function(d) {
                    return xValue
                }).attr("y", (y - 30)).attr("dy", lineNumber * lineHeight + dy + "em")
                    .style("font-size", "10px")
                    .style("text-anchor", "center")
                    .text(word);
            }
        }
    });
}