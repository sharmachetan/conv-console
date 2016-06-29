import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import codegen1 
import line 


class MainWindow(QMainWindow):
   count = 0
   
   
   V_MS_TYPE="SYS"
   V_MS_NAME = " ada "
   V_MS_MODE = ""
   V_MS_LANG =""
   V_MS_STORAGE = ""
   V_MS_CTRL = ""
   V_MS_TERM = ""
   V_MS_TIOAPFX = ""
   V_MS_MAPATTS = ""
   V_MS_COLOR = ""
   V_MS_TERM = ""
   V_MS_HIGHLIGHT = ""

   V_MP_NAME=""
   V_MP_LINE = ""
   V_MP_SIZE = ""
   V_MP_COLUMN = ""
   V_MP_JUSTIFY = ""
   V_MP_CTRL =""
   V_MP_TIOAPFX = ""
   V_MP_COLOR = ""
   V_MP_HIGHLIGHT = ""

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


  

   
   def __init__(self, parent = None):
      super(MainWindow, self).__init__(parent)

      self.setStyleSheet("""QToolTip { 
                           background-color: yellow; 
                           color: black;
                           opacity: 1;
                           border: black solid 1px;
                           }""")
      linex = line.line()

      self.mdi = QMdiArea()
      self.setCentralWidget(self.mdi)
      bar = self.menuBar()
      tb = self.addToolBar("Run")
      
      file = bar.addMenu("File")
      view = bar.addMenu("Views")
      help = bar.addMenu("Help")

      file.addAction("New")
      file.addAction("Open File")
      file.addAction("Save")
      file.addAction("Save As..")
      file.addAction("cascade")
      file.addAction("Tiled")
      file.addAction("Quit")


      run = QAction(QIcon("D:\work\projects\conv-console\_run_icon"),"Stage",self)
      tb.addAction(run)
      tb.actionTriggered[QAction].connect(self.pressed_run)

      view.addAction("Property Window")

      file.triggered[QAction].connect(self.windowaction)
      file.triggered[QAction].connect(self.open_file)

      view.triggered[QAction].connect(self.show_propertyWindow)

      self.setWindowTitle("Convenience Console")

      self.show_propertyWindow()

   def windowaction(self, q):
      print ("triggered")
      
      if q.text() == "New":
         MainWindow.count = MainWindow.count+1
         sub = QMdiSubWindow()
         sub.setWidget(QTextEdit())
         sub.setWindowTitle("subwindow"+str(MainWindow.count))
         self.mdi.addSubWindow(sub)
         
         self.mdi.cascadeSubWindows()
         sub.show()
         
      if q.text() == "cascade":
         self.mdi.cascadeSubWindows()
      if q.text() == "Tiled":
         self.mdi.tileSubWindows()

   def show_propertyWindow(self):
      print("trying to open property window")
      # if q.text() == "Property Window":
      prop = QDockWidget("Properties",self)
      prop.setFloating(False)

      treeWidget = QTreeWidget()
      #    prop.setWidget(QTextEdit())
      prop.setWidget(treeWidget)
      prop.setAllowedAreas(Qt.RightDockWidgetArea)

      COLUMN = treeWidget.setColumnCount(2)
      treeWidget.setHeaderLabels(["Property","Value"])

      treeWidget.setColumnWidth(0,150)

      # treeWidget.show()

      root=QTreeWidgetItem(treeWidget,["MapSet"])
      root_profile = QTreeWidgetItem(root,["Profile"])

      global MS_TYPE
      MS_TYPE = QTreeWidgetItem(root_profile,["Type"])
      MS_TYPE.setCheckState(1,Qt.Checked)
      MS_TYPE.setText(1,self.V_MS_TYPE)
      
      global MS_NAME
      MS_NAME =QTreeWidgetItem(root_profile,["Name"])
      MS_NAME.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MS_NAME.setText(1,self.V_MS_NAME)

      global MS_MODE
      MS_MODE=QTreeWidgetItem(root_profile,["Mode"])
      MS_MODE.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MS_MODE.setText(1,self.V_MS_MODE)
     
      MS_MODE.setToolTip(1,"tooltip")

      combo = QComboBox()
      combo.addItem("1")
      combo.addItem("2")
      # ###TEst code
      # MS_MODE_COMBO = QTreeWidgetItem(root,["xxx"])
      # MS_MODE_COMBO.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      # MS_MODE_COMBO.setText(1,"yyy")

      global MS_LANG
      MS_LANG= QTreeWidgetItem(root_profile,["Lang"])
      MS_LANG.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MS_LANG.setText(1,self.V_MS_LANG)

      global MS_STORAGE
      MS_STORAGE= QTreeWidgetItem(root_profile,["Storage"])
      MS_STORAGE.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MS_STORAGE.setText(1,self.V_MS_STORAGE)

      global MS_CTRL
      MS_CTRL= QTreeWidgetItem(root_profile,["Ctrl"])
      MS_CTRL.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MS_CTRL.setText(1,self.V_MS_CTRL)

      global MS_TERM
      MS_TERM= QTreeWidgetItem(root_profile,["Term"])
      MS_TERM.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MS_TERM.setText(1,self.V_MS_TERM)

      global MS_TIOAPFX
      MS_TIOAPFX= QTreeWidgetItem(root_profile,["Tioapfx"])
      MS_TIOAPFX.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
      
      global MS_MAPATTS
      MS_MAPATTS= QTreeWidgetItem(root_profile,["Mapatts"])
      MS_MAPATTS.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MS_MAPATTS.setText(1,self.V_MS_MAPATTS)

      global MS_COLOR
      MS_COLOR= QTreeWidgetItem(root_profile,["Color"])
      MS_COLOR.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MS_COLOR.setText(1,self.V_MS_COLOR)

      

      MS_HIGHLIGHT= QTreeWidgetItem(root_profile,["Highlight"])
      MS_HIGHLIGHT.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MS_HIGHLIGHT.setText(1,self.V_MS_HIGHLIGHT)

   # list of Map Attributes .
      root_map=QTreeWidgetItem(root,["Map"])

      root_map_def = QTreeWidgetItem(root_map,["Map Definition"])

      global MP_NAME
      MP_NAME= QTreeWidgetItem(root_map_def,["Name"])
      MP_NAME.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_NAME.setText(1,self.V_MP_NAME)

      global MP_LINE
      MP_LINE= QTreeWidgetItem(root_map_def,["Line"])
      MP_LINE.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_LINE.setText(1,self.V_MP_LINE)

      global MP_SIZE
      MP_SIZE= QTreeWidgetItem(root_map_def,["SIZE"])
      MP_SIZE.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_SIZE.setText(1,self.V_MP_SIZE)

      global MP_COLUMN
      MP_COLUMN= QTreeWidgetItem(root_map_def,["COLUMN"])
      MP_COLUMN.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_COLUMN.setText(1,self.V_MP_COLUMN)

      global MP_JUSTIFY
      MP_JUSTIFY= QTreeWidgetItem(root_map_def,["Justify"])
      MP_JUSTIFY.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_JUSTIFY.setText(1,self.V_MP_JUSTIFY)

      global MP_CTRL
      MP_CTRL= QTreeWidgetItem(root_map_def,["Ctrl"])
      MP_CTRL.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      # MP_CTRL.setText(1,"Default")  CONVERT IN COMBOBOX

      global MP_TIOAPFX
      MP_TIOAPFX= QTreeWidgetItem(root_map_def,["Tioapfx"])
      MP_TIOAPFX.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_TIOAPFX.setText(1,self.V_MP_TIOAPFX)

      global MP_COLOR
      MP_COLOR= QTreeWidgetItem(root_map_def,["Color"])
      MP_COLOR.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_COLOR.setText(1,self.V_MP_COLOR)

      global MP_HIGHLIGHT
      MP_HIGHLIGHT= QTreeWidgetItem(root_map_def,["Highlight"])
      MP_HIGHLIGHT.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_HIGHLIGHT.setText(1,self.V_MP_HIGHLIGHT)

      self.set_field_properties(root_map,2)
    
      linex.set_field_properties(root_map,4)
      linex2.set_field_properties(root_map,5)

      





      prop.show()

