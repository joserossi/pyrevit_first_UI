import clr
import csv

clr.AddReference('System.Windows.Forms')
clr.AddReference('IronPython.Wpf')

from pyrevit import UI
from pyrevit import script
xalmfile = script.get_bundle_file('ui.xalm')

import wpf
from System import Windows

class MyWindow(Windows.Window):

	logger = script.get_logger()

	output = script.get_output()
	#output.set_height(200)
	#output.set_width(500)
	output.set_title('Titulo de prueba')

	def __init__(self):

		wpf.LoadComponent(self, xalmfile)
		self.archivo = open(
			'C:\Users\AY ONE\Desktop\Jose\pyrevit\prueba.extension\Prueba.tab\Prueba.panel\Prueba.pushbutton\prueba.txt',
			'w')

	def escribir(self, sender, args):
		datos = str(self.textbox.Text) + "\n" + str(self.textbox_2.Text)
		self.archivo.write(datos)
		print("Datos guardados correctamente")
		self.archivo.close()

	def limpiar_textbox(self, sender, args):
		self.textbox.Text = ""
		self.textbox_2.Text = ""

MyWindow().ShowDialog()
