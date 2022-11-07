# Machine-Learning
IBM firmasında çalışan veri bilimciler tarafından yaratılan çalışanların işten ayrılması ve performansları ile ilgili veri seti üzerinde makine öğrenmesi modelleri eğitilmiştir.

TOBB ETU'de almış olduğum makine öğrenmesi dersi ödevidir.

Odev ile ilgili yapılması gereken adımlar asagıda listelenmiştir:

1. ”IBM HR Analyics Attrition Dataset” isimli veri seti Kaggle sitesi uzerinden indirilir.
2. Deneylerin tekrarlanabilirligi icin SEED = 12345 olarak secilmelidir.  
3. Exploratory Data Analysis adımında veri analizi, gorsellestirmeleri gerceklestirilmelidir. 
4. Veri onisleme adımı ile gerekli normalizasyon, oznitelik donusumleri yapılmalıdır. 
5. Veri uygun sekilde egitim, validasyon, test kısımlarına ayrılmalı ve K=5 olacak ¸sekilde cross-validation uygulanmalıdır. 
6. Logistic Regression, SVM, Random Forest ile modeller egitilmeli ve sonuclar en az dort farklı metrik ile raporlanmalıdır. 
7. Egitilen modellerin overfit olup olmadıgı kontrol edilmelidir. 
8. Modeller arasında hem sınıflandırma ba¸sarımı hem de egitim ve test sureleri karsılastırılmalıdır. 
9. Parametre optimizasyonu ger¸cekle¸stirilmeli ve bu parametre optimizasyonun ba¸sarıma etkisi gosterilmelidir. 
10. En iyi 5 oznitelik istenilen yontem ile bulunmalı ve bu 5 oznitelik ile daha onceki adımda en iyi sonucu veren model tekrar egitilerek basarım, ve egitim/test sureleri karsılastırılmalıdır. 
11. Tüm deneyler boyunca elde edilen en iyi model ve verinin ön işleme adımları kaydedilmelidir. (.pickle olarak) 
12. ogrencino test.ipynb dosyası içerisinde kaydedilen veri ön işleme adımı ve eğitilen model ile örnek bir test işlemi gerçekleştirilmelidir. 
13. Bulgular bir sayfayı geçmeyecek şekilde dokümanda özetlenmelidir. 

data : https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset
