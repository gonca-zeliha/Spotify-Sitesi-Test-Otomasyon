# import pytest
# from time import sleep
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.ui import Select
# from pages.PageBase import PageBase
# from constans.globalconstans import *

# @pytest.mark.usefixtures("setup")
# class CalmaListesiOlustur(PageBase):
#     def __init__(self,driver):
#         super().__init__(driver)
#         self.driver = driver

#     # def anasayfa_profil_bilgileri_butonuna_tikla(self):
#     #     self.wait_element_visibility(ANA_PROFIL_BUTONU).click()
    
#     # def profil_ismine_tikla(self):
#     #     self.wait_element_visibility(PROFIL_ISMI_BUTONU).click()
    
#     def calma_listesi_olustur_tikla(self):
#         self.wait_element_visibility(ANA_SAYFA_CALMA_LISTESI_OLUSTUR_BUTONU).click()
    
#     def calma_listesi_ismi_olustur(self):
#         self.wait_element_visibility(CALMA_LISTESI_ISMI_OLUSTUR).send_keys(CALMA_LISTESI_ISMI)

#     def calma_litesini_ozel_yap_butonunu_aktif_et(self):
#         buton= self.wait_element_visibility(CALMA_LISTESI_OZEL_BUTONU_AKTIF_ET)
#         buton.click()

#     def calma_listesine_tanim_ekle(self):
#         self.wait_element_visibility(CALMA_LISTESINE_TANIM_EKLE).send_keys(CALMA_LISTESI_TANIMI)

#     def olustur_butonuna_tikla(self):
#         self.wait_element_visibility(OLUSTUR_TIKLA).click()

#     def calma_listesi_olusturma_basarili(self):
#         msg_box = self.wait_element_visibility(CALMA_LISTESI_OLUSTUR_BASARILI_POPUP_MESAJI)
#         return msg_box.text
    
#     def ekran_foto_cek(self):
#         ekrangoruntusu_path = FOTO_CALMA_LISTESI_OLUSTURULDU
#         self.driver.save_screenshot(ekrangoruntusu_path)
#     # def calma_listesi_olusturma_basaril(self):
#     #     beklenen_mesaj =self.wait_element_presence(CALMA_LISTESI_OLUSTUR_BASARILI_POPUP_MESAJI)
#     #     assert beklenen_mesaj.text == CALMA_LISTESI_OLUSTUR_BASARILI_POPUP_MESAJI_TEXT 
#     #     sleep(2)
    
# @pytest.mark.usefixtures("setup")
# class SarkiEkle(PageBase):
#     def __init__(self,driver):
#         super().__init__(driver)
#         self.driver = driver

#     def olusturulan_calma_listesine_tikla(self):
#         self.wait_element_visibility(ANA_SAYFA_OLUSTURULAN_CALMA_LISTESINE_TIKLA).click()

#     def sarki_ekle_butonuna_tikla(self):
#         self.wait_element_visibility(SARKI_EKLE_BUTONU).click()
    
#     def sanatci_adi_yaz(self):
#         self.wait_element_visibility(SANATCI_SARKI_ARAMA_YAP).send_keys(SANATCI_SARKI_ARAMA_YAP_METIN)

#     def ilk_sarkiyi_ekle(self):
#         self.wait_element_visibility(ILK_CIKAN_SARKI).click()

#     def ekran_foto_cek(self):
#         ekrangoruntusu_path = FOTO_SARKI_EKLE
#         self.driver.save_screenshot(ekrangoruntusu_path)

# @pytest.mark.usefixtures("setup")
# class CalmaListesiSil(PageBase):
#     def __init__(self,driver):
#         super().__init__(driver)
#         self.driver = driver
    
#     # def anasayfa_profil_bilgileri_butonuna_tikla(self):
#     #     self.wait_element_visibility(ANA_PROFIL_BUTONU).click()
    
#     # def profil_ismine_tikla(self):
#     #     self.wait_element_visibility(PROFIL_ISMI_BUTONU).click()

#     def sayfayi_asagi_kaydir (self):
#         self.driver.execute_script("scrollBy(0,500)")
#         sleep(2)
        
#     def olusturulan_calma_listesine_tikla(self):
#         self.wait_element_visibility(ANA_SAYFA_OLUSTURULAN_CALMA_LISTESINE_TIKLA).click()

    
#     def olusturulan_calma_listesinin_altindaki_3_noktaya_tikla(self):
#         self.wait_element_visibility(CALMA_LISTESINDE_3_NOKTAYA_TIKLA).click()
    
#     def bu_calma_listesini_sil_butonuna_tikla(self):
#         self.wait_element_visibility(BU_CALMA_LISTESINI_SIL).click()

#     def calma_listesini_sil_onayini_ver(self):
#         sil=self.wait_element_visibility(CALMA_LISTESINI_SIL_ONAYI)
#         sil.click()
    
#     def ekran_foto_cek(self):
#         ekrangoruntusu_path = FOTO_CALMA_LISTESI_SILINDI
#         self.driver.save_screenshot(ekrangoruntusu_path)
    
#     # def calma_listesi_silme_basarili_popup_mesaji(self):
        
#     #     msg_box = self.wait_element_visibility(CALMA_LISTESINI_SILINDI_POPUP_MESAJI)
#     #     return msg_box.text
    
#     # def calma_listesi_silme_basarili_popup_mesaji(self):
#     #     beklenen_mesaj =self.wait_element_presence(CALMA_LISTESINI_SILINDI_POPUP_MESAJI)
#     #     assert beklenen_mesaj.text == CALMA_LISTESINI_SILINDI_POPUP_MESAJI_TEXT 
#     #     sleep(2)