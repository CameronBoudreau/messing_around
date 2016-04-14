import time
from Quartz.CoreGraphics import *
​
​
def mouse_event(type, posx, posy):
    the_event = CGEventCreateMouseEvent(
        None, type, (posx, posy), kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, the_event)
​
​
def mouse_move(posx, posy):
    mouse_event(kCGEventMouseMoved, posx, posy)
​
​
def mouse_click_down(posx, posy):
    mouse_event(kCGEventLeftMouseDown, posx, posy)
​
​
def mouse_click_up(posx, posy):
    mouse_event(kCGEventLeftMouseUp, posx, posy)
​
​
def mouse_drag(posx, posy):
    mouse_event(kCGEventLeftMouseDragged, posx, posy)
​
​
def main():
    our_event = CGEventCreate(None)
    current_pos = CGEventGetLocation(our_event)
    mouse_click_down(60, 100)
    mouse_drag(60, 300)
    mouse_click_up(60, 300)
    time.sleep(1)
    mouse_move(int(current_pos.x), int(current_pos.y))
​
​
if __name__ == '__main__':
    main()
