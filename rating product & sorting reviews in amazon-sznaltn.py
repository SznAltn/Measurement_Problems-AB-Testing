
###################################################
# PROJE: Rating Product & Sorting Reviews in Amazon
###################################################

###################################################
# İş Problemi
###################################################

# E-ticaretteki en önemli problemlerden bir tanesi ürünlere satış sonrası verilen puanların doğru şekilde hesaplanmasıdır.
# Bu problemin çözümü e-ticaret sitesi için daha fazla müşteri memnuniyeti sağlamak, satıcılar için ürünün öne çıkması ve satın
# alanlar için sorunsuz bir alışveriş deneyimi demektir. Bir diğer problem ise ürünlere verilen yorumların doğru bir şekilde sıralanması
# olarak karşımıza çıkmaktadır. Yanıltıcı yorumların öne çıkması ürünün satışını doğrudan etkileyeceğinden dolayı hem maddi kayıp
# hem de müşteri kaybına neden olacaktır. Bu 2 temel problemin çözümünde e-ticaret sitesi ve satıcılar satışlarını arttırırken müşteriler
# ise satın alma yolculuğunu sorunsuz olarak tamamlayacaktır.

###################################################
# Veri Seti Hikayesi
###################################################

# Amazon ürün verilerini içeren bu veri seti ürün kategorileri ile çeşitli metadataları içermektedir.
# Elektronik kategorisindeki en fazla yorum alan ürünün kullanıcı puanları ve yorumları vardır.

# Değişkenler:
# reviewerID: Kullanıcı ID’si
# asin: Ürün ID’si
# reviewerName: Kullanıcı Adı
# helpful: Faydalı değerlendirme derecesi
# reviewText: Değerlendirme
# overall: Ürün rating’i
# summary: Değerlendirme özeti
# unixReviewTime: Değerlendirme zamanı
# reviewTime: Değerlendirme zamanı Raw
# day_diff: Değerlendirmeden itibaren geçen gün sayısı
# helpful_yes: Değerlendirmenin faydalı bulunma sayısı
# total_vote: Değerlendirmeye verilen oy sayısı



#########################################################################################################
# GÖREV 1: Average Rating'i Güncel Yorumlara Göre Hesaplayınız ve Var Olan Average Rating ile Kıyaslayınız.
#########################################################################################################

# Paylaşılan veri setinde kullanıcılar bir ürüne puanlar vermiş ve yorumlar yapmıştır.
# Bu görevde amacımız verilen puanları tarihe göre ağırlıklandırarak değerlendirmek.
# İlk ortalama puan ile elde edilecek tarihe göre ağırlıklı puanın karşılaştırılması gerekmektedir.

import pandas as pd
import math
import scipy.stats as st
from sklearn.preprocessing import MinMaxScaler

pd.set_option("display.max_columns", None) # tüm sütunları göster
pd.set_option("display.max_rows", None) # tüm satırları göster
pd.set_option("display.width", 500) # 500 e kadar göster
pd.set_option("display.expand_frame_repr", False) #
pd.set_option("display.float_format", lambda x: "%.5f" % x) # virgülden sonra 5 basamak göster



#######################################################################################################################
# Adım 1: Veri Setini Okutunuz ve Ürünün Ortalama Puanını Hesaplayınız.
#######################################################################################################################
df = pd.read_csv("Datasets/amazon_review.csv")
df.head()
df.shape # 4915 kişi puanlama yapmış
df.info() # detaylı bilgi, değişkenler tipleri

# rating dağılımı
df["overall"].value_counts() # hangi puandan kaç kişi vermiş

# Average
# ortalama puan
df["overall"].mean()

#######################################################################################################################
# Adım 2: Tarihe Göre Ağırlıklı Puan Ortalamasını Hesaplayınız.
#######################################################################################################################

# verilen veri setinde zaman belirten değişken object o yüzden dönüşüm yapmalıyız.
df["reviewTime"] = pd.to_datetime(df["reviewTime"])


df["reviewTime"].max() # en son yorum yapılan tarih


# veri seti eski o yüzden bir tarih belirliyoruz.
# bunu veri setindeki en son tarihe 2 gün ekleyerek yapıyoruz.
current_date = pd.to_datetime("2014-12-09 0:0:0")

# bugünün tarihinden yorumun yapıldığı tarihi çıkar ve gün cinsinden ifade et
df["day_diff"] = (df["reviewTime"].apply(lambda x: (current_date - x))).dt.days

# hanife nin yolu:
df["day_diff"] = (current_date - df["reviewTime"]).dt.days

#Çeyrekliklere bölerek rating hesaplama segmentler arasındaki puan farkını daha iyi gözlemlememizi sağlar

df["day_diff"].quantile([0.25, 0.5, 0.75])

