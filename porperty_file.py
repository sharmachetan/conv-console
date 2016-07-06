def set_field_properties_1(self,WIDGET,LINE_NO):


      line_no = 'Line : {number}'.format(number = LINE_NO)

      root_line=QTreeWidgetItem(WIDGET,[line_no])

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


      global V_MF_LINE_POS 
      global V_MF_LINE_COLUMN
      global V_MF_LENGTH
      global V_MF_INIT 
      global V_MF_JUSTIFY
      global V_MF_ATTRB 
      global V_MF_COLOR
      global V_MF_HIGHLIGHT
      global V_MF_PICIN 
      global V_MF_PICOUT 
      global V_MF_OCCURS 
      global V_MF_LINE_POS 
      global V_MF_LINE_COLUMN 
      global V_MF_LENGTH  
      global V_MF_INIT 
      global V_MF_JUSTIFY
      global V_MF_ATTRB
      global V_MF_COLOR
      global V_MF_HIGHLIGHT 
      global V_MF_PICIN 
      global V_MF_PICOUT
      global V_MF_OCCURS

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