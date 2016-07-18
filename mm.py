import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import codegen1
import line
import writer


class MainWindow(QMainWindow):
   count = 0

   
   filename = ""
   field_objects = {}
   STAGE_FLAG=False
   FILE_OPEN_FLAG=False

   V_MS_TYPE="SYS"
   V_MS_NAME = "CV"
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
      stg = self.addToolBar("Stage Code")

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


      run = QAction(QIcon("D:\work\projects\conv-console\_run_icon"),"Generate Code",self)

      stgg = QAction(QIcon("D:\work\projects\conv-console\stage.bmp"),"Stage Code",self)
      stg.addAction(stgg)
      stg.actionTriggered[QAction].connect(self.stage_code)
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
      self.addDockWidget(Qt.RightDockWidgetArea,prop)

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
      MS_TYPE.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
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


      global MS_HIGHLIGHT
      MS_HIGHLIGHT= QTreeWidgetItem(root_profile,["Highlight"])
      MS_HIGHLIGHT.setFlags(Qt.ItemIsSelectable| Qt.ItemIsEditable| Qt.ItemIsEnabled)
      MS_HIGHLIGHT.setText(1,self.V_MS_HIGHLIGHT)

   # list of Map Attributes .
      global root_map
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

      # self.set_field_properties(root_map,2)

      # linex.set_field_properties(root_map,4)







      prop.show()

