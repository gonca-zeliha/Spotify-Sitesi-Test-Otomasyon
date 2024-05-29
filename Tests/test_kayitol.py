from time import sleep
from ddt import ddt, data, unpack
from selenium import webdriver
from pages.kayitol import *
import allure
import softest
import unittest
import pytest
from constest import *

@pytest.mark.usefixtures("setup")
@ddt
class TestKayıtOl(softest.TestCase, unittest.TestCase):
    


    def test1_basarili_kayit_ol(self):
       
      
        kayitol = KayıtOl(self.driver)
        kayitol.çerezleri_kabul_et()
        kayitol.Kayıt_ol_butonuna_tıkla()
        kayitol.Email_adresini_gir()
        kayitol.ileri_butonuna_tıkla()
        kayitol.sifreni_gir()
        kayitol.ileri_butonuna_tıkla_birazbekle()
        kayitol.adını_yaz()
        kayitol.Dogum_tarihini_gün_ay_yıl_olarak_sec()
        kayitol.cinsiyet_sec()
        kayitol.ileri_butonuna_tıkla()
        kayitol.son_kayıt_ol_butonuna_tıkla()
        kayitol.spotify_profilini_doğrula()
    
    def test2_kayıtlı_mail_ile_kayıt_olma(self): 

        kayitol = KayıtOl(self.driver)
        kayitol.çerezleri_kabul_et
        kayitol.Kayıt_ol_butonuna_tıkla()
        kayitol.kayıtlı_mail_adresi_yaz()
        kayitol.ileri_butonuna_tıkla()
        kayitol.bos_birakilan_alanlar_hata_mesaji()
        kayitol.çerezleri_kabul_et()
        sleep(3)
        kayitol.ekran_foto_cek()
    
    
      
        