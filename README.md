# TinyJSParser
Simple JavaScript parser/interpreter in python in only one file.

This program can parse and interpret Javascript code (not convertion from Javascript to Python). For the moment it can work for AAdecode script (if you enable Unicode) and JSunpacker for exemple.   
I m using it ATM to solve some Javascript challenge to resolve url from web hoster like uptostream or netu only using python code.

```
JScode ="""
eval(function(p, a, c, k, e, r) {
    e = String;
    if (!''.replace(/^/, String)) {
        while (c--) r[c] = k[c] || c;
        k = [function(e) {
            return r[e]
        }];
        e = function() {
            return '\\w+'
        };
        c = 1
    };

    while (c--)

        if (k[c]) p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c]);

    return p
}('(0(){4 1="5 6 7 8";0 2(3){9(3)}2(1)})();', 10, 10, 'function|b|something|a|var|some|sample|packed|code|alert'.split('|'), 0, {}));
"""

JP = JsParser()
print 'Return : ' + str(JP.ProcessJS(JScode))
```

or

```
JScode ="""
var t = 78;
$(document).ready(function() {
    var y = $("#aQydkd1Gbfx").text();
    var x = $("#aQydkd1Gbf").text();
    var s = [];
    for (var i = 0; i < y.length; i++) {
        var j = y.charCodeAt(i);
        if ((j >= 33) && (j <= 126)) {
            s[i] = String.fromCharCode(33 + ((j + 14) % 94));
        } else {
            s[i] = String.fromCharCode(j);
        }
    }
    var tmp = s.join("");
    var str = tmp.substring(0, tmp.length - _CoRPE1bSt9()) + String.fromCharCode(tmp.slice(0 - _CoRPE1bSt9()).charCodeAt(0) + _0oN0h2PZmC()) + tmp.substring(tmp.length - _CoRPE1bSt9() + 1);
    $("#streamurl").text(str);
});
t = 10;
function nWuEkcMO4z() {
    return 2 + 1;
}
function _CoRPE1bSt9() {
    return nWuEkcMO4z() + 1478067443 - 1478067445;
}
function _0oN0h2PZmC() {
    return _CoRPE1bSt9() - _7L9xjpbs4N();
}
function _7L9xjpbs4N() {
    return -2;
}
"""
JP = JsParser()
Liste_var = []
JP.AddHackVar('#aQydkd1Gbfx',"b601f6becd1a6884f9a075582cb7")
JP.ProcessJS(JScode,Liste_var)
print 'Decoded url : ' + JP.GetVarHack("#streamurl")
```
   
<br><br><br><br>
   
One time the JS is executed you can access at all var, for exemple with
```
r = JP.GetVar(Liste_var,'result')
```

Or using "Hackvar" to get Jquery $("#streamurl").text()
```
print 'Decoded url : ' + JP.GetVarHack("#streamurl")
```
   
<br><br><br><br>
The version 1 is only working on python 2, can use older version for python 3.   
   
He is not totally secure, I don't use exec() but I use eval() in restricted mode (No letter).

TODO:
Mix the eval part and the parser part.
