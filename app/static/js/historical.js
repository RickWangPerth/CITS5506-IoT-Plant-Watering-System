'use strict'
//moisData = [21,20,18,30,40,70,48,46,44]
//tempData = [25,21,23,22,22,22,25,25,23]
//lightData = [70,70,80,100,200,300,150,120,110,110]

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
                return height - yScale(d) + 15;
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
                return height - yScale(d) + 18;
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
                return height - yScale(d) + 15;
            })
            .attr("font-family", "sans-serif")
            .attr("font-size", "11px")
            .attr("fill", "white")
            .attr("text-anchor", "middle");
    } else {
        document.getElementById("lightData").innerHTML = "No data";
    }


    var d = new Date(0); // The 0 there is the key, which sets the date to the epoch
    d.setUTCSeconds(timeStamp[timeStamp.length - 1]);
    document.getElementById("TimeStamp0").innerHTML = d.toLocaleString();//timeStamp[0];
    d = new Date(0); // The 0 there is the key, which sets the date to t>
    d.setUTCSeconds(timeStamp[timeStamp.length - 2]);
    document.getElementById("TimeStamp1").innerHTML = d.toLocaleString();//timeStamp[1];
    d = new Date(0);
    d.setUTCSeconds(timeStamp[timeStamp.length - 3]);
    document.getElementById("TimeStamp2").innerHTML = d.toLocaleString()//timeStamp[2];

    document.getElementById("moisAlert0").innerHTML = moisAlert[moisAlert.length-1];
    document.getElementById("moisAlert1").innerHTML = moisAlert[moisAlert.length-2];
    document.getElementById("moisAlert2").innerHTML = moisAlert[moisAlert.length-3];

    document.getElementById("tempAlert0").innerHTML = tempAlert[tempAlert.length-1];
    document.getElementById("tempAlert1").innerHTML = tempAlert[tempAlert.length-2];
    document.getElementById("tempAlert2").innerHTML = tempAlert[tempAlert.length-3];

    document.getElementById("lightAlert0").innerHTML = lightAlert[lightAlert.length-1];
    document.getElementById("lightAlert1").innerHTML = lightAlert[lightAlert.length-2];
    document.getElementById("lightAlert2").innerHTML = lightAlert[lightAlert.length-3];

})
