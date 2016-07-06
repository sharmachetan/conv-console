import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import codegen1 
import line 
import writer
import mm

class writer():

	
	def write_line(self,name):

		return name

	def set_property_object_count(self,count):
		
		# mmm = mm.MainWindow()
		# aa = mmm.get_property_object_count()
		return count


	def write_ms_type(self,name):
		self.name = name
		return name

	def write_ms_mode(self):
		pass
	def write_ms_name(self):
		pass
	def write_ms_lang(self,lang):
		return lang
	def write_ms_storage(self,storage):
		return storage
	def write_ms_ctrl(self,ctrl):
		return ctrl
	def write_ms_term(self,term):
		return term
	def write_ms_tioapfx(self,tioapfx):
		return tioapfx
	def write_ms_mapatts(self,mapatts):
		return mapatts
	def write_ms_color(self,color):
		return color
	def write_ms_highlight(self,highlight):
		return highlight

	#*************Map Values*-***********

	def write_mp_name(self,name):
		return name
	def write_mp_line(self,line):
		return line
	def write_mp_size(self,size):
		return size
	def write_mp_size(self,column):
		return column
	def write_mp_justify(self,justify):
		return justify
	def write_mp_ctrl(self,ctrl):
		return ctrl
	def write_mp_tioapfx(self,tioapfx):
		return tioapfx
	def write_mp_color(self,color):
		return color
	def write_mp_highlight(self,highlight):
		return highlight

	#********************Map Fields**************
	def write_mf_line_pos(self,pos):
		return pos
	def write_mf_line_col(self,col):
		return col
	def write_mf_init(self,init):
		return init
	def write_mf_attr(self,attr):
		return attr
	def write_mf_picin(self,picin):
		return picin
	def write_mf_picout(self,picout):
		return picout
	def write_mf_occurs(self,occurs):
		return occurs
	def write_mf_name(self,name):
		return name
	def write_mf_line(self,line):
		return line
	def write_mf_justify(self,justify):
		return justify
	def write_mf_color(self,color):
		return color
	def write_mf_highlight(self,highlight):
		return highligh


