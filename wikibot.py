import pywikibot
from pywikibot import pagegenerators
site = pywikibot.Site('uncyclopedia', 'uncyclopedia')
pagen = pywikibot.Page(site, 'User:JJPMastest/Run')
if pagen.text == 'False':
    quit()
# task 1: replacing {{title}} with {{DISPLAYTITLE}}


cat = pywikibot.Category(site, 'Category:Will this work')
gen = pagegenerators.CategorizedPageGenerator(cat)
for page in gen:
    page.text = page.text.replace('title|', 'DISPLAYTITLE:')
    page.save('Changed {{title}} to {{DISPLAYTITLE}}')
if '|[' or '|align' or '|i' or '|<' in page.text:
    pass

# task 2: ctab via proxy


def createList(r1, r2):
    # Testing if range r1 and r2
    # are equal
    if (r1 == r2):
        return r1

    else:

        # Create empty list
        res = []

        # loop to append successors to
        # list until r2 is reached.
        while (r1 < r2 + 1):
            res.append(r1)
            r1 += 1
        return res
    #
    # Driver Code


r1, r2 = 4000003, 4010000
page2 = pywikibot.Page(site, 'Forum:Count to a billion')
page2.text = page2.text + "\n==is it against policy for this bot to \"autopatrol\" users who don't actually have the autopatrol right?==\n" + str(createList(r1, r2)) + " ~~~~"
page2.save('Bot: Updating [[UN:CTAB]]')

page3 = pywikibot.Page(site, 'Template:CTAB')
page3.text = page3.text.replace(str(r1 - 1), str(r2))
page3.save('Bot: Updating {{CTAB}}')

# task 3: automatically sending uw-coi notices to users with uw-advert1 or uw-advert2 notices


cat3 = pywikibot.Category(site, 'Category:User_talk_pages_with_Uw-advert1_notices')
gen3 = pagegenerators.CategorizedPageGenerator(cat3)
if "Uw-coi" not in page.text:
    for page in gen3:
        page.text = page.text + u"<p>{{subst:Uw-coi}} ~~~~"
        page.save(u"Bot: Warning user about possible conflict of interest editing")
else:
    pass
cat4 = pywikibot.Category(site, 'Category:User_talk_pages_with_Uw-advert2_notices')
gen4 = pagegenerators.CategorizedPageGenerator(cat4)
if "Uw-coi" not in page.text:
    for page in gen4:
        page.text = page.text + u"<p>{{subst:Uw-coi}} ~~~~"
        page.save(u"Bot: Warning user about possible conflict of interest editing")
else:
    pass


# task 4: clearing the sandbox
page5 = pywikibot.Page(site, 'Uncyclopedia:Sandbox')
page6 = pywikibot.Page(site, 'User:JJPMaster/things')
page5.text = page5.text.replace(page5.text, page6.text)
page5.save('Bot: Clearing sandbox')