# zamana göre ağırlıklı ortalama

df.loc[df["day_diff"] <= 282, "overall"].mean() * 28 / 100 + \
df.loc[(df["day_diff"] > 282) & (df["day_diff"] <= 432), "overall"].mean() * 26 / 100 + \
df.loc[(df["day_diff"] > 432) & (df["day_diff"] <= 602), "overall"].mean() * 24 / 100 + \
df.loc[(df["day_diff"] > 602), "overall"].mean() * 22 / 100


def time_based_weighted_average(dataframe, w1=28, w2=26, w3=24, w4=22):
    return dataframe.loc[df["day_diff"] <= 282, "overall"].mean() * w1 / 100 + \
           dataframe.loc[ (df["day_diff"] > 282) &  (df["day_diff"] <= 432), "overall"].mean() * w2 / 100 + \
           dataframe.loc[ (df["day_diff"] > 432) &  (df["day_diff"] <= 602), "overall"].mean() * w3 / 100 + \
           dataframe.loc[df["day_diff"] > 602, "overall"].mean() * w4 / 100
time_based_weighted_average(df)

#######################################################################################################################
# Görev 2: Ürün için Ürün Detay Sayfasında Görüntülenecek 20 Review'i Belirleyiniz.
#######################################################################################################################


###################################################
# Adım 1. helpful_no Değişkenini Üretiniz
###################################################

# Not:
# total_vote bir yoruma verilen toplam up-down sayısıdır.
# up, helpful demektir.
# veri setinde helpful_no değişkeni yoktur, var olan değişkenler üzerinden üretilmesi gerekmektedir.


df["total_vote"]
df["total_vote"].head(20)
df.head(20)

# bir yoruma gelen toplam up-down sayısı total_vote
# helpful_yes: Değerlendirmenin faydalı bulunma sayısı
# total_vote den helpful_yes çıkarılırsa helpful_no ya ulaşılır.

df["helpful_no"] = df["total_vote"] - df["helpful_yes"]
df.head(45)

##############################################################################################################
# Adım 2. score_pos_neg_diff, score_average_rating ve wilson_lower_bound Skorlarını Hesaplayıp Veriye Ekleyiniz
##############################################################################################################

def score_up_down_diff(up, down):
    return up - down

# score_pos_neg_diff
df["score_pos_neg_diff"] = df.apply(lambda x: score_up_down_diff(x["helpful_yes"], x["helpful_no"]), axis=1)

df.head(15)


def score_average_rating(up, down):
    if up + down == 0:
        return 0
    return up / (up + down)


# score_average_rating
df["score_average_rating"] = df.apply(lambda x: score_average_rating(x["helpful_yes"], x["helpful_no"]), axis=1)

df.head(15)

# Wilson Lower Bound Yöntemi

# Bu yöntem bize 2 li interaction lar barındıran herhangi bir item, product ya da review i
# skorlama imkanı sağlar
# like-dislike, helpful or not gibi.
# Bernaulli parametresi P için bir güven aralığı hesaplar.
# Bunun alt sınırını WLB score u olarak kabul eder.
# Bernaulli bir olasılık dağılımıdır.
# ikili olayların olasılık dağılımını hesaplamak için kullanılır.
# yazı turanın yazı gelme olasılığı gibi
# Bizim için buradaki bir olayın gerçekleşmesi olasılığı up olayıdır.



def wilson_lower_bound(up, down, confidence=0.95):
    """
        Wilson Lower Bound Score hesapla

        - Bernoulli parametresi p için hesaplanacak güven aralığının alt sınırı WLB skoru olarak kabul edilir.
        - Hesaplanacak skor ürün sıralaması için kullanılır.
        - Not:
        Eğer skorlar 1-5 arasıdaysa 1-3 negatif, 4-5 pozitif olarak işaretlenir ve bernoulli'ye uygun hale getirilebilir.
        Bu beraberinde bazı problemleri de getirir. Bu sebeple bayesian average rating yapmak gerekir.

        Parameters
        ----------
        up: int
            up count
        down: int
            down count
        confidence: float
            confidence

        Returns
        -------
        wilson score: float

        """
    n = up + down
    if n == 0:
        return 0
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    phat = 1.0 * up / n
    return (phat + z * z / (2 * n) - z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n )) / (1 + z * z / n)




# wilson_lower_bound
df["wilson_lower_bound"] = df.apply(lambda x: wilson_lower_bound(x["helpful_yes"], x["helpful_no"]), axis=1)


df.head(15)


############################################################################################################
# Adım 3. 20 Yorumu Belirleyiniz ve Sonuçları Yorumlayınız.
############################################################################################################
df.sort_values("wilson_lower_bound", ascending=False).head(20)