# Run Function to start processing the file.


   def stage_code(self):
      try:
         print('code staged')
         self.STAGE_FLAG

         if (self.FILE_OPEN_FLAG and self.STAGE_FLAG):
            self.STAGE_FLAG=True

            total_file_lines = len(read.file_list)

            print(total_file_lines)
            title = "name"
            line_objects = {}
            line_objects_line = {}

            # title = str(linex.set_line_title(10))
            # par = linex.set_field_parent(root_map,title)
            # ff = linex.set_field_parent(par,title)
            # linex.set_field_properties(10,ff)



            for x in range(total_file_lines):
               line_objects[x] = line.line()
               keys =[]

               title = str(line_objects[x].set_line_title(x))
               par = linex.set_field_parent(root_map,title)
               
               ggg = read.get_element_pos_length(x)
               ggg_len = len(ggg)
               eee = read.get_element_name(x)

               #Input Fields in Property window.
               read.get_input_element_length(x)
               input_fields = read.input_element_position_length 

               input_fields_len  = len(input_fields)
               print("input",input_fields)
               print(input_fields_len)

               if (input_fields_len != 0):


                  input_item_key=[]
                  for k,v in (input_fields.items()):
                     input_item_key.append(k)
                  
                  print(input_item_key)

                  for element in range(input_fields_len):
                      in_obj_name = 'line_object_{line}_in{field_no}'.format(line=x,field_no=element)
                      self.field_objects[in_obj_name] = line.line()

                      field_name = 'Field :{num}'.format(num=element)

                      jj = self.field_objects[in_obj_name].set_field_parent(par,field_name)
                      self.field_objects[in_obj_name].set_field_properties(x,jj)
                      in_obj_name = 'line_object_{line}_in{field_no}'.format(line=x,field_no=element)
                      self.field_objects[in_obj_name].set_mf_line_pos(str(input_item_key[element]))
                      self.field_objects[in_obj_name].set_mf_line_col(str(input_item_key[element]))
                      self.field_objects[in_obj_name].set_mf_init("Field")
                      self.field_objects[in_obj_name].set_mf_length(str(input_fields[input_item_key[element]]))
                      # self.field_objects[in_obj_name].set_mf_length(input_fields[element])
                      #thehe
               else:
                  print("not found")

               item_key=[]
               item_key_value=[]
               for k,v in (ggg.items()):
                  item_key.append(k)
                  item_key_value.append(v)

               for y in range(ggg_len):
                  # #Cleaning Item name string before initialization . Getting rid of '{' and " ' " .
                  string = eee[item_key[y]]
                  string = str(string)
                  string_len = len(string)
                  new_string =string[2:string_len-2] 
                  # #Cleaning Item name string before initialization . Getting rid of '{'.
                  value_string = str(item_key_value[y])
                  value_string_len = len(value_string)               
                  new_value_string =value_string[1:value_string_len-1] 

                  obj_name = 'line_object_{line}_{field_no}'.format(line=x,field_no=y)
                  self.field_objects[obj_name] = line.line()
                  # line_objects_line[y] = line.line()
                  ff = self.field_objects[obj_name].set_field_parent(par,new_string)
                  self.field_objects[obj_name].set_field_properties(x,ff)

                  obj_name = 'line_object_{line}_{field_no}'.format(line=x,field_no=y)
                  self.field_objects[obj_name].set_mf_line_pos(str(item_key[y]))
                  self.field_objects[obj_name].set_mf_line_col(str(item_key[y]))
                  self.field_objects[obj_name].set_mf_length(new_value_string)
                  self.field_objects[obj_name].set_mf_init(new_string)
         else:
            print("First select file")
            self.STAGE_FLAG=False
      except TypeError:
         print("Exception : caught inside stage()")



               
               # for k,v in (ggg.items()):
               # # print(k)
               #    z=0
               #    keys[z] = k
               #    # line_objects_line[z] = line.line()
               
               # field_objects[obj_name].set_mf_line_col(str(keys[y]))

            
               


   def pressed_run(self):
      print('print Pressed')
      aa = self.get_mp_highlight()

      bb = self.get_mp_name()
      cc = self.get_mp_line()
      d = self.get_mp_size()
      e = self.get_mp_justify()

      g =self.get_mp_tioapfx()
      h = self.get_mp_ctrl()

      j = self.get_mp_color()
      print(j)

      print(h)
      print(g)

      print(e)
      print(d)
      print(aa)
      print(bb)
      print(self.field_objects)

      # print("setting value",self.field_objects['line_object_1_0'].get_mf_line_pos())

      for k,v  in self.field_objects.items():
         print('this is ',self.field_objects[k].get_mf_length())
         print('this is ',self.field_objects[k].get_mf_init())
         print('this is ',self.field_objects[k].get_mf_line_pos())
         print('this is ',self.field_objects[k].get_mf_length())
         # print('ran the function',self.field_objects[k].get_mf_name())
         print('this is value',self.field_objects[k].get_n())
         # self.field_objects[k].get_Gmf_name()
         # print('this is name ',self.field_objects[k].get_mf_name())


      ww = writer.writer()
      print(ww.set_property_object_count(self.get_property_object_count()))
      self.save_file('ccc.txt')
      
   def save_file(self,file_name):
      ww = writer.writer()
      print("this is save file")

      with open(file_name,'w') as file:

         print("This is map set name",self.get_mp_name())
         # This seciton write MapSet definition code.
         MapSetName_=self.get_ms_name()
         Type_= "type"
         Lang_=self.get_ms_lang()
         Mode_=self.get_ms_mode()
         Ctrl_=self.get_ms_ctrl()
         Tioapfx_=self.get_ms_tioapfx()
         Term_=self.get_ms_term()

         map_set_asmb_line1 = '{MapSetName}    DFHMSD  TYPE={Type},LANG={Lang},MODE={Mode},CTRL={Ctrl} ,     -'.format(Ctrl=Ctrl_,Mode=Mode_,Lang=Lang_,Type=Type_,MapSetName=MapSetName_)
         map_set_asmb_line2 = '                       TIOAPFX={Tioapfx},TERM={Term}'.format(Term=Term_,Tioapfx=Tioapfx_)
         file.write(map_set_asmb_line1 +"\n" )
         file.write(map_set_asmb_line2 +"\n" )

         #This section write Map definition code.



         MapName_=self.get_mp_name()
         MapLine_=self.get_mp_line()
         MapSize_=self.get_mp_size()
         MapColumn_=self.get_mp_column()
         MapJustify_=self.get_mp_justify()
         MapCtrl_=self.get_mp_ctrl()
         MapTioapfx_=self.get_mp_tioapfx()
         MapColor_=self.get_mp_color()
         MapHighlight_=self.get_mp_highlight()

         map_asmb_line1='{MapName}    DFHMDI SIZE=({MapLine}{MapColumn}),LINE={MapLine},COLUMN={MapColumn},JUSTIFY={MapJustify},CTRL={MapCtrl},       -'.format(MapName=MapName_,MapLine=MapLine_,MapSize=MapSize_,MapColumn=MapColumn_,MapJustify=MapJustify_,MapCtrl=MapCtrl_)
         map_asmb_line2='                  TIOAPFX={MapTioapfx},COLOR={MapColor},HIGHLIGHT={MapHighlight}'.format(MapColor=MapColor_,MapTioapfx=MapTioapfx_,MapHighlight=MapHighlight_)
         file.write(map_asmb_line1 + '\n')
         file.write(map_asmb_line2 + '\n')

         #This section write MapField code.

         print('this is ',)
         print('this is ',)
         print('this is ',)
         print('this is ',)
         # self.field_objects[k].get_Gmf_name()
         # print('this is name ',self.field_objects[k].get_mf_name())

         for k,v  in self.field_objects.items():
            FieldName_ = ww.write_mf_line_pos(self.field_objects[k].get_mf_length())
            Length_   = ww.write_mf_init(self.field_objects[k].get_mf_length())
            Init_ =  ww.write_mf_init(self.field_objects[k].get_mf_init())
            Row_ = ww.write_mf_length(self.field_objects[k].get_mf_length())
            Col_ = ww.write_mf_length(self.field_objects[k].get_mf_length())
            asmb_line1 = '{FieldName}       DFHMDF POS=({row},{col}),LENGTH={Length},ATTRB={Attrb},   -'.format(FieldName = FieldName_ ,row = Row_,Length=Length_,col=Col_,Attrb ='(ASKIP,NORM)' )
            asmb_line2 = "                INITIAL='{Init}'".format(Init = Init_ )
            file.write(asmb_line1 +"\n" )
            file.write(asmb_line2 +"\n" )
            # print('This is name',self.field_objects[k].get_mf_name())

         # file.write(asmb_line +"\n" )
         # file.write(asmb_line +"\n" )
         # file.write(asmb_line +"\n" )
         # file.write(asmb_line +"\n" )
         # file.write(ww.write_mf_line_pos(self.field_objects['line_object_1_0'].get_mf_justify()) +"\n" )
         # # file.write(+"\n" )
         # file.write(ww.write_mf_line_pos(self.field_objects['line_object_1_0'].get_mf_color()) +"\n" )
         # file.write(ww.write_mf_line_pos(self.field_objects['line_object_1_0'].get_mf_highlight()) +"\n")
         # file.write(ww.write_mf_line_pos(self.field_objects['line_object_1_0'].get_mf_picin())+"\n" )
         # file.write(ww.write_mf_line_pos(self.field_objects['line_object_1_0'].get_mf_picout())+"\n" )
         # file.write(ww.write_mf_line_pos(self.field_objects['line_object_1_0'].get_mf_occurs()) +"\n" )
         # for x in (self.field_objects):
         #    print(self.field_objects[x])
         #    print(type(x))
         #    # file.write('********')



      print('hi')

   def get_property_object_count(self):
      count = str(len(self.field_objects))
      return count


