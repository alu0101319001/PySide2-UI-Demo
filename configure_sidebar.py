# -*- coding: utf-8 -*-
#!/usr/bin/python

from section_widget import SectionWidget
from show_command_dialog import show_command_dialog

def printFunction(func):
    def inner():
        print(func)
    return inner


def build_state_section():
    state_section = SectionWidget("States")
    state_section.addButton("Power ON ALL", printFunction("Turning on..."))
    state_section.addButton("Power OFF ALL", printFunction("Turning off..."))
    state_section.addButton("ACTIVATE EXAM MODE", printFunction("EXAM MODE ACTIVATED"))
    state_section.addButton("DESACTIVATE EXAM MODE", printFunction("EXAM MODO DESACTIVATED"))
    return state_section


def build_orders_section():
    order_section = SectionWidget("Orders")
    order_section.addButton("Apt ALL", printFunction("Applyn apt for all PCs"))
    order_section.addButton("Execute a command for all PCs", lambda: show_command_dialog("Executing: ", "Command canceled"))
    return order_section