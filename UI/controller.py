import flet as ft
from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO
    def mostra(self,e):
        lista_automobili = self._model.get_automobili()
        if len(lista_automobili)>0:
            self._view.mostra_auto(lista_automobili)
        else:
            self._view.show_alert("Nessuna automobile trovata nel database")

    def cerca(self,e):
        modello = self._view.input_modello_auto
        if not modello:
            self._view.show_alert("Inserisci un modello valido")

        else:
            lista_automobili_modello = self._model.cerca_automobili_per_modello(modello)
            if len(lista_automobili_modello)>0:
                self._view.mostra_risultati_ricerca(lista_automobili_modello)
            else:
                self._view.show_alert("Inserisci un modello valido")



