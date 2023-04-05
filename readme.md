### Programı çalıştırmak için `git clone github.com/KLU5200505054/algoritma-analizi-o2-s2.git` komutu ile klonladıktan sonra proje dizininde `python -m main.py` komutunu çalıştırın.

### Uygulamanın çalışması için python kurulu olmalıdır!


### Raita algoritması

Raita algoritması, sıralanmış bir dizide (örneğin, sayılar veya harfler gibi) aranan bir öğenin konumunu bulmak için kullanılan bir algoritmadır. Bu algoritma, ikili arama (binary search) algoritmasının bir varyasyonudur ve ikili aramaya göre bazı avantajlara sahiptir.

Raita algoritması, ikili arama algoritmasından farklı olarak, öğenin bulunduğu aralığı genişletmek yerine, aralığı daraltarak öğenin konumunu bulmaya çalışır. Algoritma, aranacak öğenin adım adım daraltılan bir aralama yoluyla bulunmasını sağlar.


Döngü ile ya da recursive olarak yazılabilir.

# Döngü varyasyonu :

Bu varyasyonda Raita algoritması, bir döngü kullanılarak gerçekleştirilir. Döngü, aranan öğe bulunana kadar devam eder ve aralık başlangıç ve bitiş indeksleri birbirine eşit olduğunda sonlanır. Raita algoritmasının temel adımları şöyle özetlenebilir:

1. Sıralanmış dizinin başlangıç ve bitiş indeksleri belirlenir.

2. Döngü başlatılır ve aralık başlangıç ve bitiş indeksleri birbirine eşit olmadığı sürece devam eder.

3. Aralığın orta noktasındaki öğe, aranan öğe ile karşılaştırılır.

4. Eğer orta noktadaki öğe, aranan öğeden büyükse, aralık başlangıçtan orta noktaya kadar daraltılır.

5. Eğer orta noktadaki öğe, aranan öğeden küçükse, aralık orta noktadan bitişe kadar daraltılır.

6. Aranan öğe bulunana kadar bu adımlar tekrarlanır.

7. Eğer aranan öğe bulunamazsa, döngü sonlanır ve öğe dizide yoktur.

# Recursive varyasyon :

Bu varyasyonda Raita algoritması, bir rekürsif işlev kullanılarak gerçekleştirilir. Rekürsif işlev, aranan öğe bulunana kadar kendini çağıran bir işlemdir ve aralık başlangıç ve bitiş indeksleri birbirine eşit olduğunda sonlanır. Raita algoritmasının temel adımları şöyle özetlenebilir:

1. Sıralanmış dizinin başlangıç ve bitiş indeksleri belirlenir.

2. Rekürsif işlev çağrılır ve aralık başlangıç ve bitiş indeksleri birbirine eşit olmadığı sürece devam eder.

3. Aralığın orta noktasındaki öğe, aranan öğe ile karşılaştırılır.

4. Eğer orta noktadaki öğe, aranan öğeden büyükse, aralık başlangıçtan orta noktaya kadar daraltılır ve aynı işlev tekrar çağrılır.

5. Eğer orta noktadaki öğe, aranan öğeden küçükse, aralık orta noktadan bitişe kadar daraltılır ve aynı işlev tekrar çağrılır.

6. Aranan öğe bulunana kadar bu adımlar tekrarlanır.

7. Eğer aranan öğe bulunamazsa, işlev sonlanır ve öğe dizide yoktur.


## Zaman Karmaşıklıkları : 

RAITA algoritmasının best, worst ve average durumlardaki zaman karmaşıklığı şu şekilde olabilir:

 - Best case: RAITA algoritmasının en iyi durumu, aranan desenin metinde çok az yerde olması durumudur. Bu durumda RAITA, metindeki tüm karakterleri en fazla bir kez kontrol eder. Yani, bu durumda zaman karmaşıklığı O(n)'dir.
 - Worst case: RAITA algoritmasının en kötü durumu, aranan desenin metindeki her pozisyonda olması durumudur. Bu durumda RAITA, metindeki her karakteri en fazla m kez kontrol eder. Dolayısıyla, bu durumda zaman karmaşıklığı O(nm)'dir.
 - Average case: RAITA algoritması için ortalama durum, desenin metindeki rastgele yerlerde bulunduğu durumdur. Bu durumda RAITA, genellikle O(n) ve O(nm) arasında bir zaman karmaşıklığına sahiptir.

Dikkat edilmesi gereken bir nokta, RAITA algoritmasının, boyutu sabit olan bir önyükleme işlemi gerektirdiğidir. Bu işlem, genellikle O(m+sigma) zaman karmaşıklığına ve O(sigma) alan karmaşıklığına sahiptir, burada m, desenin uzunluğudur ve sigma, karakter setinin boyutudur.

## Yazdığım kodun zaman karmaşıklığı

Sabit değişkenlerin tanımlanması:
 - Sabit zaman karmaşıklığı: O(1)
RAITA fonksiyonunun tanımlanması:
 - Sabit zaman karmaşıklığı: O(1)
Değişkenlerin tanımlanması:
 - Sabit zaman karmaşıklığı: O(1)
Dosyanın açılması:
 - Sabit zaman karmaşıklığı: O(1)
Dosyanın okunması ve kelimelerin alınması:
 - Kelimelerin sayısı n kadar olduğundan, okumanın zaman karmaşıklığı: O(n)
Kelimelerin kontrol edilmesi ve sayım yapılması:
 - RAITA fonksiyonu içerisinde bir döngü kullanılmıştır. Bu döngü n kadar tekrar edilebilir.
 - if blokları sabit zaman karmaşıklığına sahiptir. Bu nedenle, RAITA fonksiyonunun zaman karmaşıklığına bağlı olarak, bu bloğun zaman karmaşıklığı değişebilir.
Her bir kelime için 4 kez if blokları çalışacağından, bu blokların zaman karmaşıklığı toplamı: O(4n x f(n)), burada f(n) RAITA fonksiyonunun zaman karmaşıklığıdır.
Dosyanın kapatılması:
 - Sabit zaman karmaşıklığı: O(1)

Raita algoritmasının zmana karmaşıklığı da O(n) olduğuna göre, toplam zaman karmaşıklığı O(4n * O(n)) = O(n^2) olacaktır.

