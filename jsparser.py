# -*- coding: utf-8 -*- 
#
# Vstream https://github.com/Kodi-vStream/venom-xbmc-addons
#

#******************************
#   A Basic Javascript parser
#******************************

# TODO LIST
# ---------
# Regex will work only for normal name, not for exotic name
# Object
# Globla/Local variables/function/object

#help
#https://sarfraznawaz.wordpress.com/2012/01/26/javascript-self-invoking-functions/
#https://nemisj.com/python-api-javascript/
#https://fr.wikiversity.org/wiki/Python/Les_types_de_base
#https://javascriptobfuscator.com/Javascript-Obfuscator.aspx


#UNICODE ERROR
#print a.decode('utf-8').encode('ascii','replace')
#

import re
import types
from types import NoneType
import time

import sys

REG_NAME = '[\w]+'
REG_OP = '[\/\*\-\+\(\)\{\}\[\]<>\|=~^]+' #not space here
DEBUG = True
MAX_RECURSION = 50

JScode8585 = """
ﾟωﾟﾉ= /｀ｍ´）ﾉ ~┻━┻   //*´∇｀*/ ['_']; o=(ﾟｰﾟ)  =_=3; c=(ﾟΘﾟ) =(ﾟｰﾟ)-(ﾟｰﾟ); (ﾟДﾟ) =(ﾟΘﾟ)= (o^_^o)/ (o^_^o);(ﾟДﾟ)={ﾟΘﾟ: '_' ,ﾟωﾟﾉ : ((ﾟωﾟﾉ==3) +'_') [ﾟΘﾟ] ,ﾟｰﾟﾉ :(ﾟωﾟﾉ+ '_')[o^_^o -(ﾟΘﾟ)] ,ﾟДﾟﾉ:((ﾟｰﾟ==3) +'_')[ﾟｰﾟ] }; (ﾟДﾟ) [ﾟΘﾟ] =((ﾟωﾟﾉ==3) +'_') [c^_^o];(ﾟДﾟ) ['c'] = ((ﾟДﾟ)+'_') [ (ﾟｰﾟ)+(ﾟｰﾟ)-(ﾟΘﾟ) ];(ﾟДﾟ) ['o'] = ((ﾟДﾟ)+'_') [ﾟΘﾟ];(ﾟoﾟ)=(ﾟДﾟ) ['c']+(ﾟДﾟ) ['o']+(ﾟωﾟﾉ +'_')[ﾟΘﾟ]+ ((ﾟωﾟﾉ==3) +'_') [ﾟｰﾟ] + ((ﾟДﾟ) +'_') [(ﾟｰﾟ)+(ﾟｰﾟ)]+ ((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+((ﾟｰﾟ==3) +'_') [(ﾟｰﾟ) - (ﾟΘﾟ)]+(ﾟДﾟ) ['c']+((ﾟДﾟ)+'_') [(ﾟｰﾟ)+(ﾟｰﾟ)]+ (ﾟДﾟ) ['o']+((ﾟｰﾟ==3) +'_') [ﾟΘﾟ];(ﾟДﾟ) ['_'] =(o^_^o) [ﾟoﾟ] [ﾟoﾟ];(ﾟεﾟ)=((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+ (ﾟДﾟ) .ﾟДﾟﾉ+((ﾟДﾟ)+'_') [(ﾟｰﾟ) + (ﾟｰﾟ)]+((ﾟｰﾟ==3) +'_') [o^_^o -ﾟΘﾟ]+((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+ (ﾟωﾟﾉ +'_') [ﾟΘﾟ]; (ﾟｰﾟ)+=(ﾟΘﾟ); (ﾟДﾟ)[ﾟεﾟ]='\\'; (ﾟДﾟ).ﾟΘﾟﾉ=(ﾟДﾟ+ ﾟｰﾟ)[o^_^o -(ﾟΘﾟ)];(oﾟｰﾟo)=(ﾟωﾟﾉ +'_')[c^_^o];(ﾟДﾟ) [ﾟoﾟ]='\"';(ﾟДﾟ) ['_'] ( (ﾟДﾟ) ['_'] (ﾟεﾟ+(ﾟДﾟ)[ﾟoﾟ]+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (ﾟΘﾟ))+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟｰﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟΘﾟ)+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ ((ﾟｰﾟ) + (o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟｰﾟ)+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟΘﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ ((o^_^o) +(o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ (o^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ (o^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟｰﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟoﾟ]) (ﾟΘﾟ)) ('_');
"""

JScodeQ ="""
eval(function(p,a,c,k,e,r){e=String;if(!''.replace(/^/,String)){while(c--)r[c]=k[c]||c;k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('(0(){4 1="5 6 7 8";0 2(3){9(3)}2(1)})();',10,10,'function|b|something|a|var|some|sample|packed|code|alert'.split('|'),0,{}));
"""

JScode ="""
ff = {'a':5,'b': 9};
ff.c = ff.b;
debug();
"""

