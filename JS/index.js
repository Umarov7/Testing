// let num = 100
// if(num <= 100 && num >= 90){
//     console.log("U got A")
// } else if(num < 90 && num >= 80){
//     console.log("U got B")
// } else if(num < 80 && num >= 70){
//     console.log("U got C")
// } else {
//     console.log("U got D, What a shame, dude!")
// }



/*let month = 12
let monthName 

if (month == 1) {
    monthName = 'Jan'
} else if (month == 2) {
    monthName = 'Feb'
} else if (month == 3) {
    monthName = 'Mar'
} else if (month == 4) {
    monthName = 'Apr'
} else if (month == 5) {
    monthName = 'May'
} else if (month == 6) {
    monthName = 'Jun'
} else if (month == 7) {
    monthName = 'Jul'
} else if (month == 8) {
    monthName = 'Aug'
} else if (month == 9) {
    monthName = 'Sep'
} else if (month == 10) {
    monthName = 'Oct'
} else if (month == 11) {
    monthName = 'Nov'
} else if (month == 12) {
    monthName = 'Dec'
} else {
    monthName = 'Invalid month'
}
console.log(monthName)

let weight = 54
let height = 1.79
let BMI = weight / (height * height)
let weightStatus

if (BMI < 18.5) {
    weightStatus = 'Underweight'
} else if (BMI >= 18.5 && BMI <= 24.9) {
    weightStatus = 'Healthy Weight' 
} else if (BMI >= 25 && BMI <= 29.9) {
    weightStatus = 'Overweight'
} else {
    weightStatus = 'Obesity'
}
console.log(weightStatus)*/



// let a = 9
// if (a % 3) {console.log("Qoldiqli")} else {console.log("Qoldiqsiz")}

// let x = 96
// x /= 4
// x += 5
// x *= 3
// x -= 1
// x %= 3
// console.log(x)

// let age = window.prompt("How old are you?")
// console.log(typeof age)
// age = Number(age)
// console.log(typeof age)
// age += 1
// console.log("Wow, you are", age, "years old") 

// let username = window.prompt("What's your name?")
// console.log(username)
// let surname = window.prompt("What is your surname?")
// console.log(surname)

// let x
// let y
// let z
// x = Number("3.14")
// y = String(3.14)
// z = Boolean("")
// console.log(x, typeof x)
// console.log(y, typeof y)
// console.log(z, typeof z)



/*let age = 25
switch(age) {
    case 18:
        console.log('U are 18 years old')
        break
    case 25:
        console.log('U are 25 years old')
        break
    case 30:
        console.log('U are 30 years old')
        break
    default:
        console.log('Error')  
}

switch(age) {
    case 0:
        console.log('Not allowed')
        break
    case 18:
        console.log('Allowed') 
        break
    case 50: 
        console.log('Allowed')   
        break
    case 60:
        console.log('Not allowed')       
        break
    default:
        console.log('Hello')
}



let day = 7
let dayName

switch (day) {
    case 1:
        dayName = 'Monday'
        break
    
    case 2:
        dayName = 'Tuesday' 
        break
        
    case 3:
        dayName = 'Wednesday'
        break
        
    case 4:
        dayName = 'Thursday'
        break
        
    case 5:
        dayName = 'Friday'
        break
        
    case 6:
        dayName = 'Saturday'
        break
        
    case 7:
        dayName = 'Sunday'
        break
        
    default:
        dayName = 'Invalid day'    
} 
console.log(dayName)*/          

// for(i=0;i<=100;i++) {
//     if(i % 5 == 0)
//     console.log(i)
// }

// let car = {
//     colour :'black',
//     weight :'400 kg',
//     model :3,
//     year :2022,
//     price :'500$'
// }  
// console.log(car)



// let a = "Hello"
// for(i=0; i<4; i++) {
//     console.log(a)
// }

// for(i=10; i>0; i-=1) {
//     console.log(i)
// }

