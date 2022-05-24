#appModules/topbanking.py
#A part of NonVisual Desktop Access (NVDA)#Copyright (C) 2006-2012 NVDA Contributors
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
import appModuleHandler
from config import conf
from NVDAObjects.IAccessible import IAccessible
from NVDAObjects.UIA import ListItem, UIA
import controlTypes
class topbankingitem(ListItem):
	def _get_name(self):
		return self.children[1].name + "; " + self.children[2].name

#	def _get_states(self):
#		return self.children[0].states
#	def _set_states(self, new_states):
#		self.states = new_states

#class topbankingtab(UIA):
#	def _get_name(self):
#		return self.firstChild.next.name

class topbankingcell(UIA):
	def _get_name(self):
		linenumbers = conf["documentFormatting"]["reportLineNumber"]
		columnheaders = conf["documentFormatting"]["reportTableHeaders"]
		ret = self.UIAElement.CurrentName
		linenumber = self.parent.name
		if not linenumbers:
			ret = ret.replace(linenumber,u'')
		if not columnheaders:
			ret = ret.replace(self.columnHeaderText,"")
		return ret

class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clslist):
		if isinstance(obj,UIA):
			try:
				tabelle = obj.table
			except:
				tabelle = None
			try:
				zeilennummer = obj.rowNumber
			except:
				zeilennummer = -1
			if tabelle and zeilennummer != -1:
				clslist.insert(0, topbankingcell)
#		elif obj.role == controlTypes.ROLE_TAB and isinstance(obj, UIA):
#			clslist.insert(0,topbankingtab)
		elif isinstance(obj, UIA) and obj.UIAElement.CurrentName == 'Subsembly.BankingForms.PayeePickerItem':
			clslist.insert(0,topbankingitem)

