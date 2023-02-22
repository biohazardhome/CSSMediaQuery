import sublime
import sublime_plugin
# import compile_regex
import os
import re
import string



"""
Загрузка пакета
* Разобраться как прописать названия комманд плагина в Command Palette
@ Сгрупировать все блоки медиа кроме активного (на который кликаем по региону) как аккардион
@ Поиск по css селектору в разных медиа
	Найти все медиа в них css селектор в списоке выбрать нужный 

Выделение блока медиа полностью
Перемотать до верхнего или нижнего блока медиа
Список блоков медиа


Вызов списка
	По сочитанию клавиш 
	По пункту меню
	По клику на регион
"""


# from CSSMediaQuery.select_command import SelectCommand
# from CSSMediaQuery.next_command import NextCommand
# from CSSMediaQuery.panel_command import PanelCommand
# from CSSMediaQuery.fold_toggle_command import FoldToggleCommand



class Plugin():

	SETTINGS_FILE_NAME = 'CSSMediaQuery.sublime-settings'
	settings = []
	# settings = {}
	
	def __init__(self, window):
		self.window = window

	def init():
		Plugin.load_settings()
		# self.load_settings()

	def load_settings():
		Plugin.settings = sublime.load_settings(Plugin.SETTINGS_FILE_NAME)
		return Plugin.settings

		# self.settings = sublime.load_settings(self.SETTINGS_FILE_NAME)
		# return self.settings

	# def load_settings(self):
	# 	self.settings = sublime.load_settings(self.SETTINGS_FILE_NAME)
	# 	# print(self.settings.get('file_extensions'))
	# 	return self.settings

	def reload_settings(self):
		pass

	# @classmethod
	@staticmethod
	def get_windows():
		return sublime.windows()

	@staticmethod
	def get_active_window():
		return sublime.active_window()

	@staticmethod
	def get_active_view():
		return sublime.active_window().active_view()

	@classmethod
	def view_in_extension(cls, view):
		extension = cls.view_file_extension(view)
		return cls.in_extension(extension)

	@classmethod
	def view_file_extension(cls, view):
		file_name = view.file_name()
		# print(file_name)
		if file_name is None:
			return None

		segments = os.path.splitext(file_name)
		extension = segments[1]
		extensionWithoutDot = extension[1:]
		return extensionWithoutDot

	@classmethod
	def in_extension(cls, extension):
		# print(cls.settings.get('file_extensions'))
		extensions = cls.settings.get('file_extensions')
		# print(extension, extensions)
		return extension in extensions

	# 
	@classmethod
	def view_active_in_extension(cls):
		extension = cls.view_active_file_extension()
		# print(extension)
		return cls.in_extension(extension)

	# Get extension filename for active view
	@classmethod
	def view_active_file_extension(cls):
		winVars = cls.get_active_window().extract_variables()
		# print(winVars)
		extension = winVars.get('file_extension')
		# print(extension)
		return extension