/*let person = {
    name:'John',
    surname:'Smith',
    age:25,
    address: {
        house:7,
        street:'Tango',
        city:'Liverpool',
        country:'England'
    }
}
person.age = 26
person.gender = "male"
delete person.gender
console.log('age' in person)
console.log("gender" in person)
console.log(person['gender'])*/



/*let a = 5
for (i=1; i<10; i++) {
    let result = a * i
    console.log(a,"x",i,"=",result)
}

for (i=1; i<10; i++) {
    for (j=1; j<10; j++){
    result = i * j
    console.log(i,"x",j,"=",result)
}
}

let names = ['Ali', 'Akbar', 'Zaynab', 'Soliha']
names[2] = "Akrom" // to change the value of an element
console.log(names[2], names.length) // to access an element in an array --- [index], to show the number of elements --- .length
names.push("Abror") // to add an element to the end of an array --- .push()
names.unshift("Anvar") // to add an element to the beginning of an array --- .unshift()
console.log(names)
names.pop("Abror") // to remove an element from the end of an array --- .pop()
names.shift("Anvar") // to remove an element from the beginning of an array --- .shift()
console.log(names)
index = names.indexOf("Soliha") // to find the index of an element
console.log(index)
console.log(Array.isArray(names)) // to check if a value is an array

for (i=0; i<=names.length; i++) {
    console.log(names.length)
}
for(a of names) {
    console.log(names)
}

let numbers = [1,2,3,4,5,6,7,8,9]
let sum=1
for(i=1; i<numbers.length; i++) {
    sum *= numbers[i]
}
console.log(sum)

let array = [1,2,3,4,5,6,7,8,9]
let array2 = [1,2,3,4,5,6,7,8,9]
let sum = 0
let sum2 = 0
for(i=0; i<array.length; i++) {
    sum += array[i]}
for(j=0; j<array2.length; j++){
        sum2 += array2[j]
    }
sum3 = sum + sum2
console.log(sum3)

let array3 = [1,2,3,4,5,6,7,8,9]
let array4 = [1,2,3,4,5,6,7,8,9]
let array5 = [...array3,...array4]
let sum4 = 0
for (i=0; i<array5.length; i++) {
    sum4 += array5[i]
    console.log(sum4)
}*/



/*let word = "Hello World"
let array = ["a", "o", "i", "u", "e"]
let word2 = word.toLowerCase()
 
for (a of word2) {
    for (b of array) {
        if (a===b) {
            console.log(a)
        }
    }
}

let count = 0 
let sum = 0
for (i=1; i<=100; i++) {
    if (i % 2===1) {
        count++
        sum += i
    }
}
console.log(sum / count)

for (num=2; num<=100; num++) {
    prime=true

    for (i=2; i<num; i++) {
        if (num%i===0) {
            prime=false
            break
        }
    }
    if (prime==true) {
        console.log(num)
    }
}*/



/*function F(a,b) {
    let result=(1/2)*a*b
    return result
} 
console.log(F(4,5))

function S(a,b) {
    result=a*b
    return result
}
console.log(S(5,8))

function P(a,b) {
    result=(a+b)*2
    return result
}
console.log(P(4,7))

function Sum(num) {
    sum=0
    for (i=0; i<=num; i++) {
        sum+=i
    }
    return sum
}
console.log(Sum(100))

function Fac(num) {
    result=1
    for (i=1; i<=num; i++) {
        result*=i
    }
    return result
}
console.log(Fac(5))

function Fib(n){
    if(n==0){
        return 1
    }

    return n*Fib(n-1)
}

console.log(Fib(5));


function FIB(number) {
    let first_numbers = [0,1]
    let sum = first_numbers[0] + first_numbers[1]

    for (i = 2; i < number; i++) {
        next_number = first_numbers[i-1] + first_numbers[i-2]
        first_numbers.push(next_number)
        sum += next_number
    }
    
    return sum
}
console.log(FIB(11))

function FIB(number) {
    let first_numbers = [0,1]
    let sum = first_numbers[0] + first_numbers[1]

    for (i = 2; i < number; i++) {
        next_number = first_numbers[i-1] + first_numbers[i-2]
        first_numbers.push(next_number)
        sum += next_number
    }

    console.log(sum)
}
FIB(11)

let num = 1
while (num < 10) {
    console.log(num)
    num += 2
}

let count = 0
do {
    console.log(count)
    count++
} while (count < 5)
do { count++, console.log(count)} while (count < 5)*/



