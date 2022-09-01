'use strict'
$(window).on('load', () => {

    // Alarm
    const alarm = document.getElementById("alarm")
    //Emoji
    const cold = "./images/emoji/cold.gif"
    const hot = "./images/emoji/hot.gif"
    const happy = "./images/emoji/happy.gif"
    const sad = "./images/emoji/sad.gif"
    const emoji = document.getElementById('emoji')

    //Temperature
    const highTemp = 35
    const lowTemp = 5
    const tempValue = document.getElementById('temp-value').innerHTML

    const tooHot = tempValue>highTemp
    const goodTemp = tempValue<highTemp & tempValue>lowTemp
    const tooCold = tempValue<lowTemp
    //Moisture
    const highMois = 60
    const lowMois = 20
    const moisValue =  document.getElementById('mois-value').innerHTML

    const tooMois = moisValue>highMois
    const goodMois = moisValue<highMois & moisValue>lowMois
    const lessMois = moisValue<lowMois

    //Light
    const highLight = 60
    const lowLight = 20
    const lightValue = document.getElementById('light-value').innerHTML

    //Watering
    const wateringButton = document.getElementById('watering-btn')

    //Photo
    const photo = document.getElementById('photo')
    const photoButton = document.getElementById('photo-btn')

    // Emoji & Alarm feature
    if(tooCold){
        emoji.src=cold
        alarm.innerHTML = "Too cold! Please move me to a warm place"
    }
    else if(tooHot){
        emoji.src=hot
        alarm.innerHTML = "Too hot! Please move me to a cool place"
    }
    else if(goodTemp & tooMois){
        emoji.src=sad
        alarm.innerHTML = "too much water! I dont want water anymore"
    }
    else if(goodTemp & lessMois ){
        emoji.src=sad
        alarm.innerHTML = "lack of water! Please give me some water"
    }
    else{
        emoji.src=happy
    }
    // Style sheet & type
    const styleSheet = document.styleSheets[1];
    const type = ["moisRight","moisLeft","tempRight","tempLeft","lightRight","lightLeft"]

    // Mois bar keyframe
    const moisHalf = 50
    if(moisValue>moisHalf){
        var degreeRight = 180
        var keyframe = "@keyframes loading-"+type[0]+"{0%{-webkit-transform: rotate(0deg);transform: rotate(0deg);}100%{-webkit-transform: rotate("+ degreeRight +"deg);transform: rotate("+ degreeRight + "deg);}"
        styleSheet.insertRule(keyframe,styleSheet.cssRules.length)
        var degreeLeft = (moisValue-moisHalf)/100*360
        var keyframe = "@keyframes loading-"+type[1]+"{0%{-webkit-transform: rotate(0deg);transform: rotate(0deg);}100%{-webkit-transform: rotate("+ degreeLeft +"deg);transform: rotate("+ degreeLeft + "deg);}"
        styleSheet.insertRule(keyframe,styleSheet.cssRules.length)
    }else{
        var degreeRight = moisValue/100*360
        var keyframe = "@keyframes loading-"+type[0]+"{0%{-webkit-transform: rotate(0deg);transform: rotate(0deg);}100%{-webkit-transform: rotate("+ degreeRight +"deg);transform: rotate("+ degreeRight + "deg);}"
        styleSheet.insertRule(keyframe,styleSheet.cssRules.length)
    }

    //Temp bar keyframe
    const tempHalf = 20
    if(tempValue>tempHalf){
        var degreeRight = 180
        var keyframe = "@keyframes loading-"+type[2]+"{0%{-webkit-transform: rotate(0deg);transform: rotate(0deg);}100%{-webkit-transform: rotate("+ degreeRight +"deg);transform: rotate("+ degreeRight + "deg);}"
        styleSheet.insertRule(keyframe,styleSheet.cssRules.length)
        var degreeLeft = (tempValue-tempHalf)/100*360
        var keyframe = "@keyframes loading-"+type[3]+"{0%{-webkit-transform: rotate(0deg);transform: rotate(0deg);}100%{-webkit-transform: rotate("+ degreeLeft +"deg);transform: rotate("+ degreeLeft + "deg);}"
        styleSheet.insertRule(keyframe,styleSheet.cssRules.length)
    }else{
        var degreeRight = tempValue/20*180
        var keyframe = "@keyframes loading-"+type[2]+"{0%{-webkit-transform: rotate(0deg);transform: rotate(0deg);}100%{-webkit-transform: rotate("+ degreeRight +"deg);transform: rotate("+ degreeRight + "deg);}"
        styleSheet.insertRule(keyframe,styleSheet.cssRules.length)
    }

    //Light bar keyframe
    const lightHalf = 20
    if(lightValue>lightHalf){
        var degreeRight = 180
        var keyframe = "@keyframes loading-"+type[4]+"{0%{-webkit-transform: rotate(0deg);transform: rotate(0deg);}100%{-webkit-transform: rotate("+ degreeRight +"deg);transform: rotate("+ degreeRight + "deg);}"
        styleSheet.insertRule(keyframe,styleSheet.cssRules.length)
        var degreeLeft = (lightValue-lightHalf)/100*360
        var keyframe = "@keyframes loading-"+type[5]+"{0%{-webkit-transform: rotate(0deg);transform: rotate(0deg);}100%{-webkit-transform: rotate("+ degreeLeft +"deg);transform: rotate("+ degreeLeft + "deg);}"
        styleSheet.insertRule(keyframe,styleSheet.cssRules.length)
    }else{
        var degreeRight = lightValue/20*180
        var keyframe = "@keyframes loading-"+type[4]+"{0%{-webkit-transform: rotate(0deg);transform: rotate(0deg);}100%{-webkit-transform: rotate("+ degreeRight +"deg);transform: rotate("+ degreeRight + "deg);}"
        styleSheet.insertRule(keyframe,styleSheet.cssRules.length)
    }

}
)
