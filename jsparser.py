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

import re
import types
import time

REG_NAME = '[\w]+'
REG_OP = '[\/*-+\(\)\{\}\[\]<>\|]+'

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
})('(0(){4 1="5 6 7 8";0 2(3){9(3)}2(1)})();', 10, 10, "function|b|something|a|var|some|sample|packed|code|alert".split("|"), 0, {});
"""


JScode3 ="""
eval(function(p,a,c,k,e,r){e=String;if(!''.replace(/^/,String)){while(c--)r[c]=k[c]||c;k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('(0(){4 1="5 6 7 8";0 2(3){9(3)}2(1)})();',10,10,'function|b|something|a|var|some|sample|packed|code|alert'.split('|'),0,{}));
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
    
def MySplit(string,char):
    r = []
    l = len(string)
    i = 0
    chain = 0
    e = ''
    while (l > i):
        c = string[i]
        if c == '"':
            chain = 1-chain
            
        if (c == char) and (chain == 0):
            r.append(e.strip())
            e = ''
            i = i + 1
        else:    
            e = e + c
            
        i = i + 1
        
    r.append(e.strip())
    return r

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
            #Dans tout les cas les parenthses doivent etre fermees
            if (p == 0):
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
                    #on repart
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
            return ''
            
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
            return ''
            
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

    #WARNING : Take care if you edit this function, eval is realy unsafe.
    #better to use ast.literal_eval() but not implemented before python 3
    def SafeEval(self,str):
        f = re.search('[^0-9+-.\(\)<>=&%!]',str)
        if f:
            out ('Wrong parameter to Eval : ' + str)
            return 0
        #out('SafeEval : ' + str)
        
        str = str.replace('!','not')
        
        return eval(str)
        
    def CheckTrueFalse(self,string):
        if string == 'True':
            return True
        if string == '':
            return False
        if not (string == 0):
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
    
        #https://nemisj.com/python-api-javascript/

        #plus que la chaine a evaluer
        JScode = JScode.replace(' ','')
        
        debug = JScode
        

        out( '-------------')
        out( 'A evaluer >'+ JScode)
            
        #********************************************************
        
        InterpretedCode = ''
        
        while (len(JScode)>0):
            c = JScode[0]
            
            #print 'InterpretedCode > ' + InterpretedCode
            #print 'JScode > ' + JScode

            #Alpha chain
            if c == '"':
                e = JScode[1:].find('"') + 2
                if e == 1:
                    raise Exception("Can't eval chain " + JScode)
                InterpretedCode = InterpretedCode + JScode[0:e]
                JScode = JScode[(e):]
                continue
            if c == "'":
                e = JScode[1:].find("'") + 2
                if e == 1:
                    raise Exception("Can't eval chain " + JScode)
                InterpretedCode = InterpretedCode + JScode[0:e]
                JScode = JScode[(e+1):]
                continue
            #numeric chain
            r = re.search('(^[0-9]+)',JScode)
            if r:
                InterpretedCode = InterpretedCode + JScode[0:r.end()]
                JScode = JScode[(r.end()):]
                continue
            #parentheses
            if c == "(":
                c2 = self.GetBeetweenParenth(JScode)[1]
                v = self.evalJS(c2,vars,func,allow_recursion)
                InterpretedCode = InterpretedCode + v
                JScode = JScode[(len(c2) + 2):]
                continue
                
            #hack
            r = re.search('^\$\("#([\w]+)"\)\.text\(\)',JScode)
            if r:
                InterpretedCode = InterpretedCode + self.FormatVarOutput(self.GetVar(self.HackVars,r.group(1)))
                JScode = JScode[(r.end()):]
                continue            
                
            #use precedent result ?
            if c == '.':
                #Make a false var
                self.SetVar(vars,'LAST_RESULT',InterpretedCode)
                #And a small rollback
                JScode = 'LAST_RESULT' + JScode
                InterpretedCode = ''
                
            name = ''            
            #Extraction info
            m = re.search(r'^(?:([\w]+)\.)*([\w]+) *\(', JScode,re.DOTALL)
            #Syntax > aaaaaa.bbbbbb(cccccc)
            if m:
                name == ''
                if m.group(1):
                    name = m.group(1)
                function = m.group(2)
                pos3,arg = self.GetBeetweenParenth(JScode[(m.end()-1):])

                print 'DEBUG EVAL > Name: ' + name + ' arg: ' + arg + ' function: ' + function
             
                #fonction defined ?
                if function:
                    
                    out( "> function : " + function +' arg=' + arg)
                    
                    #Def function ?
                    fe = self.IsFunc(func,function)
                    if fe:
                        n,p,c = fe
                        arg = arg.split(',')
                        
                        if (len(p) > 0) and (len(arg)>0):
                            nv = tuple(zip(p, arg))
                            vars.extend(nv)

                        v = self.Parse(c,vars,func,allow_recursion)
                        if v:
                            InterpretedCode = InterpretedCode + v
                            
                        JScode = JScode[(len(m.group(0)) + pos3 + 0):]
                        continue
   
                    #Native
                    #charCodeAt
                    if function=='charCodeAt':
                        s = self.GetVar(vars,name)
                        v = self.evalJS(arg,vars,func,allow_recursion)
                        InterpretedCode = InterpretedCode + str(ord(s[int(v)]))
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #length
                    if function=='length':
                        s = self.GetVar(vars,name)
                        InterpretedCode = InterpretedCode + str(len(s))
                        JScode = JScode[(len(m.group(0)) + pos3):]
                        continue
                    #Substring
                    if function=='substring':
                        s = self.GetVar(vars,name)
                        arg = arg.split(',')
                        p1 = self.evalJS(arg[0],vars,func,allow_recursion)
                        if len(arg)> 1:
                            p2 = self.evalJS(arg[1],vars,func,allow_recursion)
                            InterpretedCode = InterpretedCode + '"' + s[ int(p1) : int(p2) ] + '"'
                        else:
                            InterpretedCode = InterpretedCode + '"' + s[ int(p1) :] + '"'
                        #out('Substring : var = ' + s + ' index=' + str(p1) )
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #join
                    if function=='join':
                        t = arg.replace('"','').replace("'","")
                        s = self.GetVar(vars,name)
                        #out('Join : avec ' + str(t) + 'var = ' + str(s))
                        InterpretedCode = InterpretedCode + '"' + t.join(s) + '"'
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #replace
                    if function=='replace':
                        arg = arg.split(',')
                        t1 = arg[0].replace('"','').replace("'","")
                        t2 = arg[1].replace('"','').replace("'","")
                        s = self.GetVar(vars,name)
                        InterpretedCode = InterpretedCode + '"' + s.replace(t1,t2) + '"'
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
                        InterpretedCode = InterpretedCode + sr
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #string.fromCharCode
                    if (function=='fromCharCode') and (name=='String'):
                        v = self.evalJS(arg,vars,func,allow_recursion)
                        #out('StringFromCharcode ' +  r.group(1) + '=' + str(v))
                        InterpretedCode = InterpretedCode + '"' + chr(int(v)) + '"'
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #split
                    if function=='split':
                        arg = arg.replace('"','').replace("'","")
                        s = self.GetVar(vars,name)
                        InterpretedCode = InterpretedCode + '"' + s.split(arg) + '"'
                        vv(mm)
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                        
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

                    v = self.FormatVarOutput(self.GetVar(vars,r.group(1)))
                    
                    if t:
                        t2 = self.evalJS(t,vars,func,allow_recursion)
                        v = v[int(t2)]
                        print '----' + t2 + ' '+ v
                        print vars
                    
                    InterpretedCode = InterpretedCode + v
                    JScode = JScode[pos7:]
                    continue
                    
                raise Exception("Can't find var " + r.group(1))

            #variables operation a++ or a--?
            m = re.search(r'^(' + REG_NAME + ')\+\+', JScode)
            if m:
                v = str(int(self.GetVar(vars,m.group(1))) + 1)
                self.SetVar(vars,m.group(1),v)
                InterpretedCode = InterpretedCode + str(v)
                JScode = JScode[(len(m.group(0))):]
                continue
            m = re.search(r'^(' + REG_NAME + ')\-\-', JScode)
            if m:
                v = str(int(self.GetVar(vars,m.group(1))) - 1)
                self.SetVar(vars,m.group(1),v)
                InterpretedCode = InterpretedCode + str(v)
                JScode = JScode[(len(m.group(0))):]                
                continue                
                
            #Simple operation
            if c in '+<>-*/=&%!':
                InterpretedCode = InterpretedCode + c
                JScode = JScode[1:]
                continue
                    
            # Not found part
            # We will make another turn
            out("Can't eval string :" + JScode)
            out("Last eval : " + self.LastEval)
            print c
            print debug
            raise Exception("Can't Eval chain : " + JScode)


        #Bool operation
        if ('True' in InterpretedCode) or ('False' in InterpretedCode):
            InterpretedCode = InterpretedCode.replace('True','1')
            InterpretedCode = InterpretedCode.replace('False','0')
            InterpretedCode = InterpretedCode.replace('&&','&')
            InterpretedCode = InterpretedCode.replace('||','|')
            InterpretedCode = str(self.SafeEval(InterpretedCode))
            InterpretedCode = InterpretedCode.replace('1','True')
            InterpretedCode = InterpretedCode.replace('0','False')
            
        
        #Numeric calculation
        r = re.search('^[0-9+-.\(\)<>&=%!]+$',InterpretedCode)
        if r:
            InterpretedCode = str(self.SafeEval(InterpretedCode))
    
        #Alphanumeric concatenation
        InterpretedCode = self.AlphaConcat(InterpretedCode)
        #InterpretedCode = InterpretedCode.replace('+','')
        

        out( 'Evalue >'+ InterpretedCode )
        out( '-------------')
        
        self.LastEval = InterpretedCode
        
        return InterpretedCode
        
    def FormatVarOutput(sel,variable):
        if (isinstance(variable, types.StringTypes)):
            return '"' + variable + '"'
        elif type(variable) in [list,tuple]:
            return variable
        else:
            return str(variable)    
        
    def GetVar(self,var,variable):
    
        variable = variable.strip()
    
        for j in var:
            if j[0] == variable:
                    return j[1]
        raise Exception('Variable not defined: ' + variable)
            
    def SetVar(self,var,variable,value,i = 0):

        variable = variable.strip()

        #Array
        if value == '[]':
            value = []
        else:
            try:
                #Alpha
                r = re.match(r'^"(.+)"$', value)
                if r:
                    value = r.group(1)
                #Numeric
                else:
                    value = int(value)
            except:
                pass
            
        #Existing var ?
        for j in var:
            if j[0] == variable:

                #vars ?
                if (isinstance(var[var.index(j)][1], types.StringTypes)):
                    var[var.index(j)] = (variable,value)
                #Array
                elif type(var[var.index(j)][1]) in [list,tuple]:

                    Listvalue = var[var.index(j)][1]
                    
                    print Listvalue
                    
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
        
    def IsFunc(self,Func,name):
        for j in Func:
            if j[0] == name:
                return j
        return False
    
    def ReplaceVar(self,JScode):
        modif = True
        while (modif):
            modif = False
            for j in self.Var:
                if j[0] in JScode:
                    JScode = JScode.replace(j[0],'(' + j[1]+ ')')
                    modif = True
                    
        return JScode
        
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
                if m.group(2):
                    name = m.group(2)
                else:
                    n0 = 0
                    while self.IsFunc(func,'AnonymousFunc' + str(n0)):
                        n0=n0+1
                    name = 'AnonymousFunc' + str(n0)
                    
                if (self.SpecialOption):
                    if self.SpecialOption.split('=')[0] == 'Namefunc':
                        name = self.SpecialOption.split('=')[1]
                    self.SpecialOption = ''
                     
                param = MySplit(m.group(3),',')
                
                out('Function ' + name + ' ' + str(param))

                #self invoked ? Not workign yet
                if m.group(1):
                    pos,content = self.GetBeetweenCroch(chain)
                    pos = pos + 1
                    out('content >' + content)
                    func.append((name,param,content.lstrip()))
                    
                    chain = chain[(pos+1):] 
                    
                else:
                    pos,content = self.GetBeetweenCroch(chain)
                    pos = pos + 1
                    out('content >' + content)
                    func.append((name,param,content.lstrip()))

                    chain = chain[pos:] 
                    
                #param in function ?
                if len(chain)> 0:
                    r = name + chain
                    if not chain.endswith(';'):
                        r = r + ';'
                    out('Self invoked > ' + r)
                    out('param inside ' + chain)
                    JScode = JScode[:Startoff]+ r + JScode[Endoff:]

                else:
                    JScode = JScode[:Startoff]+ JScode[Endoff:]
                    posG = Startoff
                    

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
                    
                #fonction           
                if self.IsFunc(func,name):
                    fe = self.IsFunc(func,name)
                    if fe:
                        out( '> Fonction : name=' + name)
                    
                        n,p,c = fe
                        a = MySplit(arg,',')
                        
                        a2 = []
                        for i in a:
                            a2.append(self.evalJS(i,vars,func,allow_recursion))
                        
                        if (len(p) > 0) and (len(a2)>0):
                            nv = tuple(zip(p, a2))
                            vars.extend(nv)
                            out( '> Fonction : arg=' + str(nv))

                        out( '> Fonction : code=' + c)
                        self.Parse(c,vars,func,allow_recursion)
                        continue

            #Variable operation/creation ?
            m = re.search(r'^(?:var )*([^\s\[]+) *= *(.+) *;$', chain)
            if m:
                variable = m.group(1)
                value = m.group(2)
                
                if value == 'String':
                    value = '""'
                
                out( '> Variable Creation => ' + variable + ' = ' + value)
                print chain
                
                #chain
                m = re.match(r'^"([^"]+)"$', value)
                if m:
                    self.SetVar(vars,variable,value)
                #list
                elif value == '[]':
                    self.SetVar(vars,variable,'[]')
                #number
                elif re.match(r'([0-9.-]+)', value):
                    self.SetVar(vars,variable,value)
                #to eval
                else:
                    v = self.evalJS(value,vars,func,allow_recursion)
                    self.SetVar(vars,variable,v)
                continue
                
            #modification
            m = re.search(r'^([\w]+)(?:\[([^\]]+)\])*\s*=([^;]+);$', chain)
            if m:
                out( '> Variable Modification => ' + m.group(1) + ' = ' + m.group(3))
            
                v = self.evalJS(m.group(3),vars,func,allow_recursion)

                if not m.group(2):
                    self.SetVar(vars,m.group(1),v)
                else:
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
                    return self.evalJS(chain,vars,func,allow_recursion)
                    
            #operation ?
            m = re.search(r'^(' + REG_NAME + ')\+\+;', chain)
            if m:
                v = str(int(self.GetVar(vars,m.group(1))) + 1)
                self.SetVar(vars,m.group(1),v)
                continue
            m = re.search(r'^(' + REG_NAME + ')\-\-;', chain)
            if m:
                v = str(int(self.GetVar(vars,m.group(1))) - 1)
                self.SetVar(vars,m.group(1),v)
                continue
                    
            
            #Pas trouve, une fonction ?
            #self.evalJS(chain,vars,func,allow_recursion)
            
            #Non gere encore
            print '> ' + JScode
            raise Exception('> ERROR : can t parse >' + chain)
            
        return

    def ProcessJS(self,JScode,vars = []):
        func = []
        vars_return = []
        
        #Special
        vars.append(('String','""'))
        
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
