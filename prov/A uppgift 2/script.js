function scrabbleScore(word) {
    let points = 0; //Skapar variabeln points och sätter den til startvärdet 0
    arr = word.split(""); //Gör om ordet till en lista
    for (let i = 0; i < arr.length; i++) { //Går igenom alla bokstäver i ordet som nu är en lista och ger ökar den totala poängen beroende på vilken bokstav som är i varje index
        if (arr[i] == "a") {
            points += 1
        }
        else if (arr[i] == "e") {
            points += 1
        }
        else if (arr[i] == "i") {
            points += 1
        }
        else if (arr[i] == "o") {
            points += 1
        }
        else if (arr[i] == "u") {
            points += 1
        }
        else if (arr[i] == "l") {
            points += 1
        }
        else if (arr[i] == "n") {
            points += 1
        }
        else if (arr[i] == "r") {
            points += 1
        }
        else if (arr[i] == "s") {
            points += 1
        }
        else if (arr[i] == "t") {
            points += 1
        }
        else if (arr[i] == "d") {
            points += 2
        }
        else if (arr[i] == "g") {
            points += 2
        }
        else if (arr[i] == "b") {
            points += 3
        }
        else if (arr[i] == "c") {
            points += 3
        }
        else if (arr[i] == "m") {
            points += 3
        }
        else if (arr[i] == "p") {
            points += 3
        }
        else if (arr[i] == "f") {
            points += 4
        }
        else if (arr[i] == "h") {
            points += 4
        }
        else if (arr[i] == "v") {
            points += 4
        }
        else if (arr[i] == "W") {
            points += 4
        }
        else if (arr[i] == "y") {
            points += 4
        }
        else if (arr[i] == "k") {
            points += 5
        }
        else if (arr[i] == "j") {
            points += 8
        }
        else if (arr[i] == "x") {
            points += 8
        }
        else if (arr[i] == "q") {
            points += 10
        }
        else if (arr[i] == "z") {
            points += 10
        }
    }
    console.log("Poäng: " + points) //Skriver ut poängen som ordet är värt
}

scrabbleScore("cabbage"); //Kör funktionen