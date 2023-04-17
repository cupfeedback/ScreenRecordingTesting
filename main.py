from pynput import keyboard, mouse
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import time
import tkinter as tk
import threading


# 이벤트 리스트
events = []


# 키보드와 마우스 이벤트 핸들러
def on_keyboard_event(key):
    events.append(('keyboard', key))
    print(events)


def on_mouse_event(x, y, button, pressed):
    events.append(('mouse', x, y, button, pressed))
    print(events)


# 이벤트 리스너 스레드 정의
def listen_events():
    with mouse.Listener(on_move=on_mouse_event, on_click=on_mouse_event, on_scroll=on_mouse_event) as mouse_listener:
        with keyboard.Listener(on_press=on_keyboard_event, on_release=on_keyboard_event) as keyboard_listener:
            mouse_listener.join()
            keyboard_listener.join()

# 이벤트 기록 시작
def start_recording():
    events.clear()
    with keyboard.Listener(on_press=on_keyboard_event) as keyboard_listener, \
            mouse.Listener(on_click=on_mouse_event) as mouse_listener:
        keyboard_listener.join()
        mouse_listener.join()


# 이벤트 기록 중지
def stop_recording():
    mouse.Listener.stop()
    keyboard.Listener.stop()
    # 스레드 종료 대기
    # mouse_listener_thread.join()
    # keyboard_listener_thread.join()


# 매크로 실행
def run_macro():
    mouse_controller = MouseController()
    keyboard_controller = KeyboardController()

    for event in events:
        event_type = event[0]
        if event_type == 'keyboard':
            key = event[1]
            if isinstance(key, Key):
                # Key 객체일 경우
                if key == Key.space:
                    keyboard_controller.press(Key.space)
                    keyboard_controller.release(Key.space)
                else:
                    keyboard_controller.press(key)
            else:
                # 문자일 경우
                keyboard_controller.type(key)
        elif event_type == 'mouse':
            x = event[1]
            y = event[2]
            button = event[3]
            pressed = event[4]
            if pressed:
                mouse_controller.position = (x, y)
                if button == Button.left:
                    mouse_controller.press(Button.left)
                elif button == Button.right:
                    mouse_controller.press(Button.right)
            else:
                if button == Button.left:
                    mouse_controller.release(Button.left)
                elif button == Button.right:
                    mouse_controller.release(Button.right)

    events.clear()


# GUI 생성
root = tk.Tk()
root.title("매크로 레코더")
root.geometry('300x200')

# mouse.Listener 객체 생성
# mouse_listener = mouse.Listener(
#     on_move=on_mouse_event,
#     on_click=on_mouse_event,
#     on_scroll=on_mouse_event
# )

# keyboard.Listener 객체 생성
# keyboard_listener = keyboard.Listener(
#     on_press=on_keyboard_event,
#     on_release=on_keyboard_event
# )

# 스레드 생성
# mouse_listener_thread = threading.Thread(target=mouse_listener.run)
# keyboard_listener_thread = threading.Thread(target=keyboard_listener.run)

event_thread = threading.Thread(target=listen_events)
event_thread.start()

# 이벤트 리스너 생성
with mouse.Listener(on_move=None, on_click=on_mouse_event, on_scroll=None) as mouse_listener:
    mouse_listener.join()


# 버튼 생성
start_button = tk.Button(root, text="레코딩 시작", command=start_recording)
start_button.pack()

stop_button = tk.Button(root, text="레코딩 중지", command=stop_recording)
stop_button.pack()

run_button = tk.Button(root, text="매크로 실행", command=run_macro)
run_button.pack()


# GUI 실행
root.mainloop()
