from time import sleep
from ddt import ddt, data, unpack
from selenium import webdriver
from pages.giris import *
from pages.kayitol import *
import allure
import softest
import unittest
import pytest
from constest import *

@pytest.mark.usefixtures("setup")
@ddt
class TestGirisYap(softest.TestCase, unittest.TestCase):
    


    def test1_giris_yap(self):
        girisyap = GirisYap(self.driver)
        kayitol = KayıtOl(self.driver)
        kayitol.çerezleri_kabul_et()
        girisyap.giris_yap_butonuna_tikla()
        girisyap.sayfayi_asagi_kaydir()
        girisyap.giris_bilgisi_doldur()
        girisyap.oturumu_ac_butonuna_tıkla()
        girisyap.hata_mesaji()
        girisyap.oturumu_kapat()

     
    def test2_giris_isleminde_mail_ve_sifre_formata_uygun_degil(self):
        girisyap = GirisYap(self.driver)
        kayitol = KayıtOl(self.driver)
        kayitol.çerezleri_kabul_et()
        girisyap.giris_yap_butonuna_tikla()
        girisyap.sayfayi_asagi_kaydir()
        girisyap.giris_bilgisini_formata_uygun_olmadan_doldur()
        girisyap.oturumu_ac_butonuna_tıkla()
        girisyap.hata_mesaji()
        girisyap.ekran_foto_cek()
    
    def test3_giris_islemini_bos_birak(self):

        girisyap = GirisYap(self.driver)
        kayitol = KayıtOl(self.driver)
        kayitol.çerezleri_kabul_et()
        girisyap.giris_yap_butonuna_tikla()
        girisyap.sayfayi_asagi_kaydir()
        girisyap.oturumu_ac_butonuna_tıkla()
        girisyap.hata_mesaji()
        girisyap.ekran_fotosu_cek()
     


      
        