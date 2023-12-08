
function showGraphics(data) {
    var newData = data
    var stringData = JSON.stringify(newData['shortlog']);
    var values = Object.keys(newData['shortlog']).map(function(key){
        return Number(newData['shortlog'][key]);
    });
    console.log(values);
    var dataset = values
    var chartWidth = 240
    var chartHeight = 120
    var padding = 20
    var heightScalingFactor = chartHeight / getMax(dataset)

    var svg = d3
        .select('#map-container')
        .append('svg')
        .attr('width', chartWidth)
        .attr('height', chartHeight)

    svg.selectAll('rect')
        .data(dataset)
        .enter()
        .append('rect')
        .attr('x', function (value, index) {
            return (index * (chartWidth / dataset.length)) + padding
        })
        .attr('y', function (value, index) {
            return chartHeight - (value * heightScalingFactor)
        })
        .attr('width', (chartWidth / dataset.length) - padding)
        .attr('height', function (value, index) {
            return value * heightScalingFactor
        })
        .attr('fill', 'pink')

}

function getMax(collection) {
    var max = 0
    collection.forEach(function (element) {
        max = element > max ? element : max
    })
    return max
}