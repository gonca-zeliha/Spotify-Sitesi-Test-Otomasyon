import random
from selenium.webdriver.common.by import By


##kayıtol##

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


##LOGIN##

GIRIS_YAP_BUTONU_LOCATER = (By.XPATH, "//*[@id='main']/div/div[2]/div[3]/header/div[2]/div[3]/div[1]/button[2]")
GIRIS_MAILI_LOCATER = (By.ID, "login-username")
GIRIS_SIFRE_LOCATER = (By.ID, "login-password")
OTURUM_ACMA_BUTONU_LOCATER = (By.CLASS_NAME, "ButtonInner-sc-14ud5tc-0.liTfRZ.encore-bright-accent-set")
HATA_MESAJI = (By.CLASS_NAME, "Message-sc-15vkh7g-0.dHbxKh")
HATA_MESAJI_TEXT = "Kullanıcı adı veya parola yanlış."
OTURUMU_KAPAT = (By.CLASS_NAME, "Type__TypeElement-sc-goli3j-0.dsbIME.ellipsis-one-line.htqz7Vb8mLJvGKTi1vrs")
BOS_GIRIS_HATA_MESAJI=(By.CLASS_NAME,"Text-sc-g5kv67-0.jYLjty")



##PLAYBACK##

SEARCH_BUTTON_LOCATE = (By.CLASS_NAME, "Svg-sc-ytk21e-0.bneLcE.search-icon.QbaKKdcHNA2x3_YJvpYu")
SEARCH_BOX_LOCATE = (By.CLASS_NAME, "encore-text.encore-text-body-small.NtkAQg9R1r5CjuP0XHwl")
IMG_PLAY_BUTTON = (By.CLASS_NAME, "Svg-sc-ytk21e-0.bneLcE.zOsKPnD_9x3KJqQCSmAq")
PAUSED_ICON_TEXT = ("Duraklat")
PLAY_ICON_TEXT = ("Çal")
PLAY_ICON_LOCATE = (By.CLASS_NAME, "vnCew8qzJq3cVGlYFXRI")
HOVER_BUTTON = (By.CLASS_NAME, "IjYxRc5luMiDPhKhZVUH.UpiE7J6vPrJIa59qxts4.ZgAJecvDDVREPXktThbA")
FOOTER_PLAY_BUTTON = (By.CLASS_NAME, "vnCew8qzJq3cVGlYFXRI")
SKIP_ICON_LOCATE = (By.CLASS_NAME, "mnipjT4SLDMgwiDCEnRC")
FOOTER_SONG_NAME_LOCATE = (By.CLASS_NAME, "deomraqfhIAoSB3SgXpu")
RAMMSTEIN_SONG_TEXT = ("Şu anda çalan: Rammstein tarafından Sonne")

##PLAYLIST##

CROSS_ICON_LOCATE = (By.CLASS_NAME, "IconWrapper__Wrapper-sc-16usrgb-0.hYdsxw")
CREATE_PLAYLIST_BUTTON = (By.CLASS_NAME, "Type__TypeElement-sc-goli3j-0.dsbIME.ellipsis-one-line.htqz7Vb8mLJvGKTi1vrs")
POP_UP_LOCATE = (By.CLASS_NAME, "Button-sc-1dqy6lx-0.hidZeW.yclq4HDmRA_euiUYwB9O")
PLAYLIST_TEXT_LOCATE = (By.CLASS_NAME, "encore-text.encore-text-body-small.lp9Tfm4rsM9_pfbIE0zd")
PLAYLIST_TEXT = "Çalma listesi"
SEARCH_BAR_LOCATE = (By.CLASS_NAME, "encore-text.encore-text-body-small.FeWwGSRANj36qpOBoxdx")
ADD_TEST_SONG1 = (By.XPATH, "//*[@id='main']/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/main/div[1]/section/div[2]/div[3]/div/div[1]/div/div[2]/div[4]/div/div[4]/button")
ADD_TEST_SONG2 = (By.XPATH, "//*[@id='main']/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/main/div[1]/section/div[2]/div[3]/div/div[1]/div/div[2]/div[5]/div/div[4]/button")
SONG_LOCATE = (By.CLASS_NAME, "IjYxRc5luMiDPhKhZVUH.UpiE7J6vPrJIa59qxts4")


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