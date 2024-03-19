from PySide2.QtWidgets import QInputDialog

def show_command_dialog(accept_text, cancel_text):
    command, ok = QInputDialog.getText(None, "Execute Command", "Enter the command:")
    if ok:
        print(accept_text, command)
        return command
    else:
        print(cancel_text)
        return None