/*function Palindrome(number) {
    let num = number
    let reverse = 0 
    
    while (num > 0) {
        let digit = num % 10
        reverse = reverse * 10 + digit
        num = Math.floor(num / 10)
    }

    if (number === reverse) {
        return true
    } else {
        return false
    }
}
console.log(Palindrome(4994))

function palindromeStr(word) {
    let wordReversed = word.split('').reverse().join('')
    
    if (word === wordReversed) {
        return true
    } else {
        return false
    }
}
console.log(palindromeStr('racecar'))*/



// 18.07.2023
/*stack = []

function IsEmpty() {
    if (stack.length == 0) {
        return true
    } return false
}
IsEmpty(stack)

function Push(element) {
    return stack.push(element)
}
Push(1), Push(2), Push(3), Push(4), Push(5)

function Pop() {
    return stack.pop()
}
Pop(stack)

function Peek() {
    return stack[stack.length-1]
}
Peek(stack)

function Size() {
    return stack.length
}
console.log(Size(stack))


queue = []

function IsEmpty() {
    if (queue.length == 0) {
        return true
    } return false
}
IsEmpty(queue)

function Enqueue(element) {
    return queue.push(element)
}
Enqueue(1), Enqueue(2), Enqueue(3), Enqueue(4), Enqueue(5)

function Dequeue() {
    return queue.shift()
}
Dequeue(queue)

function Front() {
    return queue[0]
}
Front(queue)

function Back() {
    return queue[queue.length-1]
}
Back(queue)

function Size() {
    return queue.length
}
console.log(Size(queue))*/



// 19.07.2023
/*function Consonants(str) {
    let vowels = ['a', 'o', 'i', 'u', 'e']
    str = str.toLowerCase()
    count = 0

    for (a of str) {
        isVowel = false

        for (b of vowels) {
            if (a===b) {
                isVowel = true
                break
            }
        }

        if (isVowel == false) {
            count++
        }
    }

    return count
}
console.log(Consonants('JavaScrIpt'))

function Consonants2(str) {
    let vowels = 'aoiue'
    str = str.toLowerCase()
    count = 0

    for (letters of str) {
        if (!vowels.includes(letters)) {
            count++
        }
    }

    return count
}
console.log(Consonants2('JavaScrIpt'))

function strReversed(str) {
    word = [] 

    for (i = str.length - 1; i >= 0; i--) {
        word += str[i]
    }

    return word
}
console.log(strReversed('JavaScript'))*/


