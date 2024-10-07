// Conditional statements:

function Equality(num1, num2) {
    if (num1 !== num2) {
        return 'not equal'
    } else {
        return 'equal'
    }
}
console.log(Equality(15,16))

function Odd_Even(num) {
    if (num % 2 !== 0) {
        return "odd"
    } return "even"
}
console.log(Odd_Even(45))

function Positive_Negative(num) {
    if (num >= 0) {
        return 'positive'
    } return 'negative'
}
console.log(Positive_Negative(0))

function Leap_Year(year) {
    if (year % 400 == 0) {
        return year + "is a leap year"
    } else if (year % 100 == 0) {
        return year + " isn't a leap year"
    } else if (year % 4 == 0) {
        return `${year} is a leap year`
    } else {
        return `${year} is not a leap year`
    }    
}
console.log(Leap_Year(2023))

function election(age) {
    if (age < 18) {
        return `You\'be able to vote after ${18-age} years`
    }
    return 'U can vote'
}
console.log(election(21))

function value_N (m) {
    if (m > 0) {
        return 'The value of n = 1'
    } else if (m == 0) {
        return 'The value of n = 0'
    } else {
        return 'The value of n = -1'
    }
}
console.log(value_N(-5))

