#coding: utf-8
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

import re
import types
import time

REG_NAME = '[\w]+'
REG_OP = '[\/*-+\(\)\{\}\[\]<>\| ]+'

JScode ="""
(function(s, opt_attributes, key, pairs, i, params) {
  /** @type {function (new:String, *=): string} */
  i = String;
  if (!"".replace(/^/, String)) {
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
})('(0(){4 1="5 6 7 8";0 2(3){9(3)}2(1)})();', 10, 10, "function|b|something|a|var|some|sample|packed|code|alert".split("|"), 0, []);
"""


JScode3 ="""
eval(function(p,a,c,k,e,r){e=String;if(!''.replace(/^/,String)){while(c--)r[c]=k[c]||c;k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('(0(){4 1="5 6 7 8";0 2(3){9(3)}2(1)})();',10,10,'function|b|something|a|var|some|sample|packed|code|alert'.split('|'),0,[]));
"""



JScode2 ="""
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
def out(string):
    print str(string)
    
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
    
def MySplit(string,char):
    r = []
    l = len(string)
    i = 0
    chain = 0
    p = 0
    e = ''
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
            #i = i + 1
        else:    
            e = e + c
            
        i = i + 1
        
    r.append(e.strip())
    return r

class JSBuffer(object):
    def __init__(self):
        self.type = ''
        self.op = ''
        self.buffer = ''
        
    def SetOp(self,op):
        self.op = self.op + op
        
    def AddValue(self,value):
        if not self.type:
            self.type = self.CheckType(value)
            self.buffer = value
            return
        elif not (self.type == self.CheckType(value)):
            print '>' + str(self.buffer) + ' ' + str(type(self.buffer))
            print '>' + str(value) + ' '+ str(type(value))
            raise Exception("Values or not same type")
            
        if not self.op:
            print '>' + self.buffer
            print '>' + value
            raise Exception("Missing operator")
            
        if self.type == 'String':
            if self.op == '+':
                self.buffer = self.buffer + value
        if self.type == 'Numeric':    
            r = re.search('^[0-9+-.\(\)<>&=%!]+$',str(self.buffer))
            if r:
                v = str(self.buffer) + self.op + str(value)
                self.buffer = self.SafeEval(v)

        self.op = ''
        
    def CheckType(self,value):
        if (isinstance(value, types.StringTypes)):
            return 'String'
        if isinstance(value, ( bool ) ):
            return 'Bool'
        if isinstance(value, ( int, long ) ):
            return 'Numeric'
        if type(value) in [list,tuple]:
            return 'Array'
        return 'Unknow'
        
    def GetBuffer(self):
        return self.buffer
        
    #WARNING : Take care if you edit this function, eval is realy unsafe.
    #better to use ast.literal_eval() but not implemented before python 3
    def SafeEval(self,str):
        f = re.search('[^0-9+-.\(\)<>=&%!]',str)
        if f:
            raise Exception ('Wrong parameter to Eval : ' + str)
            return 0
        str = str.replace('!','not ')
        #str = str.replace('=','==')
        
        return eval(str)
    
class JsParser(object):
    def __init__(self):
        self.HackVars = []
        self.debug = False
        self.LastEval = ''
        self.SpecialOption = ''
    
    def AddHackVar(self,name, value):
        self.HackVars.append((name,value))
        
    def GetVarHack(self,name):
        return self.GetVar(self.HackVars,name)
    
    #Need to take care at chain var with " and '
    def ExtractFirstchain(self,string):
        if len(string.strip()) == 0:
            return '',0
    
        l = len(string)
        string = string + ' ' #To prevent index out of range, hack
        
        i = 0
        p = 0 #parenbthese
        a = 0 #accolade
        b = 0 #bracket
        f = False #fonction ?
        com = False
        
        stringR = ''
        
        while (l > i):

            #ignore comment
            if string[i:(i+2)] == '/*':
                com = True
            if (com):
                if string[i:(i+2)] == '*/':
                    com = False
                    i = i + 2
                else:
                    i = i + 1
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
                               
            #Dans tout les cas les parenthses doivent etre fermees, ainsi que les crochet
            if (p == 0) and (b ==0):
                #Si on rencontre un ; par defaut
                if (ch == ';') and not (f):
                    #Ok, accolade fermees aussi, c'est tout bon
                    if(a == 0):
                        i = i + 1
                        return stringR,i
                    #Accoloade non fermee, c'est une fonction
                    else:
                        f = True

                #si c'est une fonction et l'accolade fermee
                if (f) and (a == 0):
                    #quel est le caractere suivant ?
                    j = i
                    while (string[j].isspace()) and(l > j):
                        j = j + 1
                    #Si parenthese on repart
                    if string[j] == '(':
                        continue
                    
                    # Mal formated string ?
                    # Sometime, coder forget the last ; before the }
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
                    
                        
                    return stringR,i+1
                    
            i = i + 1
        
        #chaine bugguée ?
        if ';' not in string:
            out('ERROR Extract chain without ";" > ' + string )
            
        raise Exception("Can't extract chain " + string)
           
    def GetBeetweenParenth(self,str):
        #Search the first (
        s = str.find('(')
        if s == -1:
            return 0,''
            
        n = 1
        e = s + 1
        while (n > 0) and (e < len(str)):
            c = str[e]
            if c == '(':
                n = n + 1
            if c == ')':
                n = n - 1
            e = e + 1
            
        s = s + 1
        e = e - 1
        return e,str[s:e]
        
    def GetBeetweenCroch(self,str):
        #Search the first (
        s = str.find('{')
        if s == -1:
            return 0,''
            
        n = 1
        e = s + 1
        while (n > 0) and (e < len(str)):
            c = str[e]
            if c == '{':
                n = n + 1
            if c == '}':
                n = n - 1
            e = e + 1
            
        s = s + 1
        e = e - 1
        return e,str[s:e]


        
    def CheckTrueFalse(self,string):
        print type(string)
        if isinstance(string, ( bool ) ):
            if string == True:
                return True
            if string == False:
                return False
        if string == 'True':
            return True
        if string == 'False':
            return False            
        if (isinstance(string, types.StringTypes)):
            if not string == '':
                return True
        if isinstance(string, ( int, long ) ):
            if not (string == -1):
                return True
        return False
        
    def AlphaConcat(self,string):
        #if string.startswith('"'):
        #    string = string[1:]
        #if string.endswith('"'):
        #    string = string[:-1]
        string =string.replace('"+"','')  
        return string
        
    def evalJS(self,JScode,vars,func,allow_recursion):
    
        if allow_recursion < 0:
            raise Exception('Recursion limit reached')
            
        allow_recursion = allow_recursion - 1

        #plus que la chaine a evaluer
        #JScode = JScode.replace(' ','')
        JScode = JScode.strip()
        
        debug = JScode
        

        out( '-------------')
        out( 'A evaluer >'+ JScode)
            
        #********************************************************
        
        InterpretedCode = JSBuffer()
        
        while (len(JScode)>0):
            c = JScode[0]
            Last_chain = ''
            
            #print 'InterpretedCode > ' + InterpretedCode
            #print 'JScode > ' + JScode

            #Alpha chain
            if c == '"':
                e = JScode[1:].find('"') + 2
                if e == 1:
                    raise Exception("Can't eval chain " + JScode)
                Last_chain = JScode[0:e]
                #if it's not the form "abc".err
                if not GetNextchar(JScode,e - 1) == '.':
                    InterpretedCode.AddValue(JScode[0:e])
                    JScode = JScode[(e):]
                    continue
            if c == "'":
                e = JScode[1:].find("'") + 2
                if e == 1:
                    raise Exception("Can't eval chain " + JScode)
                Last_chain = JScode[0:e]
                #if it's not the form "abc".err
                if not GetNextchar(JScode,e - 1) == '.':
                    InterpretedCode.AddValue(JScode[0:e])
                    JScode = JScode[(e+1):]
                    continue
            #numeric chain
            r = re.search('(^[0-9]+)',JScode)
            if r:
                InterpretedCode.AddValue(int(JScode[0:r.end()]))
                JScode = JScode[(r.end()):]
                continue
            #parentheses
            if c == "(":
                pos2,c2 = self.GetBeetweenParenth(JScode)
                v = self.evalJS(c2,vars,func,allow_recursion)
                #print '*******' + GetNextchar(JScode,pos2)
                InterpretedCode.AddValue(v)
                JScode = JScode[(pos2 + 1):]
                continue
                
            #hack
            r = re.search('^\$\("#([\w]+)"\)\.text\(\)',JScode)
            if r:
                InterpretedCode.AddValue(self.GetVar(self.HackVars,r.group(1)))
                JScode = JScode[(r.end()):]
                continue
                
            #useless code
            if JScode.startswith('new '):
                JScode = JScode[4:]
                continue           
            
                
            name = ''            
            #Extraction info
            m = re.search(r'^(?:((?:"[^"]*")|(?:[\w]+))\.)*([\w]+) *\(', JScode,re.DOTALL)
            #Syntax > aaaaaa.bbbbbb(cccccc) ou bbbb(cccc) ou "aaaa".bb(ccc)
            if m:
                name == ''
                string = ''
                if m.group(1):
                    if m.group(1).startswith('"'):
                        self.SetVar(vars,'TEMPORARY_VARS',self.RemoveGuil(m.group(1)))
                        name = 'TEMPORARY_VARS'
                    else:
                        name = m.group(1)
                function = m.group(2)
                pos3,arg = self.GetBeetweenParenth(JScode[(m.end()-1):])

                print 'DEBUG EVAL > Name: ' + name + ' arg: ' + arg + ' function: ' + function
             
                #fonction defined ?
                if function:
                    
                    out( "> function : " + function + ' arg=' + arg)
                    
                    #Def function ?
                    fe = self.IsFunc(vars,func,function)
                    if fe:
                        out('> def fonvtion : ' + function)
                        n,p,c = fe
                        a = MySplit(arg,',')
                        
                        a2 = []
                        for i in a:
                            vv = self.evalJS(i,vars,func,allow_recursion)
                            a2.append(self.RemoveGuil(vv))
                        
                        if (len(p) > 0) and (len(a2)>0):
                            nv = tuple(zip(p, a2))
                            for z,w in nv:
                                self.SetVar(vars,z,w)

                        v = self.Parse(c,vars,func,allow_recursion)
                        if v:
                            InterpretedCode.AddValue(v)
                            
                        JScode = JScode[(len(m.group(0)) + pos3 + 0):]
                        continue                   
   
                    #Native
                    #charCodeAt
                    if function=='charCodeAt':
                        s = self.GetVar(vars,name)
                        v = self.evalJS(arg,vars,func,allow_recursion)
                        InterpretedCode.AddValue(ord(s[int(v)]))
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #length
                    if function=='length':
                        s = self.GetVar(vars,name)
                        InterpretedCode.AddValue(len(s))
                        JScode = JScode[(len(m.group(0)) + pos3):]
                        continue
                    #Substring
                    if function=='substring':
                        s = self.GetVar(vars,name)
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
                        s = self.GetVar(vars,name)
                        #out('Join : avec ' + str(t) + 'var = ' + str(s))
                        print t
                        print s
                        print vars
                        InterpretedCode.AddValue(t.join(s))
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #replace
                    #print re.sub('1',lambda m: f(m.group()),s)
                    if function=='replace':
                        arg = MySplit(arg,',')
                        t1 = arg[0]
                        if '"' in t1:
                            t1 = self.evalJS(t1,vars,func,allow_recursion)
                        t2 = self.evalJS(arg[1],vars,func,allow_recursion)
                        
                        s = self.GetVar(vars,name)
                        #regex mode ?
                        if t1.startswith('/'):
                            jr = re.findall(t1.split('/')[1], s)
                            i = 0
                            for k in jr:
                                if t2.startswith('"'):
                                    t2 = self.RemoveGuil(t2)
                                    s = s.replace(k,t2)
                                else:
                                    #hack
                                    v = self.evalJS(t2+'('+ k + ')',vars,func,allow_recursion)
                                    print k + ' > ' + v
                                    s = s.replace(k,v)
                                    i = i + 1
                            InterpretedCode.AddValue( s )
                        #String mode
                        else:
                            t1 = self.evalJS(t1,vars,func,allow_recursion)
                            InterpretedCode.AddValue( s.replace(t1,t2))
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #slice
                    if function=='slice':
                        s = self.GetVar(vars,name)
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
                        s = self.GetVar(vars,name)
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
                        print vars
                        raise Exception("DEBUG")
                        
                    raise Exception("Unknow fonction : " + function)

                
            #variables
            #Syntaxe aaaa[bbb]+ ou aaa+
            r = re.search('^(' + REG_NAME + ')(?:\[([^\]]+)\])*(?:' + REG_OP + '|$)',JScode)
            if r:
                v = r.group(1)
                t = ''
                pos7 = len(r.group(1))

                if r.group(2):
                    t = r.group(2)
                    out("> var " + v + '[' + t + ']')
                    pos7 = pos7 + len(r.group(2)) + 2
                else:
                    out("> var " + v)

                if self.IsVar(vars,r.group(1)):

                    v = self.GetVar(vars,r.group(1))

                    if t:
                        t2 = self.evalJS(t,vars,func,allow_recursion)
                        v = v[int(t2)]
                    InterpretedCode.AddValue(v)
                    
                    JScode = JScode[pos7:]
                    continue
                    
                raise Exception("Can't find var " + r.group(1))

            #variables operation a++ or a--?
            m = re.search(r'^(' + REG_NAME + ')\+\+', JScode)
            if m:
                v = int(self.GetVar(vars,m.group(1))) + 1
                self.SetVar(vars,m.group(1),v)
                InterpretedCode.AddValue(v)
                JScode = JScode[(len(m.group(0))):]
                continue
            m = re.search(r'^(' + REG_NAME + ')\-\-', JScode)
            if m:
                v = int(self.GetVar(vars,m.group(1))) - 1
                self.SetVar(vars,m.group(1),v)
                InterpretedCode.AddValue(v)
                JScode = JScode[(len(m.group(0))):]                
                continue

            #TODO hack inside
            if c == '.':
                JScode = InterpretedCode.buffer + JScode
                InterpretedCode.type = ''#to reset it
                continue
                
            #Space to remove
            if c == ' ':
                JScode = JScode[1:]
                continue
                
            #Simple operation
            if c in '+<>-*/=&%|!':
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
            out("Can't eval string :" + JScode)
            out("Last eval : " + str(self.LastEval))
            print c
            print debug
            raise Exception("Can't Eval chain : " + JScode)

        #Si c'est une liste on retourne direct
        #if type(InterpretedCode) in [list,tuple]:
        #    return InterpretedCode


        #Bool operation
        #if ('True' in InterpretedCode) or ('False' in InterpretedCode):
        #    InterpretedCode = InterpretedCode.replace('True','1')
        #    InterpretedCode = InterpretedCode.replace('False','0')
        #    InterpretedCode = InterpretedCode.replace('&&','&')
        #    InterpretedCode = InterpretedCode.replace('||','|')
        #    InterpretedCode = str(self.SafeEval(InterpretedCode))
        #    InterpretedCode = InterpretedCode.replace('1','True')
        #    InterpretedCode = InterpretedCode.replace('0','False')

    
 #       if (InterpretedCode == True) or (InterpretedCode == False):
 #               InterpretedCode = str(InterpretedCode)
        
        InterpretedCode2 = InterpretedCode.GetBuffer()
        
        #hack
        if InterpretedCode2 == '!""':
            InterpretedCode2 = 'True'
        if InterpretedCode2 == '[]':
            InterpretedCode2 = []       

        out( 'Evalue > '+ str(InterpretedCode2) + " type " + str(type(InterpretedCode2)) )
        out( '-------------')
        
        self.LastEval = InterpretedCode2
        
        return InterpretedCode2
        
    def RemoveGuil(sel,string):
        if not (isinstance(string, types.StringTypes)):
            return string
        if string.startswith('"') and string.endswith('"'):
            return string[1:-1]
        return string
        
    def GetVar(self,var,variable):
    
        variable = variable.strip()
    
        for j in var:
            if j[0] == variable:
                return j[1]
        raise Exception('Variable not defined: ' + variable)
            
    def SetVar(self,var,variable,value,i = 0):

        variable = variable.strip()

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
                #Numeric
                else:
                    var[var.index(j)] = (variable,value)

                return
                
        #New var
        var.append((variable,value))
    
    def IsVar(self,var,variable):
        for j in var:
            if j[0] == variable:
                return True
        return False
        
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
             
        param = MySplit(parametres,',')
        
        out('Function ' + name + ' ' + str(param))
        #out('data ' + str(data))

        pos = 0
        replac = ''
        
        #self invoked ? Not workign yet
        if selfinvoked:
            pos2,content = self.GetBeetweenCroch(data)
            pos = pos2 + 2
            func.append((name,param,content.lstrip()))
            
            data = data[pos:] 
            
        else:
            pos2,content = self.GetBeetweenCroch(data)
            pos = pos2 + 2
            func.append((name,param,content.lstrip()))

            data = data[pos:] 
            
        #param in function ?
        if len(data)> 0:
            r = name + data
            if not data.endswith(';'):
                r = r + ';'
            replac = r

            pos = pos + len(data)
            
        return replac, pos , name
        
    def Parse(self,JScode,vars,func,allow_recursion=50):
    
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
            chain = chain.lstrip()
             
            #out('> ' + chain)
            #actual special option
            
            
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
            print chain
            print 'F++++++++++++++++++'
            
            #hack ?
            m = re.search(r'^\$\("#([^"]+)"\)\.text\(([^\)]+)\);', chain)
            if m:
                out( '> hack ' + m.group(0) + ' , variable est ' + m.group(1))
                self.SetVar(self.HackVars,m.group(1),self.GetVar(vars,m.group(2)))
                continue
  
            name = ''            
            #Extraction info
            m = re.search(r'^([\w]+) *\(', chain,re.DOTALL)
            #Syntax > aaaaa(bbbbb) .........
            if m:
                name = m.group(1)
                pos3,arg = self.GetBeetweenParenth(chain[(m.end()-1):])
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
                    self.Parse(arg,vars,func,allow_recursion)
                    continue

                #For boucle ?
                if name == 'for':
                    arg = arg.split(';')
                    v = arg[0] + ';'
                    t = arg[1]
                    i = arg[2] + ';'
                    f = code
                    if GetFirstChar(f) =='{':
                        f = self.GetBeetweenCroch(f)[1]
                    
                    #out('> Boucle for : Var=' + v + ' test=' + t + ' incrementation=' + i + ' code=' + f)
                    
                    #init var              
                    self.Parse(v,vars,func,allow_recursion)
                    #loop
                    while (self.CheckTrueFalse(self.evalJS(t,vars,func,allow_recursion))):
                        #fonction
                        self.Parse(f,vars,func,allow_recursion)
                        #incrementation
                        self.Parse(i,vars,func,allow_recursion)

                    continue
                    
                #Boucle if
                if name == 'if':
                    t = arg
                    f = code
                    e = ''
                    
                    if GetFirstChar(f) =='{':
                        f = self.GetBeetweenCroch(f)[1]

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
                   
                if (False):
                    #fonction           
                    if self.IsFunc(vars,func,name):
                        fe = self.IsFunc(vars,func,name)
                        if fe:
                            out( '> Fonction : name=' + name)
                        
                            n,p,c = fe
                            a = MySplit(arg,',')
                            
                            a2 = []
                            for i in a:
                                a2.append(self.evalJS(i,vars,func,allow_recursion))
                            
                            if (len(p) > 0) and (len(a2)>0):
                                nv = tuple(zip(p, a2))
                                for z,w in nv:
                                    self.SetVar(vars,z,w)
                                out( '> Fonction : arg=' + str(nv))

                            out( '> Fonction : code=' + c)
                            self.Parse(c,vars,func,allow_recursion)
                            continue

            #Variable operation/creation ?
            m = re.search(r'^(?:var )*([^\s\[]+) *= *(.+) *;$',chain,re.DOTALL)
            if m:
                variable = m.group(1)
                value = m.group(2)
                
                out( '> Variable Creation => ' + variable + ' = ' + value)
                
                #chain
                m = re.match(r'^"([^"]+)"$', value)
                if m:
                    self.SetVar(vars,variable,value)
                #list
                elif value.startswith('[') and  value.endswith(']'):
                    content6 = value[1:-1]
                    v = self.evalJS(content6,vars,func,allow_recursion)
                    self.SetVar(vars,variable,[])
                    self.SetVar(vars,variable,v,0)
                #number
                elif re.match(r'([0-9.-]+)', value):
                    self.SetVar(vars,variable,int(value))
                #to eval
                else:
                    v = self.evalJS(value,vars,func,allow_recursion)
                    self.SetVar(vars,variable,v)
                continue
                
            #modification
            m = re.search(r'^([\w]+)(?:\[([^\]]+)\])*\s*=([^;]+);$', chain,re.DOTALL)
            if m:
                v = self.evalJS(m.group(3),vars,func,allow_recursion)

                if not m.group(2):
                    out( '> Variable Modification => ' + m.group(1) + ' = ' + m.group(3))
                    self.SetVar(vars,m.group(1),v)
                else:
                    out( '> Variable Modification => ' + m.group(1) + '[' + m.group(2) + ']' +' = ' + m.group(3))
                    i = self.evalJS(m.group(2),vars,func,allow_recursion)
                    self.SetVar(vars,m.group(1),v,i)
                continue
   
            #Return ?
            if chain.startswith('return '):
                m = re.match(r'return *;', chain)
                if m:
                    return ''
                m = re.match(r'^return ([^;]+)', chain)
                if m:
                    chain = m.group(1)
                    print 'fini'
                    return self.evalJS(chain,vars,func,allow_recursion)
                    
            #operation ?
            m = re.search(r'^(' + REG_NAME + ')\+\+;', chain)
            if m:
                v = int(self.GetVar(vars,m.group(1))) + 1
                self.SetVar(vars,m.group(1),v)
                continue
            m = re.search(r'^(' + REG_NAME + ')\-\-;', chain)
            if m:
                v = int(self.GetVar(vars,m.group(1))) - 1
                self.SetVar(vars,m.group(1),v)
                continue
                    
            
            #Pas trouve, une fonction ?
            self.evalJS(chain,vars,func,allow_recursion)
            
            #Non gere encore
            #print '> ' + JScode
            #raise Exception('> ERROR : can t parse >' + chain)
            
        return

    def ProcessJS(self,JScode,vars = []):
        func = []
        vars_return = []
        
        #Special
        vars.append(('String',''))
        
        #Hack
        JScode = JScode.replace('$(document).ready','DOCUMENT_READY')
        JScode = JScode.replace('.length','.length()')
        
        #Start the parsing
        self.Parse(JScode,vars,func)

        
#---------------------------------------------------------------------------------------------------------------------------------------- 

#main

JP = JsParser()
JP.AddHackVar('aQydkd1Gbfx',"u'@D||&FBgHO`cfggghaddOb`]bg]_]_OE59ys33I")
JP.AddHackVar('aQydkd1Gbf',"u'@D||&FBgHO`cfggghaddOb`]bg]_]_OE59ys33)")
JP.ProcessJS(JScode)
print 'Result :'  + JP.GetVarHack('streamurl')
