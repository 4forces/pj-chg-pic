import rpa as r

r.init(visual_automation=True, chrome_browser=False)
print('rpa initialised...')

# ============ select clariant logo ================= #

def del_clogo():
    '''Delete clariant logo'''
    r.keyboard('[alt][tab]')
    r.click('c_logo.PNG')
    r.keyboard('[delete]')


def ins_alogo():
    '''# insert avient logo'''
    r.keyboard('[alt]n')
    r.keyboard('pp')
    r.keyboard('av[down][enter]')


def goto_pic_layout():
    '''go to picture settings layout screen'''
    r.keyboard('[alt]jp')
    r.keyboard('po')
    r.keyboard('l')




r.keyboard('[tab][right]')
r.keyboard('[tab][right][right][right][right][right][right]')

r.keyboard('[tab][tab][tab][left]')


r.keyboard('[tab][tab]5.06')

r.keyboard('[tab][tab][tab]0.16')

r.keyboard('[tab][up][up][enter]')

r.keyboard('[tab][down][spacebar]')

r.keyboard('[left][left][spacebar]')

r.keyboard('[enter]')

