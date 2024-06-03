import pytest
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from pages.PageBase import PageBase
from constans.globalconstans import*

@pytest.mark.usefixtures("setup")
class CalmaListesiEkle(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    
    def çalma_listesi_ekle_butonuna_tıkla(self):
        self.wait_element_visibility(CALMA_LISTESI_BUTONU).click()

    def yeni_bir_çalma_listesi_oluştur(self):
        self.wait_element_visibility(YENI_CALMA_LISTESI_OLUSTUR_BUTONU).click()

    def sarkı_araması_yap(self):
        tıkla=self.wait_element_visibility(SARKI_ARA)
        tıkla.click()
        tıkla.send_keys(SARKI_ADI)

    def sarkıyı_listeye_ekle(self):
        self.wait_element_visibility(EKLE_BUTONUNA_TIKLA).click()

@pytest.mark.usefixtures("setup")
class CalmaListesiDüzenle(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    def oluşturulan_calma_listesine_tıkla(self):
        self.wait_element_visibility(OLUSTURULAN_CALMA_LISTESINE_TIKLA).click()

    def calma_listesi_adını_değiştir(self):
        self.wait_element_visibility(CALMA_LISTESI_ADINI_DEGISIR).click()

    def calma_listesi_adı_ekle(self):
        tıkla=self.wait_element_visibility(CALMA_LISTESI_EKLE)
        tıkla.click()
        sleep(2)
        tıkla.send_keys(CALMA_LISTESI_ADI_TEXT)
    

    def kaydet_butonuna_tıkla(self):
        self.wait_element_visibility(KAYDET_BUTONU).click()
    
    def ekran_foto_cek(self):
        ekrangoruntusu_path = FOTO_CALMA_LISTESI_ADI
        self.driver.save_screenshot(ekrangoruntusu_path)