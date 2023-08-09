
K.L.A.R.A. - Kinetic Language Assistance and Resource Apparatus
# Capstone Concept - Charlie Jung

## Problem Statement #1
A portable and wearable, personal companion for nuero-divergent minds to help with non-verbal communication.
  - non-verbal communication, sometimes you're out of spoons and need to communicate something. Weather you are selective mute, mute or def. Having something to communicate without words is useful. Starting off with emotes as form of communication and even some strings that can display for answering. "Yes", "No", "One second I need to type it out", "I'm def", "I'm taking space". The idea came from a nuero-divergent artist creating pins for communicating things. Like "dont touch me", "I'm non-verbal", "I have ASD".

## Problems to solve if time for additional features
  - reminders through a blinking led, reminders can be hard to sort through and some are more regular or urgent. It can be hard to tell when looking at a chain of notifications. Having something non offensive or overwhelming to que you to check the device yourself for a reminder.
  - sometimes using a phone to help que communication non-verbally can cause tension. A physical device that can display top emotes that is discreet would be helpful. Like when ordering food, you maybe mute or def and the attendent does not know ASL. You could press a button to que that you're def or mute. That you need to take your phone out because you need to communicate without talking. 

## MVP Feature Set

1.  UI
    - A UI to trigger the display of your emotes,using buttons.
2.  Input Field
    - and input field that stores the title of the emote, the src, the emotes purpose and stores it in a database to be pulled through http responesses.

### Potential Additional Features

1.  A capacitive glove that can be worn discreetly to trigger top 16 emotes without using your browser in your phone.
2.  Led Reminder check feature to help you see an important reminder needs to be checked. (like seeing if you took your medication)
3.  BT for mobile app instead of inbrowser

## Draft Technology Choices

- Hardware ESP32(SPI) microcontroller and waveshare 1.27" RGB oled display, using arduino an python libraries
- Full Stack flow, Sql database and react interface
- Stretch feature being a capacitive glove also using an ESP32 microcontroller(SPI) that can display the top 16 emotes

## Additional content, diagrams, wireframes, user flows, etc.
Adafruit for referancing builds
llama hub for incorporoating db's if we get to that point (google calender) 
BT to create an UI on mobile. 

##LONG TERM GOALS( to complete even after capstone)
- The ESP32 has a camera on it that has been used for AI builds. Eventually I'd like to build an ai that starts to learn your habits. Starting with connecting it to a medical db that recognizses pill bottles and pills. Over time I intend to teach Klara how to recognize if I took my medication so that when I forget she can tell me. 
