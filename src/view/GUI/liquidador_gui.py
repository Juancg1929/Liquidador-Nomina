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
        contenedor = GridLayout(cols=2, padding=20, spacing=20)
        
        # Salario básico
        contenedor.add_widget(Label(text="Salario básico"))
        self.salario = TextInput(font_size=30)
        contenedor.add_widget(self.salario)
        
        # Días trabajados
        contenedor.add_widget(Label(text="Días trabajados"))
        self.dias = TextInput(font_size=30)
        contenedor.add_widget(self.dias)
        
        # Bonificación
        contenedor.add_widget(Label(text="Bonificación"))
        self.bonificacion = TextInput(font_size=30)
        contenedor.add_widget(self.bonificacion)
        
        # Comisión
        contenedor.add_widget(Label(text="Comisión"))
        self.comision = TextInput(font_size=30)
        contenedor.add_widget(self.comision)
        
        # Otros descuentos
        contenedor.add_widget(Label(text="Otros descuentos"))
        self.descuentos = TextInput(font_size=30)
        contenedor.add_widget(self.descuentos)
        
        # Resultado
        self.resultado = Label(text="", font_size=20)
        contenedor.add_widget(self.resultado)
        
        # Botón calcular
        calcular = Button(text="Calcular", font_size=40)
        calcular.bind(on_press=self.calcular_liquidacion)
        contenedor.add_widget(calcular)
        
        return contenedor
    
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
    LiquidadorNominaApp().run()
