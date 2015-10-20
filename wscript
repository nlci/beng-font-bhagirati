# bhagirati

# set folder names
out='results'
TESTDIR='tests'
STANDARDS='tests/reference'

# set meta-information
script='beng'
APPNAME='nlci-' + script
VERSION='0.100'
TTF_VERSION='0.100'
COPYRIGHT='Copyright (c) 2009-2015, NLCI (http://www.nlci.in/fonts/)'

DESC_SHORT='Bengali Unicode font with OT support'
DESC_LONG='''
Pan Bengali font designed to support all the languages using the Bengali script.
'''
DESC_NAME='NLCI-' + script
DEBPKG='fonts-nlci-' + script

# set test parameters
TESTSTRING=u'\u0995'

# set fonts to build
faces = ('Bhagirati',)
facesLegacy = ('BHAG',)
styles = ('-R', '-B', '-I')
stylesName = ('Regular', 'Bold', 'Italic')
stylesLegacy = ('', 'BD', 'I')

# set build parameters
fontbase = 'source/'
tag = script.upper()

for f, fLegacy in zip(faces, facesLegacy):
    for (s, sn, sLegacy) in zip(styles, stylesName, stylesLegacy):
        font(target = process(tag + f + '-' + sn.replace(' ', '') + '.ttf',
                cmd('psfix ${DEP} ${TGT}'),
                name(tag + ' ' + f, lang='en-US', subfamily=(sn))
                ),
            source = legacy(f + s + '.ttf',
                            source = fontbase + 'archive/' + fLegacy + sLegacy + '.ttf',
                            xml = fontbase + 'bhagirati_unicode.xml',
                            noap = ''),
            opentype = internal(),
            #graphite = gdl(fontbase + f + s + '.gdl',
            #    master = fontbase + 'master.gdl',
            #    make_params = '-p 1 -s 2 -l first',
            #    params = '-d -v2'
            #    ),
            #classes = fontbase + 'bhagirati_classes.xml',
            ap = f + s + '.xml',
            version = TTF_VERSION,
            copyright = COPYRIGHT,
            license = ofl('Bhagirati', 'NLCI'),
            woff = woff(),
            script = 'beng',
            fret = fret(params = '-r')
        )
