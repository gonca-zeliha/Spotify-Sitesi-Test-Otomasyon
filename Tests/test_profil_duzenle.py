# from time import sleep
# from ddt import ddt, data, unpack
# from selenium import webdriver
# from pages.kayitol import *
# from pages.giris import *
# import allure
# import softest
# import unittest
# import pytest
# from constest import *
# from pages.profil_duzenle import *

# @pytest.mark.usefixtures("setup")
# @ddt
# class TestProfilDuzenle(softest.TestCase, unittest.TestCase):
    


#     def test1_calma_listesi_olustur(self):
#         kayitol = KayitOl(self.driver)
#         profilduzenle= CalmaListesiOlustur(self.driver)
#         kayitol.cerezleri_kabul_et()
#         sleep(2)
#         giris=AnaGiris(self.driver) 
#         giris.ana_giris()
#         sleep(2)
#         profilduzenle.calma_listesi_olustur_tikla()
#         profilduzenle.calma_listesi_ismi_olustur()
#         sleep(2)
#         profilduzenle.calma_litesini_ozel_yap_butonunu_aktif_et()
#         profilduzenle.calma_listesine_tanim_ekle()
#         (2)
#         profilduzenle.olustur_butonuna_tikla()
#         profilduzenle.calma_listesi_olusturma_basarili()
#         profilduzenle.ekran_foto_cek()
    
#     def test2_calma_listesine_sarki_ekle(self):
#         kayitol = KayitOl(self.driver)
#         kayitol.cerezleri_kabul_et()
#         giris=AnaGiris(self.driver) 
#         giris.ana_giris()
#         sarki_ekle= SarkiEkle(self.driver)
#         sarki_ekle.olusturulan_calma_listesine_tikla()
#         sarki_ekle.sarki_ekle_butonuna_tikla()
#         sarki_ekle.sanatci_adi_yaz()
#         sarki_ekle.ilk_sarkiyi_ekle()
#         sarki_ekle.ekran_foto_cek()


#     def test3_calma_listesi_sil(self):
#         kayitol = KayitOl(self.driver)
#         kayitol.cerezleri_kabul_et()
#         sleep(2)
#         giris=AnaGiris(self.driver) 
#         giris.ana_giris()
#         profilduzenle= CalmaListesiSil(self.driver)
#         sleep(2)
#         profilduzenle.sayfayi_asagi_kaydir()
#         profilduzenle.olusturulan_calma_listesine_tikla()
#         profilduzenle.olusturulan_calma_listesinin_altindaki_3_noktaya_tikla()
#         profilduzenle.bu_calma_listesini_sil_butonuna_tikla()
#         profilduzenle.calma_listesini_sil_onayini_ver()
#         profilduzenle.ekran_foto_cek()
     
        
        
      
    