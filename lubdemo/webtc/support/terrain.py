from lettuce import *
from selenium import webdriver

@before.each_scenario
def startupdriver(scenario):
        world.browser=webdriver.Firefox()
