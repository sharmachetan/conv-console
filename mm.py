import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainWindow(QMainWindow):
   count = 0
   
   def __init__(self, parent = None):
      super(MainWindow, self).__init__(parent)
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

   def show_propertyWindow(self,q):
      print("trying to open property window")
      # if q.text() == "Property Window":
      prop = QDockWidget("Properties",self)
      treeWidget = QTreeWidget()
      #    prop.setWidget(QTextEdit())
      prop.setWidget(treeWidget)
      prop.setAllowedAreas(Qt.RightDockWidgetArea)

      COLUMN = treeWidget.setColumnCount(2)
      treeWidget.setHeaderLabels(["Property","Value"])

      # treeWidget.show()
      root=QTreeWidgetItem(treeWidget,["MapSet"])
      MS_TYPE = QTreeWidgetItem(root,["Type"])
      MS_TYPE.setCheckState(1,Qt.Checked)

      MS_NAME =QTreeWidgetItem(root,["Name"])
      MS_NAME.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MS_NAME.setText(1,"Default")

      MS_MODE=QTreeWidgetItem(root,["Mode"])
      combo = QComboBox()
      combo.addItem("1")
      combo.addItem("2")
      # ###TEst code
      # MS_MODE_COMBO = QTreeWidgetItem(root,["xxx"])
      # MS_MODE_COMBO.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      # MS_MODE_COMBO.setText(1,"yyy")


      MS_LANG= QTreeWidgetItem(root,["Lang"])

      MS_STORAGE= QTreeWidgetItem(root,["Storage"])
      MS_STORAGE.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MS_STORAGE.setText(1,"AUTO")

      MS_CTRL= QTreeWidgetItem(root,["Ctrl"])

      MS_TERM= QTreeWidgetItem(root,["Term"])
      MS_TERM.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MS_TERM.setText(1,"TERMINAL")

      MS_TIOAPFX= QTreeWidgetItem(root,["Tioapfx"])
      MS_MAPATTS= QTreeWidgetItem(root,["Mapatts"])
      MS_COLOR= QTreeWidgetItem(root,["Color"])
      MS_HIGHLIGHT= QTreeWidgetItem(root,["Highlight"])
      MS_TIOAPFX.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)


   # list of Map Attributes .
      root_map=QTreeWidgetItem(root,["Map"])
      MP_NAME= QTreeWidgetItem(root_map,["Name"])
      MP_NAME.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_NAME.setText(1,"Default")

      MP_LINE= QTreeWidgetItem(root_map,["Line"])
      MP_LINE.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_LINE.setText(1,"1")

      MP_SIZE= QTreeWidgetItem(root_map,["SIZE"])
      MP_SIZE.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_SIZE.setText(1,"1,1")

      MP_COLUMN= QTreeWidgetItem(root_map,["COLUMN"])
      MP_COLUMN.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_COLUMN.setText(1,"0")

      MP_JUSTIFY= QTreeWidgetItem(root_map,["Justify"])
      MP_JUSTIFY.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_JUSTIFY.setText(1,"LEFT/RIGHT")

      MP_CTRL= QTreeWidgetItem(root_map,["Ctrl"])
      MP_CTRL.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      # MP_CTRL.setText(1,"Default")  CONVERT IN COMBOBOX

      MP_TIOAPFX= QTreeWidgetItem(root_map,["Tioapfx"])
      MP_TIOAPFX.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_TIOAPFX.setText(1,"YES")

      MP_COLOR= QTreeWidgetItem(root_map,["Color"])
      MP_COLOR.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_COLOR.setText(1,"Default")

      MP_HIGHLIGHT= QTreeWidgetItem(root_map,["Highlight"])
      MP_HIGHLIGHT.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MP_HIGHLIGHT.setText(1,"Default")



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

def main():
   app = QApplication(sys.argv)
   ex = MainWindow()
   ex.show()
   sys.exit(app.exec_())
   
if __name__ == '__main__':
   main()