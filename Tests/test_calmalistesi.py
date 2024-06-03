from time import sleep
from ddt import ddt, data, unpack
from selenium import webdriver
from pages.giris import *
from pages.kayitol import *
from pages.calmalistesi import *
import allure
import softest
import unittest
import pytest
from constest import *

@pytest.mark.usefixtures("setup")
@ddt
class Testcalmalistesi(softest.TestCase, unittest.TestCase):
    


    def test1_calma_listesi_oluştur(self):
        girisyap = AnaGiris(self.driver)
        kayitol = KayıtOl(self.driver)
        calmalistesi =CalmaListesiEkle(self.driver)
        kayitol.çerezleri_kabul_et()
        girisyap.ana_giris()
        calmalistesi.çalma_listesi_ekle_butonuna_tıkla()
        calmalistesi.yeni_bir_çalma_listesi_oluştur()
        calmalistesi.sarkı_araması_yap()
        calmalistesi.sarkıyı_listeye_ekle()

    def test2_calma_listesi_adını_değiştir(self):
        girisyap = AnaGiris(self.driver)
        kayitol = KayıtOl(self.driver)
        calmalistesi =CalmaListesiDüzenle(self.driver)
        kayitol.çerezleri_kabul_et()
        girisyap.ana_giris()
        calmalistesi.oluşturulan_calma_listesine_tıkla()
        calmalistesi.calma_listesi_adını_değiştir()
        calmalistesi.calma_listesi_adı_ekle()
        calmalistesi.kaydet_butonuna_tıkla()
        calmalistesi.ekran_foto_cek()
