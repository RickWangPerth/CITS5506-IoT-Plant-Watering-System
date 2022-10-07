'use strict'
//moisData = [21,20,18,30,40,70,48,46,44]
//tempData = [25,21,23,22,22,22,25,25,23]
//lightData = [700,700,800,900,1000,1300,1500,1200,1100,1100]

$(window).on('load', () => {
    const margin = 10;
    var width = window.outerWidth / 2 - 2 * margin;
    if (window.outerWidth > 1800)
        width = 700 - 2 * margin;
    if (window.outerWidth < 400)
        width = window.outerWidth - 2*margin;
    console.log(window.outerWidth)
    var height = 180 - 2 * margin;
    var barPadding = 3;


    if (moisData.length > 0) { // If we've received sensor data
        var yScale = d3.scaleLinear()
            .domain([0,d3.max(moisData)])
            .range([0,height]);

        var moissvg = d3.select("#moisData")
            .append("svg")
            .attr("width", width)
            .attr("height", height);

        moissvg.selectAll("rect")
            .data(moisData)
            .enter()
            .append("rect")
            .attr("x", function(d, i) {
                return i * (width / moisData.length);
            })
            .attr("y", function(d){
                return height - yScale(d);
            })
            .attr("width", width / moisData.length - barPadding)
            .attr("height", function(d) {
                return  yScale(d);
            })
            .attr("fill", function(d) {
                return "rgb(0, 0, " + (d * 10) + ")";
            });

        moissvg.selectAll("text")
            .data(moisData)
            .enter()
            .append("text")
            .text(function(d) {
                return d;
            })
            .attr("x", function(d, i) {
                return i * (width / moisData.length) + (width / moisData.length - barPadding) / 2;
            })
            .attr("y", function(d) {
                return height - (d * 2) + 10;
            })
            .attr("font-family", "sans-serif")
            .attr("font-size", "11px")
            .attr("fill", "white")
            .attr("text-anchor", "middle");
    } else { // If we haven't received sensor data
        document.getElementById("moisData").innerHTML = "No data"; // Placeholder 'no data' indicator
    }
    var height = 180 - 2 * margin;
    if (tempData.length > 0) {
        var yScale = d3.scaleLinear()
            .domain([0,d3.max(tempData)])
            .range([0,height]);

        var tempsvg = d3.select("#tempData")
            .append("svg")
            .attr("width", width)
            .attr("height", height);

        tempsvg.selectAll("rect")
            .data(tempData)
            .enter()
            .append("rect")
            .attr("x", function(d, i) {
                return i * (width / tempData.length);
            })
            .attr("y", function(d){
                return height - yScale(d);
            })
            .attr("width", width / tempData.length - barPadding)
            .attr("height", function(d) {
                return yScale(d);
            })
            .attr("fill", function(d) {
                return "rgb(0, 0, " + (d * 10) + ")";
            });

        tempsvg.selectAll("text")
            .data(tempData)
            .enter()
            .append("text")
            .text(function(d) {
                return d;
            })
            .attr("x", function(d, i) {
                return i * (width / tempData.length) + (width / tempData.length - barPadding) / 2;
            })
            .attr("y", function(d) {
                return height - (d * 6) + 15;
            })
            .attr("font-family", "sans-serif")
            .attr("font-size", "11px")
            .attr("fill", "white")
            .attr("text-anchor", "middle");
    } else {
        document.getElementById("tempData").innerHTML = "No data";
    }

    var height = 180 - 2 * margin;
    if (lightData.length > 0) {
        var lightsvg = d3.select("#lightData")
            .append("svg")
            .attr("width", width)
            .attr("height", height);

        var yScale = d3.scaleLinear()
            .domain([0,d3.max(lightData)])
            .range([0,height]);

        lightsvg.selectAll("rect")
            .data(lightData)
            .enter()
            .append("rect")
            .attr("x", function(d, i) {
                return i * (width / lightData.length);
            })
            .attr("y", function(d){
                return height - yScale(d)
            })
            .attr("width", width / lightData.length - barPadding)
            .attr("height", function(d) {
                return yScale(d);
            })
            .attr("fill", function(d) {
                return "rgb(0, 0, " + (d * 2) + ")";
            });

        lightsvg.selectAll("text")
            .data(lightData)
            .enter()
            .append("text")
            .text(function(d) {
                return d;
            })
            .attr("x", function(d, i) {
                return i * (width / lightData.length) + (width / lightData.length - barPadding) / 2;
            })
            .attr("y", function(d) {
                return height - (d / 10) + 15;
            })
            .attr("font-family", "sans-serif")
            .attr("font-size", "11px")
            .attr("fill", "white")
            .attr("text-anchor", "middle");
    } else {
        document.getElementById("lightData").innerHTML = "No data";
    }
})