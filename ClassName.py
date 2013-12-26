import sublime
import sublime_plugin
import os
import os.path

class ClassNameCommand(sublime_plugin.WindowCommand):
	def getFilePath(self, paths=None):
		if paths:
			file = '*'.join(paths)
		else:
			view = sublime.active_window().active_view()
			file = view.file_name() if view else None
		return file


class ClassnameCopyCommand(ClassNameCommand):
	def run(self, paths=None):
		file = self.getFilePath(paths)
		fullname = self.getClassName(file) if file else None
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
		if not file:
			return None

		folders = sublime.active_window().folders()
		(path, ext) = os.path.splitext(file)
		extLen = len(ext)
		for dir in folders:
			if 0 == file.find(dir):
				fullname = file[len(dir)+1:]
				if extLen > 0:
					fullname = fullname[0:-extLen]
				fullname = fullname.replace(os.sep, sublime.load_settings('ClassName.sublime-settings').get('namespace_separator'))
				return fullname

		return None



	def is_visible(self, paths=None):
		file = self.getFilePath(paths)
		return os.path.isfile(file) if file else False

class ClassnameCopyPackageCommand(ClassNameCommand):
	def run(self, paths=None):
		file = self.getFilePath(paths)
		package = self.getPackage(file) if file else None
		if package:
			sublime.set_clipboard(package)
			sublime.status_message("Copied class package path: " + package)
		else:
			sublime.status_message("Can not find package")

	def getPackage(self, file):
		file = file if os.path.isdir(file) else os.path.dirname(file)
		folders = sublime.active_window().folders()
		for dir in folders:
			if 0 == file.find(dir):
				package = file[len(dir)+1:]
				package = package.replace(os.sep, sublime.load_settings('ClassName.sublime-settings').get('namespace_separator'))
				return package

		return None
