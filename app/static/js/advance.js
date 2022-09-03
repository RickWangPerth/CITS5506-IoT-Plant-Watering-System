'use strict'
$(window).on('load', () => {

    // Default setting
    const moisMaxDefault = 70
    const moisMinDefault = 70
    const tempMaxDefault = 70
    const tempMinDefault = 70
    const lightMaxDefault = 70
    const lightMinDefault = 70

    // Gap between data
    const moisGap = 10
    const tempGap = 10
    const lightGap = 10


    // Btn
    const updateBtn = document.getElementById("update-btn")
    const resetBtn = document.getElementById("reset-btn")

    // raise alert for inappropriate data
    function dataAlert(dataType,gap){
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

    // Clicked update btn
    updateBtn.addEventListener('click', () => {
      const moisMax = document.getElementById("moisMax").value
      const moisMin = document.getElementById("moisMin").value
      const tempMax = document.getElementById("tempMax").value
      const tempMin = document.getElementById("tempMin").value
      const lightMax = document.getElementById("lightMax").value
      const lightMin = document.getElementById("lightMin").value
      const wateringTime = document.getElementById("wateringTime").value

      if(moisMax - moisMin < moisGap){
        dataAlert('Moisture', moisGap)
      }else if(tempMax - tempMin < tempGap){
        dataAlert('Temperature', tempGap)
      }else if(lightMax - lightMin < lightGap){
        dataAlert('Light', lightGap)
      }else if(wateringTime > 6 | wateringTime < 1){
        dataAlert('Watering Time')
      }
    })

    // Clicked update btn
    resetBtn.addEventListener('click', () => {

    })
})