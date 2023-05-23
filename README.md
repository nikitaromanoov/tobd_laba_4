# Лабораторная работа №1
## Цель работы
Получить навыки разработки CI/CD pipeline для ML моделей с достижением
метрик моделей и качества.

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



# Лабораторная работа №2
## Цель работы
Получить навыки выгрузки исходных данных и отправки результатов модели
с использованием различных источников данных согласно варианту задания.

## Ход работы

1. Создать репозитории-форк модели на GitHub, созданной в рамках
лабораторной работы №1, регулярно проводить commit + push в ветку
разработки, важна история коммитов.

https://github.com/nikitaromanoov/tobd_laba_2.git


2. Реализовать взаимодействие сервиса модели и базы данных, согласно
варианту задания.

По Варианту - Redis

3. Обеспечить процессы аутентификации/авторизации при обращении
сервиса модели к базе данных в момент отправки результата работы
модели. В исходном коде не должно быть явно прописаны пары
логин/пароль, адрес/порт сервера базы данных, токены доступа.

Пары логин/пароль, адрес/порт сервера базы данных, токены доступа прописаны в секретах гитхаба. 

Функция для обращения к базе данных в момент отправки рехультата работы:

```python

def redis_f(name, value):
        
        r = redis.Redis(host=os.environ.get("REDIS_ADDRESS"),
                        port=int(os.environ.get("REDIS_PORT")),
                        username=os.environ.get("REDIS_USER"),
                        password=os.environ.get("REDIS_PASSWORD"),
                        decode_responses=True)

        r.set(name, value)

        return r.get(name) 
```

4. Переиспользовать CI pipeline (Jenkins, Team City, Circle CI и др.) для
сборки docker image и отправки их на DockerHub.
5. Переиспользовать CD pipeline для запуска контейнеров и проведения
функционального тестирования по сценарию, запуск должен стартовать
по требованию или расписанию или как вызов с последнего этапа CI
pipeline.

<img width="649" alt="image" src="https://github.com/nikitaromanoov/tobd_laba_2/assets/91135334/239fcec6-8fd3-4c70-8c22-044318d7b670">

6.Результаты функционального тестирования и скрипты конфигурации
CI/CD pipeline приложить к отчёту. 

https://github.com/nikitaromanoov/tobd_laba_2/tree/master/.github/workflows

<img width="584" alt="image" src="https://github.com/nikitaromanoov/tobd_laba_2/assets/91135334/5137fb54-c20f-44e1-8066-2d69432f5299">


# Лабораторная работа №3
## Цель работы
Получить навыки размещения секретов в хранилище и взаимодействия с ним.

## Ход работы

1. Создать репозитории-форк модели на GitHub, созданной в рамках
лабораторной работы №2, регулярно проводить commit + push в ветку
разработки, важна история коммитов.

https://github.com/nikitaromanoov/tobd_laba_3.git


2. Настроить хранилище секретов согласно варианту - Ansible Vault.



3. Реализовать взаимодействие следующим образом:
* разместить данные для авторизации (секреты) в хранилище секретов;
* реализовать получение секретов при обращении к сервису БД;
* удалить локальные конфигурационные файлы, содержащие секреты.

```
def ansible():

    vault = Vault(os.environ.get("ANSIBLE"))
    data = vault.load(open("password.txt").read()).split(" ")
    
    REDIS_ADDRESS = data[2]
    REDIS_PORT = data[3]
    REDIS_USER = data[0]
    REDIS_PASSWORD = data[1]
    return REDIS_ADDRESS, REDIS_PORT, REDIS_USER, REDIS_PASSWORD        
        
        
        
def redis_f(name, value):
        REDIS_ADDRESS, REDIS_PORT, REDIS_USER, REDIS_PASSWORD = ansible()
        r = redis.Redis(host=REDIS_ADDRESS,
                        port=REDIS_PORT,
                        username=REDIS_USER,
                        password=REDIS_PASSWORD,
                        decode_responses=True)

        r.set(name, value)

        return r.get(name)     
```


4. Инициализация сервиса хранилища секретов должна проходить на этапе сборки контейнера.

