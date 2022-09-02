'use strict'
$(window).on('load', () => {
    const margin = 10;
    const width = 500 - 2 * margin;
    const height = 150 - 2 * margin;
    var barPadding = 3;
    var moisDataset = [ 5, 10, 13, 19, 21, 25, 22, 18, 15, 13,
        11, 12, 15, 20, 18, 17, 16, 18, 23, 25 ];
    var tempDataset = [ 5, 10, 13, 19, 21, 25, 22, 18, 15, 13,
        11, 12, 15, 20, 18, 17, 16, 18, 23, 25 ];
    var lightDataset = [ 5, 10, 13, 19, 21, 25, 22, 18, 15, 13,
        11, 12, 15, 20, 18, 17, 16, 18, 23, 25 ];

    var moissvg = d3.select("#moisData")
        .append("svg")
        .attr("width", width)
        .attr("height", height);

    moissvg.selectAll("rect")
        .data(moisDataset)
        .enter()
        .append("rect")
        .attr("x", function(d, i) {
            return i * (width / moisDataset.length);
        })
        .attr("y", function(d){
            return height - (d * 4);
        })
        .attr("width", width / moisDataset.length - barPadding)
        .attr("height", function(d) {
            return d*10;
        })
        .attr("fill", function(d) {
            return "rgb(0, 0, " + (d * 10) + ")";
        });

    moissvg.selectAll("text")
        .data(moisDataset)
        .enter()
        .append("text")
        .text(function(d) {
            return d;
        })
        .attr("x", function(d, i) {
            return i * (width / moisDataset.length) + (width / moisDataset.length - barPadding) / 2;
        })
        .attr("y", function(d) {
            return height - (d * 4) + 15;
        })
        .attr("font-family", "sans-serif")
        .attr("font-size", "11px")
        .attr("fill", "white")
        .attr("text-anchor", "middle");

    var tempsvg = d3.select("#tempData")
        .append("svg")
        .attr("width", width)
        .attr("height", height);

    tempsvg.selectAll("rect")
        .data(tempDataset)
        .enter()
        .append("rect")
        .attr("x", function(d, i) {
            return i * (width / tempDataset.length);
        })
        .attr("y", function(d){
            return height - (d * 4);
        })
        .attr("width", width / tempDataset.length - barPadding)
        .attr("height", function(d) {
            return d*10;
        })
        .attr("fill", function(d) {
            return "rgb(0, 0, " + (d * 10) + ")";
        });

    tempsvg.selectAll("text")
        .data(tempDataset)
        .enter()
        .append("text")
        .text(function(d) {
            return d;
        })
        .attr("x", function(d, i) {
            return i * (width / tempDataset.length) + (width / tempDataset.length - barPadding) / 2;
        })
        .attr("y", function(d) {
            return height - (d * 4) + 15;
        })
        .attr("font-family", "sans-serif")
        .attr("font-size", "11px")
        .attr("fill", "white")
        .attr("text-anchor", "middle");
})