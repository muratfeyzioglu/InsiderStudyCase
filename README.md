# InsiderStudyCase
 Selenium(Python)/ API(Python)/ JMeter

 **Selenium Project**: InsiderSelenium projesi altındadır.
 Test case Tests/test_demo.py içindedir.
 conftest.py kullanılmıştır. Driver, terminal parameteri(tarayacı seçimi için) ve ekran görüntüsü alma işlemleri bu sınıfın içinde tanımlanmıştır.
 Pytest kullanılmıştır. 
 Test sınıfını run etmek için IDE içinde bulunan run butonlarını kullanmak yerine terminal üzerinden verilecek komutla çalıştırmanız, browser parametresi göndermenize yarayacaktır.

 Örnek terminal komutu : 
 pytest -v -s Tests/test_demo.py --browser firefox
 pytest -v -s Tests/test_demo.py --browser chrome
 pytest -v -s Tests/test_demo.py (_default olarak chrome açılır_)

 **API Project**: InsiderAPI projesi altındadır.
 Positif test case Tests/test_positive.py içindedir.
 Negatif test case Test/test_negative.py içindedir.

  **JMeter Project**: InsiderJmeter projesi altındadır.


 



