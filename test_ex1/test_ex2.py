import time
import pytest
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

def test_tchibo():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.tchibo.de/")
    print()
    print("********", driver.title)               # ret title of the page
    print("********", driver.current_url)         # ret url

    cookies = driver.find_element(By.CSS_SELECTOR, 'div#onetrust-button-group button#onetrust-accept-btn-handler:nth-child(3)')
    cookies.click()
    time.sleep(2.0)

    open_element = driver.find_element(By.LINK_TEXT, 'Kaffee')
    open_element.click()
    time.sleep(1.0)

    texte = driver.find_element(By.CSS_SELECTOR, 'h2.m-coffee-text-headline.c-tp-display.c-tp-display-4')
    t = texte.text
    assert t == "Unsere Kaffeevielfalt auf einen Blick", "No OK"
    print(t)

    #kaffee_pads = driver.find_element(By.CSS_SELECTOR, 'a#m-coffee-qs-pads-category img.c-tp-accordiontoggle-image.js-tp-imagelazy--loaded')    #'a#m-coffee-qs-pads-category span.c-tp-accordiontoggle-text')
    kaf_pad = driver.find_element(By.CSS_SELECTOR, 'a#m-coffee-qs-pads-category span.c-tp-accordiontoggle-text')
    k = kaf_pad.text
    assert k == 'Kaffeepads', 'No kaffeepads'
    print("Selectie cafea: ", kaf_pad.text)
    #kaffee_pads.click()
    time.sleep(2.0)

    pads = driver.find_element(By.CSS_SELECTOR, 'a#m-coffee-qs-pads-category')
    g = pads.text
    print("Selectie cafea: ", g)
    pads.click()
    time.sleep(2.0)

    # a#id10b     a#id68d 134
    #gala_kreation = driver.find_element(By.CSS_SELECTOR, 'span.huml_content_2000000001327068 a#id10b span.m-tp-productbox002-title-text') #    produsul la reducere la care i s-a schimbat pretul - oferta
    #gala_kreation = driver.find_element(By.CSS_SELECTOR, '.m-tp-productbox002-imagewrapper a[data-pds-link="402051284"]')      #   produs vechi cantitate mai mica
    gala_kreation = driver.find_element(By.CSS_SELECTOR, '.m-tp-productbox002-title:nth-child(2) a[onclick="return fdc.Quickbuy.open([402051284]);"] .m-tp-productbox002-title-text')
    print("Nume cafea: ", gala_kreation.text)

    #price = driver.find_element(By.CSS_SELECTOR, 'div.m-tp-productbox002-p402051284 div.c-tp-price.c-tp-price--120.c-tp-price--centered.c-tp-price--coffee:nth-child(1) div.c-tp-price-currentprice:nth-child(2)') # span.tp-price-decimal')
    price = driver.find_element(By.CSS_SELECTOR, '.m-tp-productbox002.m-tp-productbox002--background.m-tp-productbox002-p402051284 .c-tp-price.c-tp-price--120.c-tp-price--centered.c-tp-price--coffee .c-tp-price-currentprice')   # a ramas produsul vechi
    print(price.text)
    to_pay = price.text
    #print()
    for i in range(len(to_pay)+1):
        if i == 1:
            print(",", end="")
        elif i == 0:
            print("Pret = ", to_pay[i], end="")
        # elif i == 1:
        #     print(to_pay[i], end="")
        else:
            print(to_pay[abs(1 - i)], end="")

    # ce scrie dupa pret
    valuta = driver.find_element(By.CSS_SELECTOR, 'div.m-tp-productbox002.m-tp-productbox002--background.m-tp-productbox002-p402051284 div.m-tp-productbox002-price div.c-tp-price-baseprice')      # ce apare dupa pret
    print(" , ", valuta.text,", ", end="")

    # Open: Gala „Kreation des Jahres“ Caffè Crema   id10b   id68d 134
    #open_gala_kreation = driver.find_element(By.CSS_SELECTOR, 'span.huml_content_2000000001327068 a#id10b span.m-tp-productbox002-title-text')     #   produs nou ce schimba id-ul - oferta pret
    #open_gala_kreation = driver.find_element(By.CSS_SELECTOR, '.m-tp-productbox002-imagewrapper a[data-pds-link="402051284"]')     #   produs vechi cantitate mai mica
    open_gala_kreation = driver.find_element(By.CSS_SELECTOR, '.m-tp-productbox002-title:nth-child(2) a[onclick="return fdc.Quickbuy.open([402051284]);"] .m-tp-productbox002-title-text')
    open_gala_kreation.text
    open_gala_kreation.click()
    time.sleep(2.0)

    in_cos = driver.find_element(By.CSS_SELECTOR, '.tp-col.tp-col-12.tp-col-s-7 .qb__section.qb__section__buy .qb__subsection .qb__subsection__add-to-cart__item.qb__showcase__confirmation-button')
    print(in_cos.text)
    in_cos.click()
    time.sleep(2.0)

    spre_plata = driver.find_element(By.CSS_SELECTOR, 'div[variant="banner"] span.tp-button-content')
    print(spre_plata.text)
    spre_plata.click()
    time.sleep(2.0)

    sterge_produs_cos = driver.find_element(By.CSS_SELECTOR, 'div[data-locator="cart_delete_product"]')
    print(sterge_produs_cos.text)
    sterge_produs_cos.click()
    time.sleep(2.0)

    inapoi_la_cumparaturi = driver.find_element(By.CSS_SELECTOR, 'div.c-header2020-logo a .c-header2020-logo-image')
    print(inapoi_la_cumparaturi.text)
    inapoi_la_cumparaturi.click()
    time.sleep(3.0)

    suchen = driver.find_element(By.CSS_SELECTOR, '.tp-card.c-header2020-search .tp-search-suggest-container')
    print(suchen.text)
    suchen.click()
    time.sleep(1.0)

    search_in_box = driver.find_element(By.CSS_SELECTOR, '#c-header2020-icons .tp-search-suggest-container input[placeholder="Lieblingsprodukt suchen..."]')
    search_in_box.send_keys('World of Cafissimo − Probierbox')
    print(search_in_box.text)
    search_in_box.click()
    time.sleep(2.0)

    such_begriffe = driver.find_element(By.CSS_SELECTOR, '.tp-card.suggested-panel.visible.overlay .search-terms .box-header')
    print("*", such_begriffe.text)

    lupa = driver.find_element(By.CSS_SELECTOR, '.tp-search-suggest-container .tp-button.tp-search-suggest-search-icon .tp-icon')
    lupa.click()

    probierbox = driver.find_element(By.CSS_SELECTOR, 'a[title="World of Cafissimo − Probierbox"] .m-tp-productbox002-title-text')
    print(probierbox.text)
    probierbox.click()
    time.sleep(2.0)

    poze = driver.find_element(By.CSS_SELECTOR, '.m-tp-productimagegallery .m-tp-productimagegallery-thumbnails-wrapper .m-tp-mainImagePreview')
    poze.click()
    time.sleep(1.0)

    sir_poze_unu = driver.find_element(By.CSS_SELECTOR, '.m-tp-productimagegallery .m-tp-productimagegallery-thumbnails-wrapper .m-tp-mainImagePreview:nth-child(1)')
    sir_poze_unu.click()
    time.sleep(1.0)

    sir_poze_doi = driver.find_element(By.CSS_SELECTOR, '.m-tp-productimagegallery .m-tp-productimagegallery-thumbnails-wrapper .m-tp-mainImagePreview:nth-child(2)')
    sir_poze_doi.click()
    time.sleep(1.0)

    sir_poze_trei = driver.find_element(By.CSS_SELECTOR, '.m-tp-productimagegallery .m-tp-productimagegallery-thumbnails-wrapper .m-tp-mainImagePreview:nth-child(3)')
    sir_poze_trei.click()
    time.sleep(1.0)

    sir_poze_patru = driver.find_element(By.CSS_SELECTOR, '.m-tp-productimagegallery .m-tp-productimagegallery-thumbnails-wrapper .m-tp-mainImagePreview:nth-child(4)')
    sir_poze_patru.click()
    time.sleep(1.0)

    sir_poze_cinci = driver.find_element(By.CSS_SELECTOR, '.m-tp-productimagegallery .m-tp-productimagegallery-thumbnails-wrapper .m-tp-mainImagePreview:nth-child(3)')
    sir_poze_cinci.click()
    time.sleep(1.0)

    time.sleep(2.0)



    # for i in range(len(b)):
    #     if i == 1:
    #         assert b[1] == 'cafissimo', 'No cafissimo'
    #         b[1].click()
    #     else:
    #         pass
    time.sleep(2.0)

    logo_albastru_jos = driver.find_element(By.CSS_SELECTOR, ".flyout-component__content-container")
    action = ActionChains(driver)
    action.move_to_element(logo_albastru_jos).perform()

    # new_product = driver.find_element(By.CSS_SELECTOR, 'a[title="World of Cafissimo − Probierbox"] span.m-tp-productbox002-title-text')
    # print(new_product.text)
    # new_product.click()



    # optiuni = driver.find_element(By.CSS_SELECTOR, 'a[data-cs-override-id="navigationMainItem_Kaffee"]:nth-child(3)')   #acceseaza Kaffee
    # optiuni.click()
    # select_alle_kaffees = driver.find_element(By.CSS_SELECTOR, '')
    #
    # select_alle_kaffees.click()
    # select_kaffees = driver.find_element(By.LINK_TEXT, 'Alle Kaffees')
    # select_kaffees.click()
# select_harry_potter = driver.find_element(By.CSS_SELECTOR, 'p.top-thema-teaser__link a[title="Discover now"]')
# select_harry_potter.click()
#hp = select_harry_potter.text
#assert hp == "Harry Potter collection", "Not Harry Potter"


#driver.close()
