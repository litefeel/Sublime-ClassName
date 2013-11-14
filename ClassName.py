import sublime
import sublime_plugin
import os
import os.path

class ClassnameCopyCommand(sublime_plugin.WindowCommand):
	def run(self, paths=None):
		if paths:
			file = '*'.join(paths)
		else:
			file = sublime.active_window().active_view().file_name()
		
		if file and len(file) > 0:
			fullname = self.getClassName(file)
			if fullname:
				settings = sublime.load_settings('ClassName.sublime-settings')
				prefix = settings.get('classname_prefix')
				suffix = settings.get('classname_suffix')
				prefix = prefix if prefix else ''
				suffix = suffix if suffix else ''
				fullname = prefix + fullname + suffix
				sublime.set_clipboard(fullname)
				sublime.status_message("Copied class full name: " + fullname)
			else:
				sublime.status_message("Can not find class name")

	def getClassName(self, file):
		folders = sublime.active_window().folders()
		(path, ext) = os.path.splitext(file)
		extLen = len(ext)
		for dir in folders:
			if 0 == file.find(dir):
				fullname = file[len(dir)+1:]
				if extLen > 0:
					fullname = fullname[0:-extLen]
				fullname = fullname.replace(os.sep, '.')
				return fullname
		
		return None



	def is_visible(self, paths=None):
		if paths:
			file = '*'.join(paths)
		else:
			file = sublime.active_window().active_view().file_name()
		return os.path.isfile(file)

class ClassnameCopyPackageCommand(sublime_plugin.WindowCommand):
	def run(self, paths=None):
		if paths:
			file = '*'.join(paths)
		else:
			file = sublime.active_window().active_view().file_name()
		
		if file and len(file) > 0:
			dir = file if os.path.isdir(file) else os.path.dirname(file)
			package = self.getPackage(dir)
			if package:
				sublime.set_clipboard(package)
				sublime.status_message("Copied class package path: " + package)
			else:
				sublime.status_message("Can not find package")

	def getPackage(self, file):
		folders = sublime.active_window().folders()
		for dir in folders:
			if 0 == file.find(dir):
				package = file[len(dir)+1:]
				package = package.replace(os.sep, '.')
				return package
		
		return None


	def is_visible(self, paths=None):
		if paths:
			dir = '*'.join(paths)
			return os.path.isdir(dir)

		return False

