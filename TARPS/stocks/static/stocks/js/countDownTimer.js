// Countdown timer for stock predictions
var countDownDate = (cacheTimeLength * 1000) + Date.now();
var countDownTimer = setInterval(function() {
var currentDate = new Date().getTime();

    var timeDifference = countDownDate - currentDate;
    var days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
    var hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);
    document.getElementById("countDownTimerHTML").innerHTML = days + "d " + hours + "h "
    + minutes + "m " + seconds + "s ";

    if (timeDifference < 0) {
    clearInterval(countDownTimer);
    document.getElementById("countDownTimerHTML").innerHTML = "EXPIRED - Refresh the page to get a new prediction";
    }

}, 1000);