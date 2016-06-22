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
         sub.show()
         
      if q.text() == "cascade":
         self.mdi.cascadeSubWindows()
         
      if q.text() == "Tiled":
         self.mdi.tileSubWindows()

   def show_propertyWindow(self,q):
      print("trying to open property window")
      if q.text() == "Property Window":
         prop = QDockWidget("Properties",self)
         prop.setWidget(QTextEdit())
         prop.setAllowedAreas(Qt.RightDockWidgetArea)
         prop.show()

  
   def open_file(self):
      print("opening file")
      filename = ""
      filename = QFileDialog.getOpenFileName(self,'Open File',".","(*.txt)")

      if self.filename:
         with open(self.filename,"rt") as file:
            MainWindow.count = MainWindow.count+1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            self.text.setText(file.read())
            sub.setWindowTitle("subwindow"+str(MainWindow.count))
            self.mdi.addSubWindow(sub)
            sub.show()



def main():
   app = QApplication(sys.argv)
   ex = MainWindow()
   ex.show()
   sys.exit(app.exec_())
   
if __name__ == '__main__':
   main()