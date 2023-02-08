let razlika = 0
let ZBROJ = 0
input.onButtonPressed(Button.AB, function () {
    let B = 0
    let A = 0
    if (A > B) {
        razlika = A - B
        basic.showNumber(razlika)
    } else {
        ZBROJ = A + B
        basic.showNumber(ZBROJ)
    }
})
