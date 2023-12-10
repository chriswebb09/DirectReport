
function showGraphics(data) {
    const newData = data
    const stringData = JSON.stringify(newData['shortlog']);
    const values = Object.keys(newData['shortlog']).map(function(key){
        return Number(newData['shortlog'][key]);
    });
    console.log(values);
    const dataset = values
    const chartWidth = 240
    const chartHeight = 120
    const padding = 20
    const heightScalingFactor = chartHeight / getMax(dataset)

    const svg = d3
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