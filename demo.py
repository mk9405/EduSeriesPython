class Car:
    def __init__(self):
        pass

    def drive(self):
        print("driving..")
    
    def stop(self):
        print("stoped...")

class LandRover(Car):
    def playMusic():
        print("Music playing...")


class RangRover(Car):
    def playMovie():
        print("playMovie...")

class RangRover1(Car):
    def playMovie1():
        print("playMovie...")

lr = LandRover()
print(lr.drive())
