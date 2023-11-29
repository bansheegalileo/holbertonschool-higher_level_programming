#!/usr/bin/node

const argument = process.argv[2];
const numberOfOccurrences = parseInt(argument);

if (!isNaN(numberOfOccurrences)) {
    for (let i = 0; i < numberOfOccurrences; i++) {
        console.log("C is fun");
    }
} else {
    console.log("Missing number of occurrences");
}
