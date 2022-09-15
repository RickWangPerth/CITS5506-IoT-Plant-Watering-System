'use strict'
$(window).on('load', () => {

    // Default setting
    const moisMaxDefault = 70
    const moisMinDefault = 20
    const tempMaxDefault = 35
    const tempMinDefault = 5
    const lightMaxDefault = 5
    const lightMinDefault = 2
    const wateringTimeDefault = 2

    // Gap between data
    const moisGap = 10
    const tempGap = 10
    const lightGap = 2

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
      if (dataType = 'moisMax'){
        if(data > 90){
          alert('Max number of moisture should be less than 90', 'danger')
          document.getElementById("moisMax").value = moisMaxDefault
        }
      }else if(dataType = 'moisMin'){
        if(data < 10){
          alert('Min number of moisture should be graeter than 10', 'danger')
          document.getElementById("moisMin").value = moisMinDefault
        }
      }else if(dataType = 'tempMax'){
        if(data > 50){
          alert('Max number of temperature should be less than 50', 'danger')
          document.getElementById("tempMax").value = tempMaxDefault
        }
      }else if(dataType = 'tempMin'){
        if(data < -10){
          alert('Min number of temperature  should be graeter than -10', 'danger')
          document.getElementById("tempMin").value = tempMinDefault
        }
      }else if(dataType = 'lightMax'){
        if(data > 50){
          alert('Max number of moisture should be less than 20', 'danger')
          document.getElementById("lightMax").value = lightMaxDefault
        }
      }else if(dataType = 'lightMin'){
        if(data < 0){
          alert('Min number of moisture should be graeter than 0', 'danger')
          document.getElementById("lightMin").value = lightMinDefault
        }
      }
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

      dataRangeCheck("moisMax",moisMax)
      dataRangeCheck("moisMin",moisMin)
      dataRangeCheck("tempMax",tempMax)
      dataRangeCheck("tempMin",tempMin)
      dataRangeCheck("lightMax",lightMax)
      dataRangeCheck("lightMin",lightMin)

      if(moisMax - moisMin < moisGap){
        dataGapCheck('Moisture', moisGap)
      }else if(tempMax - tempMin < tempGap){
        dataGapCheck('Temperature', tempGap)
      }else if(lightMax - lightMin < lightGap){
        dataGapCheck('Light', lightGap)
      }else if(wateringTime > 6 | wateringTime < 1){
        dataGapCheck('Watering Time')
      }
      
      $.ajax({
        url: "/Setting",
        type: "POST",
        data: JSON.stringify({ id:1, moisMin: moisMin, moisMax: moisMax, tempMin:tempMin, 
          tempMax:tempMax, lightMin:lightMin, lightMax:lightMax, wateringTime:wateringTime}),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (data) {
          console.log(data);
        },
      });
      alert("Seting updated succefully",'success')
    })

    // Clicked update btn
    resetBtn.addEventListener('click', () => {

      document.getElementById("moisMax").value = moisMaxDefault
      document.getElementById("moisMin").value = moisMinDefault
      document.getElementById("tempMax").value = tempMaxDefault
      document.getElementById("tempMin").value = tempMinDefault
      document.getElementById("lightMax").value = lightMaxDefault
      document.getElementById("lightMin").value = lightMinDefault
      document.getElementById("wateringTime").value = wateringTimeDefault

      $.ajax({
        url: "/Setting",
        type: "POST",
        data: JSON.stringify({ id:1, moisMin: moisMinDefault, moisMax: moisMaxDefault, tempMin:tempMinDefault, tempMax:tempMaxDefault, lightMin:lightMinDefault, lightMax:lightMaxDefault, wateringTime:wateringTimeDefault}),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (data) {
          console.log(data);
        },
      });


      

    })
})