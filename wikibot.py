import pywikibot
from pywikibot import pagegenerators
# task 0: exclusion compliance
if "{{nobots}}" in page.text:
    pass

# -*- coding: utf-8  -*-
# task 1: replacing {{title}} with {{DISPLAYTITLE}}
site = pywikibot.Site('uncyclopedia', 'uncyclopedia')
cat = pywikibot.Category(site, 'Category:Will this work')
gen = pagegenerators.CategorizedPageGenerator(cat)
for page in gen:
    page.text = page.text.replace('title|', 'DISPLAYTITLE:')
    page.save('Changed {{title}} to {{DISPLAYTITLE}}')
if '|[' or '|align' in page.text:
    pass

# task 2: icu'ing blank pages
site = pywikibot.Site('en', 'uncyclopedia')  # The site we want to run our bot on
page = pywikibot.Page(site, 'User talk:JJPMaster/sandbox')
page.text = page.text.replace('', '{{ICU|~~~~~|sub=short}}')
page.save('Hey look ma, I’m a bot developer now!')  # Saves the page
