import pywikibot
from pywikibot import pagegenerators
site = pywikibot.Site('uncyclopedia', 'uncyclopedia')
pagen = pywikibot.Page(site, 'User:JJPMastest/Run')
if pagen.text == 'False':
    quit()
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
