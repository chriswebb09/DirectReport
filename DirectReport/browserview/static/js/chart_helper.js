

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


function showGraphics(data, divtag) {

    const newData = data
    const dict = sortOnKeys(newData['pull_requests']);
    const stringData = JSON.stringify(dict);

    const values = Object.keys(dict).map(function (key) {
        return [key, Number(newData['pull_requests'][key])]
    });

    const chartWidth = 350
    const chartHeight = 300
    const padding = 25

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
            return (chartHeight - 18) - (value[1] * 20)
        })
        .attr("width", function (value, index) {
            return (chartWidth / data.length) - padding
        })
        .attr("height", function (value, index) {
            return value[1] * 20
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
            return (chartHeight + 5)
        })
        .attr("dy", "-1em")
        .style("font-size", "11px")
        .style("text-anchor", "center")
        .text(function (value, index) {
            return value[0].split("_")[0].slice(0, 6)
        })
}

function showGraphics2(data, divtag) {

    const newData = data
    const stringData = JSON.stringify(newData['commit_nums']);

    const values = Object.keys(newData['commit_nums']).map(function (key) {
        return [key, Number(newData['commit_nums'][key])]
    });
    // const stringData = JSON.stringify(newData['broad_categories']);
    //
    // const values = Object.keys(newData['broad_categories']).map(function (key) {
    //     return [key, Number(newData['broad_categories'][key])]
    // });

    const chartWidth = 350
    const chartHeight = 300
    const padding = 25

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
            return (chartHeight - 18) - (value[1] * 20)
        })
        .attr("width", function (value, index) {
            return (chartWidth / data.length) - padding
        })
        .attr("height", function (value, index) {
            return value[1] * 20
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
            return (chartHeight + 5)
        })
        .attr("dy", "-1em")
        .style("font-size", "11px")
        .style("text-anchor", "center")
        .text(function (value, index) {
            return value[0].split("_")[0].slice(0, 6)
        })
}

function showGraphics3(data, divtag) {

    const newData = data

    const stringData = JSON.stringify(newData['broad_categories']);

    const values = Object.keys(newData['broad_categories']).map(function (key) {
        return [key, Number(newData['broad_categories'][key])]
    });

    const chartWidth = 350
    const chartHeight = 300
    const padding = 25

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
            return value[0].split("_")[0].slice(0, 6)
        })
}
function getMax(collection) {
    var max = 0
    collection.forEach(function (element) {
        max = element > max ? element : max
    })
    return max
}