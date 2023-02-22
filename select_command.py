import sublime
import sublime_plugin
import re

class SelectCommand(sublime_plugin.TextCommand):

	media_query = None
	listener = None

	def run(self, edit):
		print(sublime.listener)
		listener = sublime.listener

		if listener is None or not listener.is_extension():
			return

		self.media_query = listener
		self.select(1)

	def select(self, value):
		if value is not None:
			index = 0
			for (region, text) in self.media_query.generateMatches():
				if value == index:
					#self.view.show(sublime.Region(0, 600)) # scroll
					self.view.show(region)
				index+=1

			# print(list(self.media_query.generateMatches()))

	def is_enabled(self):
		return True

	def is_visible(self):
		return True

	def description(self):
		return 'test'

	def input():
		pass