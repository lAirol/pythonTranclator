import argostranslate.package
import argostranslate.translate
import sys
from classes.TranslatedLangs import TranslatedLangs

translatedLangs = TranslatedLangs()

variable = ""

if len(sys.argv) > 1:
    variable = sys.argv[1]
    print(f"Received variable: {variable}")

print(f"Received variable: {variable}")
argostranslate.package.update_package_index()

available_packages = argostranslate.package.get_available_packages()

print(available_packages)

language_pairs = [
    ('ru', 'en'),
    ('en', 'es'),
    ('en', 'de'),
    ('en', 'pl'),
    ('en', 'zh')
]

for from_code, to_code in language_pairs:
    try:
        package_to_install = next(filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages))
        argostranslate.package.install_from_path(package_to_install.download())
    except StopIteration:
        print(f"No package found for {from_code} to {to_code}")


def translate_text(text, from_lang, to_lang):
    return argostranslate.translate.translate(text, from_lang, to_lang)


text_to_translate = ""

if variable != "":
    text_to_translate = variable
else:
    text_to_translate = '''3 кавычки для того, чтобы можно было переностить текст 
    так '''
    # text_to_translate = '“Таинственный Лес”В глубинах дремучего леса, где солнечные лучи едва проникали сквозь густую листву, находилась маленькая деревушка. Её жители жили в симбиозе с природой, уважая её и боясь одновременно.Однажды, в самую тёмную ночь, когда звёзды сверкали на небе, произошло нечто странное. Старый деревенский сторож, Иван, услышал загадочный шорох в кустах. Он решил отправиться на разведку, несмотря на предостережения соседей.Иван шёл всё глубже в лес, его сердце билось сильнее. Вдруг перед ним возникла фигура в плаще, словно из мрака. Это была Лесная Дева – древняя хранительница леса. Она смотрела на Ивана сверкающими глазами.“Что ты ищешь, смертный?” – спросила она.Иван рассказал ей о шорохе и своём любопытстве. Лесная Дева улыбнулась:“Ты первый, кто осмелился прийти ко мне. Возможно, ты достоин узнать тайну этого леса.”Иван узнал, что каждое дерево, каждый камень в этом лесу имеет свою историю. Лес – это не просто скопление деревьев, а живой организм, который помнит прошлое и предсказывает будущее.С тех пор Иван стал рассказывать детям о Лесной Деве и её тайнах. Деревенская жизнь стала более волшебной, а лес – более загадочным. Иван ушёл в легенды, но его история живёт в сердцах жителей деревни.Конец'

translatedLangs.en = translate_text(text_to_translate, 'ru', 'en')

translatedLangs.es = translate_text(translatedLangs.en, 'en', 'es')
translatedLangs.de = translate_text(translatedLangs.en, 'en', 'de')
translatedLangs.pl = translate_text(translatedLangs.en, 'en', 'pl')
translatedLangs.zh = translate_text(translatedLangs.en, 'en', 'zh')


for language in translatedLangs.get_keys():
    print(f"{language}: {translatedLangs.__getattribute__(language)}")