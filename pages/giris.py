import pytest
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from pages.PageBase import PageBase
from constans.globalconstans import *

@pytest.mark.usefixtures("setup")
class AnaGiris(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
   
    def ana_giris(self):
        self.wait_element_visibility(GIRIS_YAP_BUTONU_LOCATER).click()
        self.wait_element_visibility(GIRIS_MAILI_LOCATER).send_keys(GIRIS_MAILI)
        self.wait_element_visibility(GIRIS_SIFRE_LOCATER).send_keys(SIFRE)
        self.wait_element_clickable(OTURUM_ACMA_BUTONU_LOCATER).click()


@pytest.mark.usefixtures("setup")
class GirisYap(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

##basarılı giris yapıp sonra oturumu kapatacak

    def giris_yap_butonuna_tikla(self):
        self.wait_element_visibility(GIRIS_YAP_BUTONU_LOCATER).click()


    def sayfayi_asagi_kaydir (self):
        self.driver.execute_script("scrollBy(0,500)")
        
    
    def giris_bilgisi_doldur(self):
        self.wait_element_visibility(GIRIS_MAILI_LOCATER).send_keys(GIRIS_MAILI)
        self.wait_element_visibility(GIRIS_SIFRE_LOCATER).send_keys(SIFRE)
    
    def oturumu_ac_butonuna_tıkla(self):
        self.wait_element_visibility(OTURUM_ACMA_BUTONU_LOCATER).click()
    
    def hata_mesaji(self):
        popup = self.wait_element_visibility(HATA_MESAJI)
        return popup.text
    
    def oturumu_kapat(self):
       self.wait_element_visibility(OTURUMU_KAPAT).click()

    ##formata uygun olmayan mailve şifre giris yap

    def giris_bilgisini_formata_uygun_olmadan_doldur(self):
        self.wait_element_visibility(GIRIS_MAILI_LOCATER).send_keys(FORMAT_DISI_MAIL)
        self.wait_element_visibility(GIRIS_SIFRE_LOCATER).send_keys(FORMAT_DISI_SIFRE)
    
    def ekran_foto_cek(self):
        ekrangoruntusu_path = FOTO_GIRISDE_HATALI_MAIL_VE_SIFRE_POPUP_MESAJI
        self.driver.save_screenshot(ekrangoruntusu_path)
    

    ## giris işleminde mail ve şifreyi boş bırak

    def ekran_fotosu_cek(self):
        ekrangoruntusu_path = FOTO_GIRISDE_BOS_MAIL_VE_SIFRE
        self.driver.save_screenshot(ekrangoruntusu_path)
    
  
        
    