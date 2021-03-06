#!/usr/bin/python
# this is a smith configuration file

# bhagirati

# command line options
opts = preprocess_args(
    {'opt' : '-l'}, # build fonts from legacy for inclusion into final fonts
    {'opt' : '-p'}, # do not run psfix on the final fonts
    {'opt' : '-s'}  # only build a single font
    )

import os2

# set the default output folders
out='results'

# locations of files needed for some tasks
DOCDIR = ['documentation', 'web']
STANDARDS='tests/reference'

# set meta-information
script='beng'
APPNAME='nlci-' + script

DESC_SHORT='Bengali Unicode font with OT support'
DESC_NAME='NLCI-' + script
DEBPKG='fonts-nlci-' + script
getufoinfo('source/Bhagirati-Regular.ufo')

# set test parameters
TESTSTRING=u'\u0995'

# set fonts to build
faces = ('Bhagirati',)
facesLegacy = ('BHAG',)
styles = ('-R', '-B', '-I')
stylesName = ('Regular', 'Bold', 'Italic')
stylesLegacy = ('', 'BD', 'I')

if '-s' in opts:
    faces = (faces[0],)
    facesLegacy = (facesLegacy[0],)
    styles = (styles[0],)
    stylesName = (stylesName[0],)
    stylesLegacy = (stylesLegacy[0],)

# set build parameters
fontbase = 'source/'
archive = fontbase + 'archive/unhinted/'
generated = 'generated/'
tag = script.upper()

panose = [2, 0, 0, 3]
codePageRange = [0, 29]
unicodeRange = [0, 1, 2, 3, 4, 5, 6, 7, 15, 16, 29, 31, 32, 33, 35, 38, 39, 40, 45, 60, 62, 67, 69, 91]
hackos2 = os2.hackos2(panose, codePageRange, unicodeRange)

if '-l' in opts:
    for f, fLegacy in zip(faces, facesLegacy):
        for (s, sn, sLegacy) in zip(styles, stylesName, stylesLegacy):
            font(target = process('ufo/' + f + '-' + sn.replace(' ', '') + '.ttf',
                    cmd(hackos2 + ' ${DEP} ${TGT}'),
                    name(f, lang='en-US', subfamily=(sn))
                    ),
                source = legacy(f + s + '.ttf',
                                source = archive + fLegacy + sLegacy + '.ttf',
                                xml = fontbase + 'bhagirati_unicode.xml',
                                params = '',
                                noap = '')
                )

if '-l' in opts:
    faces = list()
for f in faces:
    p = package(
        appname = APPNAME + '-' + f.lower(),
        version = VERSION,
        docdir = DOCDIR # 'documentation'
    )
    for sn in stylesName:
        snf = '-' + sn.replace(' ', '')
        fontfilename = tag + f + snf
        font(target = process(fontfilename + '.ttf',
                cmd('${PSFCHANGETTFGLYPHNAMES} ${SRC} ${DEP} ${TGT}', [fontbase + f + snf + '.ufo']),
                name(tag + ' ' + f, lang='en-US', subfamily=(sn))
                ),
            source = fontbase + f + snf + '.ufo',
            # opentype = fea(f + snf + '.fea',
            #     master = fontbase + 'master.fea',
            #     make_params = ''
            #     ),
            #graphite = gdl(generated + f + snf + '.gdl',
            #    master = fontbase + 'master.gdl',
            #    make_params = '-p 1 -s 2',
            #    params = '-e ' + f + snf + '_gdlerr.txt'
            #    ),
            #classes = fontbase + 'bhagirati_classes.xml',
            #ap = generated + f + snf + '.xml',
            version = VERSION,
            #woff = woff('woff/' + fontfilename + '.woff', params = '-v ' + VERSION + ' -m ../' + fontbase + f + '-WOFF-metadata.xml'),
            #script = 'beng',
            package = p,
            fret = fret(params = '-r -oi')
        )

def configure(ctx):
    ctx.find_program('psfchangettfglyphnames')