#***************************Getters for Map set***********

#Get Values of Item Name of Map Set
   def get_ms_name(self):
      text = MS_NAME.text(1)
      return text
#Get Values of Item Mode of Map Set
   def get_ms_mode(self):
      text = MS_MODE.text(1)
      return text

#Get Values of Item Lang of Map Set
   def get_ms_lang(self):
      text = MS_LANG.text(1)
      return text
#Get Values of Item Storage of Map Set
   def get_ms_storage(self):
      text = MS_STORAGE.text(1)
      return text
#Get Values of Item Ctrl of Map Set
   def get_ms_ctrl(self):
      text = MS_CTRL.text(1)
      return text
#Get Values of Item term of Map Set
   def get_ms_term(self):
      text = MS_TERM.text(1)
      return text
#Get Values of Item Tioapfx of Map Set
   def get_ms_tioapfx(self):
      text = MS_TIOAPFX.text(1)
      return text
#Get Values of Item Mapatts of Map Set
   def get_ms_mapatts(self):
      text = MS_MAPATTS.text(1)
      return text
#Get Values of Item Color of Map Set
   def get_ms_color(self):
      text = MS_COLOR.text(1)
      return text
#Get Values of Item Storage of Map Set
   def get_ms_storage(self):
      text = MS_STORAGE.text(1)
      return text