JScode2452 ="""
cc = /\uff40\uff4d\u00b4\uff09\uff89 ~\u253b\u2501\u253b   /["_"];
o = ee = _ = 3;
c = dd = ee - ee;
ff = dd = (o ^ _ ^ o) / (o ^ _ ^ o);
ff = {
  "dd" : "_",
  "cc" : ((cc == 3) + "_")[dd],
  "bb" : (cc + "_")[o ^ _ ^ o - dd],
  "aa" : ((ee == 3) + "_")[ee]
};
ff[dd] = ((cc == 3) + "_")[c ^ _ ^ o];
ff["c"] = (ff + "_")[ee + ee - dd];
ff["o"] = (ff + "_")[dd];

gg = ff["c"] + ff["o"] + (cc + "_")[dd] + ((cc == 3) + "_")[ee] + (ff + "_")[ee + ee] + ((ee == 3) + "_")[dd] + ((ee == 3) + "_")[ee - dd] + ff["c"] + (ff + "_")[ee + ee] + ff["o"] + ((ee == 3) + "_")[dd];
ff["_"] = (o ^ _ ^ o)[gg][gg];

hh = ((ee == 3) + "_")[dd] + ff.aa + (ff + "_")[ee + ee] + ((ee == 3) + "_")[o ^ _ ^ o - dd] + ((ee == 3) + "_")[dd] + (cc + "_")[dd];
ee += dd;

ff[hh] = "\\";
ff.dd\uff89 = (ff + ee)[o ^ _ ^ o - dd];
oeeo = (cc + "_")[c ^ _ ^ o];

ff[gg] = '"';
ff["_"](ff["_"](hh + ff[gg] + ff[hh] + dd + ee + dd + ff[hh] + dd + (ee + dd) + ee + ff[hh] + dd + ee + (ee + dd) + ff[hh] + 
dd + ((o ^ _ ^ o) + (o ^ _ ^ o)) + ((o ^ _ ^ o) - dd) + ff[hh] + dd + ((o ^ _ ^ o) + (o ^ _ ^ o)) + ee + ff[hh] + (ee + dd) + (c ^ _ ^ o) + ff[hh] + ee + ((o ^ _ ^ o) - dd) + ff[hh] + dd + dd + (c ^ _ ^ o) + ff[hh] + 
dd + ee + (ee + dd) + ff[hh] + dd + (ee + dd) + ee + ff[hh] + dd + (ee + dd) + ee + ff[hh] + dd + (ee + dd) + (ee + (o ^ _ ^ o)) + ff[hh] + 
(ee + dd) + ee + ff[hh] + ee + (c ^ _ ^ o) + ff[hh] + dd + dd + ((o ^ _ ^ o) - dd) + ff[hh] + dd + ee + dd + ff[hh] + dd + ((o ^ _ ^ o) + (o ^ _ ^ o)) + ((o ^ _ ^ o) + (o ^ _ ^ o)) + ff[hh] + 
dd + ee + dd + ff[hh] + dd + ((o ^ _ ^ o) - dd) + (o ^ _ ^ o) + ff[hh] + dd + ee + (o ^ _ ^ o) + ff[hh] + dd + ((o ^ _ ^ o) + (o ^ _ ^ o)) + ((o ^ _ ^ o) - dd) + ff[hh] + dd + (ee + dd) + 
dd + ff[hh] + dd + ((o ^ _ ^ o) + (o ^ _ ^ o)) + (c ^ _ ^ o) + ff[hh] + dd + ((o ^ _ ^ o) + (o ^ _ ^ o)) + ee + ff[hh] + ee + ((o ^ _ ^ o) - dd) + ff[hh] + (ee + dd) + dd + ff[gg])(dd))("_");

debug();
"""

JScode542452 ="""
var g;
o = _ = 3;
h = (o ^ _ ^ o) / (o ^ _ ^ o);
a = {
  "b" : "_",
  "c" : ((g == 3) + "_")[h],
  "d" : (g + "_")[o ^ _ ^ o - h],
  "e" : ((o == 3) + "_")[o]
};
debug();
"""

JScode45 ="""
(function(s, opt_attributes, key, pairs, i, params) {
  /** @type {function (new:String, *=): string} */
  i = String;
  if (!''.replace(/^/,String)) {
    for (;key--;) {
      /** @type {(number|string)} */
      params[key] = pairs[key] || key;

    }
    /** @type {Array} */
    pairs = [function(urlParam) {
      return params[urlParam];
    }];

    /**
     * @return {?}
     */
    i = function() {
      return "\\w+";
    };

    /** @type {number} */
    key = 1;
  }

  for (;key--;) {
    if (pairs[key]) {
      /** @type {string} */
      s = s.replace(new RegExp("\\b" + i(key) + "\\b", "g"), pairs[key]);

    }
  }

  return s;
})('(0(){4 1="5 6 7 8";0 2(3){9(3)}2(1)})();', 10, 10, "function|b|something|a|var|some|sample|packed|code|alert".split("|"), 0, {});
"""


JScodevxc ="""
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

JScodeW = """
var cars = ["aa", "bb", "cc", "dd"];
var i, len, text="to erase";
for (i = 0, len = cars.length, text = ""; i < len; i++) {
    text += cars[i] + " " ;
    if ( i == 0) break;
}

var j = 2.5;
j*=2;

debug();
text += j;

return text;
"""

JScode78 ="""
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

def IsUnicode(s):
    if isinstance(s, unicode):
        return True
    return False
    
def out(string):
    if DEBUG:
        print str(string.encode('ascii','replace'))
        
def Ustr(string):
    if isinstance(string, unicode):
        return str(string.encode('ascii','replace'))
    return str(string)
 
    
def GetFirstChar(string):
    j = 0
    try:
        while (string[j].isspace()):
            j = j + 1
    except:
        return ''
    return string[j]
    
def GetNextchar(string, pos):
    if len(string) <= (pos + 1):
        return ''
    return string[pos+1]
    
def GetBeetweenChar(str,char1,char2):
        s = str.find(char1)
        if s == -1:
            return 0,''
            
        n = 1
        e = s + 1
        while (n > 0) and (e < len(str)):
            c = str[e]
            if c == char1:
                n = n + 1
            if c == char2:
                n = n - 1
            e = e + 1
            
        s = s + 1
        e = e - 1
        return e,str[s:e]
        
def CheckType(value):
    if (isinstance(value, types.StringTypes)):
        return 'String'
    if isinstance(value, ( bool ) ):
        return 'Bool'
    if isinstance(value, ( int, long ) ):
        return 'Numeric'
    if type(value) in [list,tuple, dict]:
        return 'Array'
    if (isinstance(value, (NoneType))):
        return 'Undefined'
    return 'Unknow'

#Fonction to return only one parameter from a string with correct closed [] () "" and ''      
def GetItemAlone(string,separator = ' '):
    l = len(string) - 1
    ret = ''
    
    i = -1
    p = 0 #parenthese
    a = 0 #accolade
    b = 0 #bracket
    c1 = 0
    c2 = 0
    n = False
    last_char = ''

    s = False
    
    while (i < l):
        i = i + 1
        ch = string[i]
        ret = ret + ch
        n = False
        
        #Skip empty space
        if (ch.isspace()):
            continue

        if ch == '(':
            p = p + 1
        if ch == ')':
            p = p - 1
        if ch == '{':
            a = a + 1
        if ch == '}':
            a = a - 1
        if ch == '[':
            b = b + 1
        if ch == ']':
            b = b - 1
        if ch == '"':
            c1 = 1 - c1
        if ch == "'":
            c2 = 1 - c2
        if ch == '.' and not ((last_char in '0123456789') or (string[i+1] in '0123456789')):
            n = True
            
        if (ch in separator) and (p==0) and (a==0) and (b==0) and (c1==0) and (c2==0) and not(n):
            return ret
            
        last_char = ch   

    return ret
    
