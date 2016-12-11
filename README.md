# EasyJSParser
Simple JavaScript parser/interpreter in python

This program can parse and interpret Javascript code. For the moment it can work for AAdecode script (if you enable Unicode) and JSunpacker for exemple.

''
JScode ="""
eval(function(p,a,c,k,e,r){e=String;if(!''.replace(/^/,String)){while(c--)r[c]=k[c]||c;k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('(0(){4 1="5 6 7 8";0 2(3){9(3)}2(1)})();',10,10,'function|b|something|a|var|some|sample|packed|code|alert'.split('|'),0,{}));
"""

JP = JsParser()
print 'Return : ' + str(JP.ProcessJS(JScode))
''

He is not totally secure, I don't use exec() but I use eval() in restricted mode (No letter).

TODO:
Mix the eval part and the parser part.
