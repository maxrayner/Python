# Boxing Simulator Python Terminal Game

## About

I recently started learning python's objective-oriented programming (OOP) so decided to practice by making a boxing game structuring it using classes and also learning about private and public access modifiers (name mangling and default settings). There are many different attacks and defences (jabs, hooks, blocks, parrys) to experiment with and you can create your own profile with a different amount of health, defence and power depending on your preference. 

## Research

I updated my repositories on github a few weeks ago, so I had to research how to update those commits locally (fetch and pull). Furthermore, I had to understand how private access modifiers work and therefore what methods are needed to access those attributes (getter and setter methods). 


## How It Works

This program is structured using the paradigm of OOP. It has three main classes (Boxer, Attack and Defence) with two subclasses of boxers (speed vs power). You can also customise your profile using the options provided at the start. 

You can fight a computer opponent or a friend (by sharing the terminal together). There are 12 rounds lasting of 6-10 exchanges of defences/punches or if someone gets knocked out or submits (forfeits). There are a range of attacks and defences as listed below which have different powers and defensive abilities yet comes with the price of your stamina, so you have to think tactically about what defence/attack to go with. There is an element of randomness/luck as if your punch/defence is successful is partially decided using the library random. 

Attacks:
* Jab
* Straight
* Lead Hook
* Rear Hook
* Lead Uppercut
* Rear Uppercut

Defences:
* Slip
* Parry
* Roll
* Dip (ducking)
* Weaving (bobbing/weaving)
* Footwork (moving away using feet)
* Blocking
* Clinching

## Technologies

* Python
* Git   

## What I Learned

* Using OOP
* Inheritance
* Composition
* Aggregation
* Classes and objects
* Access modifiers
* Attributes
* Polymorphism
* Encapsulation
* Structuring code


## Limitations

Uses randomness so not all done on skill

## Future Improvements

* Add more attacks and defences
* Possibly make a GUI to make it more interactive
* Add sound effects
