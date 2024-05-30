from django.conf import settings
from os          import path, listdir

def RenderStaticFilesInline(render):
    def wrapper(*a, **kw):
        rootDir  = settings.STATIC_ROOT
        cssDir   = path.join(rootDir, "CSS")
        jsDir    = path.join(rootDir, "JS")

        cssSources  = []
        jsSources   = []

        for staticFile in listdir(cssDir):
            with open(path.join(cssDir, staticFile), "r") as cssFile:
                cssSource = cssFile.read()
                cssSources.append(cssSource)

        for staticFile in listdir(jsDir):
            with open(path.join(jsDir, staticFile), "r") as jsFile:
                jsSource = jsFile.read()
                jsSources.append(jsSource)

        return render(cssSources=cssSources, jsSources=jsSources, *a, **kw)

    return wrapper
