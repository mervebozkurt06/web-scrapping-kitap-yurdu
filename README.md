﻿# web-scrapping-kitap-yurdu

 kitapyurdu.com sitesinden kaynak kodu açılır. Ve html css kodları incelenir. Scraping işlemi için div class vb yapısı incelenerek yapılır. İhtiyaç duyulan ortamlar hazırlandıktan sonra import edilir. Bu projede Mongo veritabanına kayıt edileceği için önce bir db açılır. Collection olarakta kitapyurdu isimli collection oluşturulur. 
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) komutu ile chrome kullanılır. Sonrasında find_elements ile div lerin class isimleri kullanılarak verileri kazıma işlemi yapılır. books isimli json array oluşturularak title,publisher,writer ve price isimleri array'e kaydedilir.
 collection'a bağlantı yapılarak insert_many ile veritabanına array deki veriler kaydedilir. 

