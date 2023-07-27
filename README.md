# Foundation

function sortObjects(arr) {
    arr.sort(function (a, b) {return a.age-b.age})
    return arr
}
console.log(sortObjects([{name: 'John', age:25}, {name: 'Mark', age:18}, {name: "David", age:16}, {name: "Tom", age:36}]))
