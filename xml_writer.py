import xml.etree.ElementTree as ET
import codegen1 as cd

readFile = cd.reader('cif.txt')
name = readFile.name
op = readFile.file_in_list('cif.txt')

print("**********************************************")
print("")
print("")
ggg = readFile.get_element_pos_length(10)
print("***Element pos-length dic",ggg)
print("")
abcd = readFile.get_element_name(10)
print("***this sis get_element_name",abcd)
print("")

print("***",readFile.input_element_position_length)

class xml_writer:
	line_count = readFile.calculate_lines(name)
	
	

	def __init__(self):
		global ROOT
		global CTRL
		global TYPE_
		global STORAGE
		global TERM
		global MODE
		ROOT = ET.Element('mapset')
		ROOT.attrib['macro']='DFHMSD'

		CTRL = ET.SubElement(ROOT,'ctrl')
		TYPE_ = ET.SubElement(ROOT,'type')
		STORAGE = ET.SubElement(ROOT,'storage')
		TERM = ET.SubElement(ROOT,'term')
		MODE = ET.SubElement(ROOT,'mode')
		tree = ET.ElementTree(ROOT)
		tree.write('map',)

	

	def out(self,ROOT):
		return ET.dump(ROOT)

	def add_map_def(self,map_name):
		self.MAP_DEF=ET.SubElement(ROOT,'map-def')
		self.MAP_DEF.attrib['macro'] = 'DFHMDI'
		MAP_DEF.attrib['map-name'] = map_name

	def add_map_size(self,map,map_size):
		self.MAP_SIZE = ET.SubElement(MAP_DEF,'map-size')




	


xmlwr = xml_writer()

if (xmlwr.line_count != 0):
	print(" [Initiate]  XML generation. ")
	
	xmlwr.out(ROOT)
	
	

else:
	print(" FIle is Empty.")





# top = Element('top')
# child = SubElement(top,"child1")


# ET = x_writer()
# ET.dump(top)




