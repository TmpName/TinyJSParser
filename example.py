# -*- coding: utf-8 -*- 
#

from tinyjsparser import JsParser


JScode6 ="""

"""

JScode7 ="""

"""

JScode5 ="""
function base64_decode(r) {
  var e;
  var n;
  var i;
  var t;
  var a;
  var d;
  var o = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
  var f = 0;
  var h = 0;
  var c = [];
  if (!r) {
    return r;
  }
  r += "";
  do {
    e = (d = o.indexOf(r.charAt(f++)) << 18 | o.indexOf(r.charAt(f++)) << 12 | (t = o.indexOf(r.charAt(f++))) << 6 | (a = o.indexOf(r.charAt(f++)))) >> 16 & 255;
    n = d >> 8 & 255;
    i = 255 & d;
    c[h++] = 64 == t ? String.fromCharCode(e) : 64 == a ? String.fromCharCode(e, n) : String.fromCharCode(e, n, i);
  } while (f < r.length);
  return c.join("").replace(/\0+$/, "");
}
function ord(r) {
  var t = r + "";
  var e = t.charCodeAt(0);

  if (e >= 55296 && 56319 >= e) {
    debug();
    var o = e;
    return 1 === t.length ? e : 1024 * (o - 55296) + (t.charCodeAt(1) - 56320) + 65536;
  }

  return e;
}
function hta(r) {
  var t = r.toString();
  var e = "";
  var o = 0;
  for (;o < t.length;o += 2) {
    e += String.fromCharCode(parseInt(t.substr(o, 2), 16));
  }
  return e;
}
function strrev(r) {
  return r.split("").reverse().join("");
}
function strswpcs(r) {
  var t = "";
  var e = 0;
  for (;e < r.length;e++) {
    t += r[e].match(/^[A-Za-z]$/) ? r[e] === r[e].toLowerCase() ? r[e].toUpperCase() : r[e].toLowerCase() : r[e];
  }
  return t;
}
function decrypt(r, t) {
  var e = "";
  var o = r.substring(0, 3);
  r = r.substring(3);
  if ("36f" == o) {
    r = strrev(base64_decode(r));
  } else {
    if ("fc0" == o) {
      r = hta(strrev(r));
    } else {
      if ("663" == o) {
        r = base64_decode(strrev(r));
      } else {
        if ("53a" == o) {
          r = base64_decode(strswpcs(r));
        }
      }
    }
  }
  
  var s = 0;
  s = 0;
  for (;s < r.length;s++) {
    var n = r.substr(s, 1);
    var a = t.substr(s % t.length - 1, 1);
    n = Math.floor(ord(n) - ord(a));
    e += n = String.fromCharCode(n);
  }
  return e;
}
tt = decrypt("663=ompjS2nseJZ69JrOSmpfiIi4Rme7lHiFyHeLmIZ+lHh7hIfkp2ZmhGZV6ZmkuJq8V5lCW2dAGIe6d5e8J6iuVmmbi5obWWpZSmmXWqokupplWWZwlqpqqqn", "6" );

"""

JScode111 = """


aa = 1;
try {
aa= 3;
}
catch (err) {
  aa = 2;
}
debug();
"""

