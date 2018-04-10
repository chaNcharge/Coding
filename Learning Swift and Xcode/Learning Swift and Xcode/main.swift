//
//  main.swift
//  Learning Swift and Xcode
//
//  Created by Ethan Cha on 4/5/18.
//  Copyright © 2018 Ethan Cha. All rights reserved.
//
import Foundation


// If statements
print("Are you old enough?")

let minimum_age = 18
let current_age1 = Int(readLine()!)! // readLine similar to Python input()

if current_age1 < minimum_age {
    print("You are not old enough!")
} else {
    print("You are old enough!")
}

// Loops
print("Repeatedly multiplying!")
sleep(2)

for i in 1 ... 20 {
    print(i * 2)
}
