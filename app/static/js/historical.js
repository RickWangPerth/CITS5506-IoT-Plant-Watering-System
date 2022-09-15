'use strict'
$(window).on('load', () => {
    const margin = 10;
    const width = 500 - 2 * margin;
    const height = 150 - 2 * margin;
    var barPadding = 3;

    if (moisData.length > 0) { // If we've received sensor data
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
                return height - (d * 4);
            })
            .attr("width", width / moisData.length - barPadding)
            .attr("height", function(d) {
                return d*10;
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
                return height - (d * 4) + 15;
            })
            .attr("font-family", "sans-serif")
            .attr("font-size", "11px")
            .attr("fill", "white")
            .attr("text-anchor", "middle");
    } else { // If we haven't received sensor data
        document.getElementById("moisData").innerHTML = "No data"; // Placeholder 'no data' indicator
    }

    if (tempData.length > 0) {
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
                return height - (d * 4);
            })
            .attr("width", width / tempData.length - barPadding)
            .attr("height", function(d) {
                return d*10;
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
                return height - (d * 4) + 15;
            })
            .attr("font-family", "sans-serif")
            .attr("font-size", "11px")
            .attr("fill", "white")
            .attr("text-anchor", "middle");
    } else {
        document.getElementById("tempData").innerHTML = "No data";
    }

    if (lightData.length > 0) {
        var lightsvg = d3.select("#lightData")
            .append("svg")
            .attr("width", width)
            .attr("height", height);

        lightsvg.selectAll("rect")
            .data(lightData)
            .enter()
            .append("rect")
            .attr("x", function(d, i) {
                return i * (width / lightData.length);
            })
            .attr("y", function(d){
                return height - (d * 4);
            })
            .attr("width", width / lightData.length - barPadding)
            .attr("height", function(d) {
                return d*10;
            })
            .attr("fill", function(d) {
                return "rgb(0, 0, " + (d * 10) + ")";
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
                return height - (d * 4) + 15;
            })
            .attr("font-family", "sans-serif")
            .attr("font-size", "11px")
            .attr("fill", "white")
            .attr("text-anchor", "middle");
    } else {
        document.getElementById("lightData").innerHTML = "No data";
    }
})