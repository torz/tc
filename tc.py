#!/usr/bin/env python
import os
import urwid

palette = [
    (None,  'light gray', 'black'),
    ('reversed', 'standout', ''),
    ('banner', 'black', 'light gray'),
    ('streak', 'black', 'dark red'),
    ('bg', 'black', 'dark blue'),]


class BrowserPanel(urwid.ListBox):
    def __init__(self):
        self.rootPath = '/'
        self.previousPath = '/'
        self.currentPath = '/'
        self.fileList = sorted(os.listdir(self.currentPath))
        body = self.create_buttons() 
        super(BrowserPanel, self).__init__(body)

    def update_file_list(self, choice):
        if choice == '..':
            newPath = os.path.dirname(self.currentPath)
        else:
            newPath = os.path.join(os.path.join(self.currentPath, choice))
        if os.path.isdir(newPath):
            self.previousPath = self.currentPath
            self.currentPath = newPath
        try:
            self.fileList = os.listdir(self.currentPath)
        except:
            self.currentPath = self.previousPath
            self.fileList = os.listdir(self.currentPath)
        if self.currentPath != '/':
            self.fileList.insert(0, '..')

    def create_buttons(self):
        body = [urwid.Text(self.currentPath), urwid.Divider()]
        for oneFile in sorted(self.fileList):
            button = urwid.Button(oneFile)
            if os.path.isdir(os.path.join(self.currentPath, oneFile)):
                urwid.connect_signal(button, 'click', self.update_body, oneFile)
            body.append(urwid.AttrMap(button, None, focus_map='reversed'))
        return urwid.SimpleFocusListWalker(body)
    
    def update_body(self, button, choice):
        self.update_file_list(choice)
        self.body = self.create_buttons()

                
#class MainFrame(urwid.Frame):
#    def __init__():

def exit_program(button):
    if button == 'q':
        raise urwid.ExitMainLoop()

def main():
    main = BrowserPanel()
    loop = urwid.MainLoop(main, palette, unhandled_input=exit_program)
    loop.run()

if __name__ == '__main__':
    main()

