# Measurement_Problems-AB-Testing
Measurement Problems/ AB Testing / ANOVA
# Measurement Problems (Ölçüm Problemleri)

**Social Proof (Sosyal İspat):** Bir kullanıcının satın almasını en fazla etkileyen sebeptir. Topluluğun kanaati de denebilir.

**The Wisdom of Crowds:** Kalabalığın bileliğidir, sürü psikiolojisi de denebilir. Herhangi bir olayda çoğunluğun yönelimini doğu bulma da denebilir.

- **Rating Products**
- **Sorting Products**
- **Sorting Reviews**
- **AB Testing**
- **Dynamic Pricing**

# Rating Products (Ürün Puanlama)

Olası faktörleri göz önünde bulundurarak ağırlıklı ürün puanlama.

Ürün puanlama yaparken kullanabileceğimiz değerlendirme çeşitleri:

- **Average (Ortalama)**

Bu kısımda bir ürüne verilen puanların genel ortalaması alınır. Örneğin 1 yıldız dan 5 yıldıza kadar derecelendirilen bir ürünün verilen yıldız sayısına göre ortalamasını bulmuş oluruz. Bu yöntem matematiksel olarak doğru olsa da potansiyeli olan ürünleri kaçırmamıza sebep olabilir. Bu sebeple diğer yönteme bakalım…

- **Time-Based Weighted Average (Puan Zamanlarına Göre Ağırlıklı Ortalama)**

Son zamanlardaki trendin ne olduğunu tespit etmek için kullanılır. 

- **User-Based Weighted Average (Kullanıcı temelli ağırlıklı ortalama)**
- **Weighted Rating (Ağırlıklı Derecelendirme)**

# Sorting Products (Ürün Sıralama)

- Sorting by Rating (Derecelendirmeye Göre Sıralama)
- Sorting by Comment Count or Purchase Count (Yorum ve satın alma sayısına göre sıralama)
- Sorting by Rating, Comment and Purchase (Derecelendirme, Satın alma ve yoruma göre sıralama)
- Bayesian Average Rating Score (Bayes ortalama derecelendirme puanı)
- Hybrid Sorting: BAR Score + Diğer Faktorler (Karma Sıralama)

### **Yorum:**

- bar_score bize veri seti içerisinde yeni olsa da potansiyel vaad edenleri de yukarıya taşır ve görmemizi sağlar.
- bar_score yöntemi hibrit bir sıralamada ağırlığı olan bir faktördür.
- bar_score potansiyeli yüksek ama henüz yeterli social_proof u alamamış ürünleri de yukarı çıkarır.
- İş bilgisi açısından önemli olabilecek faktörler bir şekilde göz önünde bulunudrulmalı.
- Birden fazla faktör varsa bu faktörlerin etkileri aynı anda göz önünde bulundurulmak üzere önce standartlaştırılmalı daha sonra eğer etkilerin farkı varsa bu ağırlık ile ifade edilmeli.
- Literatüre bakıldığında istatistiksel bazı yöntemleri de bulsak bunlar oldukça güvenilir dahi olsa bu yöntemleri tek başına kullanmak yerine yine iş bilgisi ile bir şekilde harmanlanacak şekilde bu bilgileri birlikte kullanmalıyız.

# Sorting Reviews

## Wilson Lower Bound Score (Wilson Alt Sınır Puanı)

Elimizdeki örnekleme ilişkin up-rate oranının istatistiksel olarak % 95 güven ve % 5 hata payı ile artık hangi aralıkta olabileceğini biliyoruz ve o aralığı atladık, o aralığın alt sınırına geldik. En alt noktadan , en kötü senaryodan bir referans noktasına tutunarak hesaplanan skordur.

- Bu yöntem bize 2 li interaction lar barındıran herhangi bir item, product ya da review i skorlama imkanı sağlar. like-dislike, helpful or not gibi.
- Bernaulli parametresi P için bir güven aralığı hesaplar. Bunun alt sınırını WLB score u olarak kabul eder.
- Bernaulli bir olasılık dağılımıdır.
- İkili olayların olasılık dağılımını hesaplamak için kullanılır.  Yazı turanın yazı gelme olasılığı gibi. Bizim için buradaki bir olayın gerçekleşmesi olasılığı up olayıdır.

