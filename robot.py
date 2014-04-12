import drive
import nxt


class Robot:
    def __init__(self):
        self.b = nxt.find_one_brick()
        self.leftWheel = drive.Drive(self.b, nxt.PORT_B)
        self.rightWheel = drive.Drive(self.b, nxt.PORT_C)

        self.leftWheel.SetParam(1, 1, 1)
        self.rightWheel.SetParam(1, 1, 1)

        self.leftWheel.start()
        self.rightWheel.start()


    def resetData(self):
        self.leftWheel.stop()
        self.leftWheel.join()

        self.rightWheel.stop()
        self.rightWheel.join()

        self.leftWheel = drive.Drive(self.b, nxt.PORT_B)
        self.rightWheel = drive.Drive(self.b, nxt.PORT_C)
    def __turnLeft(self):
        self.resetData()

        self.leftWheel.SetParam(-1, degree=10)
        self.rightWheel.SetParam(1, degree=10)

        self.leftWheel.start()
        self.rightWheel.start()

    def __turnRight(self):
        self.resetData()

        self.leftWheel.SetParam(1, degree=10)
        self.rightWheel.SetParam(-1, degree=10)

        self.leftWheel.start()
        self.rightWheel.start()

    def __moveForward(self):
        self.resetData()

        self.leftWheel.SetParam()
        self.rightWheel.SetParam()

        self.leftWheel.start()
        self.rightWheel.start()

    def __stop(self):
        self.resetData()

        self.leftWheel.SetParam(1, 1, 1)
        self.rightWheel.SetParam(1, 1, 1)

        self.leftWheel.start()
        self.rightWheel.start()

    def doCommand(self, cmd):
        if cmd == "2":
            self.__turnLeft()
        elif cmd == "3":
            self.__turnRight()
        elif cmd == "4":
            self.__moveForward()
        elif cmd == "5":
            self.__stop()