JScode1 = """

window.cc_cc_cc=''+'gItZEkCYUy';var _0x9495=['Zft','pow','tcV','EAk','QHb','charCodeAt','11|12|13|0|14|3|2|9|16|1|4|8|5|6|15|10|7','split','xXM','length','jLa','substring','aZP','dOD','Poy','write','push','dkF','text','tjf','HIZ','WyX','faz','Gcy','ucs','2|0|5|4|3|1','dhh','pQu','eMz','ZBD','Lnk','fromCharCode','DYl','4|3|0|5|6|2|1','WOa','gzw','cBV'];(function(_0x1f55fe,_0x45ae62){
var _0x3d4039=function(_0x32de24){
while(--_0x32de24){
_0x1f55fe['push'](_0x1f55fe['shift']());
}

}
;_0x3d4039(++_0x45ae62);
}
(_0x9495,191));var _0x5949=function(_0x1f55fe,_0x45ae62){
_0x1f55fe=_0x1f55fe-0;var _0x3d4039=_0x9495[_0x1f55fe];return _0x3d4039;
}
;
var _0x45ae41={
'xXM':function _0x184df4(_0x3f842b,_0x6062d8){
return _0x3f842b<_0x6062d8;
}
,'jLa':function _0x3457b8(_0x38f439,_0x457b87){
return _0x38f439*_0x457b87;
}
,'aZP':function _0x961da7(_0x56acea,_0x37f246){
return _0x56acea+_0x37f246;
}
,'dOD':function _0x2dfccb(_0x44ea34,_0xe1a069,_0x49022f){
return _0x44ea34(_0xe1a069,_0x49022f);
}
,'Poy':function _0x170b95(_0x49e0ac,_0x204c53){
return _0x49e0ac in _0x204c53;
}
,'dkF':function _0x275cbe(_0x48d105,_0x930083){
return _0x48d105(_0x930083);
}
,'tjf':function _0x2af2f3(_0x5d6e96,_0x41b58f){
return _0x5d6e96*_0x41b58f;
}
,'HIZ':function _0x1ccc24(_0x2f473c,_0xef0da5){
return _0x2f473c^_0xef0da5;
}
,'WyX':function _0x83e7c(_0x4fa9eb,_0x4fc60d){
return _0x4fa9eb^_0x4fc60d;
}
,'faz':function _0x7ec967(_0x1d25ce,_0x2d0418){
return _0x1d25ce^_0x2d0418;
}
,'Gcy':function _0x3346a1(_0x5cef79,_0x59b5a3){
return _0x5cef79%_0x59b5a3;
}
,'ucs':function _0x2f75f3(_0x3e1dda,_0x192d4c){
return _0x3e1dda<_0x192d4c;
}
,'dhh':function _0x2cc0da(_0x240c12,_0x5b7c4c){
return _0x240c12*_0x5b7c4c;
}
,'pQu':function _0xe29029(_0x45e457,_0x88979d){
return _0x45e457/_0x88979d;
}
,'eMz':function _0xe40d05(_0x5a668a,_0x2c7bd1){
return _0x5a668a<<_0x2c7bd1;
}
,'ZBD':function _0x46f50e(_0x5ba232,_0x312024){
return _0x5ba232&_0x312024;
}
,'Lnk':function _0x56789d(_0x3aa5f8,_0x3172ef){
return _0x3aa5f8!=_0x3172ef;
}
,'DYl':function _0x19031e(_0x144a2e,_0x309a9f){
return _0x144a2e>>_0x309a9f;
}
,'WOa':function _0x1689bf(_0x39dbf0,_0x42e9f7){
return _0x39dbf0 in _0x42e9f7;
}
,'gzw':function _0x5cedc0(_0x21a7ef,_0x482441){
return _0x21a7ef<_0x482441;
}
,'cBV':function _0x47a063(_0x47d3f1,_0x4bebf9){
return _0x47d3f1<<_0x4bebf9;
}
,'Zft':function _0x533710(_0x3fbb19,_0x2691b7){
return _0x3fbb19&_0x2691b7;
}
,'tcV':function _0x32ae2b(_0x524ea6,_0x3d4c00){
return _0x524ea6>=_0x3d4c00;
}
,'EAk':function _0xc9d930(_0xcaad79,_0x4bf3dc,_0x1666a8){
return _0xcaad79(_0x4bf3dc,_0x1666a8);
}
,'QHb':function _0x5b77e5(_0x177c9e,_0x33caaa){
return _0x177c9e>=_0x33caaa;
}

}
;function pt(){
try{
null[0]();
}
catch(e){
if(typeof e.stack != 'undefined'){
if(e.stack.toString().indexOf('phantomjs')!=-1){
return true
}

}
return ![];
}

}
;var _0x23d67d=_0x5949('0')[_0x5949('1')]('|'),_0x436e75=0;while(true){
switch(_0x23d67d[_0x436e75++]){

case'0':var _0x1bf6e5='';continue;
case'1':for(i=0;_0x45ae41[_0x5949('2')](i,_0x439a49[_0x5949('3')]);i+=8){
_0x41e0ff=_0x45ae41[_0x5949('4')](i,8);var _0x40b427=_0x439a49[_0x5949('5')](i,_0x45ae41[_0x5949('6')](i,8));var _0x577716=_0x45ae41[_0x5949('7')](parseInt,_0x40b427,16);with(_0x31f4aa){
if(!_0x45ae41[_0x5949('8')](_0x5949('9'),document)||!(!(function(){
//return false;
try{
if('_phantom'in window||'callPhantom'in window||'__phantomas'in window||'webdriver'in window&&1==window.a||'webdriver'in window.navigator&&1==window.navigator.a||'domAutomation'in window||'_Selenium_IDE_Recorder'in window||'__webdriver_script_fn'in document)return!0;try{
if(window.document.documentElement.getAttribute('webdriver'))return!0;var b='__webdriver_evaluate;__selenium_evaluate;__webdriver_script_function;__webdriver_script_func;__webdriver_script_fn __fxdriver_evaluate __driver_unwrapped;__webdriver_unwrapped;__driver_evaluate;__selenium_unwrapped;__fxdriver_unwrapped'.split(';'),c='_phantom __nightmare;_selenium;callPhantom;callSelenium;_Selenium_IDE_Recorder;__stopAllTimers'.split(';'),d;for(d in c)if(window[c[d]])return!0;for(j in b)if(window.document[b[j]])return!0;for(var e in window.document)if(e.match(/$[a-z]dc_/)&&window.document[e].b)return!0
}
catch(f){

}
return window.external&&window.external.toString()&&-1!=window.external.toString().indexOf('Sequentum')?!0:window.document.documentElement.getAttribute('selenium')?!0:window.document.documentElement.getAttribute('driver')?!0:null!==document.documentElement.getAttribute('selenium')?!0:null!==document.documentElement.getAttribute('webdriver')?!0:null!==document.documentElement.getAttribute('driver')?!0:!1
}
catch(f){
return!1
}

}
)())){
_0x577716=0;
}
ke[_0x5949('10')](_0x577716);
}

}
continue;
case'2':var _0x439a49=_0x5d72cd[_0x5949('5')](0,_0x41e0ff);continue;
case'3':var _0xccbe62=_0x5d72cd[_0x5949('3')];continue;
case'4':_0x3d7b02=_0x31f4aa['ke'];with(Math){
if (false) {
_0x3d7b02=[];
}

}
;continue;
case'5':_0x5d72cd=_0x5d72cd[_0x5949('5')](_0x41e0ff);continue;
case'6':var _0x439a49=0;continue;
case'7':
_0x45ae41[_0x5949('11')]($,'#lqEH1')[_0x5949('12')](_0x1bf6e5);

continue;
case'8':_0x41e0ff=_0x45ae41[_0x5949('4')](9,8);continue;
case'9':var _0x3d7b02=[];continue;
case'10':while(_0x45ae41[_0x5949('2')](_0x439a49,_0x5d72cd[_0x5949('3')])){
var _0x138ee5='5|8|0|12|13|9|10|4|11|6|3|1|7|2'[_0x5949('1')]('|'),_0x2d6ce4=0;while(true){
switch(_0x138ee5[_0x2d6ce4++]){

case'0':var _0x896767=0;continue;
case'1':var _0x2de433=_0x45ae41[_0x5949('6')](_0x45ae41[_0x5949('13')](_0x5eb93a,2),_0x37c346);continue;
case'2':_0x145894+=1;continue;
case'3':_0x30725e=_0x45ae41[_0x5949('14')](_0x45ae41[_0x5949('15')](_0x30725e,(parseInt('116527272660',8)-527+4-3)/(14-8)),_1x4bfb36);continue;
case'4':var _0x59ce16=681741804;continue;
case'5':var _0x5eb93a=64;continue;
case'6':var _0x30725e=_0x45ae41[_0x5949('16')](_0x896767,_0x3d7b02[_0x45ae41[_0x5949('17')](_0x145894,9)]);continue;
case'7':for(i=0;_0x45ae41[_0x5949('18')](i,4);i++){
var _0x444853=_0x5949('19')[_0x5949('1')]('|'),_0x3d6c21=0;while(true){
switch(_0x444853[_0x3d6c21++]){

case'0':var _0x1a0e90=_0x45ae41[_0x5949('20')](_0x45ae41[_0x5949('21')](_0x41e0ff,9),i);continue;
case'1':_0x2de433=_0x45ae41[_0x5949('22')](_0x2de433,_0x45ae41[_0x5949('21')](_0x41e0ff,9));continue;
case'2':var _0x1a9381=_0x45ae41[_0x5949('23')](_0x30725e,_0x2de433);continue;
case'3':if(_0x45ae41[_0x5949('24')](_0x3fa834,'$'))_0x1bf6e5+=_0x3fa834;continue;
case'4':var _0x3fa834=String[_0x5949('25')](_0x1a9381-1);continue;
case'5':_0x1a9381=_0x45ae41[_0x5949('26')](_0x1a9381,_0x1a0e90);continue;
}
break;
}

}
continue;
case'8':var _0x37c346=127;continue;
case'9':var _0x31f4aa={
'mm':128,'xx':63
}
;continue;
case'10':do{
var _0x1fb52e=_0x5949('27')[_0x5949('1')]('|'),_0x204cab=0;while(true){
switch(_0x1fb52e[_0x204cab++]){

case'0':_0x439a49++;continue;
case'1':_0x1a873b+=6;continue;
case'2':with(_0x31f4aa){
if (false) {
_0x3d9c8e +=10; xx= 17;
}
if(_0x45ae41[_0x5949('29')](_0x1a873b,_0x45ae41[_0x5949('20')](6,5))){
var _0x332549=_0x45ae41[_0x5949('23')](_0x3d9c8e,xx);_0x896767+=_0x45ae41[_0x5949('30')](_0x332549,_0x1a873b);
}
else{
var _0x332549=_0x45ae41[_0x5949('31')](_0x3d9c8e,xx);_0x896767+=_0x45ae41[_0x5949('20')](_0x332549,Math[_0x5949('32')](2,_0x1a873b));
}

}
continue;
case'3':var _0x1fa71e=_0x5d72cd[_0x5949('5')](_0x439a49,_0x45ae41[_0x5949('6')](_0x439a49,2));continue;
case'4':if(_0x45ae41[_0x5949('33')](_0x45ae41[_0x5949('6')](_0x439a49,1),_0x5d72cd[_0x5949('3')])){
_0x5eb93a=143;
}
continue;
case'5':_0x439a49++;continue;
case'6':_0x3d9c8e=_0x45ae41[_0x5949('34')](parseInt,_0x1fa71e,16);continue;
}
break;
}

}
while(_0x45ae41[_0x5949('35')](_0x3d9c8e,_0x5eb93a));continue;
case'11':var  _1x4bfb36=parseInt('21007362032',8)-50;continue;
case'12':var _0x1a873b=0;continue;
case'13':var _0x3d9c8e=0;continue;
}
break;
}

}
continue;
case'11':var _0x531f91=_0x45ae41['dkF']($,_0x45ae41[_0x5949('6')]('#',cc_cc_cc))[_0x5949('12')]();continue;
case'12':var _0x5d72cd=_0x531f91[_0x5949('36')](0);continue;
case'13':_0x5d72cd=_0x531f91;continue;
case'14':var _0x41e0ff=_0x45ae41[_0x5949('20')](9,8);continue;
case'15':var _0x145894=0;continue;
case'16':var _0x31f4aa={
'k':_0x439a49,'ke':[]
}
;continue;
}
break;
}

"""

