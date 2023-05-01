d3.csv('ue_industry.csv', data => {

    const xScales = d3.scaleLinear()
        .domain(d3.extent(data, d => +d.index))
        .range([20, 1180]);

    const yScales = d3.scaleLinear()
        .domain(d3.extent(data, d => +d.Agriculture))
        .range([580, 20]);

    let lines = d3.line()
        .x(d => xScales(d.index))
        .y(d => yScales(d.Agriculture));

    d3.select('#answer1')
        .append('path')
        .attr('d', lines(data))
        .attr('stroke', '#2e2928')

});
