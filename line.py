import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class line():

   V_MF_LINE_POS = ""
   V_MF_LINE_COLUMN = ""
   V_MF_LENGTH = ""
   V_MF_INIT = ""
   V_MF_JUSTIFY=""
   V_MF_ATTRB = ""
   V_MF_COLOR=""
   V_MF_HIGHLIGHT = ""
   V_MF_PICIN =""
   V_MF_PICOUT = ""
   V_MF_OCCURS = ""
   V_MF_NAME=""


   def set_line_title(self,LINE_NO):
      line_no = 'Line : {number}'.format(number = LINE_NO)
      return line_no


   def set_field_parent(self,parent,title):
      parent_item = QTreeWidgetItem(parent,[title])
      return parent_item

   def set_field_properties(self,LINE_NO,parent):

      #root
	    

      root_line=parent

      global MF_NAME
      global MF_LINE_POS
      global MF_LINE_COLUMN
      global MF_LENGTH
      global MF_INIT
      global MF_JUSTIFY
      global MF_ATTRB
      global MF_HIGHLIGHT
      global MF_COLOR
      global MF_PICIN
      global MF_PICOUT
      global MF_OCCURS


      MF_NAME= QTreeWidgetItem(root_line,["Name"])
      MF_NAME.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MF_NAME.setText(1,self.V_MF_NAME)

      MF_LINE_POS= QTreeWidgetItem(root_line,["Line-Position"])
      MF_LINE_POS.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)


      MF_LINE_POS.setText(1,self.V_MF_LINE_POS)

	      # global MF_LINE_COLUMN

      MF_LINE_COLUMN= QTreeWidgetItem(root_line,["Line-Column"])
      MF_LINE_COLUMN.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MF_LINE_COLUMN.setText(1,self.V_MF_LINE_COLUMN)

      MF_LENGTH= QTreeWidgetItem(root_line,["Length"])
      MF_LENGTH.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MF_LENGTH.setText(1,self.V_MF_LENGTH)
      MF_INIT = QTreeWidgetItem(root_line,["Initialize"])
      MF_INIT.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MF_INIT.setText(1,self.V_MF_INIT)

      MF_JUSTIFY= QTreeWidgetItem(root_line,["Justify"])
      MF_JUSTIFY.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MF_JUSTIFY.setText(1,self.V_MF_JUSTIFY)

      MF_ATTRB= QTreeWidgetItem(root_line,["Attribute"])
      MF_ATTRB.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MF_ATTRB.setText(1,self.V_MF_ATTRB)

      MF_COLOR= QTreeWidgetItem(root_line,["Color"])
      MF_COLOR.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MF_COLOR.setText(1,self.V_MF_COLOR)

      MF_HIGHLIGHT= QTreeWidgetItem(root_line,["Highlight"])
      MF_HIGHLIGHT.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MF_HIGHLIGHT.setText(1,self.V_MF_HIGHLIGHT)

      MF_PICIN= QTreeWidgetItem(root_line,["PICIN"])
      MF_PICIN.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MF_PICIN.setText(1,self.V_MF_PICIN)

      MF_PICOUT= QTreeWidgetItem(root_line,["PICOUT"])
      MF_PICOUT.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MF_PICOUT.setText(1,self.V_MF_PICOUT)

      MF_OCCURS= QTreeWidgetItem(root_line,["OCCURS"])
      MF_OCCURS.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MF_OCCURS.setText(1,self.V_MF_OCCURS)

#Get Values of Item Line position of Line field
   def get_mf_line_pos(self):
      text = MF_LINE_POS.text(1)
      return text
#Get Values of Item Line Column no. of Line Field
   def get_mf_line_column(self):
      text = MF_LINE_COLUMN.text(1)
      return text

#Get Values of Item Size of length of field
   def get_mf_length(self):
      text = MF_LENGTH.text(1)
      return text
#Get Values of Item Column of Initialize field.
   def get_mf_init(self):
      text = MF_INIT.text(1)
      return text
#Get Values of Item Ctrl of Justify the field
   def get_mf_justify(self):
      text = MF_JUSTIFY.text(1)
      return text
#Get Values of Item Justify of attribute of field
   def get_mf_attrb(self):
      text = MF_ATTRB.text(1)
      return text
#Get Values of Item color of field.
   def get_mf_color(self):
      text = MF_COLOR.text(1)
      return text
#Get Values of Item  line : color
   def get_mf_highlight(self):
      text = Mf_HIGHLIGHT.text(1)
      return text

#Get Values of Item Picin of field
   def get_mf_picin(self):
      text = MF_PICIN.text(1)
      return text
#Get Values of Item Picout of field
   def get_mf_picout(self):
      text = MF_PICOUT.text(1)
      return text
#Get Values of Item Occurs of field
   def get_mf_occurs(self):
      text = MF_OCCURS.text(1)
      return text

#***********************Setters of Field******************
#Set Values of Item Name of field
   def set_mf_init(self,field_name):
       self.V_MF_INIT = field_name
       MF_INIT.setText(1,self.V_MF_INIT)
#Set Value of Item Line-Position of Field.
   def set_mf_line_pos(self,field_name):
      self.V_MF_LINE_POS = field_name
      MF_LINE_POS.setText(1,self.V_MF_LINE_POS)
#Set Value of Item Line-Column of Field
   def set_mf_line_col(self,field_name):
       self.V_MF_LINE_COLUMN = field_name
       MF_LINE_COLUMN.setText(1,self.V_MF_LINE_COLUMN)
#Set Value of item Length of Field
   def set_mf_length(self,field_name):
             self.V_MF_LENGTH = field_name
             MF_LENGTH.setText(1,self.V_MF_LENGTH)