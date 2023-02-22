import sublime
import sublime_plugin
import re

currentRegion = None

class NextCommand(sublime_plugin.TextCommand):

	media_query = None

	def run(self, edit):
		# print(sublime.listener)
		listener = sublime.listener

		if listener is None or not listener.in_extension():
			return

		self.media_query = listener
		# print(self.media_query)
		self.next()

	def next(self):
		global currentRegion
		print(currentRegion)

		# currentRegion = self.media_query.currentRegion()

		matches = self.media_query.generateMatches()
		matches = list(matches)

		regionFirst = matches[0][0]
		regionLast = matches[-1][0]

		if currentRegion is None:
			currentRegion = regionFirst
		
		for (region, text) in matches:
			
			print(currentRegion.a > region.a, currentRegion.a, region.a)
			#self.view.show(sublime.Region(0, 600)) # scroll

			print('matches', currentRegion == regionLast, currentRegion, regionFirst)

			self.view.show(currentRegion)
			self.media_query.highlightMediaRegion(currentRegion)
			if currentRegion.a < region.a:
				currentRegion = region
				return

		if currentRegion == regionLast:
			currentRegion = regionFirst

		"""ПСЕВДОКОД"""

		"""
			
		"""

		# print(list(self.media_query.generateMatches()))
