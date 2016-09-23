
/*
 * Lesson 1 - Introduction to the development environment
 */

//Every line of code needs to be terminated by a semi-colon - ';'

// Required for any Arduino sketch
#include <Arduino.h> 

//Neopixel library that allows us to control the lights
#include <Adafruit_NeoPixel.h> 

// Number of LEDs in NeoPixel strip that you want to control
// You may not be able to control all the LEDs on a strip if you have a tiny board
// The Adafruit Gemma can not control more than 107, but you should not really go above 40
#define NUM_LEDS      17 

// NeoPixels are connected to this pin on the board
#define LED_DATA_PIN   1 

//Let the program know what kind of strip it is dealing with and how it is connected
Adafruit_NeoPixel    strip(NUM_LEDS, LED_DATA_PIN);

void setup() {
  // Allocate NeoPixel buffer
  // This sets up the LED strip
  strip.begin();               
}

void loop() {
  // Set the color of a particular pixel
  // Parameter 1: The number of the pixel you want to control
  // Parameter 2: Intensity of the red LED
  // Parameter 3: Intensity of the green LED
  // Parameter 4: Intensity of the blue LED
  strip.setPixelColor(1, 0, 0, 255); 
  strip.setPixelColor(2, 0, 0, 255); 
  strip.setPixelColor(3,  0, 0, 255); 
  strip.setPixelColor(4,  0, 0, 255); 
  strip.setPixelColor(5, 255, 255, 255); 
  strip.setPixelColor(6, 255, 255, 255); 
  strip.setPixelColor(7, 255, 255, 255); 
  strip.setPixelColor(8, 255, 250, 0); 
  strip.setPixelColor(9, 255, 250, 0); 
  strip.setPixelColor(10, 255, 255, 255); 
  strip.setPixelColor(11, 255, 255, 255); 
  strip.setPixelColor(12, 255, 255, 255); 
  strip.setPixelColor(13,  0, 0, 255); 
  strip.setPixelColor(14,  0, 0, 255); 
  strip.setPixelColor(15,  0, 0, 255); 
  strip.setPixelColor(16,  0, 0, 255); 
  strip.setPixelColor(17,  0, 0, 255); 
 

  // After you have set the values, this turns the pixels on
  strip.show();
}



