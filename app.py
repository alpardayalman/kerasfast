import streamlit as st
from PIL import Image
from tensorflow.keras import models
import os
import numpy as np

model = models.load_model("baseline.keras")
accepted = False

class Recognition:

    def __init__(self, class_names, model=model):
        self.model = model
        self.class_names = class_names
        self.accepted = False

    def format_image(self):
         self.image = self.image.convert("RGB")
         self.image = self.image.resize((32, 32))

    def predict_image(self, image):
            self.format_image()
            data = np.asarray(self.image) # image normalization
            data = data / 255
        
            probs = self.model.predict(np.array([data])[:1])
            print(probs)
            best_prob = probs.max()
            best_pred = np.argmax(probs)
            st.markdown('<style> .big-text { font-size: 24px; color: #FFD700; text-shadow: 2px 2px 4px #000000;}</style><p class="big-text">'+ self.class_names[best_pred] +"</p>", unsafe_allow_html=True)

            st.progress(round(best_prob*100))
            st.write(f"{best_prob*100:0.2f}")

    def run(self):
        st.title("Detektif v0.1")
        st.write("Klasifikasyon Uygulamasi")
        self.show_acceptance_popup()
        st.write('Ucak, Otomobil, Kuş, Kedi, Geyik, Köpek, Kurbağa, At, Gemi ve Kamyon resmi kullanınız :)')
        uploaded_file = st.file_uploader("Bir resim secin...", type=["jpg", "jpeg", "png"])

        if accepted:
            accepted = True
            if uploaded_file is not None:
                self.image = Image.open(uploaded_file)
                st.image(self.image, caption="Uploaded Image", use_column_width=True)
                self.predict_image(image=self.image)
        else:
            st.error("Klasifikasyon Uygulamasini kullanmak icin lutfen kvkk metinini onaylayiniz.")
            
    def show_acceptance_popup(self):
        with st.expander("Terms and Conditions"):
            st.write("""
            KİŞİSEL VERİLERİN İŞLENMESİ AYDINLATMA METNİ
             
            1.    Veri Sorumlusunun Kimliği
             
            6698 sayılı Kişisel Verilerin Korunması Kanununun (KVK Kanunu) 10 uncu maddesi ile Aydınlatma Yükümlülüğünün Yerine Getirilmesinde Uyulacak Usul ve Esaslar Hakkında Tebliğ kapsamında İçişleri Bakanlığı tarafından hazırlanmıştır.
             
            2.    Kişisel Verilerinizin İşlenme Amaçları
            
            İçişleri Bakanlığı Nüfus ve Vatandaşlık İşleri Genel Müdürlüğü (NVİGM) aşağıda yer alan;
            Mevzuatlar tarafından öngörülen esas ve usuller doğrultusunda veya zorunlu kıldığı şekilde, hukuki yükümlülüklerin yerine getirilmesi,
            Kurum faaliyetlerin yürütülmesi,
            NVİGM’nin Kimlik Paylaşımı Sistemi uygulaması kapsamında yaptığı Veri Paylaşımı Taahhütnameleri kapsamında ve alıcı gurubuna karşı hizmet standartları çerçevesinde hizmet sağlanması ve Taahhütname gerekliliklerinin yerine getirilmesi,
            Amaçları kapsamında kişisel verilerinizi işlemektedir.
             
            3.    Kişisel Verilerinizin Üçüncü Kişilerle Paylaşılması ve Hangi Amaçla Aktarıldığı
            
            Kişisel verileriniz 5490 sayılı Nüfus Hizmetleri Kanunun 45 inci maddesinin 1 inci fıkrası kapsamında belirtilen kamu kurum, kuruluş ve kamu hizmeti sunan diğer tüzel kişilikler ile Veri Paylaşımı Taahhütnamesi imzalanarak paylaşılmaktadır. Paylaşım yapılan alıcı kurum listesi Genel Müdürlüğümüzün https://kpsbasvuru.nvi.gov.tr/Acik/KpsNedir web adresinde yer almaktadır. 
            
            Veri aktarımı, 6698 sayılı Kişisel Verilerin Korunması Kanununun Kişisel verilerin aktarılması başlıklı 8. Maddesinin 2. Fıkrasının “a” bendindeki; “5 inci maddenin ikinci fıkrasında, (5. Maddenin 2. Fıkrası: Kanunlarda açıkça öngörülmesi.) belirtilen şartlardan birinin bulunması hâlinde, ilgili kişinin açık rızası aranmaksızın aktarılabilir.” hükmü kapsamında Kimlik Paylaşımı Sistemi ile yapılmaktadır.
            
            Veri paylaşımı yapılan kurumlar ve yetkileri, 5490 sayılı Nüfus Hizmetleri Kanunun 2. Fıkrası: “Veri paylaşımından yararlanacakları belirlemeye, paylaşımın kapsamına ve hangi yöntemle yapılacağına karar vermek üzere Genel Müdürlük bünyesinde Veri Paylaşımı Kurulu oluşturulur. Veri Paylaşımı Kurulunun çalışma usul ve esasları Bakanlıkça çıkarılan yönetmelikle belirlenir.” Hükmü kapsamında oluşturulmuş olan Veri Paylaşımı Kurulunca belirlenmektedir.
             
            4.    Kişisel Verilerinizin Toplanma Yöntemi ve Hukuki Sebebi
            
            NVİGM 5490 sayılı Nüfus Hizmetleri Kanunun Aile kütüklerinde bulunması gereken kişisel bilgiler başlıklı 7. Maddesinde belirtilen veriler ile Cumhurbaşkanlığı Teşkilatı Hakkındaki 1 sayılı Cumhurbaşkanlığı Kararnamesinin 258 inci maddesinde belirtilen iş ve işlemleri yürütmek üzere veri kayıt sistemleri ile işlemektedir.
            5490 sayılı Kanunun ilgili hükmü:
            
            Aile kütüklerinde bulunması gereken kişisel bilgiler
            MADDE 7- (1) Her mahalle veya köy için ayrı aile kütüğü tutulur. Aile kütüklerinde aşağıdaki bilgiler bulunur:
            a) Türkiye Cumhuriyeti kimlik numarası.
            b) Kayıtlı bulunduğu il, ilçe, köy veya mahalle adı ile cilt, aile ve birey sıra numarası.
            c) Kişinin adı ve soyadı, cinsiyeti, baba ve ana adı ile soyadları, evli kadınların önceki soyadları.
            ç) Doğum yeri ile gün, ay ve yıl olarak doğum tarihi ve kütüğe kayıt tarihi.
            d) Evlenme, boşanma, soybağının kurulması veya reddi, ölüm, vatandaşlığın kazanılması veya kaybedilmesi gibi kişisel durumda meydana gelen değişiklik veya yetkili makamlarca yapılan düzeltmeler.
            e) Dini.
            f) Medenî hali.
            g) Yerleşim yeri adresi.
            ğ) Fotoğrafı.
            h) Biyometrik verisi.
            ı) Velayete ve vesayete ilişkin bilgileri. (a), (g), (ğ), (h) ve (ı) bentlerinde belirtilen kayıtlar sadece elektronik ortamda tutulur.
            1 sayılı Cumhurbaşkanlığı Kararnamesinin ilgili hükmü;
            Nüfus ve Vatandaşlık İşleri Genel Müdürlüğü 
            MADDE 258 –(1) Nüfus ve Vatandaşlık İşleri Genel Müdürlüğünün görev ve yetkileri şunlardır: 
            
            a) Ülke nüfusunun yapısı, nitelikleri, nüfus hareketleri ve bunlardaki gelişmelere göre takip edilecek politikaların tespitine dair çalışmaları ilgili kuruluşlarla işbirliği içinde yapmak, belirlenecek esasların yürütülmesini sağlamak, 
            
            b) Nüfus hareketlerini takip etmek ve değerlendirmek, merkezde bir nüfus bilgi bankası kurmak, aile ve hayat istatistiklerine ait verileri toplamak, ilgili kuruluşlarla işbirliği içerisinde yayınlamak, 
            
            c) Nüfus hizmetlerini düzenlemek, yürütmek, takip etmek, denetlemek ve değerlendirmek, usulüne göre tesis edilmemiş kayıtların silinmesini karara bağlamak, maddi hataları düzeltmek, aile kayıtlarını birleştirmek, mükerrer kayıtları birbirine göre tamamlamak ve diğerlerini silmek, nüfus hizmetleri ile ilgili olarak diğer bakanlık, kurum ve kuruluşlar arasında koordinasyon sağlamak,
             
            ç) Vatandaşlığın kazanılması, kaybı ve göçmen olarak kabule dair işlemleri yürütmek ve vatandaşlıkla ilgili kanunları uygulamak, vatandaşlık anlaşmazlıklarını karara bağlamak ve vatandaşlık incelemelerini yapmak,
            
            d) Nüfus cüzdanlarının yürürlük, değiştirme ve geçerlilik tarihlerini belirlemek ve nüfus cüzdanlarının üretiminde uygulanacak sistem ve teknolojiyi tespit etmek, 
            
            e) Pasaport, pasaport yerine geçen belgeler ve sürücü belgelerinde yer alacak bilgiler ile biyometrik verinin türü, niteliği ve alınma yaşını tespit etmek, bu belgelerin tasarımı, temini, basımı, dağıtımı, teslimi ile üretim ve kişiselleştirilmesine ilişkin işlemleri yürütmek ve bunlara dair usul ve esasları belirlemek,
            
            f) Bakan tarafından verilen diğer görevleri yapmak.
             
            5.    Kişisel Veri Sahibinin 6698 sayılı Kanunun 11 inci Maddesinde Sayılan Hakları
             
            6698 sayılı Kanunu’nun 11 inci maddesinde düzenlenen haklarını, bu Kanunu’nun 13 üncü maddesi ve Veri Sorumlusuna Başvuru Usul ve Esasları Hakkında Tebliğ hükümleri çerçevesinde yazılı başvuruları İçişleri Bakanlığının Meşrutiyet Caddesi Karanfil 2 Sokak No: 67 Kızılay/ANKARA adresine, Kayıtlı Elektronik Posta (KEP) ile yapılacak başvurular ise "icisleribakanligi@hs01.kep.tr" (e-posta: kvkk@icisleri.gov.tr ) adresine iletilmelidir.
             
            İşbu Aydınlatma Metni KVKK ve ilgili mevzuat uyarınca veri sahiplerini bilgilendirmek ve aydınlatmak amacı ile hazırlanmıştır.
            """)
            if st.button("I Accept"):
                st.success("You have accepted the terms and conditions! You may now use the application")
                accepted = True


def main():
    class_names = {
    0: 'Ucak',
    1: 'Otomobil',
    2: 'Kuş',
    3: 'Kedi',
    4: 'Geyik',
    5: 'Köpek',
    6: 'Kurbağa',
    7: 'At',
    8: 'Gemi',
    9: 'Kamyon',
    }

    Recognition(class_names=class_names, model=model).run()


if __name__ == "__main__":
    main()
