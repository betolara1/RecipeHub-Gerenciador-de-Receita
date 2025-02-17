from kivymd.app import MDApp
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.core.window import Window
import sqlite3
from functools import partial
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.scrollview import ScrollView
from kivymd.uix.tab import MDTabsBase
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu

KV = '''
ScreenManager:
	Screen:
		name: 'screenCategorie'
		BoxLayout:
			orientation: 'vertical'
			MDToolbar:
				id: tbCategorie
				right_action_items: [["circle-edit-outline", lambda x: app.callback_option()]]
				md_bg_color: 0, 0, 0, 1
			Categorias:
				id: categoria
	
	Screen:
		name: 'screenList'
		BoxLayout:
			orientation: 'vertical'
			MDToolbar:
				id: tbList
				left_action_items: [["arrow-left-bold", lambda x: app.callback_select(x)]]
				right_action_items: [["plus-box-outline", lambda x: app.callback_telaAdd()]]
				md_bg_color: 0, 0, 0, 1
			ScreenList:
				id: screenlist
	
	Screen:
		name: 'telaAdicionar'
		BoxLayout:
			orientation: 'vertical'
			MDToolbar:
				id: tbAdd
				left_action_items: [["arrow-left-bold", lambda x: app.callback_add(x)]]
				right_action_items: [["check-underline", lambda x: app.salvarReceita()]]
				md_bg_color: 0, 0, 0, 1
			MDTabs:
			    id: tabadd
			    background_color: 0, 0, 0, 1
			    font_name: 'verdana.ttf' 
			    Tab:
			    	id: tabrecipe
			    	text: 'RECEITA'
					TelaAdiciona:
						id: telaadiciona
				Tab:
					id: tabingred
					text: 'INGREDIENTES'
					TelaAdiciona2:
						id: telaadiciona2
				Tab:
					id: tabprep
					text: 'MODO DE PREPARO'
					TelaAdiciona3:
						id: telaadiciona3
	
	Screen:
		name: 'telaAbreReceitas'
		BoxLayout:
			orientation: 'vertical'
			MDToolbar:
				id: tbRecipe
				left_action_items: [["arrow-left-bold", lambda x: app.callback_add(x)]]
				right_action_items: [["pencil-outline", lambda x: app.callback_modificaReceita()], ["trash-can-outline", lambda x: app.deleteFile()]]
				md_bg_color: 0, 0, 0, 1
			TelaAbreReceitas:
				id: telaabre
				
	Screen:
		name: 'telaModificaReceitas'
		BoxLayout:
			orientation: 'vertical'
			MDToolbar:
				id: tbMod
				left_action_items: [["arrow-left-bold", lambda x: app.callback_add(x)]]
				right_action_items: [["check-underline", lambda x: app.salvaModificarReceita()]]
				md_bg_color: 0, 0, 0, 1
			MDTabs:
			    id: tabmod
			    background_color: 0, 0, 0, 1
			    font_name: 'verdana.ttf' 
			    Tab:
			    	id: tabmodrecipe
					text: 'RECEITAS'
					TelaModificaReceita:
						id: telamodifica
				Tab:
					id: tabmodingred
					text: 'INGREDIENTES'
					TelaModificaReceita2:
						id: telamodifica2
				Tab:
					id: tabmodprep
					text: 'MODO DE PREPARO'
					TelaModificaReceita3:
						id: telamodifica3
						
	Screen:
		name: 'screenOption'
		BoxLayout:
			orientation: 'vertical'
			MDToolbar:
				id: tbOption
				left_action_items: [["arrow-left-bold", lambda x: app.callback_select(x)]]
				md_bg_color: 0, 0, 0, 1
			Options:
				id: screenoption

<Categorias>:
	ScrollView:
		MDList: 
			padding: '5dp'
			MDRoundFlatIconButton:
				id: btCat1
				text: 'teste'
				icon: 'glass-cocktail'
				font_size: '20sp'
				size_hint: (1, None)
				halign: 'left'
				font_name: 'verdana.ttf'
				line_color: (128/255,128/255,128/255)
				text_color: 0,2,0,1
				icon_color: 0,0,0,1
				on_press: 
					app.callback()
					app.toolbarText = 'BEBIDAS'
					app.showRecipes()
					app.root.ids.tbList.title = self.text
				
			MDRoundFlatIconButton:
				id: btCat2
				icon: 'cupcake'
				font_size: '20sp'
				size_hint: (1, None)
				halign: 'left'
				font_name: 'verdana.ttf'
				line_color: (128/255,128/255,128/255)
				text_color: 0,2,0,1
				icon_color: 0,0,0,1
				on_press: 
					app.callback()
					app.toolbarText = 'BOLOS E TORTAS DOCES'
					app.showRecipes()
					app.root.ids.tbList.title = self.text

			MDRoundFlatIconButton:
				id: btCat3
				icon: 'food-steak'
				font_size: '20sp'
				size_hint: (1, None)
				halign: 'left'
				font_name: 'verdana.ttf'
				line_color: (128/255,128/255,128/255)
				text_color: 0,2,0,1
				icon_color: 0,0,0,1
				on_press: 
					app.callback()
					app.toolbarText = 'CARNES E AVES'
					app.showRecipes()
					app.root.ids.tbList.title = self.text
					
			MDRoundFlatIconButton:
				id: btCat4
				icon: 'hamburger'
				font_size: '20sp'
				size_hint: (1, None)
				halign: 'left'
				font_name: 'verdana.ttf'
				line_color: (128/255,128/255,128/255)
				text_color: 0,2,0,1
				icon_color: 0,0,0,1
				on_press: 
					app.callback()
					app.toolbarText = 'LANCHES'
					app.showRecipes()
					app.root.ids.tbList.title = self.text
					
			MDRoundFlatIconButton:
				id: btCat5
				icon: 'pasta'
				font_size: '20sp'
				size_hint: (1, None)
				halign: 'left'
				font_name: 'verdana.ttf'
				line_color: (128/255,128/255,128/255)
				text_color: 0,2,0,1
				icon_color: 0,0,0,1
				on_press: 
					app.callback()
					app.toolbarText = 'PÃES E MASSAS'
					app.showRecipes()
					app.root.ids.tbList.title = self.text
					
			MDRoundFlatIconButton:
				id: btCat6
				icon: 'fish'
				font_size: '20sp'
				size_hint: (1, None)
				halign: 'left'
				font_name: 'verdana.ttf'
				line_color: (128/255,128/255,128/255)
				text_color: 0,2,0,1
				icon_color: 0,0,0,1
				on_press: 
					app.callback()
					app.toolbarText = 'PEIXES E FRUTOS DO MAR'
					app.showRecipes()
					app.root.ids.tbList.title = self.text
				
			MDRoundFlatIconButton:
				id: btCat7
				icon: 'food-turkey'
				font_size: '20sp'
				size_hint: (1, None)
				halign: 'left'
				font_name: 'verdana.ttf'
				line_color: (128/255,128/255,128/255)
				text_color: 0,2,0,1
				icon_color: 0,0,0,1
				on_press: 
					app.callback()
					app.toolbarText = 'PRATOS ESPECIAIS'
					app.showRecipes()
					app.root.ids.tbList.title = self.text
					
			MDRoundFlatIconButton:
				id: btCat8
				icon: 'soy-sauce'
				font_size: '19sp'
				size_hint: (1, None)
				halign: 'left'
				font_name: 'verdana.ttf'
				line_color: (128/255,128/255,128/255)
				text_color: 0,2,0,1
				icon_color: 0,0,0,1
				on_press: 
					app.callback()
					app.toolbarText = 'SALADAS, MOLHOS E ACOMPANHAMENTOS'
					app.showRecipes()
					app.root.ids.tbList.title = self.text
				
			MDRoundFlatIconButton:
				id: btCat9
				icon: 'food-fork-drink'
				font_size: '20sp'
				size_hint: (1, None)
				halign: 'left'
				font_name: 'verdana.ttf'
				line_color: (128/255,128/255,128/255)
				text_color: 0,2,0,1
				icon_color: 0,0,0,1
				on_press: 
					app.callback()
					app.toolbarText = 'SOBREMESAS'
					app.showRecipes()
					app.root.ids.tbList.title = self.text
					
			MDRoundFlatIconButton:
				id: btCat10
				icon: 'food-variant'
				font_size: '20sp'
				size_hint: (1, None)
				halign: 'left'
				font_name: 'verdana.ttf'
				line_color: (128/255,128/255,128/255)
				text_color: 0,2,0,1
				icon_color: 0,0,0,1
				on_press: 
					app.callback()
					app.toolbarText = 'SOPAS'
					app.showRecipes()
					app.root.ids.tbList.title = self.text			
		
<ScreenList>:	
	ScrollView:
		MDList:
			id: mostraReceita
			padding: '20dp'

<TelaAdiciona>:
	ScrollView:
		MDList:
			id: lista
			spacing: '20dp'
			padding: '25dp'
			
			MDLabel:
			MDLabel:
				id: nameadd
				font_style: 'H5'
				font_name: 'verdanab.ttf'
			
			MDTextField:
				id: nomeReceita
				font_size: self.width / 20
				mode: 'rectangle'
				input_filter: lambda text, from_undo: text[:30 - len(self.text)]
				max_text_length: 30
				
			MDLabel:				
			MDLabel:
				id: descadd
				font_style: 'H5'
				font_name: 'verdanab.ttf'
			
			MDTextField:
				id: descricaoReceita
				font_size: self.width / 20
				mode: 'rectangle'

<TelaAdiciona2>:	
	ScrollView:	
		MDList:
			id: lista2
			spacing: '20dp'
			padding: '25dp'
				
			MDLabel:
			MDLabel:
				id: ingredadd
				font_style: 'H5'
				font_name: 'verdanab.ttf'
				
			MDTextField:
				id: ingred
				mode: 'rectangle'
				multiline: True
				font_size: self.width / 20
				font_name: 'verdana.ttf'

<TelaAdiciona3>:
	ScrollView:	
		MDList:
			id: lista3
			spacing: '20dp'
			padding: '25dp'
			
			MDLabel:
			MDLabel:
				id: prepadd
				font_style: 'H5'
				font_name: 'verdanab.ttf'
				
			MDTextField:
				id: modoPreparo
				mode: 'rectangle'
				multiline: True
				font_size: self.width / 20
				font_name: 'verdana.ttf'

<TelaAbreReceitas>:
	ScrollView:
		MDList:
			spacing: '20dp'
			padding: '25dp'
			id: abreReceita
			
			MDLabel:
			MDLabel:
				id: labelreceita
				halign: 'center'
				markup: True
				font_style: 'H4'
				font_name: 'verdanab.ttf'
				
			MDLabel:
			MDLabel:
			MDLabel:
				id: labeldescricao
				halign: 'center'
				font_style: 'H5'
				font_name: 'verdana.ttf'
				
			MDLabel:
			MDLabel:
			MDLabel:
				id: ingredabre
				text: 'Ingredientes:'
				halign: 'center'
				font_style: 'H5'
				font_name: 'verdanab.ttf'
				
			MDTextField:
				id: labelingred
				halign: 'center'
				font_size: self.width / 20
				multiline: True
				readonly: True
				font_name: 'verdana.ttf'
				line_color_normal: 1, 0, 0, 0
				text_color_normal: 0, 0, 0, 1
			
			MDLabel:
			MDLabel:
				id: prepabre
				text: 'Modo de Preparo:'
				halign: 'center'
				font_style: 'H5'
				font_name: 'verdanab.ttf'
			
			MDTextField:
				id: labelpreparo
				halign: 'center'
				font_size: self.width / 20
				multiline: True
				readonly: True
				font_name: 'verdana.ttf'
				line_color_normal: 1, 0, 0, 0
				text_color_normal: 0, 0, 0, 1
				
<TelaModificaReceita>:
	ScrollView:
		MDList:
			id: modificaReceita
			spacing: '20dp'
			padding: '25dp'
			
			MDLabel:
			MDLabel:
				id: namemod
				text: '  NOME DA RECEITA: '
				font_style: 'H5'
				font_name: 'verdanab.ttf'
			
			MDTextField:
				id: modreceita
				font_size: self.width / 20
				mode: 'rectangle'
				max_text_length: 30
				input_filter: lambda text, from_undo: text[:30 - len(self.text)]
				
			MDLabel:
			MDLabel:
				id: descmod
				text: '  DESCRIÇÃO DA RECEITA: '
				font_style: 'H5'
				font_name: 'verdanab.ttf'
				
			MDTextField:
				id: moddescricao
				font_size: self.width / 20
				mode: 'rectangle'

<TelaModificaReceita2>:	
	ScrollView:
		MDList:
			id: modificaReceita
			spacing: '20dp'
			padding: '25dp'
			
			MDLabel:
			MDLabel:
				id: ingredmod
				text: '  INGREDIENTES:'
				font_style: 'H5'
				font_name: 'verdanab.ttf'
				
			MDTextField:
				id: modingred
				mode: 'rectangle'
				multiline: True
				font_size: self.width / 20
				font_name: 'verdana.ttf'

<TelaModificaReceita3>:
	ScrollView:
		MDList:
			id: modificaReceita
			spacing: '20dp'
			padding: '25dp'
					
			MDLabel:
			MDLabel:
				id: prepmod
				text: '  MODO DE PREPARO:'
				font_style: 'H5'
				font_name: 'verdanab.ttf'
				
			MDTextField:
				id: modpreparo
				mode: 'rectangle'
				multiline: True
				font_size: self.width / 20
				font_name: 'verdana.ttf'

<Options>
	ScrollView:
		MDList:
			spacing: '20dp'
			padding: '25dp'
					
			MDLabel:
			MDLabel:
				id: txtLang
				#text: '  IDIOMAS:'
				font_style: 'H5'
				halign: "left"
				font_name: 'verdanab.ttf'
			
			MDLabel:
			MDLabel:
			BoxLayout:
				MDFlatButton:
					text: 'EN'
					id: txtDialog1
					font_name: 'verdana.ttf'
					on_release: app.resetChangeLangEN()
					line_color: (128/255,128/255,128/255)
						
				MDFlatButton:
					text: 'PT-BR'
					id: txtDialog2
					font_name: 'verdana.ttf'
					on_release: app.resetChangeLangBR()
					line_color: (128/255,128/255,128/255)
			
			MDLabel:
			MDLabel:
				id: txtTheme
				text: '  CORES TEMA:'
				font_style: 'H5'
				halign: "left"
				font_name: 'verdanab.ttf'
				
			MDLabel:
			MDLabel:	
			BoxLayout:
				MDFlatButton:
					md_bg_color: [0, 0, 0, 1]
					on_release: 
						app.changeThemeColor([0,0,0,1])
						app.idColor = 'color1'
						app.saveColor()
					line_color: (128/255,128/255,128/255)
				
				MDLabel:		
				MDFlatButton:
					md_bg_color: (128/255,0/255,128/255)
					on_release: 
						app.changeThemeColor([.5,0,.5,1])
						app.idColor = 'color2'
						app.saveColor()
					line_color: (128/255,128/255,128/255)
				
				MDLabel:	
				MDFlatButton:
					md_bg_color: (255/255,0/255,0/255)
					on_release: 
						app.changeThemeColor([1,0,0,1])
						app.idColor = 'color3'
						app.saveColor()
					line_color: (128/255,128/255,128/255)
				
				MDLabel:
				MDFlatButton:
					md_bg_color: (0/255,0/255,255/255)
					on_release: 
						app.changeThemeColor([0,0,1,1])
						app.idColor = 'color4'
						app.saveColor()
					line_color: (128/255,128/255,128/255)
			
			MDLabel:
			BoxLayout:
				MDFlatButton:
					md_bg_color: (255/255,0/255,255/255)
					on_release: 
						app.changeThemeColor([1,0,1,1])
						app.idColor = 'color5'
						app.saveColor()
					line_color: (128/255,128/255,128/255)
				
				MDLabel:
				MDFlatButton:
					md_bg_color: (255/255,255/255,0/255)
					on_release: 
						app.changeThemeColor([1,1,0,1])
						app.idColor = 'color6'
						app.saveColor()
					line_color: (128/255,128/255,128/255)
				
				MDLabel:
				MDFlatButton:
					md_bg_color: (0/255,128/255,0/255)
					on_release: 
						app.changeThemeColor([0,.5,0,1])
						app.idColor = 'color7'
						app.saveColor()
					line_color: (128/255,128/255,128/255)
					
				MDLabel:
				MDFlatButton:
					md_bg_color: (128/255,128/255,128/255)
					on_release: 
						app.changeThemeColor([.5,.5,.5,1])
						app.idColor = 'color8'
						app.saveColor()
					line_color: (128/255,128/255,128/255)
'''

