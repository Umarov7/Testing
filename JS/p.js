function T(num) {
    for (i = 1; i <= num; i++) {
        pattern = "" 

        for (j = 1; j <=num; j++)
        pattern += "* "

        console.log(pattern)
    }
}
T(5)


function Simple_Pyramid(rows) {
    for (i = 1; i <= rows; i++) {
        pattern = "" 

        for (j = 1; j <= i; j++) {
            pattern += "* " 
        }

        console.log(pattern)
    }
}
Simple_Pyramid(5)

function Rotated_Simple_Pyramid(rows) {
    for (i = 1; i <= rows; i++) {
        pattern = "" 

        for (j = 1; j <= rows - i; j++) {
            pattern += "  "
        }

        for (k = 1; k <= i; k++) {
            pattern += "* "
        }

        console.log(pattern)
    }
}
Rotated_Simple_Pyramid(5)

function Inverted_Pyramid(rows) {
    for (i = rows; i >= 1; i--) {
        pattern = ""

        for (j = 1; j <= i; j++) {
            pattern += "* "
        }
        
        console.log(pattern)
    }
}
Inverted_Pyramid(5)

function Rotated_Inverted_Pyramid(rows) {
    for (i = rows; i >= 1; i--) {
        pattern = "" 

        for (j = 1; j <= rows - i; j++) {
            pattern += "  "
        }

        for (k = 1; k <= i; k++) {
            pattern += "* "
        }

        console.log(pattern)
    }
}
Rotated_Inverted_Pyramid(5)

function Triangle(rows) {
    for (i = 1; i <= rows; i++) {
        pattern = ""

        for (j = 1; j <= rows - i; j++) {
            pattern += " "
        }

        for (k = 1; k <= i; k++) {
            pattern += "* "
        }

        console.log(pattern)
    }
}
Triangle(5)
function Triangle_Pyramid(rows) {
    for (let i = 1; i <= rows; i++) {
        let pattern = ""
        
        for (let j = 1; j <= rows - i; j++) {
            pattern += " "
        }
        
        for (let k = 1; k <= i * 2 - 1; k++) {
            pattern += "*"
        }
        
        console.log(pattern)
    }
}
Triangle_Pyramid(5)

function Inverted_Triangle(rows) {
    for (i = rows; i >= 1; i--) {
        pattern = ""

        for (j = 1; j <= rows - i; j++) {
            pattern += " "
        }

        for (k = 1; k <= i; k++) {
            pattern += "* "
        }

        console.log(pattern)
    }
}
Inverted_Triangle(5)
function Inverted_Triangle_Pyramid(rows) {
    for (i = rows; i >= 1; i--) {
        pattern = ""

        for (j = 1; j <= rows - i; j++) {
            pattern += " "
        }

        for (k = 1; k <= i * 2 - 1; k++) {
            pattern += "*"
        }

        console.log(pattern)
    }
}
Inverted_Triangle_Pyramid(5)

function Number_Pyramid(rows) {
    for (i = 1; i <= rows; i++) {
        pattern = ''

        for (j = 1; j <= i; j++) {
            pattern += i + ' '
        }

        console.log(pattern)
    }
}
Number_Pyramid(4)

function Continuous_Number_Pyramid(rows) {
    let number = 1

    for (i = 1; i <= rows; i++) {
        pattern = ''

        for (j = 1; j <= i; j++) {
            pattern += number + ' '
            number++
        }

        console.log(pattern)
    }
}
Continuous_Number_Pyramid(4)

function Rotated_Number_Pyramid (rows) {
    let number = 1

    for (i = 1; i <= rows; i++) {
        pattern = ''

        for (j = 1; j <= rows - i; j++) {
            pattern += '  '
        }

        for (k = 1; k <= i; k++) {
            pattern += number + ' '
            number++
        }

        console.log(pattern)
    }
}
Rotated_Number_Pyramid (4)

function Palindrome_Triangle(rows) {
    let number = 1

    for (i = 1; i <= rows; i++) {
        pattern = ''

        for (j = 1; j <= rows - i; j++) {
            pattern += ' '
        }

        for (k = 1; k <= i; k++) {
            pattern += number + ' '
            number++
        }

        console.log(pattern)
    }
}
Palindrome_Triangle(4)

function Alphabet_Pyramid(rows) {
    let letters = 'ABCD'

    for (i = 0; i < rows; i++) {
        pattern = ''

        for (j = 0; j <= i; j++) {
            pattern += letters[i] + ' '
        }

        console.log(pattern)
    }
}
Alphabet_Pyramid(4)

function Continuous_Alphabet_Pyramid(rows) {
    let letters = 'ABCDEFGHIJ'
    let letter_index = 0
    
    for (i = 1; i <= rows; i++) {
        pattern = ''

        for (j = 1; j <= i; j++) {
            pattern += letters[letter_index % letters.length] + ' '
            letter_index++
        }

        console.log(pattern)
    }
}
Continuous_Alphabet_Pyramid(4)
