import pytest
from time import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from pages.PageBase import PageBase
from constans.globalconstans import*


@pytest.mark.usefixtures("setup")
class KayıtOl(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def çerezleri_kabul_et(self):
        self.wait_element_visibility(CEREZLERI_KABUL_ET).click()

    def Kayıt_ol_butonuna_tıkla(self):
        self.wait_element_visibility(KAYITOL_BUTON).click()

    def Email_adresini_gir(self):
        self.wait_element_visibility(KAYIT_OL_MAIL).send_keys(kullanici_eposta)
        sleep(1)

    def ileri_butonuna_tıkla(self):
        self.wait_element_visibility(ILERI_BUTONU).click()
    
    def sifreni_gir(self):
        self.wait_element_visibility(KAYITOL_SIFRE).send_keys(kullanici_sifre)
        sleep(1)
    
    def ileri_butonuna_tıkla_birazbekle(self):
        self.wait_element_visibility(ILERI_BUTONU).click()
        sleep(5)

    def adını_yaz(self):
        self.wait_element_visibility(KAYITOL_ISIM).send_keys(ISIM)
    
    def Dogum_tarihini_gün_ay_yıl_olarak_sec(self):

        self.wait_element_visibility(YAS_LOCATER).send_keys(GUN)
        sleep(1)
        Select(self.wait_element_visibility(AY_LOCATER)).select_by_value("1")
        sleep(1)
        self.wait_element_visibility(YIL_LOCATER).send_keys(YIL)

    def cinsiyet_sec(self):
        self.wait_element_visibility(CINSIYET_SEC_LOCATER).click()
    
    def ileri_butonuna_tıkla(self):
        self.wait_element_visibility(ILERI_BUTONU).click()
        sleep(1)

    def son_kayıt_ol_butonuna_tıkla(self):
        self.wait_element_visibility(SON_KAYIT_OL_BUTONU).click()
    
    # def ekran_foto_cek(self):
    #     ekrangoruntusu_path = FOTO_CALMA_LISTESI_OLUSTURULDU
    #     self.driver.save_screenshot(ekrangoruntusu_path)
    
    def spotify_profilini_doğrula(self):
        profil_buttonu = self.wait_element_visibility(PROFILE_PIC_LOCATE)
        etiket = profil_buttonu.get_attribute('aria-label')
        return etiket
    
    ##aynı mail ile kayıtol

    def kayıtlı_mail_adresi_yaz(self):
        self.wait_element_visibility(KAYIT_OL_MAIL).send_keys(KAYITOL_MAILI)
    
    def bos_birakilan_alanlar_hata_mesaji(self):
        popup = self.wait_element_visibility(KAYITLI_MAIL_UYARI_MESAJI)
        return popup.text
    
    def ekran_foto_cek(self):
        ekrangoruntusu_path = FOTO_KAYITLI_MAIL_ADRESI_POPUP_MESAJI
        self.driver.save_screenshot(ekrangoruntusu_path)

    