def MySplit(string,char,NoEmpty = False):
    r = []
    l = len(string)
    i = 0
    chain = 0
    p = 0
    e = ""
    
    if l == 0:
        if (NoEmpty):
            return []
            
    while (l > i):
        c = string[i]
        if c == '"':
            chain = 1-chain
        if c == '(':
            p = p + 1
        if c == ')':
            p = p - 1           
            
        if (c == char) and (chain == 0) and (p==0):
            r.append(e.strip())
            e = ''
        else:    
            e = e + c
            
        i = i + 1

    r.append(e.strip())
    return r
    
def GetConstructor(value):
    if isinstance(value, ( int, long ) ):
        return 'function Number() {\n    [native code]\n}'
    elif 'function' in value:
        return 'function Function() {\n    [native code]\n}'
    elif (isinstance(value, types.StringTypes)):
        return 'function String() {\n    [native code]\n}'        

    return ''

class JSBuffer(object):
    PRIORITY = {'+':3 , '-':3 , '*':4 , '/':4 , '>':1 , '<':1 , '&':2 , '|':2}
    #print prio.get('*',0)
    def __init__(self):
        self.type = None
        self.buffer = ''
        self.__op = ''
        self.__value = None
        
        #buffers
        self.buf=[]
        self.opBuf = []
        
    def SetOp(self,op):
        #print 'Set op  ' + str(op)
        if (op == '&') and  (self.__op == '&'):
            return
        if (op == '|') and  (self.__op == '|'):
            return
        else:
            self.__op = self.__op + op
            
        
    #Need 3 values for priority   
    def AddValue(self,value):
        print 'ADD ' + str(value) + ' ' + str(type(value)) + ' a ' + str(self.buf)
        if not self.type:
            self.type = CheckType(value)
            self.Push(value,self.__op)
            return       
         
        if not self.__op:
            print 'op ' + str(self.opBuf) + ' - buff ' +str(self.buf)
            raise Exception("Missing operator")
            
        self.Push(value,self.__op)
        self.__op = ''
    
    def GetPrevious(self):
        ret = self.buf[-1]
        del self.buf[-1]
        self.__op = self.opBuf[-1]
        del self.opBuf[-1]
        if len(self.buf) == 0:
            self.type = None
        return ret
        
    def Compute(self):

        #Work for operateur + | !
        if self.type == 'String':
            if '!' in self.opBuf[0]:
                self.buf[0] = not self.buf[0]
                self.opBuf[0] = self.opBuf[0].replace('!','')
            if len(self.buf) > 1:
                if '!' in self.opBuf[1]:
                    self.buf[1] = not self.buf[1]
                    self.opBuf[1] = self.opBuf[1].replace('!','')
                if '+' in self.opBuf[1]:
                    self.buf[0] = self.buf[0] + self.buf[1]
                if '|' in self.opBuf[1]:
                    if not self.buf[0]:
                        self.buf[0] = self.buf[1]
                #decale
                del self.opBuf[-1]
                del self.buf[-1]
                                       
        #work for all operator      
        elif self.type == 'Numeric':
            if len(self.buf) > 1:
                self.buf[0] = self.opBuf[0] + str(self.buf[0]) + self.opBuf[1] + str(self.buf[1])
                self.opBuf[0] = ''
                #decale
                del self.opBuf[-1]
                del self.buf[-1]
            else:
                self.buf[0] = self.opBuf[0] + str(self.buf[0])
                self.opBuf[0] = ''

        # work for
        elif self.type == 'Logic':
            if not self.buf[0] == self.buf[1]:
                self.buf[0] = False
            else:
                self.buf[0] = True
            #decale
            del self.opBuf[-1]
            del self.buf[-1]
            
        elif len(self.buf) > 1:
            print self.type
            print self.buf
            print self.opBuf
            raise Exception("Can't compute")
    
    #on decale tout
    def Push(self,value,op):
        
        if len(self.buf) > 1:
            self.Compute()

        if not (self.type == CheckType(value)):
            #Type different mais JS peut convertir en string
            if self.type == 'String' or CheckType(value) == 'String':
                if not CheckType(self.buf[0]) == 'String':
                        self.buf[0]=self.SpecialStr(self.buf[0])
                if len(self.buf) > 1:
                    if not CheckType(self.buf[1]) == 'String':
                        self.buf[1]=self.SpecialStr(self.buf[1])
                value=str(value)
                self.type = 'String'

            #Type different mais juste operation logique
            elif op == '==':
                self.type = 'Logic'
            else:
                print '> Need ' + str(self.type)
                print '> have ' + str(type(value))
                raise Exception("Values or not same type")

        self.buf.append(value)
        self.opBuf.append(op)
        return

    def SpecialStr(self,value):
        if value == None:
            return 'Undefined'
        if value == True:
            return 'true'
        if value == False:
            return 'false'
        if type(value) in [list]:
            convert_first_to_generator = (str(w) for w in value)
            return ','.join(convert_first_to_generator)
        if type(value) in [dict]:
            return '[object Object]'
        return str(value)
    
    #ok all finished, force compute
    def GetBuffer(self):
    
        #Force compute
        self.Compute()
        while len(self.buf) > 1:
            self.Compute()
          
        if self.type == 'Logic':
            return self.buf[0]
    
        if self.type == 'Numeric':
            return self.SafeEval(self.buf[0])
        
        if self.type == None:
            return ''
        
        return self.buf[0]
        
    #WARNING : Take care if you edit this function, eval is realy unsafe.
    #better to use ast.literal_eval() but not implemented before python 3
    def SafeEval(self,str):
        if not str:
            raise Exception ('Nothing to eval')
        f = re.search('[^0-9+-.\(\)<>=&%!*\^\/]',str)
        if f:
            raise Exception ('Wrong parameter to Eval : ' + str)
            return 0
        str = str.replace('!','not ')
        #str = str.replace('=','==')
        #print '>>' + str
        return eval(str)
    
