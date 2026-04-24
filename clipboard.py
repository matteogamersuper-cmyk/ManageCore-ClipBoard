import pyperclip

def get_clipboard():
    return pyperclip.paste()

def set_clipboard(text):
    pyperclip.copy(text)