# A/B TESTING

A bir özelliği ya da grubu temsil ederken B de farklı bir özelliği ya da grubu temsil etsin. Bu ikisi arasında farklılık olup olmadığını araştırırız.

## Temel İstatistik Kavramları

“Without a grounding in Statistic, a Data Scientist is a Data Lab Asistant.”

“The future of AI will be about less Data, not more.”

### Sampling(Örnekleme)

Sampling: Bir ana kitle içerisinden bu ana kitlenin özelliklerini iyi taşıdığı varsayılan, özelliklerini iyi temsil ettiği varsayılan bir alt kümedir. Bir populasyonun temsilcisidir.

**Neden örneklem ile çalışıyoruz?**

Diyelimki 10000 kişilik bir ilçede yaşayan insanların yaş ortalamasını bulmaya çalışıyoruz. Örnek teorisi der ki, 10000 kişiyi iyi temsil eden  bir alt küme seç rastgele ve yansız olsun. Bu durumda 10000 kişiyi gezmeden bir genelleme yapma şansı bulmuş oluruz. Örneklem bize zaman, para, işgücü gibi durumlarda kolaylık sağlar.

**Dikkat!**

Örneklem sayısı arttığında bu örneklem dağılımına ilişkin ortalama da populasyana (ana kitlenin ortalamasına) yakınlaşacaktır.

### Betimsel İstatistikler

**Medyan:** (ortanca) bir veri seti küçükten büyüğe sıralanınca ortadaki değerdir. Medyan non-parametriktir.

**Mean:** ortalama değerdir, parametriktir.

**Not:** Bir veri setinin değişkenlerinde  aykırı değer olup olmadığını tespit etmek için medyan ve ortalamaya bakılır. Medyan ile ortalama birbirine çok yakın ise aykırı değer yoktur ve ortalamaya da bakılsa medyana da bakılsa sonuçlar birbirine çok yakın olur. Ama medyan ve ortalama birbirinden uzak ise aykırı değer vardır ve medyana bakılmalıdır.

### Güven Aralıkları(Confidence Intervals)

Ana kütle parametresinin tahmini değeri (istatistik) kapsayabilecek iki sayıdan oluşan bir aralık bulunmasıdır.

Güven aralığına karar vermek gerekir %95 mi % 99 mu? Genellikle %95 güven aralığı kullanılır.

Güven aralığı der ki olası alınabilecek 100 örneklemden 95 inin ortalaması hesapladığın güven aralıktadır.

### Correlation(Korelasyon)

Korelasyon: Değişkenler arasındaki ilişki, bu ilişkinin yönü ve şiddeti ile ilgili bilgiler sağlayan istatistiksel bir yöntemdir.

- -1 ile + 1 arasında değerler alır.
- Sıfır korelasyon ilişki yoktur demektir.
- +1 e yaklaştıkça pozitif mükemmel korelasyon, -1 e yaklaştıkça negatif mükemmel korelasyona ulaşılır.
- 0.5 ile 1 arasındaki ya da -0.5 ile 0 arasındaki değerlerde düşük korelasyon var demektir. Değişkenler beraber hareket etmez deriz.
- Pozitif korelasyon, bir değişkenin değerleri artarken diğer değişkenin de değerleri artıyor demektir, doğru orantılıdır.
- Negatif korelasyon, bir değişkenin değerleri azalırken diğer değişkenin de değerleri azalıyor demektir, ters orantılıdır.

### Hipotez Testleri (Hypothesis Testing)

**Hipotez:** Bir inanışı bir savı test etmek için kullanılan istatistiksel yöntemlerdir.

**Hipotez Testleri:(AB Testleri)** Grup karşılaştırmalarında temel amaç olası farklılıkların şans eseri ortaya çıkıp çıkmadığını göstermeye çalışmaktır.

### AB Testi (Bağımsız İki Örneklem T Testi)

AB testi dendiğinde çok yaygın olarak ya iki grubun ortalaması kıyaslanıyordur ya da iki gruba ilişkin oranlar kıyaslanıyordur.