JScode2 = """
ﾟωﾟﾉ= /｀ｍ´）ﾉ ~┻━┻   //*´∇｀*/ ['_']; o=(ﾟｰﾟ)  =_=3; c=(ﾟΘﾟ) =(ﾟｰﾟ)-(ﾟｰﾟ);
(ﾟДﾟ) =(ﾟΘﾟ)= (o^_^o)/ (o^_^o);

(ﾟДﾟ)={
      ﾟΘﾟ: '_' ,
      ﾟωﾟﾉ : ((ﾟωﾟﾉ==3) +'_') [ﾟΘﾟ] ,
      ﾟｰﾟﾉ :(ﾟωﾟﾉ+ '_')[o^_^o -(ﾟΘﾟ)] ,
      ﾟДﾟﾉ:((ﾟｰﾟ==3) +'_')[ﾟｰﾟ] 
      };

(ﾟДﾟ) [ﾟΘﾟ] =((ﾟωﾟﾉ==3) +'_') [c^_^o];
(ﾟДﾟ) ['c'] = ((ﾟДﾟ)+'_') [ (ﾟｰﾟ)+(ﾟｰﾟ)-(ﾟΘﾟ) ];
(ﾟДﾟ) ['o'] = ((ﾟДﾟ)+'_') [ﾟΘﾟ];

(ﾟoﾟ)=(ﾟДﾟ) ['c']+(ﾟДﾟ) ['o']+(ﾟωﾟﾉ +'_')[ﾟΘﾟ]+ ((ﾟωﾟﾉ==3) +'_') [ﾟｰﾟ] + ((ﾟДﾟ) +'_') [(ﾟｰﾟ)+(ﾟｰﾟ)]+ ((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+((ﾟｰﾟ==3) +'_') [(ﾟｰﾟ) - (ﾟΘﾟ)]+(ﾟДﾟ) ['c']+((ﾟДﾟ)+'_') [(ﾟｰﾟ)+(ﾟｰﾟ)]+ (ﾟДﾟ) ['o']+((ﾟｰﾟ==3) +'_') [ﾟΘﾟ];
(ﾟДﾟ) ['_'] =(o^_^o) [ﾟoﾟ] [ﾟoﾟ];

(ﾟεﾟ)=((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+ (ﾟДﾟ) .ﾟДﾟﾉ+((ﾟДﾟ)+'_') [(ﾟｰﾟ) + (ﾟｰﾟ)]+((ﾟｰﾟ==3) +'_') [o^_^o -ﾟΘﾟ]+((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+ (ﾟωﾟﾉ +'_') [ﾟΘﾟ];

(ﾟｰﾟ)+=(ﾟΘﾟ);
(ﾟДﾟ)[ﾟεﾟ]='\\';
(ﾟДﾟ).ﾟΘﾟﾉ=(ﾟДﾟ+ ﾟｰﾟ)[o^_^o -(ﾟΘﾟ)];
(oﾟｰﾟo)=(ﾟωﾟﾉ +'_')[c^_^o];
(ﾟДﾟ) [ﾟoﾟ]='\"';

(ﾟДﾟ) ['_'] ( (ﾟДﾟ) ['_'] (ﾟεﾟ+(ﾟДﾟ)[ﾟoﾟ]+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (ﾟΘﾟ))+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟｰﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟΘﾟ)+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ ((ﾟｰﾟ) + (o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟｰﾟ)+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟΘﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ ((o^_^o) +(o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ (o^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ (o^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟｰﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟoﾟ]) (ﾟΘﾟ)) ('_');

"""