/*function maxNumber(array) {
    return Math.max(...array)
}
console.log(maxNumber([1,7,56,49,37,84,95,67]))

function maxNumber2(array) {
    max = array[0] 

    for (i = 1; i < array.length; i++) {

        if (array[i] > max) {
            max = array[i]
        }
    }

    return max
}
console.log(maxNumber2([1,7,56,49,37,84,95,67]))

function occurrence(array) {
    count = 0

    for (numbers of array) {
        if (numbers === 1) {
            count++
        }
    }

    return count
}
console.log(occurrence([2,1,3,4,1,6,1,5]))

function bubbleSort(array) {
    for (i = 0; i < array.length; i++) {

        for (j = 0; j < array.length - 1; j++) {

            if (array[j] > array[j + 1]) {
                swap = array[j]
                array[j] = array[j + 1]
                array[j + 1] = swap
            }
        }
    }

    return array
}
console.log(bubbleSort([1,7,56,49,37,84,95,67,-5]))

function mergeSort(array1, array2) {
    array3 = array1.concat(array2)

    for (i = 0; i < array3.length; i++) {

        for (j = 0; j < array3.length - 1; j++) {

            if (array3[j] > array3[j + 1]) {
                swap = array3[j] 
                array3[j] = array3[j + 1] 
                array3[j + 1] = swap
            }
        }
    }

    return array3
}
console.log(mergeSort([1,7,56,49,37], [84,95,67,-5]))

function mergeSort2(array1, array2) {
    array3 = array1.concat(array2)

    array3.sort(function (a, b) {
        return a - b
    })

    return array3
}
console.log(mergeSort2([1,7,56,49,37], [84,95,67,-5]))

function mergeSort3(array1, array2) {
    array3 = [...array1, ...array2] 

    array3.sort(function (a, b) {
        return a - b
    })

    return array3
}
console.log(mergeSort3([1,7,56,49,37], [84,95,67,-5]))

function perfectNumber(number) {
    divisors = []
    sum = 0

    for (i = 1; i < number; i++) {

        if (number % i === 0) {
            divisors.push(i)
            sum += i
        }
    }

    return sum
}
console.log(perfectNumber(28))*/



// 22.07.2023
/*function duplicate(numbers) {

    for (i = 0; i < numbers.length; i++) {

        for (j = i + 1; j < numbers.length; j++) {

            if (numbers[i] == numbers[j]) {
                console.log(numbers[j])
            }
        }
    }

}
duplicate([1,2,2,5,4,8,5,3,7,3])

function duplicate2(numbers) {
    duplicates = []
    for (i = 0; i < numbers.length; i++) {

        for (j = i + 1; j < numbers.length; j++) {

            if (numbers[i] == numbers[j]) {
                duplicates.push(numbers[j])
            }
        }
    }
    return duplicates
}
console.log(duplicate2([1,2,2,5,4,8,5,3,7,3]))

function duplicateObj(numbers) {
    countNum = {}
    result = []

    for (num of numbers) {
        countNum[num] = 0
    }
    for (num of numbers) {
        countNum[num]++
    }
    for (key in countNum) {
        if (countNum[key] > 1) {
            result.push(key)
        }
    }

    return result
}
console.log(duplicateObj([1,2,2,5,4,8,5,3,7,3]))

function Parenthesis(str) {
    stack = []

    for (a of str) {
        if (a == '(') {
            stack.push(a)
        } else if (a == ')' && stack[stack.length - 1] == '(') {
            stack.pop()
        } else if (a == ')' && stack[stack.length - 1] != '(') {
            return false
        } else {
            continue
        }
    }
    
    if (stack.length == 0) {
        return true
    } return false
}
console.log(Parenthesis('((3))6(23)'))*/



/*let map = new Map ([
    ['Iphone', 1000],
    ['Samsung', 900],
    ['Mi', 700]  
])
console.log(map)

for (stuff of map.keys()) {
    console.log(stuff)
}

function duplicate3(array) {
    duplicates = []

    for (i of array)
    for (j of array) {}

    if (i == j) {
        duplicates.push(i)
    }

    return duplicates
}
console.log(duplicate3(['abc', 'ab', 'abc', 'acd', 'abc']))

function chessBoard(str, num) {

    if (str === 'a' || 'c' || 'e' || 'g') {
        if (num % 2 != 0) {
            console.log('black')
        } else {
            console.log('white')
        }

    } else if (str === 'b' || 'd' || 'f' || 'h') {
        if (num % 2 != 0) {
            console.log('white')
        } else {
            console.log('black')
        }

    } else {
        console.log('Error')
    }

}
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
chessBoard(letters, numbers)

function onlyNums(array) {
    return array

    .map(item => item.match(/\d+/))
    .filter(item => item !== null)
    .map(item => parseInt(item))
    
}  
console.log(onlyNums(['a52', '31c', 'ab6c', 'a3275c']))*/