class JsParser(object):
    class fonction(object):
        def __init__(self, param, data):
            self.code = data
            self.p = param  


    def __init__(self):
        self.Unicode = False
        self.HackVars = []
        self.debug = False
        self.LastEval = ''
        self.SpecialOption = ''
        
        self.Return = False
        self.Break = False 
                        
    def SetReturn(self,r,v):
        self.Return = True
        self.RecursionReturn = r
        self.ReturnValue = v
    
    def AddHackVar(self,name, value):
        self.HackVars.append((name,value))
        
    def GetVarHack(self,name):
        return self.GetVar(self.HackVars,None,name)
    
    #Need to take care at chain var with " and '
    def ExtractFirstchain(self,string):

        #print string.encode('ascii','replace')
    
        if len(string.strip()) == 0:
            return '',0
    
        l = len(string)
        string = string + ' ' #To prevent index out of range, hack
        
        i = -1
        p = 0 #parenbthese
        a = 0 #accolade
        b = 0 #bracket
        f = False #fonction ?
        r = False #Regex
        com1 = False
        com2 = False
        prev = '' #previous char
        
        stringR = ''
        
        while (l > i):
        
            i = i + 1
            
            #ignore comment
            if string[i:(i+2)] == '/*':
                com1 = True
            if (com1):
                if string[i:(i+2)] == '*/':
                    com1 = False
                    i = i + 1
                continue
            if string[i:(i+2)] == '//' and  not (r):
                com2 = True
            if (com2):
                if string[i] == '\n':
                    com2 = False
                else:
                    continue

            ch = string[i]
            stringR = stringR + ch
            
            if ch == '(':
                p = p + 1
            if ch == ')':
                p = p - 1
            if ch == '{':
                a = a + 1
            if ch == '}':
                a = a - 1
            if ch == '[':
                b = b + 1
            if ch == ']':
                b = b - 1
            if (r) and ch == '/':
                r = False
            if ch == '/' and prev == '=':
                r = True
                
            #memorise last char
            if not ch.isspace():
                prev = ch                    
                               
            #Dans tout les cas les parenthses doivent etre fermees, ainsi que les crochet
            if (p == 0) and (b == 0):
                #Si on rencontre un ; par defaut
                if (ch == ';') and not (f):
                    #Ok, accolade fermees aussi, c'est tout bon
                    if (a == 0):
                        return stringR,i
                    #Accoloade non fermee, c'est une fonction
                    else:
                        f = True
                #si c'est une fonction et l'accolade fermee
                if (f) and (a == 0):
                
                    #quel est le caractere suivant ?
                    j = i + 1
                    while (string[j].isspace()) and(l > j):
                        j = j + 1
                    #Si parenthese on repart
                    if string[j] == '(':
                        continue
                    
                    # Mal formated string ?
                    # Sometime, coder forget the last ; before the }
                    # Desactived for the moment, because can bug in 'a = {};'
                    if False:
                        j = -2            
                        while (stringR[j].isspace()) or (stringR[j] == '}'):
                            j = j - 1
                        if not (stringR[j] == ';'):
                            j = j + 1
                            stringR = stringR[:j] + ';' + stringR[j:]
                        
                    # if there is a last ; add it
                    if string[i+1] == ';':
                        stringR = stringR + ';'
                        i = i + 1

                    return stringR,i
        
        #chaine bugguée ?
        if ';' not in string:
            #out('ERROR Extract chain without ";" > ' + string )
            return string.rstrip() + ';', i
            
        raise Exception("Can't extract chain " + string)

    #Everything Without a "Real" is False   
    def CheckTrueFalse(self,string):
        #out( '> Check True or false : ' + str(string) )

        if isinstance(string, ( bool ) ):
            if string == True:
                return True       
        elif (isinstance(string, types.StringTypes)):
            if not string == '':
                return True
        if isinstance(string, ( int, long , float) ):
            if not (string == 0):
                return True
        if isinstance(string, ( list, tuple) ):
            if not (string == []):
                return True
        return False
        
    def evalJS(self,JScode,vars,func,allow_recursion):
    
        if allow_recursion < 0:
            raise Exception('Recursion limit reached')
            
        allow_recursion = allow_recursion - 1

        #plus que la chaine a evaluer
        JScode = JScode.strip()
        
        debug = JScode
        
        out( '-------------')
        out( str(allow_recursion) + ' : A evaluer >'+ JScode + '<')
            
        #********************************************************
        
        InterpretedCode = JSBuffer()
        
        while (len(JScode)>0):
            c = JScode[0]

            #print 'InterpretedCode > ' + InterpretedCode
            #print 'JScode > ' + JScode

            #Alpha chain
            if c == '"':
                e = JScode[1:].find('"') + 1
                if e == 0:
                    raise Exception("Can't eval chain " + JScode)
                #if it's not the form "abc".err
                if not GetNextchar(JScode,e) == '.':
                    InterpretedCode.AddValue(JScode[1:e])
                    JScode = JScode[(e+1):]
                    continue
                else:
                    self.SetVar(vars,func,'TEMPORARY_VARS',JScode[1:e])
                    JScode = 'TEMPORARY_VARS' + JScode[(e+1):]
            if c == "'":
                e = JScode[1:].find("'") + 1
                if e == 0:
                    raise Exception("Can't eval chain " + JScode)
                #if it's not the form "abc".err
                if not GetNextchar(JScode,e ) == '.':
                    InterpretedCode.AddValue(JScode[1:e])
                    JScode = JScode[(e+1):]
                    continue
                else:
                    self.SetVar(vars,func,'TEMPORARY_VARS',JScode[1:e])     
                    JScode = 'TEMPORARY_VARS' + JScode[(e+1):]                   
            #numeric chain
            r = re.search('(^[0-9]+)',JScode)
            if r:
                InterpretedCode.AddValue(int(JScode[0:r.end()]))
                JScode = JScode[(r.end()):]
                continue
            #Regex
            r = re.search('^\/.*\/(.*$)',JScode)
            if r:
                reg = r.group(0)
                flag = r.group(1)
                #test if the regex is valid
                if flag:
                    for i in flag:
                        if i not in 'gimuy':
                            reg = None
                            break
                InterpretedCode.AddValue(reg)
                JScode = JScode[(len(r.group(0))):]
                continue            
            #parentheses
            if c == "(":
                pos2,c2 = GetBeetweenChar(JScode,'(',')')
                v = self.evalJS(c2,vars,func,allow_recursion)
                InterpretedCode.AddValue(v)
                JScode = JScode[(pos2 + 1):]
                continue
            #braket BUGGED
            if c == "[":
                pos2,c2 = GetBeetweenChar(JScode,'[',']')
                v = self.evalJS(c2,vars,func,allow_recursion)
                if v == 'constructor':
                    v2 = InterpretedCode.GetPrevious()
                    print '********' + str(v2)
                    v3 = GetConstructor(v2)
                    InterpretedCode.AddValue(v3)
                elif CheckType(v) == 'Numeric':
                    v2 = InterpretedCode.GetPrevious()
                    InterpretedCode.AddValue(v2[int(v)])
                else:
                    InterpretedCode.AddValue([])
                JScode = JScode[(pos2 + 1):]
                continue           
                
            #hackVars
            r = re.search('^\$\("#([\w]+)"\)\.text\(\)',JScode)
            if r:
                InterpretedCode.AddValue(self.GetVar(self.HackVars,None,r.group(1)))
                JScode = JScode[(r.end()):]
                continue
                
            #remove useless code
            if JScode.startswith('new '):
                JScode = JScode[4:]
                continue           
            
                
            name = ''            
            #Extraction info
            m = re.search(r'^(?:([\w]+)\.)*([\w]+) *\(', JScode,re.DOTALL)
            #Syntax > aaaaaa.bbbbbb(cccccc) ou bbbb(cccc) ou "aaaa".bb(ccc)
            if m:
                name == ''
                if m.group(1):
                    name = m.group(1)
                function = m.group(2)
                pos3,arg = GetBeetweenChar(JScode[(m.end()-1):],'(',')')

                print 'DEBUG EVAL > Name: ' + name + ' arg: ' + arg + ' function: ' + function
             
                if function:
                    
                    out( "> function : " + function + ' arg=' + arg)
                    
                    #Definite function ?
                    fe = self.IsFunc(vars,func,function)
                    if fe:
                        out('> defenite fonction : ' + function)
                        n,p,c = fe
                        a = MySplit(arg,',',True)
                        a2 = []

                        for i in a:
                            vv = self.evalJS(i,vars,func,allow_recursion)
                            a2.append(self.RemoveGuil(vv))
                        
                        if (len(p) > 0) and (len(a2)>0):
                            nv = tuple(zip(p, a2))
                            for z,w in nv:
                                self.SetVar(vars,func,z,w)

                        v = self.Parse(c,vars,func,allow_recursion)
                        
                        if self.Return:
                            self.Return = False
                            InterpretedCode.AddValue(v)
                            
                        JScode = JScode[(len(m.group(0)) + pos3 + 0):]
                        continue                   
   
                    #Native
                    #charCodeAt
                    if function=='charCodeAt':
                        s = self.GetVar(vars,func,name)
                        v = self.evalJS(arg,vars,func,allow_recursion)
                        InterpretedCode.AddValue(ord(s[int(v)]))
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #length
                    if function=='length':
                        s = self.GetVar(vars,func,name)
                        InterpretedCode.AddValue(len(s))
                        JScode = JScode[(len(m.group(0)) + pos3):]
                        continue
                    #Substring
                    if function=='substring':
                        s = self.GetVar(vars,func,name)
                        arg = arg.split(',')
                        p1 = self.evalJS(arg[0],vars,func,allow_recursion)
                        if len(arg)> 1:
                            p2 = self.evalJS(arg[1],vars,func,allow_recursion)
                            InterpretedCode.AddValue(s[ int(p1) : int(p2) ])
                        else:
                            InterpretedCode.AddValue(s[ int(p1) :])
                        #out('Substring : var = ' + s + ' index=' + str(p1) )
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #join
                    if function=='join':
                        t = arg.replace('"','').replace("'","")
                        s = self.GetVar(vars,func,name)
                        #out('Join : avec ' + str(t) + 'var = ' + str(s))
                        InterpretedCode.AddValue(t.join(s))
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #replace
                    #print re.sub('1',lambda m: f(m.group()),s)
                    if function=='replace':
                        arg = MySplit(arg,',')
                        t1 = arg[0]
                        t2 = self.evalJS(arg[1],vars,func,allow_recursion)
                        
                        s = self.GetVar(vars,func,name)
                        
                        if not t1.startswith('/'):
                            t1 = self.evalJS(t1,vars,func,allow_recursion)
                            
                        #regex mode ?
                        if t1.startswith('/'):

                            jr = re.findall(t1.split('/')[1], s)

                            for k in jr:
                                out('replace ' + str(t2))
                                if not self.IsFunc(vars,func,t2):
                                    print vars
                                    #print str(k) + ' > ' + str(t2)
                                    s = s.replace(k,t2)
                                else:
                                    print '1 ' + t2+'('+ k + ')'
                                    v = self.evalJS(t2+'('+ k + ')',vars,func,allow_recursion)
                                    print '2 ' + str(v)
                                    v = str(v)
                                    print str(k) + ' > ' + str(v)
                                    s = s.replace(k,v)
                            InterpretedCode.AddValue( s )
                        #String mode
                        else:
                            #t1 = self.evalJS(t1,vars,func,allow_recursion)
                            InterpretedCode.AddValue( s.replace(t1,t2))
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #slice
                    if function=='slice':
                        s = self.GetVar(vars,func,name)
                        arg = arg.split(',')
                        p1 = self.evalJS(arg[0],vars,func,allow_recursion)
                        if len(arg)> 1:
                            p2 = self.evalJS(arg[1],vars,func,allow_recursion)
                            sr = s[int(p1):int(p2)]
                        else:
                            sr = s[int(p1):]
                        sr = '"' + sr + '"'
                        InterpretedCode.AddValue(sr)
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #string.fromCharCode
                    if (function=='fromCharCode') and (name=='String'):
                        v = self.evalJS(arg,vars,func,allow_recursion)
                        #out('StringFromCharcode ' +  r.group(1) + '=' + str(v))
                        InterpretedCode.AddValue(chr(int(v)))
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #split
                    if function=='split':
                        arg = arg.replace('"','').replace("'","")
                        s = self.GetVar(vars,func,name)
                        InterpretedCode.AddValue(s.split(arg))
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #function
                    if function=='function':
                        pos9 = len(JScode[(len(m.group(0)) + pos3 + 0):])
                        v = self.MemFonction(vars,func,'',arg,False,JScode[(len(m.group(0)) + pos3 + 0):])[2]
                        pos3 = pos3 + pos9
                        InterpretedCode.AddValue(v)
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #RegExp
                    if function=='RegExp':
                        arg = MySplit(arg,',')
                        t1 = self.evalJS(arg[0],vars,func,allow_recursion)
                        t2 = self.evalJS(arg[1],vars,func,allow_recursion)
                        InterpretedCode.AddValue('/' + self.RemoveGuil(t1) + '/' + self.RemoveGuil(t2))
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue             
                    #debug
                    if function=='debug':
                        print '------------------------------------'
                        print vars
                        print '------------------------------------'
                        print func
                        print '------------------------------------'
                        raise Exception("DEBUG")
                        
                    raise Exception("Unknow fonction : " + function)
                    
            #TODO hack inside
            if InterpretedCode.type == 'String':
                if c == '.':
                    JScode = InterpretedCode.GetPrevious() + JScode
                    continue


            #variables
            m = re.search('^(' + REG_NAME + '(?:\[[^\]]+\])* *)(' + REG_OP + '|$)',JScode, re.UNICODE)
            if m:
                v = m.group(1).strip()
                pos7 = len(m.group(1))
                r = self.GetVar(vars,func,v)

                op = ''
                if len(m.groups()) > 1:
                    op = m.group(2).strip()

                #out("> var " + v + "=" + str(r))

                if self.IsVar(vars,v):
                    #just var
                    if len(op) < 2:
                        pass
                    #check if it's i++ ou i -- form
                    elif op == '++':
                        self.SetVar(vars,func,v,r + 1)
                        pos7+=2
                    elif op == '--':
                        self.SetVar(vars,func,v,r-1)
                        pos7+=2
                    #a == 1
                    elif (op == '||') or (op == '&&'):
                        #InterpretedCode.AddValue(r)
                        #InterpretedCode.SetOp(op[0])
                        pos7+=1
                    #a+=1 form
                    elif op[1] == '=' and not op[0] == '=':
                        n = GetItemAlone(JScode[m.end():],' ' + REG_OP)
                        if op[0] == '+':
                            r = self.evalJS(v+'+'+n ,vars,func,allow_recursion)
                        elif op[0] == '-':
                            r = self.evalJS(v+'-'+n ,vars,func,allow_recursion)
                            
                        self.SetVar(vars,func,v,r)
                        l = len(n) + 2
                        pos7 = pos7 + l
                            
                    InterpretedCode.AddValue(r)       
                    JScode = JScode[pos7:]
                    continue
                    
                raise Exception("Can't find var " + r.group(1))

                
            #Space to remove
            if c == ' ':
                JScode = JScode[1:]
                continue
                
            #Simple operation
            if c in '+<>-*/=&%|!^.':
                InterpretedCode.SetOp(c)
                JScode = JScode[1:]
                continue      
                
            #No sure how to put this
            if JScode == '{}':
                InterpretedCode.AddValue({})
                JScode = JScode[2:]
                continue
            if JScode == '[]':
                InterpretedCode.AddValue([])
                JScode = JScode[2:]
                continue                
                    
            #???
            if JScode == ';':
                JScode = JScode[1:]
                continue
                
            # Not found part
            # We will make another turn
            print vars
            out("Can't eval string :" + JScode)
            out("Last eval : " + str(self.LastEval))
            print c.encode('ascii','replace')
            print debug.encode('ascii','replace')
            raise Exception("Can't Eval chain : " + JScode)

        InterpretedCode2 = InterpretedCode.GetBuffer()
        
        out( str(allow_recursion) + ' : Evalue > '+ Ustr(InterpretedCode2) + " type " + Ustr(type(InterpretedCode2)) )
        out( '-------------')

        self.LastEval = InterpretedCode2
        return InterpretedCode2
        
    def RemoveGuil(sel,string):
        if not (isinstance(string, types.StringTypes)):
            return string
        string = string.strip()
        if string.startswith('"') and string.endswith('"'):
            return string[1:-1]
        return string
        
    def InitVar(self,var,variable):
        variable = variable.strip()
    
        for j in var:
            if j[0] == variable:
                var.remove(j)
                return
        
    def GetVar(self,var,func,variable):
    
        variable = variable.strip()
        
        index = None
        if '[' in variable:
            index = variable.split('[')[1][:-1]
            variable = variable.split('[')[0]
            index = self.evalJS(index,var,func,50)
            
        for j in var:
            if j[0] == variable:
                r = j[1]
                if not(index == None):
                    if CheckType(index) == 'Numeric':
                        r = r[int(index)]
                    elif CheckType(index) == 'String':
                        index = self.RemoveGuil(index)
                        r = r[index]
                return r
                
        print var
        a= []
        a.append(variable)
        print a
        raise Exception('Variable not defined: ' + variable)
            
    def SetVar(self,var,func,variable,value,i = 0):

        variable = variable.strip()
        
        #cleaning
        if variable[0] == '(':
            variable = variable[1:-1]

        #Existing var ?
        for j in var:
            if j[0] == variable:

                #vars ?
                if (isinstance(var[var.index(j)][1], types.StringTypes)):
                    var[var.index(j)] = (variable,value)
                #Array 
                elif type(var[var.index(j)][1]) in [list,tuple]:

                    Listvalue = var[var.index(j)][1]

                    #ok this place doesn't esist yet
                    l = int(i) - len(Listvalue) + 1
                    while l > 0:
                        Listvalue.append('undefined')
                        l = l - 1
                    #Now modify it
                    Listvalue[int(i)] = value
                    var[var.index(j)] = (variable,Listvalue)
                #dictionnary
                elif type(var[var.index(j)][1]) in [dict]:
                    Listvalue = var[var.index(j)][1]
                    Listvalue[i] = value
                    var[var.index(j)] = (variable,Listvalue)                
                #Numeric
                else:
                    var[var.index(j)] = (variable,value)

                return
                
        #New var
        var.append((variable,value))
    
    def IsVar(self,var,variable):
        variable = variable.split('[')[0]
        for j in var:
            if j[0] == variable:
                return True
        return False
        
    #Need to use metaclass here
    def IsFunc(self,vars,Func,name):
        for j in Func:
            if j[0] == name:
                return j
        #ok not in fonction but in vars ?
        for k in vars:
            if k[0] == name:
                for j in Func:
                    if j[0] == k[1]:
                        return j
        return False
        
    def VarManage(self,allow_recursion,vars,func,name,value=None):

        index = None
        init = False
        
        try:
            value = value.strip()
            name = name.strip()
        except:
            pass

        #Variable is an array ?
        m = re.search(r'^([\w]+)\[(.+?)\]$', name,re.DOTALL)
        if m:
            name = m.group(1)
            index = m.group(2)
            index = self.evalJS(index,vars,func,allow_recursion)
  
        if value:
            #Values is an array []
            if value.startswith('[') and value.endswith(']'):
                value = value[1:-1]
                
                valueT = MySplit(value,',')
                v = []
                for k in valueT:
                    v2 = self.evalJS(k,vars,func,allow_recursion)
                    v.append(v2)
                value = v
                if index == None:
                    index = 0
                    init = True
            #Values is an array {}
            elif value.startswith('{') and value.endswith('}'):
                value = value[1:-1]
                valueT = MySplit(value,',',True)
                v = {}
                for k in valueT:
                    l = k.split(':')
                    #WARNING : no eval here in JS
                    #v2g = self.evalJS(l[0],vars,func,allow_recursion)
                    v2g = self.RemoveGuil(l[0])
                    v2d = self.evalJS(l[1],vars,func,allow_recursion)
                    v[v2g] = v2d
                value = v
                if index == None:
                    index = 0
                    init = True
                         
            else:
                value = self.evalJS(value,vars,func,allow_recursion)

        #Output for debug
        if not (index == None):
            out( '> Variable in parser => ' + Ustr(name) + '[' + str(index) + ']' + ' = ' + Ustr(value))
        else:
            out( '> Variable in parser => ' + Ustr(name) + ' = ' + Ustr(value))
                           
        #chain
        if (isinstance(value, types.StringTypes)):
            self.SetVar(vars,func,name,value,index)
        #number
        elif isinstance(value, ( int, long , float) ):
            self.SetVar(vars,func,name,value,index)
        #list
        elif type(value) in [list,tuple,dict]:
            if init:
                self.InitVar(vars,name)
            self.SetVar(vars,func,name,value,index)
        #undefined
        elif value == None:
            self.SetVar(vars,func,name,None,index)
        else:
            print type(value)
            raise Exception('> ERROR : Var problem >' + str(value))
        return
        

    #(Function(arg){code})(arg2) Self invoked
    # Function(arg){code}(arg2)  Not self invoked 
    def MemFonction(self,vars,func,name,parametres,selfinvoked,data):
    
        if not name:
            n0 = 0
            while self.IsFunc(vars,func,'AnonymousFunc' + str(n0)):
                n0=n0+1
            name = 'AnonymousFunc' + str(n0)
            
        if (self.SpecialOption):
            if self.SpecialOption.split('=')[0] == 'Namefunc':
                name = self.SpecialOption.split('=')[1]
            self.SpecialOption = ''
             
        param = MySplit(parametres,',',True)
        
        out('Extract function :' + name + ' Selfinvok :' + str(selfinvoked) + ' ' + str(param))
        #out('data ' + str(data))
        
        pos = 0
        replac = ''
        
        pos2,content = GetBeetweenChar(data,'{','}')
        #out('content ' + str(content))
        pos = pos2 + 1
        func.append((name,param,content.lstrip()))
        
        #self invoked ? Not working yet
        if selfinvoked:
            pos = data.find(')',pos) + 1
            data = data[pos:]          
        else:
            data = data[pos:] 

        #param in function ?
        if len(data)> 0:
            r = name + data
            if not data.endswith(';'):
                r = r + ';'
            replac = r

            pos = pos + len(data)
          
        return replac, pos , name
        
    def Parse(self,JScode,vars,func,allow_recursion=MAX_RECURSION):
    
        if allow_recursion < 0:
            raise Exception('Recursion limit reached')
            
        allow_recursion = allow_recursion - 1
    
        #************************
        #    Post traitement
        #************************
        
        #Need all functions first, because they can be called first and be at the bottom of the code
        #So we extract all functions first, and replace them by a simple call in the code, if they are self invoked
        
        posG = 0
        Startoff = 0
        Endoff = 0
        
        while (True):

            chain,pos = self.ExtractFirstchain(JScode[posG:])
            if not (chain):
                break
            
            Startoff = posG
            Endoff = posG + pos + 1
            posG = Endoff
            
            #skip empty char
            chain = chain.strip()
             
            #out('/////////////////')
            #out('> ' + chain)
            #out('/////////////////')
            
            #fonction
            m = re.search(r'^(\()* *function(?: ([\w]+))* *\(([^\)]*)\) *{', chain,re.DOTALL)
            if m:
            
                name = ''
                selfinvoked = False
                if m.group(2):
                    name = m.group(2)
                if m.group(1):
                    selfinvoked = True
            
                replac,pos3,xyz = self.MemFonction(vars,func,name,m.group(3),selfinvoked,chain)
                JScode = JScode[:Startoff]+ replac + JScode[Endoff:]

                posG = Startoff + len(replac)

        #***********************
        # The real Parser
        #**********************

        while (True):
        
            chain,pos = self.ExtractFirstchain(JScode)
            if not (chain):
                break
                
            JScode = JScode[(pos+1):]
                        
            chain = chain.lstrip()
            chain = chain.rstrip()
            
            #empty ?
            if chain == ';':
                continue
              
            print 'D++++++++++++++++++'
            print chain.encode('ascii','replace')
            print 'F++++++++++++++++++'
            
            #hackVars ?
            m = re.search(r'^\$\("#([^"]+)"\)\.text\(([^\)]+)\);', chain)
            if m:
                out( '> hack ' + m.group(0) + ' , variable est ' + m.group(1))
                self.SetVar(self.HackVars,None,m.group(1),self.GetVar(vars,func,m.group(2)))
                continue
  
            name = ''            
            #Extraction info
            #Problem, catch fonction too :(
            m = re.search(r'^([\w]+) *\(', chain,re.DOTALL)
            #Syntax > aaaaa(bbbbb) .........
            if m:
                name = m.group(1)
                pos3,arg = GetBeetweenChar(chain[(m.end()-1):],'(',')')
                code = chain[(m.end() + pos3):]
                print 'DEBUG > Name: ' + name + ' arg: ' + arg + ' code: ' + code
                
                #Jquery
                if name == 'DOCUMENT_READY':
                    out('DOCUMENT_READY ' + arg)
                    self.SpecialOption = 'Namefunc=DR'
                    self.Parse(arg,vars,func,allow_recursion)

                    #It's not the correct place to do that, but for the moment ...
                    self.Parse('DR();',vars,func,allow_recursion)
                    
                    continue
                #eval ?
                if name == 'eval':
                    out('Eval')
                    #out('To eval >' + arg)
                    r = self.Parse(arg,vars,func,allow_recursion)
                    self.Return = True
                    return r

                #For boucle ?
                if name == 'for':
                    arg = arg.split(';')
                    v = arg[0] + ';'
                    t = arg[1]
                    i = arg[2] + ';'
                    f = code
                    if GetFirstChar(f) =='{':
                        f = GetBeetweenChar(f,'{','}')[1]
                    
                    #out('> Boucle for : Var=' + v + ' test=' + t + ' incrementation=' + i + ' code=' + f)
                    
                    #init var              
                    self.Parse(v,vars,func,allow_recursion)
                    #loop
                    while (self.CheckTrueFalse(self.evalJS(t,vars,func,allow_recursion))):
                        #fonction
                        self.Parse(f,vars,func,allow_recursion)
                        if self.Break:
                            self.Break = False
                            break
                        #incrementation
                        self.Parse(i,vars,func,allow_recursion)

                    continue
                    
                #boucle while ?
                if name == 'while':
                    f = code
                    if GetFirstChar(f) =='{':
                        f = GetBeetweenChar(f,'{','}')[1]
                    
                    #out('> Boucle while : Var=' + v + ' test=' + t + ' incrementation=' + i + ' code=' + f)
                    
                    #loop
                    while (self.CheckTrueFalse(self.evalJS(arg,vars,func,allow_recursion))):
                        #fonction
                        self.Parse(f,vars,func,allow_recursion)
                        if self.Break:
                            self.Break = False
                            break

                    continue
                    
                #Boucle if
                if name == 'if':
                    t = arg
                    f = code
                    e = ''
                    
                    if GetFirstChar(f) =='{':
                        f = GetBeetweenChar(f,'{','}')[1]

                    #Need to check if there is else statement ?
                    chain2,pos2 = self.ExtractFirstchain(JScode)
                    if 'else' in chain2:
                        chain2 = chain2.lstrip()
                        JScode = JScode[(pos2 + 1):]
                        m2 = re.search(r'else\s*{(.+?)}$', chain2,re.DOTALL)
                        if m2:
                            e = m2.group(1)
                    
                    #out('> Boucle if : test=' + arg + ' code=' + f + ' else=' + e)
                    if (self.CheckTrueFalse(self.evalJS(t,vars,func,allow_recursion))):
                        self.Parse(f,vars,func,allow_recursion)
                    elif (e):
                        self.Parse(e,vars,func,allow_recursion)
                    continue  

            #Variable operation/creation/modification ?
            m = re.search(r'^\({0,1}([\w]+)(?:\[([^\]]+)\])*\){0,1}\s*=',chain,re.DOTALL | re.UNICODE)
            if m or chain.startswith('var '):
                out('var')

                if chain.startswith('var '):
                    chain = chain[4:]
                
                #Now need to extract all vars from chain
                while (chain):
                    
                    v1 = GetItemAlone(chain,',').strip()

                    chain=chain[(len(v1)):]
                    if v1.endswith(',') or v1.endswith(';'):
                        v1 = v1[:-1]
                        
                    #A=B=C=8,A=1
                    if '=' in v1:
                        t1 = []
                        while v1:
                            t3 = GetItemAlone(v1,'=')
                            v1 = v1[(len(t3)):]
                            if t3.endswith('='):
                                t3 = t3[:-1]
                            t1.append(t3.strip())

                        l = len(t1) - 2
                        while ( l >= 0 ):
                            self.VarManage(allow_recursion,vars,func,t1[l],t1[l+1])
                            l = l - 1
                    #A,B,C
                    else:
                        self.VarManage(allow_recursion,vars,func,v1,None)
                                    
                continue
  
            #break
            if chain.startswith('break'):
                self.Break = True
                return
            
            #Return ?                
            if chain.startswith('return'):
                m = re.match(r'return *;', chain)
                if m:
                    self.Return = True
                    return None
                m = re.match(r'^return *([^;]+)', chain)
                if m:
                    chain = m.group(1)
                    r = self.evalJS(chain,vars,func,allow_recursion)
                    self.Return = True
                    return r              
                    

            #Pas trouve, une fonction ?
            if chain.endswith(';'):
                return self.evalJS(chain[:-1],vars,func,allow_recursion)
            
            #Non gere encore
            #print '> ' + JScode
            #raise Exception('> ERROR : can t parse >' + chain)
            
        return

    def ProcessJS(self,JScode,vars = []):
        func = []
        vars_return = []
        
        #unicode ?
        #if isinstance(JScode, unicode):
        if (False):
            out('Unicode convertion')
            JScode = unicode(JScode, "utf-8")
            self.Unicode = True
        
        #Special
        vars.append(('String',''))
        vars.append(('true',True))
        vars.append(('false',False))
        
        #Hack
        JScode = JScode.replace('$(document).ready','DOCUMENT_READY')
        JScode = JScode.replace('.length','.length()')
        
        #Start the parsing
        return self.Parse(JScode,vars,func)

        
#---------------------------------------------------------------------------------------------------------------------------------------- 

#main


# -*- coding: utf-8 -*- 
#s = "abcşiüğ"
#my_unicode_string = unicode(s, "utf-8")
#print my_unicode_string[3].encode('utf-8')
#print ord(my_unicode_string[3])

JP = JsParser()
JP.AddHackVar('aQydkd1Gbfx',"u'@D||&FBgHO`cfggghaddOb`]bg]_]_OE59ys33I")
JP.AddHackVar('aQydkd1Gbf',"u'@D||&FBgHO`cfggghaddOb`]bg]_]_OE59ys33)")
print 'Return : ' + str(JP.ProcessJS(JScode))
print 'Result :'  + JP.GetVarHack('streamurl')
