# MotionPath Converter To Curve Blender Addon
Addon для более удобной работы с путями в blender с помощью Curve

Этот конвертер поможет вам решить такие проблемы, как красивый рендер пути, визуализация пути на рендере, привязка другив объектов к путям.

## Содержание

1.    [Запуск](https://github.com/XRenso/MotionPathConverterBlender/blob/main/docs/ru/introduction.md#запуск)
2.    [Сравнение модификатора Boolean](https://github.com/XRenso/MotionPathConverterBlender/blob/main/docs/ru/introduction.md#сравнение-модификатора-boolean)   
    1.    [С Intersect на boolean](https://github.com/XRenso/MotionPathConverterBlender/blob/main/docs/ru/introduction.md#сравнение-модификатора-boolean)
    .    
    2.    [Без Intersect на boolean](https://github.com/XRenso/MotionPathConverterBlender/blob/main/docs/ru/introduction.md#сравнение-модификатора-boolean)
    .
3.  [Работа над аддоном](https://github.com/XRenso/MotionPathConverterBlender/blob/main/docs/ru/introduction.md#работа-над-аддоном)
4.  [Планы на будущее](https://github.com/XRenso/MotionPathConverterBlender/blob/main/docs/ru/introduction.md#планы-на-будущее)
    1.    [Сделать разные версии(контекст меню и т.д)](https://github.com/XRenso/MotionPathConverterBlender/blob/main/docs/ru/introduction.md#1-сделать-разные-версииконтекст-меню-и-тд)
    2.    [Сделать более практичным](https://github.com/XRenso/MotionPathConverterBlender/blob/main/docs/ru/introduction.md#2-сделать-более-практичным)
    3.    [Сделать автоматическое создание объектов привязанных к пути](https://github.com/XRenso/MotionPathConverterBlender/blob/main/docs/ru/introduction.md#3-сделать-автоматическое-создание-объектов-привязанных-к-пути)





## Запуск
После установки вам нужно нажать F3 и найти `Convert Motion Path to Curve` , после вы увидите объект на сцене с названием `*obj_name*_path`.


![Is it working?](https://media1.giphy.com/media/9N1Gx7u0od3Tli0K66/giphy.gif?cid=790b7611034876555271d88253d5dbbcdf86cb1e406f2387&rid=giphy.gif&ct=g "Example")



```mermaid
sequenceDiagram
    autonumber
    Motion Path -) Curve: Аддон
    Curve -) Объекты на Curve: Объект с содификатором array, curve и для более красивого рендера с boolean(Intersect)
    OBJ on Curve --> Красивый рендер пути: немного косметической работы 
```


#### Весь код не был полностью написан мной. Я просто пределываю исходник для более удобной работы с motion path.

#### [К оглавлению :arrow_up:](https://github.com/XRenso/MotionPathConverterBlender/blob/main/docs/ru/introduction.md#содержание)

## Сравнение модификатора Boolean
### 1. С Intersect на boolean
![ALT-text](https://media3.giphy.com/media/TmsHZfdWiTT6hbwjbB/giphy.gif?cid=790b7611b39ea65baaaf68aeb7239bf3ebe85a101ad494cc&rid=giphy.gif&ct=g "With Intersect on boolean")

### 2. Без Intersect на boolean
![ALT-text](https://media3.giphy.com/media/4KVuHleCADz3nj5Kfd/giphy.gif?cid=790b761120d504ae7b95a01e81e62850559e950c2e649e5b&rid=giphy.gif&ct=g "Without Intersect on boolean")

#### [К оглавлению :arrow_up:](https://github.com/XRenso/MotionPathConverterBlender/blob/main/docs/ru/introduction.md#содержание)

## Работа над аддоном

```mermaid
journey
    title Поиск исходника
    section Поиск в Google
      Поиск: 4: Я
      Понимание кода: 3: Я
    section Переработка кода
      Альфа версия: 5: Я
      Бета версия: 4: Я
    section Поиск больше информации про аддоны
        Исправления: 4: Я
        Выпуск беты: 4: Я
    section Публикация
        Публикация на Github: 5: Я
        Оформление ReadMe: 3: Я

```
#### [К оглавлению :arrow_up:](https://github.com/XRenso/MotionPathConverterBlender/blob/main/docs/ru/introduction.md#содержание)

## Планы на будущее

### 1. Сделать разные версии(контекст меню и т.д)
### 2. Сделать более практичным
### 3. Сделать автоматическое создание объектов привязанных к пути

#### [К оглавлению :arrow_up:](https://github.com/XRenso/MotionPathConverterBlender/blob/main/docs/ru/introduction.md#содержание)