#Get Values of Item Term of Map Set
   def get_ms_term(self):
      text = MS_TERM.text(1)
      return text
#Get Values of Item Highlight of Map Set
   def get_ms_highlight(self):
      text = MS_HIGHLIGHT.text(1)
      return text

#*******************************************

#***************************Getters for Map ***********

#Get Values of Item Name of Map
   def get_mp_name(self):
      text = MP_NAME.text(1)
      return text
#Get Values of Item Line of Map
   def get_mp_line(self):
      text = MP_LINE.text(1)
      return text

#Get Values of Item Size of Map
   def get_mp_size(self):
      text = MP_SIZE.text(1)
      return text
#Get Values of Item Column of Map
   def get_mp_column(self):
      text = MP_COLUMN.text(1)
      return text
#Get Values of Item Ctrl of Map
   def get_mp_ctrl(self):
      text = MP_CTRL.text(1)
      return text
#Get Values of Item Justify of Map
   def get_mp_justify(self):
      text = MP_JUSTIFY.text(1)
      return text
#Get Values of Item Tioapfx of Map
   def get_mp_tioapfx(self):
      text = MP_TIOAPFX.text(1)
      return text
#Get Values of Item Mapatts of Map Set
   def get_mp_highlight(self):
      text = MP_HIGHLIGHT.text(1)
      return text
#Get Values of Item Color of Map
   def get_mp_color(self):
      text = MP_COLOR.text(1)
      return text


#Get Values of Item Term of Map Set
   def get_ms_term(self):
      text = MS_TERM.text(1)
      return text
#Get Values of Item Highlight of Map Set
   def get_ms_highlight(self):
      text = MS_HIGHLIGHT.text(1)
      return text

#*******************************************

   def editor(self):
      textEdit = QTextEdit()
      self.setCentralWidget(textEdit)

   def open_file(self):
      print("opening file")
     
      self.filename = QFileDialog.getOpenFileName(self,'Open File')
      global read
      read = codegen1.reader(self.filename)
      read.file_in_list(self.filename)


      if self.filename:
         self.FILE_OPEN_FLAG = True
         self.STAGE_FLAG=True
         with open(self.filename,"rt") as file:
            text = file.read()

      textEdit = QTextEdit()
      open_sub = QMdiSubWindow()
      open_sub.setWidget(textEdit)
      open_sub.setWindowTitle(self.filename)
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
   # linex.pp()
   # read.get_input_element_length(1)
   # ax = read.input_element_position_length(1)
   # print("this is input element ",ax)
   # rr = read.calculate_lines('cif2.txt')
   # print("no. of lines",rr)
   # print(read.input_element_position_length)
   ex = MainWindow()


   

   # if total_file_lines >24 :
   #    print("OOPs! Mainframe can't handle more than 80 lines.")
   # else:
   #    pass



   # ex.set_text(MF_LINE_COLUMN,1,str(ggg[16]))



   # print(ggg[16])



   ex.show()


   sys.exit(app.exec_())



if __name__ == '__main__':
   main()
