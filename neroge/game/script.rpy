
image bg wakeup = "1.png"
image bg door = "2.png"
image bg outdoor = "3.png"
image bg bob = "4.png"
image bg zone = "5.png"
image bg cam = "6.png"
image bg hospital = "7.png"
image bg yard = "8.png"
image gop first = "char31.png"
image gop sec = "char32.png"
image ment left = "char41.png"
image ment right = im.Flip("char41.png", horizontal=True)
image zek first = "char61.png"
image zek sec = "char71.png"

define main = Character('Рита', color="#c8ffc8")
define gop = Character('Гоп', color="#c8ffc8")
define ment = Character('Мент', color="#c8ffc8")
define nobody = Character('?', color="#c8ffc8")
define zek = Character('Насильник-кун', color="#c8ffc8")
define rag = Character('Тряпка-кун', color="#c8ffc8")

init:
    $ import scripts

label start:

    scene black

    "Каждый день я бурю..."
    "Иногда нахожу на бУрах что-нибудь интересное..."
    play music "Chris_Zabriskie_-_Undercover_Vampire_Policeman.mp3"

    $ renpy.pause(5.0)

    main "Моя голова~"
    main "Чувстую как будто мне дали пыльным мешком по голове."

    scene bg wakeup with fade

    main "Я очнулся в до боли знакомо баре"

    main "Каждый раз, когда мысли о безысходности бытия посещали меня, я приходил сюда чтобы забыться."
    main "Наверное сегодня такой же день."
    main "Мое состояние и ощущение ничтожности не покидало меня."
    main "Переполняющее меня чувство отвращения к самому себе заставило двигаться к выходу."

    scene bg door
    main '"Да лучше бы я на лекции обосрался" - мое внутреннее Я бурлило от ненависти к самому себе.'
    $ renpy.pause(1.3)
    scene bg door with scripts.Shake((0, 0, 0, 0), 0.5, dist=15)
    $ renpy.pause(1.5)
    scene bg door with scripts.Shake((0, 0, 0, 0), 0.7, dist=10)
    $ renpy.pause(2.2)
    scene bg door with scripts.Shake((0, 0, 0, 0), 0.6, dist=13)
    $ renpy.pause(2.1)
    main "Покачиваясь и задевая столы я добрался до заветной двери, за котрой меня ждала ночная свежесть."
    main "Навалившись пьяной тушей на ручки двери  и еле сдерживая равновесие я толкнул их вперед."
    main "Двери бесшумно распахнулись."
    main "Из последних сил, чтобы не упасть,  я уперся в косяк и посмотрел наружу."
    scene bg outdoor
    main "За дверьми меня ждала ночная свежесть, унылая дорога домой и множество ужасных мыслей, что терзали меня день ото дня..."
    main "С ними в одиночестве я оставаться не хотел."

    show gop first
    gop "Эээебать! Парняга!"
    gop "Чо ты тут делаешь? Ты чо, ебанутый?"
    gop "Хули нихуя?"
    main "Они подходили все ближе."
    main "Я старался держаться на ногах и отвечать адекватно."

    main '"Сасай! Мамку тваю ипал, лалка!" вырвалось из моей груди, хотя думал я совсем о другом'

    show gop sec

    main "Мой ответ очень удивил встречных, но недолго думая они бросились меня пиздить."
    hide gop

    scene black
    $ renpy.pause(3.0)
    main "Что-то пробудилось внутри меня"
    main "Какая-то алкосила заставляла раздавать пиздаки налево и на право не чувствуя боли"
    main "Контролировать себя я не мог, только ненависть рвавшаяся наружу делала то чего я хотел"
    main "Когда меня отпустило - было уже поздно"
    main "И я побежал..."

    main "Я бежал, потеряв счет времени."
    main "Кругом было безлюдно и тихо."
    main "Я понимал что совершил нечто ужасное и от этого бежал еще быстрее."
    main "В чувство меня привел дальний свет фар автомобиля, который приближался сзади."
    main "Только сейчас я ощутил усталость от бега и встал отдышаться."

    scene bg bob
    show ment left
    ment "АНДРЮХА, У НАС ТРУП! ВОЗМОЖНО КРИМИНАЛ! ПО КОНЯМ!"
    hide ment
    "ТУ ТУ ТУ ТУ ТУТ ТУ ТУ ТУ ТУ ТУ ТУ"
    show ment right
    ment "Я ДУРАК! БРОСАЙ ОРУЖИЕ!"
    hide ment
    "ТУ ТУ ТУ ТУ ТУТ ТУ ТУ"
    "ПАЗАВИ МЕНЯ С САБОЙ, Я ПРИИДУ СКВОЗЬ ЗЛЫЕ НОЧИ"

    scene black

    main "Затем был суд."
    main "Осужден по двести двадцать восьмой"
    main "На восемь лет..."

    scene bg zone

    main "Я словно пребывал в страшном сне."
    main "Мысли путались, но ясно было одно - назад дороги нет."
    main "Вот и лагерь, где мне предстоит провести ближайшие годы."
    main "Я даже не мог представить что ждало меня там, внутри забора."

    scene bg cam with fade

    ment "Давай, чушила, заходи! Мордой к стене, мразь!"
    main "Дежурный втолкнул меня в камеру."
    ment "Осваивайся, манька. Скоро сосдеди твои с работ придут."
    main '"С работ?" промелькнуло у меня в голове.'
    main "Дежурный словно читал мои мысли."
    ment "Вам скотам великая честь выпала - делаете тут игры про анимешных девочек."
    ment "И смотри, чтобы к концу отсидки готова была, а иначе.."
    main "Тут он сделал характерный жест, проведя по горлу"
    main "Дверь захлопнулась и я остался в камере один."

    scene black

    main "Чувство безысходности сново начало давить на меня."
    main "Я закрыл глаза и лег на первую попавшуюся койку."
    main "Не знаю сколько я пролежал, но лязг замка заставил меня подняться."

    scene bg cam
    show zek first
    main "В камеру зашел лысый зэк огромных размеров."
    nobody "Здарова, патлатый"
    main "Мне ничего не оставалось, кроме как ответить"
    main "Здарова, аутист"
    main "Он чему-то усмехнулся, смерил меня взглядом и продолжил"
    zek "Мня звать Насильник-кун, мы теперь соседи :3"
    zek "Смотри не напорись ненароком"
    main "Это предупреждение или угроза? "
    main "С самого начала разговор не задался"
    main "Не для тебя моя роза цвела!"
    main "Ничего умнее я в этот момент сказать не смог"
    main "Он обошел меня, немного постоял."
    zek "В общем посмотрим, а пока есть дельце для тебя."
    zek "Скажи ментам что тебе в лазарет к Тесаку надо."
    zek "Там еще один наш сосед. Унего от той игры, что мы делаем, пукан сегодня бомбанул."
    zek "Видать зашивают. Ну ты не ссы, у нас это типа прфессиональное заболевание."
    main "Насильник-кун присел на свою койку и тихонько запел песню про какую-то Занкоку."

    scene black

    main "Мне ничего не оставалось делать кроме как послушаться его и отправиться в лазарет"
    main "Я постучал в кормушку и объяснил дежурному что мне срочно требуется медпомошь"
    main "Ну, мол шишка дымится, сейчас стены сношать начну"
    main "Мои шаги гулко отдавались в пустых лагерных корридорах..."

    scene bg hospital

    ment "Тебе сюда, Тайнаков"
    main "Дежурный завел меня в кабинет, а сам развернулся и быстрым шагом пошел обратно"
    main "Полумрак лазарета подействовал на меня успокаивающе"
    main "Я осмотрелся в поисках своего нового соседа"
    nobody "АААБЛЯЯ! В уши ебать!"
    nobody "Мрази! Дайте рубль на эроге!"
    main "Хриплый крик доносился из-за ширмы"
    nobody "Шесть лет и какая-то демка! Проститу..кхэ кхэ"
    main "Послышалось шарканье ног и из-за ширмы вышел худой и изможденный зэк"

    show zek sec
    nobody "Такую идею просрали!"
    nobody 'Это могла быть "игра года-2008"!'
    main "Он выглядел бледным и поникшим"
    main "Поглядев на меня потухшим взглядом он представился"
    rag "Зови меня тряпкой-куном"
    rag "Послушаешь мою историю?"
    main "Я просто кивнул в ответ"

    hide zec sec
    scene black

    main "Мы сидели с ним в лазарете и он рассказывал мне все истории"
    main "Одна охуительнее другой просто"
    main "Про какую-то хуйню, малафью"
    main "Про дуру, какие-то три семерки"
    main "и о главном в жизни каждого игродела..."

    scene bg yard
    rag "Если уж ступил на путь эрогея"
    rag "Главное - всегда стремиться"
    rag "Стремиться сделать все охуенно"
    rag "И самому стать охуенным"
    main "Внутри меня от этих слов, будто воспрял духовный стержень"
    main "Во что бы то ни стало я должен сделать свою эроге к концу срока"
    main "Я стану охуенным Риточкой."

    pause(30.0)
    scene black
    ""




