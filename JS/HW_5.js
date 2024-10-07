//prime numbers
/*for (num=2; num<=100; num++) {
    prime = true
    for (i=2; i<=Math.sqrt(num); i++) {    
        if (num % i===0) {
            prime = false
            break
        }
    }
    if (prime) {
        console.log(num)
    }
}*/

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
}