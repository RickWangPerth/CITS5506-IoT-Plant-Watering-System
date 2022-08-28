'use strict'
$(window).on('load', () => {

    const alarm = document.getElementById("alarm");

    const cold = "./images/emoji/cold.gif";
    const hot = "./images/emoji/hot.gif";
    const happy = "./images/emoji/happy.gif";
    const sad = "./images/emoji/sad.gif";
    const photoButton = document.getElementById('photo-btn');
    const wateringButton = document.getElementById('watering-btn');

    const temp = document.getElementById('temp-value');
    const tempValue = temp.innerHTML;

    const tooHot = tempValue>35;
    const goodTemp = tempValue<35 & tempValue>5;
    const tooCold = tempValue<5;

    const mois = document.getElementById('mois-value');
    const moisValue =  mois.innerHTML;
    const tooMois = moisValue>60;
    const goodMois = moisValue<60 & moisValue>20;
    const lessMois = moisValue<20;
    const photo = document.getElementById('photo');
    const emoji = document.getElementById('emoji');

    console.log(moisValue)

    if(tooCold){
        emoji.src=cold;
        alarm.innerHTML = "Too cold! Please move me to a warm place"
    }
    else if(tooHot){
        emoji.src=hot;
        alarm.innerHTML = "Too hot! Please move me to a cool place"
    }
    else if(goodTemp & tooMois){
        emoji.src=sad;
        alarm.innerHTML = "too much water! I dont want water anymore"
    }
    else if(goodTemp & lessMois ){
        emoji.src=sad;
        alarm.innerHTML = "lack of water! Please give me some water"
    }
    else{
        emoji.src=happy;
    }
    

}
)
