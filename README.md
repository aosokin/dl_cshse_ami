# Материалы курса "Глубинное обучение", прочитанного на [ФКН ВШЭ](https://cs.hse.ru/) весной 2018г.

## Преподаватели
Лектор: [Антон Осокин ](https://aosokin.github.io/)

Семинаристы: Артем Бабенко, [Алексей Умнов](https://www.hse.ru/org/persons/141880775), Алексей Озерин

## Программа курса
* Введение ([лекция 1](lectures/DL18_lecture1_intro.pdf), [семинар 1](seminars/DL18_seminar1_intro/DL18_seminar1.ipynb))
* Основные концепции
  - Механика нейросетей и backprop ([лекция 2](lectures/DL18_lecture2_backprop.pdf), [семинар 2](seminars/DL18_seminar2_pytorch/DL18_seminar2.ipynb))
  - Виды архитектур ([лекция 3](lectures/DL18_lecture3_models.pdf), [семинар 3](seminars/DL18_seminar3_models/DL18_seminar3.ipynb))
  - Обучение и регуляризация ([лекция 4](lectures/DL18_lecture4_training.pdf), [семинар 4](seminars/DL18_seminar4_training/DL18_seminar4.ipynb))
* Продвинутые темы
  - Применения в компьютерном зрении ([лекция 5](lectures/DL18_lecture5_deepvision.pdf), [семинар 5](seminars/DL18_seminar5_deepvision/DL18_seminar5.ipynb))
  - Применения для обработки языка ([лекция 6](lectures/DL18_lecture6_deepnlp.pdf), [семинар 6](seminars/DL18_seminar6_deepnlp/DL18_seminar6.ipynb))
  - Adversarial X ([лекция 7](lectures/DL18_lecture7_adversarialX.pdf), [семинар 7](seminars/DL18_seminar7_adversarialX/DL18_seminar7.ipynb))
  - Вероятностные модели ([лекция 8](lectures/DL18_lecture8_probmodels.pdf), [семинар 8](seminars/DL18_seminar8_probmodels/DL18_seminar8.ipynb))
  - Дифференцируемое программирование ([лекция 9](lectures/DL18_lecture9_differentiableprogramming.pdf), [семинар 9](seminars/DL18_seminar9_differentiableprogramming/DL18_seminar9.ipynb))
  - Недифференцируемые модели ([лекция 10](lectures/DL18_lecture10_nondiffnets.pdf))
* Приглашенный доклад: Борис Янгель о нейросетях в диалоговых системах ([лекция 11](lectures/DL18_invitedTalk_dialogSystems.pdf))

## Disclaimer
Курс "Глубинное обучение" разрабатывался не как онлайн-курс, а как классический университетский курс с лекциями и семинарами.
Видео-запись осуществлялась только для внутреннего использования (Кристина, спасибо большое!).

Тем не менее, мы решили выложить все материалы в открытый доступ под [MIT лицензией](LICENSE) на случай если они кому-то будут полезны.
Единственная просьба, **пожалуйста, не выкладывайте решения семинаров в открытый доступ!** 
  
## Материалы
Все материалы курса на **русском** языке!

Выложены следующие материалы:
* [Презентации лекций](lectures)
* [Jupyter ноутбуки семинаров](seminars) 
* [Видеозаписи лекций](https://www.youtube.com/playlist?list=PLzY5g-rVmFayEkCcgO3_-it6HZwPZL3ld)

**Пожалуйста, не выкладывайте решения семинаров в открытый доступ!** Мы хотим переиспользовать материалы на следующих итерациях курса.

**Минутка рекламы:** на [ФКН](https://cs.hse.ru/) мы каждый год набираем студентов-магистров-аспирантов — приходите к нам учиться! Очно мы всегда стараемся дать больше, чем просто контент :-) 
 
## Технический требования семинаров
Все семинары разрабатывались для выполнения на обычных ноутбуках, т.е., не требуют значительных вычислительных ресурсов (в частности не требуют GPU). Тем не менее требования к железу ненулевые, и на некоторых компьютерах все работает очень медленно. Бесплатные вычислительные ресурсы (в том числе с GPU) можно получить, например, на сайте https://colab.research.google.com.

В рамках курса мы использовали python 3.6, [pytorch v0.3.0](https://github.com/pytorch/pytorch/releases/tag/v0.3.0), [torchvision v0.2.0](https://github.com/pytorch/vision/releases/tag/v0.2.0). Поддержка других библиотек и других версий python и pytorch не осуществлялась.
 
Для настройки библиотек мы рекомендуем использовать менеджер пакетов [Anaconda](https://www.anaconda.com/) (есть для Linux, OS X, Windows). Для установки в Linux и OS X смотрите инструкции на сайте http://pytorch.org/. 
Для установки в Windows на момент курса работали команды `conda install -c peterjc123 pytorch` и `pip install torchvision`.
 
Также можно использовать Docker (https://hub.docker.com/r/alexeyum/hse_deep_learning/), в котором всё установлено.