JScode3 ="""
a = (function(s, opt_attributes, key, pairs, func, params) {
  /**
   * @param {number} i
   * @return {?}
   */
  func = function(iii) {
    hh = (iii < opt_attributes ? "" : func(parseInt(iii / opt_attributes))) + ((iii = iii % opt_attributes) > 35 ? String.fromCharCode(iii + 29) : iii.toString(36));
    return parseInt(hh);
  };
  if (!"".replace(/^/, String)) {
    for (;key--;) {
      params[func(key)] = pairs[key] || func(key);
    }

    /** @type {Array} */
    pairs = [function(urlParam) {
      return params[urlParam];
    }];
    /**
     * @return {?}
     */
    func = function() {
      return "\\w+";
    };
    /** @type {number} */
    key = 1;
  }
  for (;key--;) {
    if (pairs[key]) {
      /** @type {string} */
      s = s.replace(new RegExp("\\b" + func(key) + "\\b", "g"), pairs[key]);
    }
  }
  return s;
})('(0(){4 1="5 6 7 8";0 2(3){9(3)}2(1)})();', 10, 10, "function|b|something|a|var|some|sample|packed|code|alert".split("|"), 0, {});
debug();
"""


#******************************************************************************************************************************************************


#main
#https://stackoverflow.com/questions/30923819/why-python-2-7-on-windows-need-a-space-before-unicode-character-when-print