// 25.07.2023
/*function identicalArrays(arr1, arr2) {
    for (i=0; i<arr1.length; i++) {
            if (arr1[i] !== arr2[i]) {
                return false
            }
    }
    return true
}
console.log(identicalArrays([1, 2, 3], [1, 2, 3]))

function removeDuplicates(array) {
    duplicates = {}
    result = []

    for (arr of array) {
        duplicates[arr] = 0
    }
    for (arr of array) {
        duplicates[arr]++
    } 
    for (key in duplicates) {
        result.push(key)
    }

    return result
}
console.log(removeDuplicates([1, 2, 1, 1, 2, 3, 4, 8]))

function longestWord(string) {
    str = string.split(' ')
    longest = ''

    for (i = 0; i < str.length; i++) {

        if (str[i].length > longest.length) {
            longest = str[i]
        }
    }

    return longest
}
console.log(longestWord('Hello World, Javascript'))

function toUppercaseLettters(str) {
    arr = str.split(' ')
    for (let i=0; i<arr.length; i++) {
        arr[i] = arr[i].charAt(0).toUpperCase() + arr[i].slice(1)
    }    

    return arr.join(' ')
}
console.log(toUppercaseLettters('hello world'))*/



/*function checkArrays(arr1, arr2) {
    for (i=0; i<arr1.length; i++) {
            if (arr1[i] !== arr2[i]) {
                return [...arr1, ...arr2]
            } 
        
    }
    return arr1
}
console.log(checkArrays([1, 2, 3], [1, 2, 3]))

function targetNum(arr) {
    target = 16

    for (i=0; i<arr.length; i++) {
        if (target == 8) {
            return arr[0]+arr[1]+arr[2]
        } else if (target == 10) {
            return arr[1]+arr[3]
        } else if (target == 16) {
            return arr[0]+arr[1]+arr[2]+arr[3]
        } else if (target >= 50) {
            return 'Sorry'
        } else {
            return "Try again"
        }
    }
}
console.log(targetNum([1, 2, 5, 8]))*/


// 27.07.2023
// function sortObjects(arr) {
//     arr.sort(function (a, b) {return a.age-b.age})
//     return arr
// }
// console.log(sortObjects([{name: 'John', age:25}, {name: 'Mark', age:18}, {name: "David", age:16}, {name: "Tom", age:36}]))

// function sumNums(arr) {
//     numbers = arr.filter(function (item) {return !isNaN (item) && typeof item === 'number'})
//     sum = numbers.reduce(function (a, b) {return a+b}, 0)
//     return sum
// }
// console.log(sumNums([1, 2, 'Hello', 5, "World"]))

// function missingNums(arr) {
//     min = Math.min(...arr)
//     max = Math.max(...arr)

//     fullArr = Array.from({length: max-min+1}, (_,i) => i+min)

//     nums = fullArr.filter(num => ! arr.includes(num))
//     return nums
// }
// console.log(missingNums([1, 2, 3, 5, 7, 8, 9, 10]))

// function missingNum(arr) {
//     fullArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

//     sum = arr.reduce((a, b) => {return a+b}, 0)
//     actualSum = fullArr.reduce((a, b) => a+b, 0)

//     return result = actualSum-sum
// }
// console.log(missingNum([1, 2, 3, 5, 6, 7, 8, 9, 10]))



// function arrReversed(arr) {
//     for (i=0; i<arr.length/2; i++) {
//         reverse = arr[i]
//         arr[i] = arr[arr.length-1-i] 
//         arr[arr.length-1-i] = reverse
//     }
//     return arr
// }
// console.log(arrReversed([1,2,3,4]))



// 31.07.2023
// function repetitiveLetters(arr) {
//     commonLetters = arr.join(' ') 
//     for (word of arr) {
//         str = word
//         commonLetters = new Set([...commonLetters].filter((letter) => str.includes(letter)))
//     }
//     return Array.from(commonLetters)
// }
// console.log(repetitiveLetters(['bella', 'label', 'roller']))
