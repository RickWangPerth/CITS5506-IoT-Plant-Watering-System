'use strict'
$(window).on('load', () => {
    //Alarm
    const alarm = document.getElementById("alarm")
    const wateralarm = document.getElementById("waterAlarm")

    //Update time
    const updateTimeElement = document.getElementById("updateTime")
    var d = new Date(0);
    d.setUTCSeconds(lastUpdated);
    updateTimeElement.textContent = d.toLocaleDateString() + " " + d.toLocaleTimeString();

    //Emoji
    const cold = "../static/images/emoji/cold.gif"
    const hot = "../static/images/emoji/hot.gif"
    const happy = "../static/images/emoji/happy.gif"
    const sad = "../static/images/emoji/sad.gif"
    const emoji = document.getElementById('emoji')

     //Moisture
     const highMois = 60
     const lowMois = 20
     const mois = moisture
     //const mois = 30
     if (mois !== null) { // moisture will be null if there are no moisture values to check
        document.getElementById('mois-value').innerHTML = Math.round(mois) + "%";
     } else {
        document.getElementById('mois-value').innerHTML = "N/A";
     }
 
     const tooMois = mois>highMois
     const goodMois = mois<highMois & mois>lowMois
     const lessMois = mois<lowMois 

    //Temperature
    const highTemp = 35
    const lowTemp = 5
    const temp = temperature
    //const temp = 26
    if (temp !== null) {
        document.getElementById('temp-value').innerHTML = temp.toFixed(1) + "°C";
    } else {
        document.getElementById('temp-value').innerHTML = "N/A";
    }

    const tooHot = temp>highTemp
    const goodTemp = temp<highTemp & temp>lowTemp
    const tooCold = temp<lowTemp
   
    //Light
    const highLight = 350
    const lowLight = 20
    const light = sensLight
    //const light = 700
    if (light !== null) {
        document.getElementById('light-value').innerHTML  = Math.round(light) + " Lux";
    } else {
        document.getElementById('light-value').innerHTML  = "N/A";
    }

    //Watering
    const wateringButton = document.getElementById('watering-btn')

    // Water level
    const waterLevelvalue = 1 // TODO
    const full = "../static/images/waterlevel/full.png"
    const empty = "../static/images/waterlevel/empyt.png"
    const waterLevel = document.getElementById('waterLevel')

    if (waterLevelvalue == 1){
        waterLevel.src = full
        waterLevel.alt = "full"
    }else{
        waterLevel.src = empty
        waterLevel.alt = "empty"
        wateralarm.style.display = "block"
        wateralarm.innerHTML = "Water tank is empty, please add water!"
        wateringButton.disabled = true
    }

    //Photo
    const photo = document.getElementById('photo')
    const photoButton = document.getElementById('photo-btn')
    $.ajax({
        url: "/latest_picture/",
        type: "GET",
        // data: JSON.stringify({}),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (data) {
          photo.src = data.image_path
        },
    });
    
    // When 'Take Photo' button is clicked
    photoButton.addEventListener('click', () => {
        $.ajax({
            url: "/take_picture",
            type: "GET",
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (data) {
                photo.src = data.image_path;
            },
        });
    })

    // Emoji & Alarm feature
    if(tooCold){
        emoji.src=cold
        alarm.style.display = "block"
        alarm.innerHTML = "Too cold! Please move me to a warm place"
    }
    else if(tooHot){
        emoji.src=hot
        alarm.style.display = "block"
        alarm.innerHTML = "Too hot! Please move me to a cool place"
    }
    else if(goodTemp & tooMois){
        emoji.src=sad
        alarm.style.display = "block"
        alarm.innerHTML = "Too much water! I dont want water anymore"
    }
    else if(goodTemp & lessMois){
        emoji.src=sad
        alarm.style.display = "block"
        alarm.innerHTML = "Lack of water! Please give me some water"
    }
    else{
        emoji.src=happy
    }

    // Style sheet & type
    const styleSheet = document.styleSheets[1];
    const type = ["moisRight","moisLeft","tempRight","tempLeft","lightRight","lightLeft"]

    // Mois bar keyframe
    const moisHalf = 40
    if(mois>moisHalf){
        var degreeRight = 180
        var keyframe = "@keyframes loading-"+type[0]+"{0%{-webkit-transform: rotate(0deg);transform: rotate(0deg);}100%{-webkit-transform: rotate("+ degreeRight +"deg);transform: rotate("+ degreeRight + "deg);}"
        styleSheet.insertRule(keyframe,styleSheet.cssRules.length)
        var degreeLeft = (mois-moisHalf)/80*360
        var keyframe = "@keyframes loading-"+type[1]+"{0%{-webkit-transform: rotate(0deg);transform: rotate(0deg);}100%{-webkit-transform: rotate("+ degreeLeft +"deg);transform: rotate("+ degreeLeft + "deg);}"
        styleSheet.insertRule(keyframe,styleSheet.cssRules.length)
    }else{
        var degreeRight = mois/80*360
        var keyframe = "@keyframes loading-"+type[0]+"{0%{-webkit-transform: rotate(0deg);transform: rotate(0deg);}100%{-webkit-transform: rotate("+ degreeRight +"deg);transform: rotate("+ degreeRight + "deg);}"
        styleSheet.insertRule(keyframe,styleSheet.cssRules.length)
    }

    //Temp bar keyframe
    const tempHalf = 20
    if(temp>tempHalf){
        var degreeRight = 180
        var keyframe = "@keyframes loading-"+type[2]+"{0%{-webkit-transform: rotate(0deg);transform: rotate(0deg);}100%{-webkit-transform: rotate("+ degreeRight +"deg);transform: rotate("+ degreeRight + "deg);}"
        styleSheet.insertRule(keyframe,styleSheet.cssRules.length)
        var degreeLeft = (temp-tempHalf)/40*360
        var keyframe = "@keyframes loading-"+type[3]+"{0%{-webkit-transform: rotate(0deg);transform: rotate(0deg);}100%{-webkit-transform: rotate("+ degreeLeft +"deg);transform: rotate("+ degreeLeft + "deg);}"
        styleSheet.insertRule(keyframe,styleSheet.cssRules.length)
    }else{
        var degreeRight = temp/40*360
        var keyframe = "@keyframes loading-"+type[2]+"{0%{-webkit-transform: rotate(0deg);transform: rotate(0deg);}100%{-webkit-transform: rotate("+ degreeRight +"deg);transform: rotate("+ degreeRight + "deg);}"
        styleSheet.insertRule(keyframe,styleSheet.cssRules.length)
    }

    //Light bar keyframe
    const lightHalf = 500
    if(light>lightHalf){
        var degreeRight = 180
        var keyframe = "@keyframes loading-"+type[4]+"{0%{-webkit-transform: rotate(0deg);transform: rotate(0deg);}100%{-webkit-transform: rotate("+ degreeRight +"deg);transform: rotate("+ degreeRight + "deg);}"
        styleSheet.insertRule(keyframe,styleSheet.cssRules.length)
        var degreeLeft = (light-lightHalf)/1000*360
        var keyframe = "@keyframes loading-"+type[5]+"{0%{-webkit-transform: rotate(0deg);transform: rotate(0deg);}100%{-webkit-transform: rotate("+ degreeLeft +"deg);transform: rotate("+ degreeLeft + "deg);}"
        styleSheet.insertRule(keyframe,styleSheet.cssRules.length)
    }else{
        var degreeRight = light/1000*360
        var keyframe = "@keyframes loading-"+type[4]+"{0%{-webkit-transform: rotate(0deg);transform: rotate(0deg);}100%{-webkit-transform: rotate("+ degreeRight +"deg);transform: rotate("+ degreeRight + "deg);}"
        styleSheet.insertRule(keyframe,styleSheet.cssRules.length)
    }
    //Watering alert
    const alertPlaceholder = document.getElementById('wateringAlertPlaceholder')
    const alert = (message, type) => {
        const info = document.createElement('div')
        info.innerHTML = [
          `<div class="alert alert-${type} alert-dismissible" role="alert">`,
          `   <div>${message}</div>`,
          '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
          '</div>'
        ].join('')
      
        alertPlaceholder.append(info)
      }
      
    wateringButton.addEventListener('click', () => {
        wateringButton.disabled = true;
        $.ajax({
            url: "/water_plant/",
            type: "GET",
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (data) {
              window.alert("Plant watered.");
              wateringButton.disabled = false;
            },
        });
    })
})
