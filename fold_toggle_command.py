import sublime
import sublime_plugin

from CSSMediaQuery.main import Plugin

class FoldToggleCommand(sublime_plugin.TextCommand):

	foldFlag = False

	def run(self, edit):
		regions = self.view.get_regions('regions-media')

		if len(regions) == 0:
			print('Not regions', self.__class__)
			return

		prevSel = self.view.sel();
		prevSelRegions = list(self.view.sel());
		# print(list(prevSelRegions))

		self.view.sel().clear()
		for region in regions:
			r = sublime.Region(region.b, region.b)
			self.view.sel().add(r)
			
		# print(list(self.view.sel()))

		if len(self.view.sel()) > 0:
			self.view.run_command('expand_selection', {'to': 'brackets'})
			
			if self.foldFlag:
				command = 'unfold'
				self.foldFlag = False
			else:
				command = 'fold'
				self.foldFlag = True

			self.view.run_command(command)

		self.view.sel().clear()
		# print(prevSelRegions)
		self.view.sel().add_all(prevSelRegions)

	def get_regions(self):
		return self.view.get_regions('regions-media')

	def is_regions(self):
		regions = self.get_regions()
		return len(regions) > 0

	# Visible in command palette menu
	def is_visible(self):
		regions = self.view.get_regions('regions-media')
		return self.is_regions()
		# return True

	def is_enabled(self):
		settings = Plugin.load_settings()
		Plugin.settings = settings

		return self.is_regions() and Plugin.view_active_in_extension()
		# return True