# -*- coding: utf-8 -*- 
#s = "abcşiüğ"
#my_unicode_string = unicode(s, "utf-8")
#print my_unicode_string[3].encode('utf-8')
#print ord(my_unicode_string[3])
#print s
#hh(mm)

# 0 - debug
# 1 - openload
# 2 - AAdecode
# 3 - Unpaccker
# 4 - AAdecode in file
# 5 - Alluc
# 6 - Uptostream
# 7 - perso

TEST = 6

#Fonction en cas de probleme de raw string
def loadRawstring(file):
    fh = open(file, "r")
    tmp = fh.read()
    fh.close()
    return tmp
    
if TEST == 0:
    pass
if TEST == 1:
    JScode = JScode1
if TEST == 2:
    JScode = JScode2
    JScode = unicode(JScode, "utf-8")
if TEST == 3:
    JScode = JScode3
if TEST == 4:
    JScode = loadRawstring('JS_AA_raw.txt')
    JScode = unicode(JScode, "utf-16")
if TEST == 5:
    JScode = JScode5
if TEST == 6:
    JScode = loadRawstring('up2stream.js')
if TEST == 7:
    JScode = JScode6
    
JP = JsParser()
Liste_var = []


if TEST == 1:
    JP.AddHackVar('#gItZEkCYUy',"7646b5310d329a21dec22b45be5b4bad6ce711857674f9b9d272e7896b81aee1b9c4e3837351587245037c585a6f7b024141755741016c5b47656a01476342497d0273476c7c6402426f4d29617279557a025f676d501c677c68795c0364614e6f4803")

#JP.SetOption('ForceTest')

# Set it tu true to display debug time process
if (False):
    import cProfile
    cProfile.run('JP.ProcessJS(JScode,Liste_var)')
else:
    JP.ProcessJS(JScode,Liste_var)
    
#print 'Return : ' + str(JP.ProcessJS(JScode))

if TEST == 1:
    print ('Decoded url : ' + JP.GetVarHack("#lqEH1"))
if TEST == 2:
    print ('return : ' + JP.LastEval.decode('string-escape'))
if TEST == 4:
    print ('return : ' + JP.LastEval.decode('string-escape').decode('string-escape'))
if TEST == 5:
    print ('return : ' + JP.LastEval)
if TEST == 6:
    print ('return : ' + JP.GetVar(Liste_var,'code') )
