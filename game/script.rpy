image bg prathica = im.Scale("images/arts/prathica.png", 1280, 720) 
label start:
    stop music fadeout 1.0
    # или:
    # renpy.music.stop(channel="music", fadeout=1.0)Copied!   
    # Пример мыслей Бухарова (текст без имени в кавычках)
    b "О НЕТ ОНИ МЕНЫ НАШЛИ!"
    play sound "audio/effects/vistreli.mp3" fadeout 1.0 
    scene bg prathica with fade  
    # Показываем картинку Роналду перед антагонистом
    show ronald_sp with dissolve:
        zoom 0.8
        xalign 0.5
        yalign 0.9
    r "Ты думал, что сможешь победить? SIIIUUU!"
    
    "Бухаров смотрел на это, не веря своим глазам."
    
    b "Роналду? Здесь? Ну и сюжетный поворот..."

    return