# Run Function to start processing the file. 
   


   def pressed_run(self):
      print('print Pressed')


   def editor(self):
      textEdit = QTextEdit()
      self.setCentralWidget(textEdit)  

   def open_file(self):
      print("opening file")
      filename = ""
      filename = QFileDialog.getOpenFileName(self,'Open File')

      

      if filename:
         with open(filename,"rt") as file:
            text = file.read()
            
      textEdit = QTextEdit()            
      open_sub = QMdiSubWindow()
      open_sub.setWidget(textEdit)
      open_sub.setWindowTitle(filename)
      self.mdi.addSubWindow(open_sub)
      textEdit.setText(text)  
      self.mdi.cascadeSubWindows()
      open_sub.show()

   def set_property_items(self):
      treeWidget = QTreeWidget()
      treeWidget.setColumnCount(2)
      treeWidget.setHeaderLabels(["Property","value"])
      treeWidget.show()


   def set_text(self,WIDGET_NAME,COL_NO,VALUE):
      WIDGET_NAME.setText(COL_NO,VALUE)

   def set_field_properties(self,WIDGET,LINE_NO):


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



   
def main():
   global linex,linex2
   linex2 = line.line()
 
   linex = line.line()
   app = QApplication(sys.argv)
   read = codegen1.reader('cif.txt')
   linex.pp()

   read.file_in_list('cif.txt')


   ex = MainWindow()


   total_file_lines = read.calculate_lines('cif.txt')

   if total_file_lines >80 :
      print("OOPs! Mainframe can't handle more than 80 lines.")
   else:
      
            
         ggg = read.get_element_pos_length(10)


         ex.set_text(MF_LINE_COLUMN,1,str(ggg[16]))



   print(ggg[16])


 
   ex.show()


   sys.exit(app.exec_())


   
if __name__ == '__main__':
   main()

