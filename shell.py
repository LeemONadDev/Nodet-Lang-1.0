import nodet_lang


while 1:
    text = input("nodet-shell> ")
    result, error = nodet_lang.run('<stdin>',text)

    if error: print(error.as_string())
    else: print(result)