```
RUN touch redis.credit && \
echo $REDIS_PASSWORD >> redis.credit && \
echo $REDIS_PORT >> redis.credit && \
echo $REDIS_ADDRESS >> redis.credit && \
echo $REDIS_USER >> redis.credit


RUN touch password.ansible && \
echo $ANSIBLE  >> password.ansible

RUN ansible-vault encrypt redis.credit --vault-password-file=password.ansible
```

5. Переиспользовать CI pipeline (Jenkins, Team City, Circle CI и др.) для
сборки docker image и отправки их на DockerHub.
6. Переиспользовать CD pipeline для запуска контейнеров и проведения
функционального тестирования по сценарию, запуск должен стартовать
по требованию или расписанию или как вызов с последнего этапа CI
pipeline.

6.Результаты функционального тестирования и скрипты конфигурации
CI/CD pipeline приложить к отчёту. 

https://github.com/nikitaromanoov/tobd_laba_3/tree/master/.github/workflows

<img width="413" alt="image" src="https://github.com/nikitaromanoov/tobd_laba_3/assets/91135334/97671796-8224-4c1a-87f8-851bdf725c64">



# Лабораторная работа №3
## Цель работы
Получить навыки реализации Kafka Producer и Consumer и их последующей интеграции.

## Ход работы

1. Создать репозитории-форк модели на GitHub, созданной в рамках
лабораторной работы №3, регулярно проводить commit + push в ветку
разработки, важна история коммитов.

https://github.com/nikitaromanoov/tobd_laba_4


2. Реализовать Kafka Producer либо на уровне сервиса модели, либо
отдельным сервисом в контейнере. Producer необходим для отправки
сообщения с результатом работы модели в Consumer.

```
from kafka import KafkaProducer


def  t_kafka(inp):
    producer = KafkaProducer(bootstrap_servers="kafka:9092", api_version=(0, 10, 2))
    producer.send("kafka-pred", bytearray(str(inp), "utf-8"))
    producer.close()
```


3. Реализовать Kafka Consumer либо на уровне сервиса модели, либо отдельным сервисом в контейнере. Consumer необходим для приёма сообщения с результатом работы модели.

```
   zookeeper:
       image: confluentinc/cp-zookeeper:7.3.2
       container_name: zookeeper
       environment:
           ZOOKEEPER_CLIENT_PORT: 2181        
   kafka:
       image: confluentinc/cp-kafka:7.3.2
       container_name: kafka
       ports:
           - "${LABA4_PORT}:${LABA4_PORT}"
       depends_on:
           - zookeeper
       environment:
           LABA4_HOST: ${LABA4_HOST}
           LABA4_PORT: ${LABA4_PORT}
           KAFKA_BROKER_ID: 1
           KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
           KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
           KAFKA_INTER_BROKER_LISTENER_NAME: INTERNAL
           KAFKA_LISTENERS: INTERNAL://:${LABA4_PORT}
           KAFKA_ADVERTISED_LISTENERS: INTERNAL://${LABA4_HOST}:${LABA4_PORT}
           KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: INTERNAL:PLAINTEXT
          
   kafka-topics-generator:
       image: confluentinc/cp-kafka:7.3.2
       container_name: kafka-topics-generator
       depends_on:
           - kafka
       command: >
           bash -c
             "sleep 5s &&
             kafka-topics --create --topic=kafka-predictions --if-not-exists --bootstrap-server=${LABA4_HOST}:${LABA4_PORT}"
   kafka-consumer:
       image: confluentinc/cp-kafka:7.3.2
       container_name: kafka-consumer
       command: >
           bash -c
             "kafka-console-consumer --bootstrap-server ${LABA4_HOST}:${LABA4_PORT} --topic kafka-pred --from-beginning"
```

4. Провести интеграцию Kafka сервиса с сервисом хранилища секретов. Необходимо сохранить защищённое обращение к сервису БД.

5. Переиспользовать CI pipeline (Jenkins, Team City, Circle CI и др.) для сборки docker image и отправки их на DockerHub.
6. Переиспользовать CD pipeline для запуска контейнеров и проведения функционального тестирования по сценарию, запуск должен стартовать по требованию или расписанию или как вызов с последнего этапа CI pipeline.
7. Результаты функционального тестирования и скрипты конфигурации
CI/CD pipeline приложить к отчёту.

https://github.com/nikitaromanoov/tobd_laba_3/tree/master/.github/workflows