class CssMediaQueryListener(sublime_plugin.ViewEventListener):
# class CssMediaQueryListener(object):

	def __init__(self, view):
		# super(CssMediaQueryListener, self).__init__(view)
		# super().__init__(view)
		print('__init__')

		self.view = view
		self.window = view.window()
		# self.settings = []

		# self.finded = []
		# self.regions = []

		# self.load_settings()
		
	@classmethod
	def is_applicable(cls, settings):		
		return Plugin.view_active_in_extension()

	@classmethod
	def applies_to_primary_view_only(cls):
	    return True

	def decorator_logging_name_method(func):
		def wrapper(self, *args, **kwargs):
			print(func.__name__)

			return func(self, *args, **kwargs)
		return wrapper

	# def decorator_extension_limit(func):
	# 	def wrapper(self, *args, **kwargs):
	# 		# print(self.in_extension())
	# 		if not self.in_extension():
	# 			return None

	# 		return func(self, *args, **kwargs)
	# 	return wrapper

	# @decorator_extension_limit
	def on_init(self):
		print('on_init')

	# @decorator_extension_limit
	def on_load(self):
		print('on_load')
		
		# self.view.insert(edit, 0, "Hello, World!")
		# print(123, self.window)
		# self.window.status_message('123')

		self.statusNearestMedia()
		self.highlightMediaRegions(regionHighlight = True)

	# @decorator_extension_limit
	@decorator_logging_name_method
	def on_activated(self):
		print('on_activated')

		sublime.listener = self

		self.statusNearestMedia()
		self.highlightMediaRegions(regionHighlight = True)

	# @decorator_extension_limit
	def on_modified(self):
		print('on_modified')

		self.statusNearestMedia()
		self.highlightMediaRegions(regionHighlight = True)

	# @decorator_extension_limit
	def on_selection_modified(self):
		print('on_selection_modified')

		self.statusNearestMedia()
		self.highlightMediaRegions(regionHighlight = True)

		# s = self.view.get_regions('regions-media');
		# print(s)

	def in_extension(self):
		extension = self.file_extension()
		# extensions = self.settings.get('file_extensions')
		# print(file_extension, extensions)
		# return extension in extensions
		return Plugin.in_extension(extension)

	def file_extension(self):
		winVars = self.window.extract_variables()
		# print(winVars)
		file_extension = winVars.get('file_extension')
		# print(file_extension)
		return file_extension

	def statusNearestMedia(self):
		currentRegion = self.currentRegion()
		# print(currentRegion)
		line = self.searchNearestRegion(currentRegion)
		# print(line)
		# match = re.match(r'\@media.*?(?=\{)', line, re.I | re.M)
		# print(match)
		# if match:
			# line = match.group(0)
		self.view.set_status('media_query', line)

	def searchMediaRegions(self):
		return [region for (region, text) in self.generateMatches()]

	def highlightMediaRegions(self, regions=None, regionHighlight=False):
		# print(regions)
		regions = self.searchMediaRegions()
		
		self.view.erase_regions('regions-media')

		regionColor = ''
		regionIcon = ''

		if regionHighlight:
			regionColor = 'region.orangish'
			regionIcon = 'dot'

		self.view.add_regions( # highlight lines
            'regions-media', 
            regions, 
            regionColor, 
            regionIcon,
            #0, # sublime.HIDDEN, sublime.PERSISTENT
            # 'white'
            # '<a href="#">123</a>',
        )

		# fold = self.view.fold(regions)
		# print(fold)
		

	def highlightMediaRegion(self, region):
		self.view.add_regions(
		    'region-media', 
		    [region], 
		    'region.redish', 
		    'dot',
		)

	def mediaNext(self):
		""" 
			Найти следующий медиа, после (текущего, активного) 
			Активный медиа что это
		"""
		print('mediaNext')
		pass

	def mediaPrev(self):
		pass

	def currentRegion(self):
		sel = self.view.sel();
		currentRegion = sel[0]
		# print(currentRegion)
		return currentRegion

	def searchNearestRegion(self, currentRegion):
		matches = list(self.generateMatches())
		currentRegion = tuple(currentRegion)

		line = ''
		for key, value in enumerate(matches):
			(region, text) = value
			region = tuple(region)
			if currentRegion[0] > region[0]:
				line = matches[key][1]

		if line == '' and len(matches):
			line = matches[0][1]

			# print(index, currentRegion, region)

		return line

	def generateMatches(self):
		regions = self.view.find_by_selector('meta.at-rule.media.css') # find by scope name view.scope_name(point)
		
		# regions = self.view.find_by_selector('meta.at-rule.media.css meta.block.css') # find by scope name view.scope_name(point)
		# regions = self.view.find_by_selector('meta.at-rule.media.css punctuation.section.group.end.css') # find by scope name view.scope_name(point)
		# regions = self.view.find_by_selector('meta.at-media-content.css') # find by scope name view.scope_name(point)
		# regions = self.view.find_all(r'\@media.*', re.M | sublime.IGNORECASE)
		# print(regions)
		for region in regions:
			text = self.view.substr(region)
			yield (region, text.strip().strip('{'))

	def region(self, a, b = None):
		return sublime.Region(a, b)

	def quick_panel_medias(self):
		# UI список с поиском и выбором элементов

		mediasText = [text for (region, text) in self.generateMatches()]
		# print(mediasText)
		self.window.show_quick_panel(
			mediasText, 
			self.quick_panel_on_done, 
			sublime.KEEP_OPEN_ON_FOCUS_LOST, 
			0,
		)
		
	def quick_panel_on_done(self, value):
		# print(value)
		if value is not None:
			index = 0
			for (region, text) in self.generateMatches():
				if value == index:
					#self.view.show(sublime.Region(0, 600)) # scroll
					self.view.show(region)
				index+=1




def plugin_loaded():
	print('plugin_loaded')

	Plugin.init()

	# print(Plugin.load_settings())
	# Plugin(window)

	plugin = Plugin(Plugin.get_active_window())
	# plugin.init()

	for window in sublime.windows():
		# plugin = Plugin(window)
		# plugin.init()

		for view in window.views():
			pass
			# print('plugin.in_extension', plugin.file_extension(),	plugin.in_extension())
			# print(plugin.view_get_extension(view), plugin.view_in_extension(view))

			# if plugin.view_in_extension(view):
				# pass
				
				# listener = CssMediaQueryListener(view)
				# sublime_plugin.view_event_listener_classes.append(CssMediaQueryListener)
				
				# sublime_plugin.create_view_event_listeners([CssMediaQueryListener], view)
				# sublime.listener = self
				
				# listeners = sublime_plugin.event_listeners_for_view(view)
				# print('listeners', listeners)
				
		# CssMediaQueryListener.on_load(window.active_view(), '__init__')

def plugin_unloaded():
	""" Remove event listener  """
	# for window in sublime.windows():
	# 	plugin = Plugin(window)
	# 	for view in window.views():
	# 		if plugin.view_in_extension(view):
	# 			# listener = sublime_plugin.find_view_event_listener(view, CssMediaQueryListener)
	# 			# print('listener', listener)
	# 			# del listener

	# 			listeners = sublime_plugin.view_event_listeners[view.view_id]
	# 			for key, listener in enumerate(listeners):
	# 				# print(issubclass(listener, CssMediaQueryListener))
	# 				print(isinstance(listener, CssMediaQueryListener))
	# 				if isinstance(listener, CssMediaQueryListener):
	# 					del sublime_plugin.view_event_listeners[view.view_id][key]

	# 			print(listeners)


# for window in sublime.windows():
# 	plugin = Plugin(window)
# 	for view in window.views():
# 		# print('plugin.in_extension', plugin.file_extension(),	plugin.in_extension())
# 		# print(plugin.view_get_extension(view), plugin.view_in_extension(view))

# 		if not plugin.view_in_extension(view):
# 			sublime_plugin.detach_view(view)
# 			index = sublime_plugin.view_event_listener_classes.index(CssMediaQueryListener)
# 			print(index)
# 			if index:
# 				del sublime_plugin.view_event_listener_classes[index]