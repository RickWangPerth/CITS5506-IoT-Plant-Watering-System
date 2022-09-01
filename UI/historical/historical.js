'use strict'
$(window).on('load', () => {
    const margin = 10;
    const width = 500 - 2 * margin;
    const height = 150 - 2 * margin;
    var barPadding = 3;
    var dataset = [ 5, 10, 13, 19, 21, 25, 22, 18, 15, 13,
        11, 12, 15, 20, 18, 17, 16, 18, 23, 25 ];
    var svg = d3.select("body")
        .append("svg")
        .attr("width", width)
        .attr("height", height);

    svg.selectAll("rect")
        .data(dataset)
        .enter()
        .append("rect")
        .attr("x", function(d, i) {
            return i * (width / dataset.length);
        })
        .attr("y", function(d){
            return height - (d * 4);
        })
        .attr("width", width / dataset.length - barPadding)
        .attr("height", function(d) {
            return d*10;
        })
        .attr("fill", function(d) {
            return "rgb(0, 0, " + (d * 10) + ")";
        });

    svg.selectAll("text")
        .data(dataset)
        .enter()
        .append("text")
        .text(function(d) {
            return d;
        })
        .attr("x", function(d, i) {
            return i * (width / dataset.length) + (width / dataset.length - barPadding) / 2;
        })
        .attr("y", function(d) {
            return height - (d * 4) + 15;
        })
        .attr("font-family", "sans-serif")
        .attr("font-size", "11px")
        .attr("fill", "white")
        .attr("text-anchor", "middle");
})