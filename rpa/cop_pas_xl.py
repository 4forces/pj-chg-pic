import rpa as r
from tagui import clipboard

r.init(visual_automation=True, chrome_browser=False)
print('rpa initialised...')


# First, you must set up 'Folder' and 'excel' file to alt-tab properly
# else the screen will run

def folder_fx():
    ''' @ folder screen'''
    r.keyboard('[f2]')
    r.keyboard('[ctrl]a')
    r.keyboard('[ctrl]c')
    r.keyboard('[alt][tab]')


def xl_fx():
    ''' @ excel '''
    r.keyboard('[ctrl]v')
    r.keyboard('[enter]')

def folder_fx2():
    r.keyboard('[alt][tab]')
    r.keyboard('[down]')


runs = input('Run for how many times? ')

for i in range(runs):
    r.wait(10)
    folder_fx()
    xl_fx()
    folder_fx2()
print('completed for', runs, 'files. End of for loop')
