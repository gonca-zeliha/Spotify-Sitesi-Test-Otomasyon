import random
from selenium.webdriver.common.by import By


#KAYIT OL

BASE_URL = "https://open.spotify.com/"
KAYITOL_BUTON = (By.CLASS_NAME, "Button-sc-1dqy6lx-0.ljUEiq.sibxBMlr_oxWTfBrEz2G")
CEREZLERI_KABUL_ET = (By.ID, "onetrust-accept-btn-handler")
KAYIT_OL_MAIL = (By.ID, "username")
ILERI_BUTONU = (By.CLASS_NAME, "Button-sc-qlcn5g-0.cUOgcY")
KAYITOL_SIFRE = (By.ID, "new-password")
KAYITOL_ISIM = (By.ID, "displayName")
YAS_LOCATER = (By.ID, "day")
AY_LOCATER = (By.ID, "month")
YIL_LOCATER = (By.ID, "year")
CINSIYET_SEC_LOCATER = (By.CLASS_NAME, "Indicator-sc-hjfusp-0.jeEHZA")
BILGILENDIRMELERI_KABUL_ET = (By.CLASS_NAME, "Label-sc-cpoq-0.havZVP")
PRIVACY_BOX_LOCATE = (By.CSS_SELECTOR, "label[for='checkbox-privacy'].Label-sc-cpoq-0.havZVP")
PROFILE_PIC_LOCATE = (By.CLASS_NAME, "Button-sc-1dqy6lx-0.hpNmgY.encore-over-media-set.SFgYidQmrqrFEVh65Zrg")
SON_KAYIT_OL_BUTONU=(By.CLASS_NAME,"Button-sc-qlcn5g-0.cUOgcY")

##kayıtlı mail ile kayıtolma
KAYITLI_MAIL_UYARI_MESAJI =(By.CLASS_NAME,"Message-sc-15vkh7g-0.kxWrWw")
KAYITLI_MAIL_UYARI_MESAJI_TEXT =("Bu adresin bağlı olduğu bir hesap var. Devam etmek için oturum aç.")

#randon giris

randonint = str(random.randint(1000, 9999))
kullanici_eposta= ("gonca"+ randonint +"@hotmail.com")
kullanici_ad = "gonca"
kullanici_sifre = "g123456789"


#GİRİŞ

GIRIS_YAP_BUTONU_LOCATER = (By.XPATH, "//*[@id='main']/div/div[2]/div[3]/header/div[2]/div[3]/div[1]/button[2]")
GIRIS_MAILI_LOCATER = (By.ID, "login-username")
GIRIS_SIFRE_LOCATER = (By.ID, "login-password")
OTURUM_ACMA_BUTONU_LOCATER = (By.CLASS_NAME, "ButtonInner-sc-14ud5tc-0.liTfRZ.encore-bright-accent-set")
HATA_MESAJI = (By.CLASS_NAME, "Message-sc-15vkh7g-0.dHbxKh")
HATA_MESAJI_TEXT = "Kullanıcı adı veya parola yanlış."
OTURUMU_KAPAT = (By.CLASS_NAME, "Type__TypeElement-sc-goli3j-0.dsbIME.ellipsis-one-line.htqz7Vb8mLJvGKTi1vrs")
BOS_GIRIS_HATA_MESAJI=(By.CLASS_NAME,"Text-sc-g5kv67-0.jYLjty")



#SARKI ARA

ARAMA_BUTONU = (By.CLASS_NAME, "Svg-sc-ytk21e-0.bneLcE.search-icon.QbaKKdcHNA2x3_YJvpYu")
ARAMA_KUTUSU = (By.CLASS_NAME, "encore-text.encore-text-body-small.NtkAQg9R1r5CjuP0XHwl")
ARANAN_SARKI_FOTO = (By.CLASS_NAME, "ouEZqTcvcvMfvezimm_J")
ARANAN_SARKIYI_GOR=(By.CLASS_NAME,"w46g_LQVSLE9xK399VYf")
DUR_BUTONU=(By.CLASS_NAME,"vnCew8qzJq3cVGlYFXRI")
DUR_BUTONU_TEXT = ("Duraklat")
PLAY_BUTONU_TEXT = ("Çal")
PLAY_BUTONU = (By.CLASS_NAME, "vnCew8qzJq3cVGlYFXRI")
BEGENILEN_SARKI_LISTESI_BUTONU=(By.CLASS_NAME,"O5NOY8Xw4NH0IhBZu8tm")
BEGENILEN_SARKI_MESAJI_LOCATER=(By.CLASS_NAME,"r4Hbxvv02KfOVeZ_v335")
BEGENILEN_SARKI_MESAJI_TEXT=("Beğenilen Şarkılar çalma listesine eklendi.")
ATLA = (By.CLASS_NAME, "mnipjT4SLDMgwiDCEnRC")
SARKIYI_BUL = (By.CLASS_NAME, "deomraqfhIAoSB3SgXpu")


