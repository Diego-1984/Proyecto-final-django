from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class PruebasFuncionales(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Usa ChromeDriver

    def tearDown(self):
        self.driver.quit()  # Cierra el navegador al terminar

    def test_pagina_inicio(self):
        # Abrir la página en el navegador
        self.driver.get(self.live_server_url)

        # Buscar un elemento por su etiqueta <h1>
        encabezado = self.driver.find_element(By.TAG_NAME, "h1")

        # Verificar que el título de la página es correcto
        self.assertEqual(encabezado.text, "Gestión de Pedidos")