**Bağımsız İki Örneklem T Testi:** İki grup ortalaması arasında karşılaştırma yapılmak istendiğinde kullanılır.

AB testlerinde ifade edilen A ve B kontrol ve deney grubunu temsil ederler.

**İki grup ortalamasını kıyaslama:**

H_0 = yokluk hipotezi

H_1 = varlık hipotezi

Hipotezler 3 farklı şekilde kurulabilir:

**1.Durum:** 

H_0 = ortalamalar eşit

H_1 = ortalamalar eşit değil

**2.Durum:**

H_0 = 1.ortalama , 2. ortalamaya eşit ya da küçüktür.

H_1 = 1. ortalama 2.ortalamadan büyüktür.

**3.Durum:**

H_0 = 1.ortalama , 2. ortalamaya eşit ya da büyüktür.

H_1 = 1. ortalama 2.ortalamadan küçüktür.

p-value değerine bakarak hiptezlerin sonucunu yorumlayacağız.

p-value değeri 0.05ten küçük ise H_0 red olacak.

**Bu yöntemlerin 2 varsayımı vardır:**

1. Normallik (İki grup da ayrı ayrı normal dağılmalı varsayımı)

  2. Varyans Homojenliği (İki grubun dağılımlarının birbirine benzer olup olmaması)

**Bu yöntemde izleyeceğimiz yol:**

1. Hipotezleri Kur
2. Varsayım Kontrolü
- Normallik Varsayımı (Shapiro testi kullanılır.)
- Varyans Homojenliği (Levene testi kullanılır.)

  3. Hipotezin Uygulanması

- Varsayımlar sağlanıyorsa bağımsız iki örneklem t testi (parametrik test)
- Varsayımlar sağlanmıyorsa mannwhitneyu testi (non-parametrik test)

 4. p-value değerine göre sonuçları yorumla 

**Not:** 

- Normallik sağlanmıyorsa direk 2 numara olan mannwhitneyu testine  (non-parametrik test) gidilir.
- Varyans homojenliği sağlanmıyorsa 1 numaraya arguman girilir. Bağımsız iki örneklem t testi (parametrik test)
- Normallik incelemesi öncesi aykırı değer incelemesi ve düzeltmesi yapmak faydalı olabilir.
- Ortalama kıyasının konuşulduğu durum parametrik durumdur.
- Non-parametrik durumlarda medyanların kıyaslanır. (Sıralama kıyaslanması da denir.)

**hipotez sonucunda;**

th > tt sonucu çıkarsa H_0 reddedilir.

Diğer durumlarda reddedilemez.

th: t hesaplanan t

tt: t nin tablo değeri

**shapiro testi:** bir değişkenin dağılımının normal olup olmadığını test eder.

**levene testi:** varyans homojenliği testini gerçekleştirmek için kullanılır.

**ttest metodu:** yalnızca normalliğin sağlandığı durumlarda kullanılır. varyans homojenliği kısmı ile ilgilenmez. Yalnızca varyans homojenliği sağlanmıyorsa equal_var=False girilmesi gerekir.

**mannwhitneyu testi:** non parametrik, ortalama kıyaslama, medyan kıyaslama testidir.

### İkiden Fazla Grup Karşılaştırma (ANOVA : A**nalysis of Variance**)

İkiden fazla grup olduğunda grupların ortalamarı arasında fark var mı yok mu sorusuna cevap aranır.

**1.Hipotez:**

- **H_0: m1 = m2 = m3 = m4 (ortalamalar eşit)**
    
    Grup ortalamaları arasında fark yoktur.
    
- **H1: .. fark vardır. (En az birisi farklıdır.)**

 **2. Varsayım kontrolü** 

- Normallik varsayımı
- Varyans homojenliği varsayımı

Varsayım sağlanıyorsa  tek yönlü one way anova testi, parametrik test

Varsayım sağlanmıyorsa ikiden fazla grup ortalaması kıyaslama testi,  non-parametrik kruskal testi kullanılır. 

 İkili karşılaştırmanın farklılığının hangi gruptan kaynaklandığını bulmak için, statsmodels içindeki çoklu karşılaştırma tukey testi ni kullanırız.

Keyifli Okumalar…

Suzan Altun Özkale
