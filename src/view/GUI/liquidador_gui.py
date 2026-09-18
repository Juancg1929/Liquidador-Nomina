from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

import sys
import os

# Obtener la ruta del proyecto raíz
# liquidador_gui.py está en: Liquidador-Nomina/src/view/GUI/
# Necesitamos: Liquidador-Nomina/
ruta_actual = os.path.dirname(os.path.abspath(__file__))  # ...GUI/
ruta_view = os.path.dirname(ruta_actual)  # ...view/
ruta_src = os.path.dirname(ruta_view)  # ...src/
ruta_proyecto = os.path.dirname(ruta_src)  # Liquidador-Nomina/

sys.path.insert(0, ruta_proyecto)

from src.model.logica_nomina import calcular_nomina
from src.model.datos_nomina import DatosNomina


class LiquidadorNominaApp(App):
    
    def build(self):
        from kivy.uix.boxlayout import BoxLayout
        
        # Contenedor principal con scroll
        contenedor_principal = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Título
        titulo = Label(
            text="LIQUIDADOR DE NÓMINA",
            font_size=32,
            bold=True,
            size_hint_y=None,
            height=50
        )
        contenedor_principal.add_widget(titulo)
        
        # Bienvenida
        bienvenida = Label(
            text="Bienvenido al sistema de cálculo de liquidación de nómina",
            font_size=14,
            size_hint_y=None,
            height=30
        )
        contenedor_principal.add_widget(bienvenida)
        
        # Descripción
        descripcion = Label(
            text="Ingrese los datos del empleado para calcular el salario neto\n"
                 "considerando deducciones de salud y pensión",
            font_size=12,
            size_hint_y=None,
            height=50,
            text_size=(500, None)
        )
        contenedor_principal.add_widget(descripcion)
        
        # Separador visual
        separador = Label(text="", size_hint_y=None, height=10)
        contenedor_principal.add_widget(separador)
        
        # Grid para los campos de entrada
        contenedor = GridLayout(cols=2, padding=10, spacing=15, size_hint_y=None, height=350)
        
        # Salario básico
        contenedor.add_widget(Label(text="Salario básico", size_hint_x=0.4))
        self.salario = TextInput(font_size=20, multiline=False)
        contenedor.add_widget(self.salario)
        
        # Días trabajados
        contenedor.add_widget(Label(text="Días trabajados", size_hint_x=0.4))
        self.dias = TextInput(font_size=20, multiline=False)
        contenedor.add_widget(self.dias)
        
        # Bonificación
        contenedor.add_widget(Label(text="Bonificación", size_hint_x=0.4))
        self.bonificacion = TextInput(font_size=20, multiline=False)
        contenedor.add_widget(self.bonificacion)
        
        # Comisión
        contenedor.add_widget(Label(text="Comisión", size_hint_x=0.4))
        self.comision = TextInput(font_size=20, multiline=False)
        contenedor.add_widget(self.comision)
        
        # Otros descuentos
        contenedor.add_widget(Label(text="Otros descuentos", size_hint_x=0.4))
        self.descuentos = TextInput(font_size=20, multiline=False)
        contenedor.add_widget(self.descuentos)
        
        # Agregar el grid de campos al contenedor principal
        contenedor_principal.add_widget(contenedor)
        
        # Botón calcular
        calcular = Button(text="Calcular", font_size=30, size_hint_y=None, height=60)
        calcular.bind(on_press=self.calcular_liquidacion)
        contenedor_principal.add_widget(calcular)
        
        # Resultado
        self.resultado = Label(text="", font_size=18, size_hint_y=None, height=80)
        contenedor_principal.add_widget(self.resultado)
        
        return contenedor_principal
    
    def calcular_liquidacion(self, value):
        try:
            self.validar()
            
            datos = DatosNomina(
                salario=float(self.salario.text),
                dias=int(self.dias.text),
                bonificacion=float(self.bonificacion.text),
                comision=float(self.comision.text),
                descuentos=float(self.descuentos.text)
            )
            
            neto = calcular_nomina(datos)
            
            texto = f"Neto a pagar: ${neto:,.2f}"
            self.resultado.text = texto
            
        except ValueError as err:
            self.mostrar_error("El valor ingresado no es un número válido")
        except Exception as err:
            self.mostrar_error(str(err))
    
    def validar(self):
        if not self.salario.text:
            raise Exception("El Salario básico no puede estar vacío")
        if not self.dias.text:
            raise Exception("Los Días trabajados no pueden estar vacíos")
        if not self.bonificacion.text:
            raise Exception("La Bonificación no puede estar vacía")
        if not self.comision.text:
            raise Exception("La Comisión no puede estar vacía")
        if not self.descuentos.text:
            raise Exception("Los Otros descuentos no pueden estar vacíos")
    
    def mostrar_error(self, err):
        contenido = GridLayout(cols=1)
        contenido.add_widget(Label(text=str(err)))
        
        cerrar = Button(text="Cerrar")
        contenido.add_widget(cerrar)
        
        popup = Popup(title="Error", content=contenido)
        cerrar.bind(on_press=popup.dismiss)
        
        popup.open()


if __name__ == "__main__":
    app = LiquidadorNominaApp()
    app.title = "Liquidador de Nómina"
    app.run()



if __name__ == "__main__":
    LiquidadorNominaApp().run()
