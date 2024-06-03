from time import sleep
from ddt import ddt, data, unpack
from selenium import webdriver
from pages.giris import *
from pages.kayitol import *
from pages.sarkı_araması import *
import allure
import softest
import unittest
import pytest
from constest import *

@pytest.mark.usefixtures("setup")
@ddt
class TestSarkiAra(softest.TestCase, unittest.TestCase):
    


    def test1_sarkı_araması_yapar_ve_sarkıyı_beğenilenler_listesine_ekler(self):
        girisyap = AnaGiris(self.driver)
        kayitol = KayıtOl(self.driver)
        sarkiarama =SarkıArama(self.driver)
        kayitol.çerezleri_kabul_et()
        girisyap.ana_giris()
        sarkiarama.arama_butonuna_tıkla()
        sarkiarama.sarkı_araması_yap()
        sarkiarama.sarkıyı_başlat()
        sarkiarama.sarkıyı_atla()
        sarkiarama.dur_butonuna_tıkla()
        sarkiarama.sarkıyı_begenilenler_listesine_ekle()
        sarkiarama.sarkıyı_begenilenler_listesine_popup_mesajı()
        sarkiarama.ekran_foto_cek()

       