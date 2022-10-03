'use strict'
$(window).on('load', () => {

    // Default setting
    const moisMaxDefault = 70
    const moisMinDefault = 20
    const tempMaxDefault = 35
    const tempMinDefault = 5
    const lightMaxDefault = 1000
    const lightMinDefault = 0
    const wateringTimeDefault = 2
    const pictureFrequencyDefault = 2

    // Gap between data
    const moisGap = 10
    const tempGap = 10
    const lightGap = 300

    // Btn
    const updateBtn = document.getElementById("update-btn")
    const resetBtn = document.getElementById("reset-btn")

    // set values for settings
    document.getElementById("moisMin").value = moisMin;
    document.getElementById("moisMax").value = moisMax;
    document.getElementById("tempMin").value = tempMin;
    document.getElementById("tempMax").value = tempMax;
    document.getElementById("lightMin").value = lightMin;
    document.getElementById("lightMax").value = lightMax;
    document.getElementById("wateringTime").value = wateringTime;
    document.getElementById("pictureFrequency").value = pictureFrequency;
    console.log("success");
    // alter Place holder
    const alertPlaceholder = document.getElementById('dataAlertPlaceholder')

    function alert (message, type){
      const info = document.createElement('div')
      info.innerHTML = [
        `<div class="alert alert-${type} alert-dismissible" role="alert">`,
        `   <div>${message}</div>`,
        '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
        '</div>'
      ].join('')
      alertPlaceholder.append(info)
    }

    // raise alert for inappropriate data
    function dataGapCheck(dataType,gap){
      const alertPlaceholder = document.getElementById('dataAlertPlaceholder')
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
      if(dataType != 'Watering Time'){
        alert('The minimum gap between Max and Min in ' + dataType +' should be greater than ' + gap, 'danger')
        
      }else{
        alert('The watering time should between 1-6 minutes', 'danger')
        
      }
      
    }

    // Data Range Check
    function dataRangeCheck(dataType,data){
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
      if (dataType == 'moisMax'){
        if(data > 100){
          alert('Max number of moisture should be less than 90', 'danger')
          document.getElementById("moisMax").value = moisMaxDefault
          return 0
        }
      }else if(dataType == 'moisMin'){
        if(data < 10){
          alert('Min number of moisture should be graeter than 10', 'danger')
          document.getElementById("moisMin").value = moisMinDefault
          return 0
        }
      }else if(dataType == 'tempMax'){
        if(data > 50){
          alert('Max number of temperature should be less than 50', 'danger')
          document.getElementById("tempMax").value = tempMaxDefault
          return 0
        }
      }else if(dataType == 'tempMin'){
        if(data < -10){
          alert('Min number of temperature  should be graeter than -10', 'danger')
          document.getElementById("tempMin").value = tempMinDefault
          return 0
        }
      }else if(dataType == 'lightMax'){
        if(data > 10000){
          alert('Max number of moisture should be less than 20', 'danger')
          document.getElementById("lightMax").value = lightMaxDefault
          return 0
        }
      }else if(dataType == 'lightMin'){
        if(data < 0){
          alert('Min number of moisture should be graeter than 0', 'danger')
          document.getElementById("lightMin").value = lightMinDefault
          return 0
        }
      }
      return 1
    }
    // Clicked update btn
    updateBtn.addEventListener('click', () => {
      var moisMax = document.getElementById("moisMax").value
      var moisMin = document.getElementById("moisMin").value
      var tempMax = document.getElementById("tempMax").value
      var tempMin = document.getElementById("tempMin").value
      var lightMax = document.getElementById("lightMax").value
      var lightMin = document.getElementById("lightMin").value
      var wateringTime = document.getElementById("wateringTime").value
      var pictureFrequency = document.getElementById("pictureFrequency").value

      var Rangecheck = 0
      Rangecheck +=  dataRangeCheck("moisMax",moisMax)
      Rangecheck +=  dataRangeCheck("moisMin",moisMin)
      Rangecheck +=  dataRangeCheck("tempMax",tempMax)
      Rangecheck +=  dataRangeCheck("tempMin",tempMin)
      Rangecheck +=  dataRangeCheck("lightMax",lightMax)
      Rangecheck +=  dataRangeCheck("lightMin",lightMin)

      var Gapcheck = 0
      if(moisMax - moisMin < moisGap){
        dataGapCheck('Moisture', moisGap)
        Gapcheck += 1
      }else if(tempMax - tempMin < tempGap){
        dataGapCheck('Temperature', tempGap)
        Gapcheck += 1
      }else if(lightMax - lightMin < lightGap){
        dataGapCheck('Light', lightGap)
        Gapcheck += 1
      }else if(wateringTime > 6 | wateringTime < 1){
        dataGapCheck('Watering Time')
        Gapcheck += 1
      }
      console.log(Gapcheck)
      console.log(Rangecheck)

      if (Gapcheck == 0 && Rangecheck == 6){
        $.ajax({
          url: "/Setting",
          type: "POST",
          data: JSON.stringify({ id:1, moisMin: moisMin, moisMax: moisMax, tempMin:tempMin, 
            tempMax: tempMax, lightMin: lightMin, lightMax: lightMax, wateringTime: wateringTime, pictureFrequency: pictureFrequency}),
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          success: function (data) {
            console.log(data);
          },
        });
      alert("Seting updated succefully",'success')
      }
    })

    // Clicked Reset btn
    resetBtn.addEventListener('click', () => {

      document.getElementById("moisMax").value = moisMaxDefault
      document.getElementById("moisMin").value = moisMinDefault
      document.getElementById("tempMax").value = tempMaxDefault
      document.getElementById("tempMin").value = tempMinDefault
      document.getElementById("lightMax").value = lightMaxDefault
      document.getElementById("lightMin").value = lightMinDefault
      document.getElementById("wateringTime").value = wateringTimeDefault
      document.getElementById("pictureFrequency").value = pictureFrequencyDefault


      $.ajax({
        url: "/Setting",
        type: "POST",
        data: JSON.stringify({ id:1, moisMin: moisMinDefault, moisMax: moisMaxDefault, tempMin:tempMinDefault, tempMax:tempMaxDefault, lightMin:lightMinDefault, lightMax:lightMaxDefault, wateringTime:wateringTimeDefault, pictureFrequency:pictureFrequencyDefault}),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (data) {
          console.log(data);
        },
      });


      

    })
})