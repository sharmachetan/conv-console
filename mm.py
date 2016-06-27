import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import codegen1


class MainWindow(QMainWindow):
   count = 0

   V_MS_TYPE="SYS"
   V_MS_NAME = "  "
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

      run = QAction(QIcon("lrun.bmp"),"Stage",self)
      tb.addAction(run)

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

      MS_TYPE = QTreeWidgetItem(root_profile,["Type"])
      MS_TYPE.setCheckState(1,Qt.Checked)
      MS_TYPE.setText(1,self.V_MS_TYPE)
      MS_NAME =QTreeWidgetItem(root_profile,["Name"])
      
      MS_NAME.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MS_NAME.setText(1,self.V_MS_NAME)

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


      MS_LANG= QTreeWidgetItem(root_profile,["Lang"])
      MS_LANG.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MS_LANG.setText(1,self.V_MS_LANG)

      MS_STORAGE= QTreeWidgetItem(root_profile,["Storage"])
      MS_STORAGE.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MS_STORAGE.setText(1,self.V_MS_STORAGE)

      MS_CTRL= QTreeWidgetItem(root_profile,["Ctrl"])
      MS_CTRL.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MS_CTRL.setText(1,self.V_MS_CTRL)

      MS_TERM= QTreeWidgetItem(root_profile,["Term"])
      MS_TERM.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MS_TERM.setText(1,self.V_MS_TERM)

      MS_TIOAPFX= QTreeWidgetItem(root_profile,["Tioapfx"])
      MS_TIOAPFX.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
      
      MS_MAPATTS= QTreeWidgetItem(root_profile,["Mapatts"])
      MS_MAPATTS.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MS_MAPATTS.setText(1,self.V_MS_MAPATTS)

      
      MS_COLOR= QTreeWidgetItem(root_profile,["Color"])
      MS_COLOR.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MS_COLOR.setText(1,self.V_MS_COLOR)

      MS_TERM.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MS_TERM.setText(1,"TERMINAL")

      MS_HIGHLIGHT= QTreeWidgetItem(root_profile,["Highlight"])
      MS_HIGHLIGHT.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MS_HIGHLIGHT.setText(1,self.V_MS_HIGHLIGHT)

   # list of Map Attributes .
      root_map=QTreeWidgetItem(root,["Map"])

      root_map_def = QTreeWidgetItem(root_map,["Map Definition"])

      MP_NAME= QTreeWidgetItem(root_map_def,["Name"])
      MP_NAME.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_NAME.setText(1,self.V_MP_NAME)

      MP_LINE= QTreeWidgetItem(root_map_def,["Line"])
      MP_LINE.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_LINE.setText(1,self.V_MP_LINE)

      MP_SIZE= QTreeWidgetItem(root_map_def,["SIZE"])
      MP_SIZE.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_SIZE.setText(1,self.V_MP_SIZE)

      MP_COLUMN= QTreeWidgetItem(root_map_def,["COLUMN"])
      MP_COLUMN.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_COLUMN.setText(1,self.V_MP_COLUMN)

      MP_JUSTIFY= QTreeWidgetItem(root_map_def,["Justify"])
      MP_JUSTIFY.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_JUSTIFY.setText(1,self.V_MP_JUSTIFY)

      MP_CTRL= QTreeWidgetItem(root_map_def,["Ctrl"])
      MP_CTRL.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      # MP_CTRL.setText(1,"Default")  CONVERT IN COMBOBOX

      MP_TIOAPFX= QTreeWidgetItem(root_map_def,["Tioapfx"])
      MP_TIOAPFX.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_TIOAPFX.setText(1,self.V_MP_TIOAPFX)

      MP_COLOR= QTreeWidgetItem(root_map_def,["Color"])
      MP_COLOR.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_COLOR.setText(1,self.V_MP_COLOR)

      MP_HIGHLIGHT= QTreeWidgetItem(root_map_def,["Highlight"])
      MP_HIGHLIGHT.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_HIGHLIGHT.setText(1,self.V_MP_HIGHLIGHT)

      self.set_field_properties(root_map,2)




      prop.show()

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


   def set_field_properties(self,WIDGET,LINE_NO):


      line_no = 'Line : {number}'.format(number = LINE_NO)

      root_line=QTreeWidgetItem(WIDGET,[line_no])

      MF_LINE_POS= QTreeWidgetItem(root_line,["Line-Position"])
      MF_LINE_POS.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MF_LINE_POS.setText(1,self.V_MF_LINE_POS)

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
   app = QApplication(sys.argv)
   ex = MainWindow()
   read = codegen1.reader('cif.txt')
   read.file_in_list('cif.txt')

   ggg = read.get_element_pos_length(10)

   ex.V_MF_LINE_POS = str(ggg[16])
   
   ex.show()

   print(ggg[16])


   sys.exit(app.exec_())


   
if __name__ == '__main__':
   main()