#CALMA LİSTESİ

CALMA_LISTESI_BUTONU=(By.CLASS_NAME,"Button-sc-1dqy6lx-0.hidZeW.cljOO1tpzixzXctKJucK.nGWhztVvLY1BInXjcWYa.NxEINIJHGytq4gF1r2N1.or84FBarW2zQhXfB9VFb.XNjgtSbyhshr7YQcVvry.O0AN8Ty_Cxd4iLwyKATB.D8wJ9TPfJzLeLJYxnad2.zWWLnqWslTLHwq3wBgGB")
YENI_CALMA_LISTESI_OLUSTUR_BUTONU=(By.XPATH,"//*[@id='context-menu']/ul/li[1]/button/span")
SARKI_ARA=(By.CLASS_NAME,"encore-text.encore-text-body-small.FeWwGSRANj36qpOBoxdx")
SARKI_ADI=("her şeyi yak")
EKLE_BUTONUNA_TIKLA=(By.XPATH,"//*[@id='main']/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/main/div[1]/section/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div/div[4]/button")
OLUSTURULAN_CALMA_LISTESINE_TIKLA=(By.XPATH,"//*[@id='Desktop_LeftSidebar_Id']/nav/div[2]/div[1]/div[2]/div[2]/div/div[2]/ul/div/div[2]/li[2]/div/div[1]")
CALMA_LISTESI_ADINI_DEGISIR=(By.CLASS_NAME,"o4KVKZmeHsoRZ2Ltl078")
CALMA_LISTESI_EKLE=(By.CLASS_NAME,"f0GjZQZc4c_bKpqdyKbq.JaGLdeBa2UaUMBT44vqI.UCj7uEr7vR_0DO3cQHcX")
CALMA_LISTESI_ADI_TEXT=("GONCA")
KAYDET_BUTONU=(By.CLASS_NAME,"ButtonInner-sc-14ud5tc-0.cnKUru.encore-inverted-light-set")

CALMA_LITESINDE_UC_NOKTA=(By.CLASS_NAME,"Svg-sc-ytk21e-0.cqasRA")
CALMA_LISTESINDE_SIL_BUTONU=(By.XPATH,"//*[@id='context-menu']/ul/li[4]/button/span")
SILMEYE_EMINMISIN_SIL=(By.CLASS_NAME,"Button-sc-qlcn5g-0.bGlWbV.encore-text-body-medium-bold")

KITAPLIGINDAN_KALDIRILDI=(By.CLASS_NAME,"encore-text.encore-text-body-medium.encore-internal-color-text-base")
KITAPLIGINDAN_KALDIRILDI_TEXT=("Kitaplığın'dan kaldırıldı.")

##TEST DATA##

GIRIS_MAILI = ("logi_01_02@hotmail.com")
KAYITOL_MAILI = ("logi_01_02@hotmail.com")
SIFRE= ("l123456789*")
ISIM = ("GONCA")
GUN = ("24")
AY = "//*[@id='month']/option[02]"
YIL = ("1992")
TEST_ARAMA_SARKISI = ("ATEŞTEN GÖMLEK")
FORMAT_DISI_MAIL=("AAAAA")
FORMAT_DISI_SIFRE=("AAAAA")

##EKRAN GÖRÜNTÜSÜ
FOTO_KAYITLI_MAIL_ADRESI_POPUP_MESAJI= r'screenshots\kayitol\Kayıtlı mail adresi uyarı mesajı.png'
FOTO_GIRISDE_HATALI_MAIL_VE_SIFRE_POPUP_MESAJI= r'screenshots\girisyap\Hatalı mail ve sifre.png'
FOTO_GIRISDE_BOS_MAIL_VE_SIFRE= r'screenshots\girisyap\Bos mail ve sifre.png'
FOTO_SARKI_BEGENILENLERE_EKLENDI_POPUP=r'screenshots\sarkıarama\Sarkıyı begenilenlere ekleme.png'
FOTO_CALMA_LISTESI_ADI=r'screenshots\calmalistesi\çalma listesi adı değiştirildi.png'
FOTO_CALMA_LISTESINDEN_SARKI_KALDIRILDI=r'screenshots\calmalistesi\çalma listesinden sarkı kaldırıldı.png'
