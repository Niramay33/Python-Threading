from threading import *

import time


class RacingCircuit:

    def busyTracks(self):

        t = current_thread()

        print("{} Entered Busy Tracks".format(t.name))

        while (RacingCircuit.lap < 5):

            if (t.name == "Car"):

                print("brrrommsss")

            else:

                print("vrrrommsss")

            time.sleep(1)

            RacingCircuit.lap += 1

            print("Lap = {}".format(RacingCircuit.lap))

        RacingCircuit.lap = 0

        print("{} Leaving Busy Tracks".format(t.name))


RacingCircuit.lap = 0


class Bike(Thread):

    def __init__(self):
        Thread.__init__(self, name="Bike")

    def run(self):
        print("Bike Starts Journey")

        b = RacingCircuit()

        b.busyTracks()

        print("Bike Ends Journey")


class Car(Thread):

    def __init__(self):
        Thread.__init__(self, name="Car")

    def run(self):
        print("Car Starts Journey")

        a = RacingCircuit()

        a.busyTracks()

        print("Car Ends Journey")


mycar = Car()

mycar.start()

mybike = Bike()

mybike.start()
