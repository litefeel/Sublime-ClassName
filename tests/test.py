import sublime
import sys
import tempfile
import os, os.path
from unittest import TestCase

version = sublime.version()


class stderrobj:
    def __init__(self):
        self.buff=''
        self.__console__=sys.stderr
        sys.stderr = self
        
    def write(self, output_stream):
        self.buff+=output_stream

    def empty(self):
        return self.buff == ''

    def reset(self):
        if self.__console__ is not None:
            sys.stderr = self.__console__
            self.__console__ = None


# for testing sublime command
class TestClassName(TestCase):

    def setUp(self):
        self.view = sublime.active_window().new_file()
        # make sure we have a window to work with
        s = sublime.load_settings("Preferences.sublime-settings")
        s.set("close_windows_when_empty", False)

        self.packagename = 'testclassname'
        self.classname = 'testclassname.classname'

        basedir = tempfile.TemporaryDirectory().name
        filedir = basedir + '/' + self.packagename
        filename = filedir + '/classname.txt'

        os.makedirs(filedir, exist_ok = True)
        with open(filename, 'w') as f:
            f.write('this is test file')

        # add an folders to sublime text
        d = {"folders":[{"path":basedir}]}
        sublime.active_window().set_project_data(d)

        self.view = sublime.active_window().open_file(filename)
        self.view.window().focus_view(self.view)

        self.obj = stderrobj()

    def tearDown(self):
        self.obj.reset()
        if self.view:
            self.view.set_scratch(True)
            self.view.window().focus_view(self.view)
            self.view.window().run_command("close_file")

        self.assertTrue(self.obj.empty(), self.obj.buff)

    def test_copy_package(self):
        sublime.set_clipboard("this is clipboard text");
        self.view.window().run_command("classname_copy_package")
        self.assertEqual(self.packagename, sublime.get_clipboard())

    def test_copy_classname(self):
        sublime.set_clipboard("this is clipboard text");
        self.view.window().run_command("classname_copy")
        self.assertEqual(self.classname, sublime.get_clipboard())

