#Картиночки
image bg prathica = im.Scale("images/arts/prathica.png", 1920, 1080) 
image bg zolo = im.Scale("images/backgrounds/zolo.png", 1920, 1080)
label start:
    stop music fadeout 1.0
    # или:
    # renpy.music.stop(channel="music", fadeout=1.0)Copied!   
    # Пример мыслей Бухарова (текст без имени в кавычках)
    b "О НЕТ ОНИ МЕНЯ НАШЛИ!"
    play sound "audio/effects/vistreli.mp3" fadeout 1.0 
    scene bg prathica with fade
    "Еле ноги унёс!"
    play sound "audio/effects/vzdoh.mp3"
    "Не стоило мне воровать тот сникерс"
    "Нужно возвращаться домой"
    play sound "audio/effects/hozdenieasfalt.mp3" fadeout 1.0
    scene black with fade
    play sound "audio/effects/zamok.mp3"
    "Закрыл, дернул ручку - дверь не поддаётся"
    "Значит, всё в порядке"
    "Вот бы мама не заметила"
    "Я мигом влетел в свою комнату"
    scene bg zolo with fade
    b "Какой кошмар я пережил"
    "Плюхнулся на кровать и моментально утонул в мыслях"
    "А если они меня найдут? А если постучат в дверь? Если поймают?"
    "Я не смогу играть бравл старс в неволе"
    "Танчики.. Фифу!"
    "Беспокойные мысли не покидали меня, завтра в колледж к первой паре, спать осталось не долго, поэтому я взял телефон и всю ночь проиграл в бравл старс"
    scene black with fade
    "По итогу я уснул, но не надолго"
    m "Димочка, просыпайся, в колледж пора!"
    "Я очнувшись протираю глаза"
    
    return