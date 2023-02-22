import sublime
import sublime_plugin
import re

from .main import Plugin

class PanelCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		print(sublime.listener)
		listener = sublime.listener

		listener.quick_panel_medias()

	def is_enabled(self):
		return Plugin.view_active_in_extension()

	def is_checked(self):
		return False

	def description(self):
	    return "Media Query Panel"

	def want_event(self):
	    return False

	def input(self, args):
		print('Panel command input method', args)
		return None

	def input_description(self):
	    return "sssssssssssssss"

	# def create_input_handler_(self, args):
	#     return self.input(args)