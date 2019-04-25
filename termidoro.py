#!/usr/local/bin/python3

import time
import os

def open_webpage(webpage):
   os.system("open {}".format(webpage))

def clear_screen():
    print("\033[H\033[J")

def countdown(t, message, extra_message=""):
    while t > -1:
        mins, secs = divmod(t, 60)
        timeformat = '{}{} for {:02d}:{:02d}'.format(message, extra_message, mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

    clear_screen()

def setup():
    work_period = int(input("How long to WORK for? "))
    rest_period = int(input("How long to REST for? "))
    work_task = " on " + input("What are you working on? ")

    return work_period, rest_period, work_task

def main():
    clear_screen()
    work_period, rest_period, work_task = setup()
    clear_screen()

    while True:
        countdown(work_period, "Work", work_task)
        open_webpage("https://en.wikipedia.org/wiki/Special:Random")
        countdown(rest_period, "Rest")
        open_webpage("https://tenor.com/view/back-to-work-gif-5800644")

if __name__ == '__main__':
    main()
