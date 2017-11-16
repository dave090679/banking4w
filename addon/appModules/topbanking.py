#appModules/topbanking.py
#A part of NonVisual Desktop Access (NVDA)#Copyright (C) 2006-2012 NVDA Contributors
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
import appModuleHandler
from config import conf
from NVDAObjects.IAccessible import IAccessible
from NVDAObjects.UIA import ListItem, UIA
import controlTypes
class topbankingtab(UIA):
	def _get_name(self):
		return self.firstChild.next.name

class topbankingcell(IAccessible):
	def _get_name(self):
		linenumbers = conf["documentFormatting"]["reportLineNumber"]
		origname = self.IAccessibleObject.accName()
		linenumber = self.parent.IAccessibleObject.accName()
		if linenumbers == True:
			ret = origname
		else:
			ret = origname.replace(linenumber,u'')
		return ret

class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clslist):
		if obj.role == controlTypes.ROLE_TABLECELL:
				clslist.insert(0, topbankingcell)
		elif obj.role == controlTypes.ROLE_TAB:
			clslist.insert(0,topbankingtab)
			
