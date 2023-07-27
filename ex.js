function sortObjects(arr) {
    arr.sort(function (a, b) {return a.age-b.age})
    return arr
}
console.log(sortObjects([{name: 'John', age:25}, {name: 'Mark', age:18}, {name: "David", age:16}, {name: "Tom", age:36}]))

function sumNums(arr) {
    numbers = arr.filter(function (item) {return !isNaN (item) && typeof item === 'number'})
    sum = numbers.reduce(function (a, b) {return a+b}, 0)
    return sum
}
console.log(sumNums([1, 2, 'Hello', 5, "World"]))