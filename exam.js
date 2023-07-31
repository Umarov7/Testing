function firstPalindrome(arr) {
    for (words of arr) {
        wordsReversed = words.split('').reverse().join('')
        if (words === wordsReversed) {
            return words
        }
    }
}
console.log(firstPalindrome(['name', 'level', 'age', 'anna']))

function targetValue(arr, target) {
    result = []
    for (i=0; i<arr.length; i++) {
        for (j=i+1; j<arr.length; j++) {
            if (arr[i]+arr[j] === target) {
                result.push(i,j)
            }
        }
    }
    if (result.length === 0) {
        return -1
    } else {
        return result
    }
}
console.log(targetValue([5,1,3,2], 7))

function allowedLetters(arr) {
    allowed = 'ab'
    count = 0
    for (words of arr) {
        if (words.includes(allowed)) {
            count++
        }
    }
    return count
}
console.log(allowedLetters(['ad', 'bd', 'aabb']))

function onlyNums(str) {
    numbers = []
    for (i=0; i<str.length; i++) {
        char = str[i]
        if (!isNaN(char)) {
            numbers.push(char)
        }
    }
    return numbers
}
console.log(onlyNums('sa83l4l53om'))