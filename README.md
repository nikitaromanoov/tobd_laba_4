# Лабораторная работа №2
## Цель работы
Получить навiki

## Ход работы

1. Создать репозитории модели на GitHub, регулярно проводить commit +
push в ветку разработки, важна история коммитов. 

2. Провести подготовку данных для набора данных, согласно варианту
задания. Данные уже представлены в виде, готовом для обучения/валидации, поэтому нужно их было разбить только на обучающую, валидационную и тестовую выборку.
3. Разработать ML модель с алгоритмом классификации деревьев. 

Пункт 2 и 3: https://github.com/nikitaromanoov/tobd_laba_1/blob/master/notebooks/experiments.ipynb


4. Конвертировать модель из *.ipynb в .py скрипты - https://github.com/nikitaromanoov/tobd_laba_1/tree/master/src
5. Покрыть код тестами, используя любой фреймворк/библиотеку - https://github.com/nikitaromanoov/tobd_laba_1/tree/master/src/unit_tests
6. Задействовать DVC 

* https://github.com/olegggatttor/ml-pipeline/blob/master/data.dvc
* https://github.com/olegggatttor/ml-pipeline/tree/master/.dvc
7. Использовать Docker для создания docker image.
8. Наполнить дистрибутив конфигурационными файлами:
• config.ini: гиперпараметры модели;
• Dockerfile и docker-compose.yml: конфигурация создания контейнера и образа модели;
• requirements.txt: используемые зависимости (библиотеки) и их версии;

<img width="608" alt="image" src="https://github.com/nikitaromanoov/tobd_laba_1/assets/91135334/97d4b226-f478-4aed-9363-2445f07f2976">

9. Создать CI pipeline (Jenkins, Team City, Circle CI и др.) для сборки docker image и отправки его на DockerHub, сборка должна автоматически
стартовать по pull request в основную ветку репозитория модели;
10. Создать CD pipeline для запуска контейнера и проведения функционального тестирования по сценарию, запуск должен стартовать по требованию или расписанию или как вызов с последнего этапа CI pipeline.

https://github.com/nikitaromanoov/tobd_laba_1/tree/master/.github/workflows

<img width="648" alt="image" src="https://github.com/nikitaromanoov/tobd_laba_1/assets/91135334/d90dcbb6-5b27-4314-94de-296ba4635f7d">



### GitHub
https://github.com/nikitaromanoov/tobd_laba_1
### Docker image
https://hub.docker.com/r/nikitaromanoov/tobd_laba_1
