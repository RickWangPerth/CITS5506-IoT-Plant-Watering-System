'use strict'
$(window).on('load', () => {

    const updateBtn = document.getElementById("update-btn")
    const resetBtn = document.getElementById("reset-btn")

    updateBtn.addEventListener('click', () => {
        const moisMax = document.getElementById("moisMax").value
        const moisMin = document.getElementById("moisMin").value
        const tempMax = document.getElementById("tempMax").value
        const tempMin = document.getElementById("tempMin").value
        const lightMax = document.getElementById("lightMax").value
        const lightMin = document.getElementById("lightMin").value
        const wateringTime = document.getElementById("wateringTime").value
        console.log(moisMax)
      })
})