Window.softinput_mode = "below_target"

class Options(FloatLayout):
	pass
	
class Tab(ScrollView, MDTabsBase):
	pass
	
class TelaModificaReceita(FloatLayout):
	pass
	
class TelaModificaReceita2(FloatLayout):
	pass 
	
class TelaModificaReceita3(FloatLayout):
	pass 
	
class TelaAbreReceitas(FloatLayout):
	pass

class TelaAdiciona(FloatLayout):
	pass	

class TelaAdiciona2(FloatLayout):
	pass
	
class TelaAdiciona3(FloatLayout):
	pass
	
class ScreenList(FloatLayout):
	pass

class Categorias(FloatLayout):
	pass

class Aplicativo(MDApp):
	cats = ['bebidas', 'doces', 'carnes', 'lanches', 'massas', 'peixes', 'especiais', 'saladas', 'sobremesas', 'sopas']
	
	toolbarText = ''
	
	def callback_telaAdd(self):
		self.root.current = 'telaAdicionar'
	
	def callback(self):
		button = self.root.current = 'screenList'
			
	def callback_add(self, button):
		button = self.root.current = 'screenList'
		self.zeraReceitaAdd()
		
	def callback_select(self, button):
		button = self.root.current = 'screenCategorie'
		
	def callback_abreReceita(self, *args):
		self.root.current = 'telaAbreReceitas'
		
	def callback_modificaReceita(self):
		self.root.current = 'telaModificaReceitas'
		self.modificarReceita()
		
	def callback_option(self):
		self.root.current = 'screenOption'
		
	def on_start(self):
		self.loadLang()
		self.loadColor()
		self.root.ids.tbCategorie.font_name = ('verdana.ttf')
		self.root.ids.tbList.font_name = ('verdana.ttf')
		self.root.ids.tbAdd.font_name = ('verdana.ttf')
		self.root.ids.tbRecipe.font_name = ('verdana.ttf')
		self.root.ids.tbMod.font_name = ('verdana.ttf')
		
	def changeThemeColor(self, color):
		self.root.ids.tbOption.md_bg_color = color
		self.root.ids.tabadd.background_color = color
		self.root.ids.tabmod.background_color = color
		self.root.ids.tbCategorie.md_bg_color = color
		self.root.ids.tbList.md_bg_color = color
		self.root.ids.tbAdd.md_bg_color = color
		self.root.ids.tbRecipe.md_bg_color = color
		self.root.ids.tbMod.md_bg_color = color
	
	def build(self):
		self.createTables()
		self.insertConfig()
		return Builder.load_string(KV)
		
	def createTables(self):
		conn = sqlite3.connect('recipeDB.db')
		c = conn.cursor()
		for x in self.cats:
			c.execute("CREATE TABLE if not exists "+x+"(id integer primary key autoincrement, name text, desc text, ingred text, prep text)")
		c.execute("CREATE TABLE if not exists config (id integer primary key, name text)")
		conn.commit()
		conn.close()
		
	def salvarReceita(self):
		conn = sqlite3.connect('recipeDB.db')
		c = conn.cursor()
		for x in self.cats:
			if x.upper() in self.toolbarText:
				c.execute("INSERT INTO "+x+" VALUES (:id, :name, :desc, :ingred, :prep)", {'id': None, 'name': self.root.ids.telaadiciona.ids.nomeReceita.text, 'desc': self.root.ids.telaadiciona.ids.descricaoReceita.text, 'ingred': self.root.ids.telaadiciona2.ids.ingred.text, 'prep': self.root.ids.telaadiciona3.ids.modoPreparo.text, })
		conn.commit()
		conn.close()
		self.showRecipes()
		self.callback()
		self.zeraReceitaAdd()
			
	def zeraReceitaAdd(self):
		self.root.ids.telaadiciona.ids.nomeReceita.text = ''
		self.root.ids.telaadiciona.ids.descricaoReceita.text = ''
		self.root.ids.telaadiciona2.ids.ingred.text = ''
		self.root.ids.telaadiciona3.ids.modoPreparo.text= ''
	
	def showRecipes(self):
		conn = sqlite3.connect('recipeDB.db')
		c = conn.cursor()
		for x in self.cats:
			if x.upper() in self.toolbarText:
				c.execute("SELECT * FROM " +x)
				records = c.fetchall()
				self.root.ids.screenlist.ids.mostraReceita.clear_widgets()
				for record in records:
					self.textLine = TwoLineListItem(text = str(record[1].upper()), secondary_text = str(record[2].capitalize()))
					self.root.ids.screenlist.ids.mostraReceita.add_widget(self.textLine)
					self.root.ids.screenlist.ids.mostraReceita.ids[record[0]] = self.textLine
					i = record[0]
					self.textLine.bind(on_release = partial(self.abrirReceita, i))
		conn.commit()
		conn.close()
		
	a = ''
	def abrirReceita(self, id_index, instance):
		conn = sqlite3.connect('recipeDB.db')
		c = conn.cursor()
		for x in self.cats:
			if x.upper() in self.toolbarText:
				table = "select * from " +x+" where id = ?"
				c.execute(table, (id_index, ))
				self.a = id_index
				records = c.fetchall()
				for record in records:
					self.root.ids.telaabre.ids.labelreceita.text = str(record[1]).upper()
					self.root.ids.telaabre.ids.labeldescricao.text = str(record[2])
					self.root.ids.telaabre.ids.labelingred.text = str(record[3])
					self.root.ids.telaabre.ids.labelpreparo.text = str(record[4])
					self.root.ids.tbRecipe.title = instance.text.upper()
					self.root.current = 'telaAbreReceitas'	
		conn.commit()
		conn.close()
		
	dialog = None
	textDialog = ''
	textBt1 = ''
	textBt2 = ''
	def deleteFile(self):
		if not self.dialog:
			self.dialog = MDDialog(text=f"{self.textDialog}", buttons=[MDFlatButton(text=f"{self.textBt2}", on_press = self.close_dialogDel),MDFlatButton(text= f"{self.textBt1}", on_press = self.delete), ], )
		self.dialog.open()
		
	def close_dialogDel(self, *args):
		self.dialog.dismiss()

	def delete(self, *args):
		conn = sqlite3.connect('recipeDB.db')
		c = conn.cursor()
		for x in self.cats:
			if x.upper() in self.toolbarText:
				c.execute("DELETE from " +x+" where id = "+str(self.a))
		conn.commit()
		conn.close()
		self.showRecipes()
		self.callback()
		self.close_dialogDel()

	def modificarReceita(self):
		conn = sqlite3.connect('recipeDB.db')
		c = conn.cursor()
		for x in self.cats:
			if x.upper() in self.toolbarText:
				c.execute("SELECT * from " +x+" where id = "+str(self.a))
				records = c.fetchall()
				for record in records:
					self.root.ids.telamodifica.ids.modreceita.text = record[1]
					self.root.ids.telamodifica.ids.moddescricao.text = record[2]
					self.root.ids.telamodifica2.ids.modingred.text = record[3]
					self.root.ids.telamodifica3.ids.modpreparo.text = record[4]
		conn.commit()
		conn.close()
	
	def salvaModificarReceita(self):
		conn = sqlite3.connect('recipeDB.db')
		c = conn.cursor()
		name = self.root.ids.telamodifica.ids.modreceita.text
		desc = self.root.ids.telamodifica.ids.moddescricao.text
		ingred = self.root.ids.telamodifica2.ids.modingred.text
		prep = self.root.ids.telamodifica3.ids.modpreparo.text
		for x in self.cats:
			if x.upper() in self.toolbarText:
				exec = "UPDATE "+x+" set name = ?, desc = ?, ingred = ?, prep = ? where id = "+str(self.a)
				data = (name, desc,ingred, prep)
				c.execute(exec, data)
		conn.commit()
		conn.close()
		self.showRecipes()
		self.callback()
	
	dialogs = None
	txtReset = ''
	txtBt1 = ''
	txtBt2 = ''
	def resetChangeLangEN(self):
		if not self.dialogs:
			self.dialogs = MDDialog(text=f"{self.txtReset}", buttons=[MDFlatButton(text=f"{self.txtBt2}", on_press = self.close_dialogLang),MDFlatButton(text= f"{self.txtBt1}", on_press = self.closeEN), ], )
		self.dialogs.open()
		
	def resetChangeLangBR(self):
		if not self.dialogs:
			self.dialogs = MDDialog(text=f"{self.txtReset}", buttons=[MDFlatButton(text=f"{self.txtBt2}", on_press = self.close_dialogLang),MDFlatButton(text= f"{self.txtBt1}", on_press = self.closeBR), ], )
		self.dialogs.open()
	
	def closeBR(self, *args):
		self.changePTBRLang()
		Aplicativo().stop()
		
	def closeEN(self, *args):
		self.changeENLang()
		Aplicativo().stop()
	
	def close_dialogLang(self, *args):
		self.dialogs.dismiss()
	
	def insertConfig(self):
		conn = sqlite3.connect('recipeDB.db')
		c = conn.cursor()
		c.execute("INSERT OR IGNORE INTO config VALUES (:id, :name)", {'id': '1', 'name': 'EN',})
		c.execute("INSERT OR IGNORE INTO config VALUES (:id, :name)", {'id': '2', 'name': 'color1',})
		conn.commit()
		conn.close()
		
	idColor = 'color2'
	def loadColor(self):
		conn = sqlite3.connect('recipeDB.db')
		c = conn.cursor()
		c.execute("SELECT * FROM config")
		records = c.fetchall()
		for record in records:
			if record[1] == 'color1': self.changeThemeColor([0, 0, 0, 1])
			elif record[1] == 'color2': self.changeThemeColor([.5,0,.5,1])
			elif record[1] == 'color3': self.changeThemeColor([1,0,0,1])
			elif record[1] == 'color4': self.changeThemeColor([0,0,1,1])
			elif record[1] == 'color5': self.changeThemeColor([1,0,1,1])
			elif record[1] == 'color6': self.changeThemeColor([1,1,0,1])
			elif record[1] == 'color7': self.changeThemeColor([0,.5,0,1])
			elif record[1] == 'color8': self.changeThemeColor([.5,.5,.5,1])
		conn.commit()
		conn.close()
		
	def saveColor(self):
		conn = sqlite3.connect('recipeDB.db')
		c = conn.cursor()
		if self.idColor == 'color1': c.execute("UPDATE config set name = 'color1' where id = 2")
		elif self.idColor == 'color2': c.execute("UPDATE config set name = 'color2' where id = 2")
		elif self.idColor == 'color3': c.execute("UPDATE config set name = 'color3' where id = 2")
		elif self.idColor == 'color4': c.execute("UPDATE config set name = 'color4' where id = 2")
		elif self.idColor == 'color5': c.execute("UPDATE config set name = 'color5' where id = 2")
		elif self.idColor == 'color6': c.execute("UPDATE config set name = 'color6' where id = 2")
		elif self.idColor == 'color7': c.execute("UPDATE config set name = 'color7' where id = 2")
		elif self.idColor == 'color8': c.execute("UPDATE config set name = 'color8' where id = 2")
		conn.commit()
		conn.close()
	
	def loadLang(self):
		conn = sqlite3.connect('recipeDB.db')
		c = conn.cursor()
		c.execute("SELECT * FROM config")
		records = c.fetchall()
		for record in records:
			if record[1] == 'EN': self.changeENLang()
			elif record[1] == 'PT-BR': self.changePTBRLang()
		conn.commit()
		conn.close()
	
	
	
	def saveLang(self):
		conn = sqlite3.connect('recipeDB.db')
		c = conn.cursor()
		if self.codLang == '1':
			c.execute("UPDATE config set name = 'EN' where id = 1")
		elif self.codLang == '2':
			c.execute("UPDATE config set name = 'PT-BR' where id = 1")
		conn.commit()
		conn.close()
	
	codLang = '1'
	def changeENLang(self):
		self.codLang = '1'
		self.saveLang()
		self.root.ids.tbCategorie.title = 'CATEGORIES'
		self.root.ids.tbAdd.title = 'NEW RECIPE'
		self.root.ids.tbMod.title = 'EDIT RECIPE'
		self.root.ids.tbOption.title = 'CONFIGURATIONS'
		self.root.ids.categoria.ids.btCat1.text = '  DRINKS'
		self.root.ids.categoria.ids.btCat2.text = '  CAKES AND SWEET PIES'
		self.root.ids.categoria.ids.btCat3.text = '  MEAT'
		self.root.ids.categoria.ids.btCat4.text = '  SNACKS'
		self.root.ids.categoria.ids.btCat5.text = '  BREADS AND PASTA'
		self.root.ids.categoria.ids.btCat6.text = '  FISHES AND SEA FOOD'
		self.root.ids.categoria.ids.btCat7.text = '  SPECIAL DISHES'
		self.root.ids.categoria.ids.btCat8.text = '  SALADS, SAUCES AND SIDE DISHES'
		self.root.ids.categoria.ids.btCat9.text = '  DESSERTS'
		self.root.ids.categoria.ids.btCat10.text = '  SOUP'
		self.root.ids.telaadiciona.ids.nameadd.text = '  RECIPE NAME: '
		self.root.ids.telaadiciona.ids.descadd.text = '  RECIPE DESCRIPTION: '
		self.root.ids.telaadiciona2.ids.ingredadd.text = '  INGREDIENTS: '
		self.root.ids.telaadiciona3.ids.prepadd.text = '  PREPARATION METHOD:  '
		self.root.ids.tabrecipe.text = 'RECIPE'
		self.root.ids.tabingred.text = 'INGREDIENTS'
		self.root.ids.tabprep.text = 'PREPARATION METHOD'
		self.root.ids.telaabre.ids.ingredabre.text = 'Ingredients: '
		self.root.ids.telaabre.ids.prepabre.text = 'Preparation Method: '
		self.root.ids.tabmodrecipe.text = 'RECIPE'
		self.root.ids.tabmodingred.text = 'INGREDIENTS'
		self.root.ids.tabmodprep.text = 'PREPARATION METHOD'
		self.root.ids.telamodifica.ids.namemod.text = '  RECIPE NAME: '
		self.root.ids.telamodifica.ids.descmod.text = '  RECIPE DESCRIPTION: '
		self.root.ids.telamodifica2.ids.ingredmod.text = '  INGREDIENTS: '
		self.root.ids.telamodifica3.ids.prepmod.text = '  PREPARATION METHOD:  '
		self.root.ids.screenoption.ids.txtLang.text = '  LANGUAGES:'
		self.root.ids.screenoption.ids.txtTheme.text = '  THEME COLORS: '
		self.textDialog = 'Would you like to delete? '
		self.textBt1 = 'Confirm'
		self.textBt2 = 'Cancel'
		self.txtReset = 'Would you like to change the language? The application will be close'
		self.txtBt1 = 'Confirm'
		self.txtBt2 = 'Cancel'
		
	def changePTBRLang(self):
		self.codLang = '2'
		self.saveLang()
		self.root.ids.tbCategorie.title = 'CATEGORIAS'
		self.root.ids.tbAdd.title = 'NOVA RECEITA'
		self.root.ids.tbMod.title = 'EDITAR RECEITA'
		self.root.ids.tbOption.title = 'CONFIGURAÇÕES'
		self.root.ids.categoria.ids.btCat1.text = '  BEBIDAS'
		self.root.ids.categoria.ids.btCat2.text = '  BOLOS E TORTAS DOCES'
		self.root.ids.categoria.ids.btCat3.text = '  CARNES E AVES'
		self.root.ids.categoria.ids.btCat4.text = '  LANCHES'
		self.root.ids.categoria.ids.btCat5.text = '  PÃES E MASSAS'
		self.root.ids.categoria.ids.btCat6.text = '  PEIXES E FRUTOS DO MAR'
		self.root.ids.categoria.ids.btCat7.text = '  PRATOS ESPECIAIS'
		self.root.ids.categoria.ids.btCat8.text = '  SALADAS, MOLHOS E ACOMPANHAMENTOS'
		self.root.ids.categoria.ids.btCat9.text = '  SOBREMESAS'
		self.root.ids.categoria.ids.btCat10.text = '  SOPAS'
		self.root.ids.telaadiciona.ids.nameadd.text = '  NOME DA RECEITA: '
		self.root.ids.telaadiciona.ids.descadd.text = '  DESCRIÇÃO DA RECEITA: '
		self.root.ids.telaadiciona2.ids.ingredadd.text = '  INGREDIENTES: '
		self.root.ids.telaadiciona3.ids.prepadd.text = '  MODO DE PREPARO: '
		self.root.ids.tabrecipe.text = 'RECEITAS'
		self.root.ids.tabingred.text = 'INGREDIENTES'
		self.root.ids.tabprep.text = 'MODO DE PREPARO'
		self.root.ids.telaabre.ids.ingredabre.text = 'Ingredientes: '
		self.root.ids.telaabre.ids.prepabre.text = 'Modo de Preparo: '
		self.root.ids.tabmodrecipe.text = 'RECEITAS'
		self.root.ids.tabmodingred.text = 'INGREDIENTES'
		self.root.ids.tabmodprep.text = 'MODO DE PREPARO'
		self.root.ids.telamodifica.ids.namemod.text = '  NOME DA RECEITA: '
		self.root.ids.telamodifica.ids.descmod.text = '  DESCRIÇÃO DA RECEITA: '
		self.root.ids.telamodifica2.ids.ingredmod.text = '  INGREDIENTES: '
		self.root.ids.telamodifica3.ids.prepmod.text = '  MODO DE PREPARO: '
		self.root.ids.screenoption.ids.txtLang.text = '  IDIOMAS:'
		self.root.ids.screenoption.ids.txtTheme.text = '  CORES TEMA: '
		self.textDialog = 'Deseja Deletar? '
		self.textBt1 = 'Confirmar'
		self.textBt2 = 'Cancelar'
		self.txtReset = 'Gostaria de trocar o idioma? O aplicativo será fechado'
		self.txtBt1 = 'Confirmar'
		self.txtBt2 = 'Cancelar'
		
Aplicativo().run()