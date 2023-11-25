import os, sys, datetime, time, json, itertools, threading, pygame as pg, random, decimal

class TimeController:
    def __init__(self, app):
        self.app = app
        self.colors = itertools.cycle([(0.29, 0.195, 2.40), (0.1,0.1,0.1)])
        self.time = 0000 

        self.started = False

        self.midnight = 0000
        self.midday = 1200
        self.noon = 700
        self.afternoon = 100

        self.FPS = 60

        self.increment = 1
        self.incrementPerSecond = 1

        self.base_color = next(self.colors)
        self.next_color = next(self.colors)
        self.current_color = self.base_color  

    def runs(self):
        self.started = True
        def r():
            while self.started:
                self.time += self.increment
                if self.time >= 2400 and self.time < 4800:
                    self.settime()
                elif self.time >= 4800:
                    self.time = 0
                    self.settime()

                #print(self.time)
                #while (self.time < 1200):
                    #print(self.time)
                    #if self.time == 1159:
                        #self.time = 0000
                    # day cycle
                    #time.sleep(0.1)
                    #self.time += self.increment

                    #self.settime()

        threading.Thread(target=r, args=(), daemon=True).start()
        return self
    
    def stops(self):
        self.started = False
        return self
    
    def settime(self):
        number_of_steps = self.increment * self.FPS
        if self.time < number_of_steps:
            # (y-x)/number_of_steps calculates the amount of change per step required to 
            # fade one channel of the old color to the new color
            # We multiply it with the current step counter
            self.current_color = [x + (((y-x)/number_of_steps)*self.time) for x, y in zip(pg.Color(self.base_color), pg.Color(self.next_color))]
        else:
            self.base_color = self.next_color
            self.next_color = next(self.colors)
        #self.app.ctx.clear(color=self.current_color)


    def get_calc_c(self):
        return self.current_color
        #return pg.Color(self.c1,self.c2,self.c3)