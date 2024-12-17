

import json
import re
from PyPDF2 import PdfReader
import pdfplumber


texts = """
Dut Pwøc
Luubö Mo Cäänö Kaper Wëël Dut Pwøc
Wëëlö man ni cwøl ni Dut Pwøc en yie da dudi ma 150. Dudi moøgø beege dut Jwøk
moa wara wär jø Icrielli. Mo thööth dïge caga Deebiti nyeny jø Icriel. Ki kwör møøk
wëëlö man di cwølø ni Dut Deebit.
Dudi moøgø na 150 yøø, møøk dïge beege dudi mo wära jiyi ni ge pwøya Jwøk ni
ge dwøga met ec jïre. Teeŋ dudi moøgø beege 8, 19, 96, 100, 103, 104, 107, 111, 145,
146, 148, 149, 150.
Dudi møøk beege dut lam mo jiy mo ena yïth gïï mo leth. Teeŋ dudi moøgø beege
3, 6, 13, 31, 56.
Dudi møøk beege dut lam ni jiy caana bääyö marge ni cwïnyge opädhö. Teeŋ dudi
moøgø beege 32, 51, 130.
Dudi møøk beege dudi mo wära jiyi ni ge nyootha ŋäädhe marge man wø ŋääthge
Jwøk ki gø. Teeŋ dudi moøgø beege 23, 27, 90, 91, 121, 139.
Dudi møøk beege dudi mo yïthge da pwöc kiper bëët jöör Jwøk. Teeŋ dudi moøgø
beege 1, 15, 119.
%
@
*#Duut Mo Nyootha Luum Bëëtö Mar Jøøa Beyø Ki Bëëtö Mar Jøøa Reyø
1 Gwïëth en jï ŋat wø ba cäädhi
køør pwöc jøøa reyø,
ni wø ba cäädhi jöör jø adhala,
ni wø ba bëëdö buut jø abuua.
2 'Ba met ec mare wø joode ka ri luup
moa no ogöörö yi wëël Jwøk,
ni eni cädö ki waŋcäŋ ki wäär
cooth kiper luup moøgø.
3 Eni caala jaath mo opiith deŋ naam,
ni wø nyïïe ciek kany wø näk ma
kare,
ni bøøge moe ba när.
Teeŋ ŋatøgø, gïï wø tïïe bëët thura karge.
4 'Ba bëëtö mar jøøa reyø patha
enøgønø;
ge caala lethø ni wø køøl jame.
5 Kiper manøgønø, jøøa reyø ba cuŋŋi kar
løøk mar Jwøk ni nyeŋge teek,
ni ge na jø adhala, ge ba cuŋŋi
ya acooŋ jøøa beyø,
6 kiper Wuuö Jwøk bëët jøøa beyø ŋääe,
'ba bëët jøøa reyø cäätha baŋ ränynyö.
@
*#Duut Mo Cäänö Kaper Ŋata Røøny Wuuö Jwøki Na Nyeya
1 ?Aŋø na ö wïth juurre ni cooŋge
dëëtge kiper ageem en,
ni cätge ki gïï mo oballe jaak?
2 Nyeye mo bäät piny aö maal,
ni ö kwääri ni dwätge ki geni na
aciel,
nee Wuuö Jwøk, ki dhaanhnhe
na näk ee røønyø na nyeya nee
nywaakge;
3 ni köge, ni «Beerra man kälø
luumge wøk bäätø na näk øøno
twöö ki gø,
ni wetø ciik moge na caal thøøth
twöc.»
4 'Ba Wuuö Jwøk ni wø bëëdö maal
ŋeethø bäätge,
ni put bëëtö ni gïrge ee taaø.
5 Køøre eni cäänö ki geni ni mare
wëër,
ni tïïc ge nee bëëtge ni lwäär ki
wëëye,
6 ni kööe, ni «Aani, ŋata nø røønya
na nyeya
arøønya nee bëëde bäät Kïn
Dhayan,
ni beeye kïnna na en kur keere.»
7 'Ba nyeya mana røøny aköö,
ni «Luumma caan Wuuö Jwøki
caana caanø.
Ena köö jïra, ni ‹Dïcäŋi ennø,
ïïna wääda,
ni tïma ni aana wäru.
8 Pëëny aani, nee wïth juurre bëët
mëëga ïïni na moï,
ni ö pinynyi bäre ni ci jïrï.
9 Ge dïïmï dïïmö ka athøny
nywïënyö,
ni raanynyï geni kaamar dak mo
ogøø piny.› »
10 Kiper manøgø nø, u na nyeye,
caarru wïthu,
ni wïnynyu ŋwøc man ŋwöny
uuni ki gø, u na kwääri mo
piny.
11 Tïnynyu Wuuö Jwøk nou lwäär,
ni mïn yïthu ni dëëtu kwanynyi.
12 Wøørru wäädö, nee ba wëëre,
nee bëëtö maru ba cääth baŋ
ränynyö,
kiper wëëye wø laara tägö.
'Ba gwïëth en jï jø wø kan dëëtge
buute.
@
*#Lam Mo Ŋäätha Jwøk Kiper Gïna Tïïe
1 Wui Wuuö Jwøk, nyïïmänna
atïmö ni thööth døc.
Gena ö maal bääta ni tïmge ni
gëëmö ki aani.
2 Jiy mo thööth wø cäänö kipera,
ni köge,
ni «Eni, bäŋ køny mo di joodø
baŋ Jwøk.»
3 'Ba ï na Wuuö Jwøk,
ï caala kwöt leny man wø gëëŋa
dëëra ki gø;
ni bee ï, ni wø jooda ajiem ki
køørï,
ni bee ï, ni wø tïïc aani nee wïïa
tïŋa maal.
4 A bëëdö naa kwaaya Wuuö Jwøk,
ni løk kwac mara jïra ki bäät
kïnne na en kur keere.
5 Dëëra wø nyaaŋa piny ni gäm
nyeŋŋa,
ni pääa ni dëëra jööt, kiper
jwïëya ena cer Wuuö Jwøk.
6 A ba lwäyi ki jiy ma kume apaar,
mo rege ege ciel laga.
7 Wui Wuuö Jwøk, ö maal,
ni kønyï aani, ï na Jwøa;
kiper nyïïmänna bëët adhööŋŋï
ki thäkge,
ni tøyï lakge, ge na jøøa reyø.
8 Bee ï na Wuuö Jwøk ni wø piem
jiy.
Wui Wuuö Jwøk, beerra man
gwïëthï jiyï.
@
*#Duut Mo Ŋäätha Jwøk Kiper Gïn Wø Tïïe
1 Wui Jwøk, wïny dwøra kany wø
kwaa ïïni,
kiper beeye ï wø ŋun aani.
Aana kønyï kanya ena yïth gïï
mo leth;
nyooth met ec marï jïra, ni
wïnynyï lam mara.
2 ?'Ba u na jiy, a këël kany mo nyïëdi
nø noo bëëdu nou jøøŋŋa aani?
?Naa këël kany mo nyïëdi nø noo
bëëdu nou poot mëër ki luup
mo oballe jaak, nou cara tööt?
3 'Ba ennø, beerra man ŋäyu gø
ni Wuuö Jwøk jø wø bëëdö ni
cwïnyge ena køøre ee cïp kur
keerge na moe.
Këël aani, kany wø kwaa Wuuö
Jwøk, dwøra wø wïnynye
wïnynyö.
4 Këël dëëtu doo tïmö ni miel ki
wëër, käru bääyö;
cädu ki cwïnynyu kany wø enu kwör
niine mou, ni döötu ba wïnyi.
5 Cïpu ko olämme ma karge nou
bëëdö ni bëëtö maru beer,
ni ŋääthu Wuuö Jwøk.
6 Jiy mo thööth wø köö, na «?Aŋa
noo nyooth gïn mo beer jïwa?»
'Ba ï na Wuuö Jwøk, wëëk tac
täärnyïmï rieny bäätwa.
7 Met ec mo dwøŋ akïthï cwïnya,
ni kaala met ec mar jø wø bëëdö
ni yïthge met
kany wø tïm beelli ki kwøk
nyïïjenni moge ni thööth.
8 A buta piny ni yia met, ni laar
nyeŋŋa gämmö,
kiper beeye ï keerï, ï na Wuuö
Jwøk,
ni wø tïïc aani naa bëëda ni bäŋ
gïn tägi dëëra.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Kwaca Jwøk Nee Dhaanhø Gwøe Ceŋ Nyïïmän
1 Wui Wuuö Jwøk, wïny kwac
mara kany wø läma,
ni wïnynyï cooyø mara.
2 Ï na nyeya mara ni bee ï Jwøa,
wïny oduuru mara,
kiper a wø kwaaya ïïni.
3 Wui Wuuö Jwøk, ka amöölla
dwøra wø wïnynyï wïnynyö,
kany wø läma naa køya man wø
løgï jïra.
4 Kiper ï patha Jwøk mo yie met ki
gïï mo reyø,
niï bëëdö ni bäŋ raay mo nyänh
buutï.
5 Ŋat ma ŋat ŋwøc ba cuŋŋi nyïmï;
niï bëëdö niï män ki jiy bëët mo
wø tïïc gïï mo reyø.
6 Jø wø cäänö ki tööt wø raanynyï
raanynyø,
niï män ki ŋat cwøk ki ŋat wø
rem jiy met jïre.
7 'Ba aani, a wø dunynya yi ødï
ki køør mëër marï na dwøŋ ni wø
ba jøøl.
A wø lämö ni cøŋŋa yaa këël piny
yi øt lam marï na en kur keere
naa wøøra ïïni.
8 Wui Wuuö Jwøk, bwøth aani ki
jöör adïëri marï,
kiper jïra da nyïïmän;
ni tïïyï jöörï ni thïïŋ nyïma.
9 Kiper jøøgø ki dëëtge bäŋ adïëri
dhøkge, 
ni cwïnyge päŋ ka aranya,
ni lwöcge bëëdö kaamar bwör
mo ŋammø,
ni ge cäänö ki lëëpge ni marge
cwøk.
10 Wui Jwøk, ŋøl luubö marge ni
jäälï ge;
beerra man ränyge ki køør luup
moa tuutge keerge;
ni riemï geni wøk kiper gïïa
tïïcge na thööth na reyø,
kiper ge bëëdö ni ge gëëmö ki
ïïni.
11 'Ba beerra man ö jø wø kan
dëëtge buutï bëët ni mïn
yïthge,
ni bëëtge ni ge wär ki dudi cooth
ni yïthge met;
niï bëëdö niï koora geni,
ni ö geni na mëër ki ïïni ni
jiemge ïïni ni yïthge met.
12 Kiper bee ï na Wuuö Jwøk ni wø
gwïëth ŋat wø bëëdö ki bëëtö
ma adïëri,
ni ö mëërri marï ni bëëde na
gëëŋi kaamar kwöt leny.
&Manøgø beeye duut Deebit.
@
*#Lam Mar Ŋat Mo Kïmmö Kiper Bëëtö Mare
1 Wui Wuuö Jwøk, kär a joogï ni
marï wëër ki aani,
ni ba wëërï kany wø pwönynyï
aani.
2 Wui Wuuö Jwøk, cïp cwïnyï piny
ki aani,
kiper aana tïmö naa jääk døc.
Wui Wuuö Jwøk, køny aani,
kiper dëëra atïmö ni kwanynyi
ki lwär.
3 Wui Wuuö Jwøk, cwïnya abwøk
døc.
?Aŋø, a yi wäne nø noo kønyï aani?
4 Wui Wuuö Jwøk, duu baŋa ni
piemï jwïëya,
køny aani ki køør mëër marï ni
wø ba jøøl.
5 Kiper bäŋ ŋat mo caar wïïe ki
ïïni køør thøø.
?Aŋa noo maar ïïni pwøc kar
bëët jwïëc jøøa no othøw?
6 Aana ööl ki kïmmö mara;
ki wäär cooth pï nyeŋŋa wø øya
yi pïën mara,
ni ö pïënni ni neethar ki pï nyeŋŋa.
7 Nyeŋŋa aränynyö ki jwøk;
ni wer nyeŋŋa ni kwayø ki jwøk
ki køør gïïa tïïc nyïïmänna.
8 'Ba u bëët ni wø tïïc gïï mo reyø,
daagu rou buuta,
kiper Wuuö Jwøk dwøra
awïnynye kanya jwöŋa.
9 Wuuö Jwøk kwac mara awïnynye,
ni jïëc lam mara.
10 Nyïïmänna bëët wïthge olääy ni
bwøk cwïnyge;
wïthge olääy møn, ni putge døø
ŋäthge.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Kwaca Wuuö Jwøk Nee Luup Jøøa Reyø Ŋøle
1 Wui Wuuö Jwøk, ï na Jwøk mara,
a bëëdö ni raa yaa kan buutï;
gwøk aani ceŋ jø wø cwaat yia ni
putï a køny,
2 kiper naa ba tïïcge ki gïn mo leth
kaawat man wø ö ŋuuwi wø cööt
lääy ni di tutö,
ni bäŋ ŋat køny läänögø.
3 Wui Wuuö Jwøk, ï na Jwøa, ni
näk mo da gïn mo raac mo yaa
tïïö,
ni da gïn mo obøth jïra, 
4 wala aano dwök baŋ nyawatwa
ki gïn mo raac,
wala a twiera nyïïmänna ki gïn
mo bäŋ tiere,
5 beerra man ö nyïïmänna ni
riemge aani ni makge aani,
ni gøøge aani piny ni 'näkge
aani,
ni putge ajiem mara raanynyø na
bäre bäre.
6 Wui Wuuö Jwøk, ö maal ni
wëërï;
jek riï kiper wëëc nyïïmänna;
jek riï, ï na Jwøa, kiper bee ï ni
wø ŋøl luup.
7 Beerra man ö wïth juurre bëët ni
cooŋge dëëtge kanya ciel nyïmï,
ni bëëdï niï ŋøla luup moge ni
ïïna kwäärö marge.
8 Wuuö Jwøk luup jiy wø di ŋølø
na kare.
Wui Wuuö Jwøk, ŋøl luumma ki
køør bëëtö mara na näk kare,
ni ŋølï luumma ki køør bëëtö
mara na beer.
9 Ï na Jwøk mana näk adïëri
ni wø raŋ acaac dhaanhø ki gïna
en cwïnye,
män gïïa reyø ni wø tïïc jø raayi,
ni tïïyï jø wø bëëdö ni marge
adïëri nee cuŋge ni teek.
10 Jwøk bëëdö ni caala kwöt leny
jïra,
ni beeye wø piem jøøa näk
cwïnyge thïïŋ.
11 Jwøk bee eni ni wø ŋøl luup na
adïëri,
ni bee eni ni wø wëër ki jø raay
ki yïth nïne bëët.
12 Ni näk mo dhaanhø cwïnye ba
løøe, Jwøk opëëllö mare di
paaø,
ni jiiŋ atheerø mare ka atum
mare.
13 Jap wø nääe ki ge ee nø jiiŋŋø,
ni dhøk athëëre moe ee tïïö ni
wääŋö.
14 Ka adïëri møn, ŋat raay acaare
mo reyø piith yi cwïnye,
ni duunge ki gïï mo reyø ki tööt.
15 Eni kunyö ki buur mo bäär,
ni cäŋ päth yi buura koonye
keere.
16 Raaye døøa wïïe keere,
ni ö gïïa reyø na tïïe ni døøge
wïïe.
17 'Ba aani, Wuuö Jwøk pwøa pwøø
ki køør adïëri mare,
ni wära ki duut naa pwøya Wuuö
Jwøk na dwøŋ ni en maal.
Manøgø beeye duut Deebit mana caae jï
Wuuö Jwøk kiper Kuuc nyï Benjamen.
@
*#Duut Mo Nyootha Ajiem Jwøk Ki Dööŋö Mar Dhaanhø
1 Wui Wuuö Jwøk, ï na Kwääcwa,
bäät piny bäre wøøra nyeŋŋï,
ni maal bäre iï pääŋö ka ajiemï.
2 Teegï anyoothï jï nyïïmännï
ki køør luup mo wø car obwöre
moa therø këël moa näk poot
dhøøth,
kiper nee nyimän ki ŋat wø
many cool kwör nee joogï.
3 Wui Wuuö Jwøk, kany wø raŋa
maal na tïïyï ki cerï,
ki dwääy ki ceer na näk iï cïp
kwörge,
4 a wø cädö ki cwïnya, ni kööa,
ni «?Dhaanhø agïnaŋø, ni lääŋŋï
gø en,
ni o dhaanhø agïnaŋø, ni gwøgï
gø en?»
5 'Ba kare atïïyï ni dwøŋ,
ni caatha køør nyïïatwiet maal ki
kany mo thiinh,
ni røønyï gø ka ajiem ki wödö.
6 Ena røønyï bäät gïïa tïïyï bëët ki
cerï,
ni cïbï jammi bëët cere,
7 ni beege dïëk ki dhäk bëët,
ki lääc paap thuwø,
8 ki weny ki rec,
ki gïï wø bëëdö yi naama dwøŋ
bëët.
9 Wui Wuuö Jwøk, ï na Kwääcwa,
bäät piny bäre wøøra nyeŋŋï.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Pwøca Jwøk Kiper Ŋøl Mare Na Thïïŋ
1 Wui Wuuö Jwøk, ï pwøa pwøø ki
cwïnya bäre,
ni caana tïïe moï bëët ni wø
rëëm ec.
2 Aani yia tïmö ni met døc ni
kanynya ki køørï;
a wär ki duut naa pwøya ïïni, ï
na dwøŋ ni en maal.
3 Kany wø nyoothï riï, nyïïmänna
wø døøa køørge,
ni cwanyge tietge ni thøwge.
4 Kiper luubö mara na näk adïëri
aŋølï na kare,
ni ïïno pï bäät wälu niï ŋøla ŋøl
ma adïëri.
5 Wïth juurre ni wø wøør juu møøk
ajoogï, ni dïïrï wïthge, ge na jø
raay,
ni putï nyeŋge rwäänyö na bäre
bäre.
6 Wïth nyïïmän adïïrï na bäre bäre
møn,
ni nyaaï päänye moge piny,
ni put wïci wïlö ki geni na bäre bäre.
7 'Ba Wuuö Jwøk puta bëëtö bäät
wälu na bäre bäre,
ni tier wälu mare ee këël piny ni
teek kiper ŋøl luup.
8 Eni luup jø bäät piny di ŋølø na
adïëri,
ni ŋøl luup jiy ki jöö mo thïïŋ.
9 Wuuö Jwøk beeye wø cuŋ jøøa
no ocaannø dëëre,
ni bëëde na kar gwøk røk jïge
kany wø näk ri gïï mo leth.
10 Jø wø ŋäc ïïni, ï ŋääthge ŋäädhö;
wui Wuuö Jwøk, jø wø many ïïni
ba weyï.
11 'Ba u na jiy, wärru duut pwøc
jï Wuuö Jwøk ni wø bëëdö
Dhayan.
Beerra man ö gïïa tïïe ni køpu ge
jï wïth juurre.
12 Kiper eni ni wø cool kwör remø
cädö kiper jøøa no ocaannø,
ni wïïe ba wïl ko oduuru marge.
13 Wui Wuuö Jwøk, køny aani;
raŋ gïïa leth ni wø jwøra ceŋ
nyïïmänna,
ni kälï aani wøk cer thøø,
14 nee gïï wø pwøc ï ki ge bëët
caana jï jø Dhayan,
naa bëëda ni yia met ki køør
pïëm marï.
15 Wïth juurre apäth yi buura
koonyge keerge,
ni ö tietge ni magi ya abïëba cekge.
16 Wuuö Jwøk nyeŋŋe ee tïïö nee
wïnye ki køør ŋøl mare.
'Ba ŋat raay dëëre ee twöö keere
ki gïïa tïïe ki cere.
17 Jø raay, jwïëcge cøøa kar bëët
jwïëc jøøa no othøw,
këël wïth juurre bëët mo wø
bëëdö ni wïthge owïl ki Jwøk.
18 'Ba Jwøk wïïe ba wïl ki ŋat mo
can,
ni ŋäädhe mar jøøa no ocaannø
ba ränynyi na bäre bäre. 
19 Wui Wuuö Jwøk, ö maal, kär
dhaanhø jïtö ki teek bäätï.
Beerra man bëët luum wïth
juurre ni ŋøla nyïmï.
20 Wui Wuuö Jwøk, døøc wïth
juurre mo lwäär,
nee ŋäcge ni gena jiy jaak.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Kwaca Wuuö Jwøk Nee Jø Raay Jääle
1 ?Wui Wuuö Jwøk, aŋø ni bëëdï
ni karï bäär en?
?Na aperŋø wø kanï dëërï kany
wø näk ri gïï mo leth en?
2 Jøøa reyø töödö ni caange jøøa
can;
beerra man ö luup moa tuutge ni
døøge dëëtge.
3 Ŋat raay wø ŋwöö keere ki køør
mana manynye ki cwïnye,
ni ö ŋat mo cwïnye päl ni jany
Wuuö Jwøk ni kwier gø.
4 Ŋat raay bëëdö ni töödö, ni eni
ba many Jwøk;
ki yïth acaare moe bëët, eni cädö
ni bäŋ Jwøk.
5 Eni gïï wø manynye joode joodø
cooth,
'ba eni ba cädö kiper ŋøl mar Jwøk.
Eni bëëdö ni nyïïmän moe bëët
ee taaø.
6 Eni wø cädö ki cwïnye ni kööe,
ni «Bäŋ gïn mo pïï dëëra;
a puta bëëtö ni bäŋ gïn mo raac
mo tägi dëëra na bäre bäre.»
7 Eni bëëdö ni dhee bëënna acïëni
ki cwøk ki ŋwöny jiy,
eni wø laara cäänö ki gïï mo leth
ki jap rääö.
8 Eni wø møøra piny töök paac,
ni kan ree kiper nee jøøa beyø
nääe,
ni eni raŋŋa jøøa näk rege ba
løny køny,
ki man tïïc gïn mo raac dëëtge.
9 Eni dëëre wø di kanø kaamar
ŋuu ni wø møør piny,
ni eni kurö kiper ŋata no
ocaannø nee maae.
Ŋata no ocaannø wø di cøøgø ni
mak gø
kaawat man wø cek lääy ka abïëp.
10 Ŋat mo ree ba løny køny wø gøøe
piny ni pädhe,
ni eni pädhi ka køør teek mar ŋat
raay.
11 Ŋat raay cädö ki cwïnye ni kööe,
ni «Jwøk bëëdö ni wïïe owïl,
ni nyeŋŋe ee miiø. Eni gïï wø tïïa
ba joode na bäre bäre.»
12 Wui Wuuö Jwøk, ï na Jwøk,
ö maal ni tïŋï cerï maal niï
nyootha teegï;
kär wïïï wïl ki jøøa no ocaannø.
13 ?Aŋø, ŋat raay kwier Jwøk
aperŋø,
ni cäde ki cwïnye en ni kööe, ni
«Aani, a ba pëëny Jwøki.»?
14 'Ba ï na Wuuö Jwøk, gïïögø bëët
ŋäyï møn,
kiper ïïni gïïa reyø ki caan jiy
nëënö jïrï,
ni løny jïrï ki man tïïyï mana
manynyï.
Ŋat mo ree ba løny køny, dëëre
cïbe cïbö jïrï,
ni beeye ï ni wø køny ŋat ma kïïc.
15 Raany teek mar ŋat raay ki ŋat
wø tïïc gïï mo reyø;
kwaan raay moe bëët bääte, ni
bäŋe aciel mo dööŋ.
16 Wuuö Jwøk bëëdö na nyeya na
bäre bäre,
ni ö wïth juurre ni wø wøør juu
møøk ni thumge bäät ŋøøpe.
17 Wui Wuuö Jwøk, lam mar jøøa
can wïnynyï wïnynyö. 
Cwïnyge cømï cømø, ni cegï ïthï
ki kwac marge,
18 nee gïn mo beer nee tïïyï kiper
jøøa näk kïïe ki jøøa näk
ocaannø,
ni ö dhaanhø ni bëën thøø en ni
ba døøc jiy mo lwäär këët.
@
*#Duut Mo Nyootha Gø Ni Wuuö Jwøk Beeye Wø Kan Røk Buute
1 Aani raa wø kana buut Wuuö
Jwøk.
?Aŋø, u kööu ki aani nidïï,
ni «Ciï ni reŋŋï bäät kïte kaawat
man wø määt wenyø;
2 kiper adïëri møn, jø raay atume
moge ajiiŋge;
athëëre moge ege nø cïp bäät
thøøth atume moge,
kiper nee ge thööthge ki yi
muudhö,
ni ge thööya jøøa marge thïïŋ.
3 ?Ni näk mo piny bëëdö ni
ränynyö,
agïnaŋø noo løny ki man tïïyi ya
jøøa marge thïïŋ?»
4 'Ba Wuuö Jwøk nut kar bëëtö
mare na en kur keere,
ni wälu mar Wuuö Jwøk ena
maal.
Eni bëëdö ni raŋŋa bëët jiy bëët.
5 Wuuö Jwøk jøøa beyø ki jø raay
wø raŋŋe raŋŋø,
ni ö eni ni männe ki ŋat wø tïïö
ki gïï mo reyø.
6 Eni cuk mo liel ki maac mo päl
døc
oleeŋ bäät jø raay,
ni jääl geni ki jamø mo lïëth mo
wääŋö.
7 Kiper Wuuö Jwøk mare beer bäre,
ni yie met ki tïïc gïï mo beyø;
jøøa marge thïïŋ täärnyïm Wuuö
Jwøk jootge joodø.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Kwaca Jwøk Ki Man Køny Dhaanhø Ceŋ Jøøa Reyø
1 Wui Wuuö Jwøk, køny waani,
kiper atïmö ni bäŋ ŋat mo
cwïnye ena køørï, ï na Jwøk,
ni bäŋ ŋat mo maar ka ŋääth mo
di joodø këët.
2 Ŋati man nø cara tööt jï watge,
ni ge cäänö ka dhøkge jaak, ni
cwïnyge oriewi.
3 Beerra man ö Wuuö Jwøki ni
mec dhøgi mo wø car cwøk
bëët,
ni ŋør lëëpi mo wø ŋwöö døc,
4 ni beege jø wø köö, ni «Løny ki
man jootwa mana manywa ki
køør cäänö marwa.
Wa cäänö jaak ni wa ŋäätha
lëëpwa. ?Aŋø, kwääywa
aŋa?»
5 'Ba Wuuö Jwøk aköö, na «A ööa
maal ennø,
ni cøøa kuna kønya jøøa no
ocaannø na näk bëëtö marge
oränynyö,
ni ge bëëdö ni ge cooyø ni bäŋ
ŋat køny ge,
ni kïtha ge kany mo ge gwøa
gwøø yie ni beeye mana
manyge.»
6 Luup mo Wuuö Jwøk beege luup
mo tøŋ ma karge,
ni caala warkey mo oleenyø
kwöre abïriiø kar thäth.
7 Wuuö Jwøk wa gwøe gwøø,
ni koor waani ki teeŋ jøøi ni reyø
ii,
8 ni beeye kany wø tïme ni jiy
pwøya gïï mo reyø,
ni jøøa reyø bëëdö ni ge cäädhö
jaak dï paac bäre. 
&Manøgø beeye duut Deebit.
@
*#Duut Mo Kwaca Wuuö Jwøk Kiper Køny
1 ?Wui Wuuö Jwøk, a këël kany
mo nyïëdi nø noo bëëdï ni wïïï
owïl ki aani?
?Aŋø, wïïï wïl ki aani na bäre
bäre møn?
?A këël kany mo nyïëdi nø noo
kanï täärnyïmï ki aani?
2 ?A këël kany mo nyïëdi nø noo
bëëda naa cädö ki cwïnya,
ni cwïnya kïmmö cooth ki yïth
nïne bëët?
?A këël kany mo nyïëdi nø noo
bëët nyimänna ni wïïe ee tïŋ
maal bääta?
3 Wui Wuuö Jwøk, ï na Jwøa, cädï
kipera ni løgï mara,
kwøw aani, naa ba buta ni mara thøø,
4 kiper nee nyimän mara ba kööe,
ni «Ena bööta,»
nee yïth nyïïmän 'moa ba mïnge
kiper ränynyö mara.
5 'Ba aani, a bëëdö naa ŋäätha
mëër marï ni wø ba jøøl;
yia wø mïnnö kany wø piemï aani.
6 Aani, a wär ki duut jïrï, ï na
Wuuö Jwøk,
kiper bëëtö mara atïïyï ni beer.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Cäänö Kaper Rääö Mar Jø Raay
1 Jiy mo wø cäänö ki cwïnyge, ni
«Bäŋ Jwøk», gena bøøre.
Gena jiy mo oränynyö, ni ge
temma gïï mo reyø,
ni bäŋ ŋat mo tïïö ki gïn mo
beer.
2 Wuuö Jwøk aräŋŋö ki maal ni
raaŋa bëët jø bäät piny,
ni ge raaŋe kaper nee jïte ki mo
wïïe leer,
mo manynya eni, eni na Jwøk.
3 'Ba ge bëët, geno nø gaa wøk,
ni geno nø tïmö ni ge reyø bëët,
ni bäŋgø mo tïïö ki gïn mo beer,
këël dhaanhø aciel kiree, bäŋgø
na bäre bäre.
4 ?Aŋø, jøø ni tïïö ki gïï mo reyø
yøø bäŋ gïn mo ŋäcge,
ni camge jap jiya kaawat man wø
cam møø jaak en,
ni nyeŋ Wuuö Jwøk ba cwølge?
5 'Ba kaaca ge tïmö ni ge lwäär
døc,
kiper Jwøk ena buut jøøa beyø.
6 Jøøa reyø manynya man kierge
wïth jøøa no ocaannø,
nee gïïa caarge nee ränyge.
'Ba Wuuö Jwøk beeye noo tïmö
na kar gwøk røk marge.
7 Beerra man ö Wuuö Jwøki ni wø
bëëdö Dhayan ni piem jiye ma
jø Icriel,
ni ö jø Icriel, ni beege nyïïkwaac
Jeekap, ni mïn yïthge ni
kanyge
kanyo ö Wuuö Jwøki noo dwøk
bëëtö marge kare.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Nyootha Teeŋ Ŋat Wø Bëëte Many Jwøki
1 ?Wui Wuuö Jwøk, aŋa noo maar
bëëtö yi ødï?
?Aŋa noo maar bëëtö bäät kïnnï
na en kur keere?
2 Beeye ŋat wø bëëdö ki bëëtö ma
kare,
ni wø tïïc mana beer,
ni wø caar adïëri ki yi cwïnye;
3 ni beeye ŋat wø ba wääö ki nyeŋ,
ni wø ba tïïö ki gïn mo raac dëër
ŋat atut mare,
ni wø ba jøøŋ watge;
4 ni wø män ki ŋat mo cwïnye ena
køør raay,
ni wø wøør jø wø lwäär ki Wuuö
Jwøk;
ŋat wø ba døø ŋääe ki gïna
kööŋe kipere,
këël gïï mo leth doo pïï bääte;
5 ŋat wø jape mac ni duui ni bäŋ
mëëdi bäätge,
ni wø ba ŋeew ki piny nee luubö
kïth bäät jøøa beyø.
'Ba ŋat wø tïïc teeŋ gïïögø bëët
bëëdö kare ni teek.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Pwøca Wuuö Jwøk Kiper Køny Mare
1 Wui, ï na Jwøk, gwøk aani, kiper
raa yaa kan buutï.
2 Aana köö jïrï, ï na Wuuö Jwøk,
ni «Beeye ïïni na Kwääya,
jammi bëët moa beyø na en jïra
käla baŋï.»
3 Jøøa bëëdö na jic Jwøk yi
ŋöömmi, gena jiy mo owøørø,
ni beege jøøa met yia ki geni døc.
4 'Ba jø wø jier juu møøk ge meeta
kïmmö bäätge.
Aani a ba cïpi ko olämme jï juu moge,
ni ba kïtha nyeŋ juu moge dhaa.
5 Wui Wuuö Jwøk, gïna pere leth
na tïïyï jïra beeye ki man
bëëdï ni ïïna Jwøk mara,
ni gum dëël mara ena cerï.
6 Adïëri møn, bëëtö mara bäre
atïïyï ni beer,
ni caala dhaanhø mo ojïtö ki
ŋøøm mo beyø mo duunnö ki
met ec jïre.
7 Aani Wuuö Jwøk wø pwøa pwøø,
eni ni wø pwöny aani;
ki wäär thuwø, acaare moe na
näk yaa kan cwïnya wø cäŋa
cïpö ki pwöc jïra.
8 Aani a wø bëëdö naa lääŋŋa
Wuuö Jwøk cooth;
a ba pädhi kiper mana bëëde ni
eni nut buuta.
9 Kiper manøgønø, yia atïmö ni
met, ni kanynya,
ni puta bëëtö ni aano gwøø.
10 Kiper jwïëya ba wiiï kar bëët
jwïëc jøøa no othøw,
ni ö dëër dhaanhnhï na en kur
keere ni ba wëëgï gø bëëtö yi
bwörö.
11 Øtjöör kwøw wø nyuunhnhï
aani,
ni døøyï yia mo met døc kiper
man wø nudï buuta;
'ba gïï wø cïpi ki met ec nutö
buutï cooth.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Kwaca Jwøk Kiper Ŋøl Mare Na Näk Adïëri
1 Wui Wuuö Jwøk, wïny luumma
ni beer, ni cegï ïthï ko oduuya,
wïny lam mara man lama ni bäŋ
cwøk yie en.
2 Beerra man ŋølï mara na kare,
ni raŋï gïna na adïëri.
3 Ni näk miï lïïmmö baŋa ki wäär,
ni neenï cwïnya,
ni raŋŋï aani døc, bäŋ gïn mo
raac mo jootï ri bëëtö mara.
A bëëdö ni dhaa yaa gwøø kiper
naa ba bääya kany wø cääna. 
4 Ki køør luummï, dëëra yaa gwøø
ki tïïe mo wø tïïc jiyi;
ni dëëra yaa mänö ki uutjïëth
dïwït.
5 A wø caatha jöörï cooth,
ni bäŋ gïn mo cwanynya tieta.
6 Wui Jwøk, a kwaya ïïni, kiper
ŋääa ni gïno kwaa tïïyï tïïö
jïra;
cek ïthï ni wïnynyï luumma.
7 Ï na dïkunyi mar jø wø kan rege
buutï kiper nyïïmän moge;
nyooth mëër marï ni wø ba jøøl
ki jöö mo rëëma ec.
8 Gwøk aani kaamar guu waŋ,
ni kanï aani tiet bwöpï,
9 kiper jø raay ni wø many man
raanyge aani,
ni beege nyïïmänna moa näk a
ege tii dïër wø many aani naa
'näkge.
10 Wïthge ege cïëgö ki gïï wø jwør
jø møøki,
ni ge cäänö ni ge töödö.
11 Gena nø lään bääta, ni ennø, a
ege tii dïër;
ni ge manynya jöö man raanyge
aani ki gø.
12 Ge caala ŋuu mo manynya gïn
jaae nee came,
ni caalge nyi ŋuu mo omøør piny.
13 Wui Wuuö Jwøk, ö maal, ni päärï
yïthakicwa ni böötï geni.
Køny aani ceŋ jøøa reyø ki køør
mano tïïyï ko opëëllö marï.
14 Wui Wuuö Jwøk, ki køør teegï,
køny aani ceŋ jiy,
ni beege jøøa näk ojäŋ ki jap
bäät piny.
Yïthge opääŋï ki gïïa näk iï kanø
kiperge,
ni jïtge ko obwöre mo thööth ki
køør mana manyge,
ni wecge japge jï obwöre moge.
15 'Ba aani ki dëëra, täärnyïmï
oneena ni bäŋ ajäla bääta këët.
Kanyo pääa,  a puta bëëtö ni
yia met ki køør mano bëëda
buutï.
&Manøgø beeye duut mana cak Deebiti ni mare lam.
@
*#Duut Mo Pwøca Wuuö Jwøk Kiper Køny Mare
1 Wui Wuuö Jwøk, ï na teek mara,
a mëër ki ïïni.
2 Wui Wuuö Jwøk, ïïna teek mara,
ni ïïna kar gwøk røk kipera,
ni beeye ïïni wø piem aani.
Ïïna Jwøk mara møn, ni teek
mara wø jooda baŋï,
ni beeye ï wø kana raa buute.
Ï caala kwöt leny naa gëëŋŋï
gëëŋŋö ki gïï mo leth,
ni beeye ï na pïëmi mara,
niï caala kiir kipera mo ogeerø
ni teek.
3 Wui Wuuö Jwøk, ï na näk orømø
ki pwøc,
kany wø kwaa ïïni, a wø putï ka
køny ceŋ nyïïmänna.
4 Aana bëëdö ni aano ciel thøø
dïër
kaamar dhaanhø mo omeenø ki
thøøl,
ni ö ränynyö mo päl ni pïïe bääta
kaamar naam mo pänhnhö.
5 Kar thøø atïmö ni cään ki aani,
naa ee meenø kaamar thøøl
møn,
ni thøø bëëdö naa ee ciiø kaamar
abïëp.
6 Wui Wuuö Jwøk, kanya ena yïth
gïï mo leth, aana jwöŋö dëërï;
aana jwöŋö dëërï møn kiper
køny, ï na Jwøk mara, 
ni ö dwøra ni wïnynyï gø niï ena
kar bëëtö marï.
Aana jwöŋö kiper køny, ni putï
gø wïnynyö møn.
7 'Ba ki køør teegï, piny aput tïmö
ni kwanynyi ni jäŋŋi,
ni ö tiet kïte ni putge rege tuk,
ni putge tïmö ni jäŋŋi ki køør
wëër marï.
8 'Ba kanya jwïëyï ki jwïëy mo dwøŋ,
jïrö mo päl aput nitul ki ummï,
ni ö maaci ki cuk mo oäpö mo jiy
di thöörö ni öge wøk ki dhiï.
9 Wui Wuuö Jwøk, maal ajapï ni
ööï piny,
ni kanya cäädhï, kuna näk da
tietï piny da pöölö mo cøl døc.
10 'Ba ïïna put mäännö niï ena bäät
nyïïatwiel maal mana cwøl ni
kirubël;
niï määnni ka yi jamø.
11 'Ba deŋŋï bäre atïïyï na muudhö,
ni tïme na gïn gëëŋ ïïni,
ni ö pøølli mo nëëni na køth ni
put maal gääbö.
12 Ni tar mo dwøŋ cäädhö nyïmï,
ni ö peyi ka agaackøth mo malla
yi pöölö mo odhïŋ ni putge
pöödhö ki nyïmï.
13 Wui Wuuö Jwøk, dwørï awïnyö
kaamar køth mo pöödö maal,
ni caanï marï, ï na Jwøa Dwøŋ ni
en Maal.
14 Ni tïïyï køth ni pöödö bäät
nyïïmän,
ni caala man wø thöödhö ka
athëëre,
ni ö nyïïmänni ni putge keethø,
ni putï wïthge kier ka agaackøth
mo mal døc.
15 Wui Wuuö Jwøk, kanya wëërï ki
nyïïmännï niï jooga geni,
kanya jwïëyï ki jwïëy mo dwøŋ,
tiet ŋøøm aput nëënö,
ni ö pï naama dwøŋ ni pääŋge
rege këël mana nëën ŋøømmi.
16 Ï na Wuuö Jwøk, cerï arwääï niï
ena maal, ni lwørï aani;
ni kälï aani wøk ki yi bëëtö mo
leth,
ni caala man wø lääm dhaanhø
wøk ki tiet pïï.
17 Aana piemï ceŋ nyïïmänna moa
bëëdö ni teeka ge bääta,
ni beege nyïïmänna moa teek
døc ni kaala aani,
ni beege jøøa bëëdö ni män ki
aani.
18 Kanya bëëda ni aano ränynyö,
nyïïmänna aö maal bääta,
'ba ï na Wuuö Jwøk, ïïna bëëdö
niï køønynya aani;
19 ni kälï aani wøk ki kany mo
diiny mo jwïëya omiiø yie;
ni japï jöö jïra ni dunynya wøk ki
yïth gïï mo leth,
ni kønyï aani kiper mana bëëdï
niï mëër ki aani.
20 Ï na Wuuö Jwøk, aana cunnï ki
køør bëëtö mara na beer;
ni ŋatï aani ki køør mana waany
dëëra ni bäŋ raay.
21 Kiper aana bëëdö ni luupï yaa
gwøø, ï na Wuuö Jwøk;
ni bäŋ gïn mo raac mo yaa tïïö
mo pää aani ki ïïni, ï na Jwøa;
22 kiper aani luup ŋøl moï bëët ena
nyïma,
ni kära gaa wøk ki ciik moï.
23 Aana bëëdö ni bäŋ gïn jøøŋŋi ri
bëëtö mara nyïmï,
ni bëëda ni raa yaa gwøø ki raay.
24 Kiper manøgønø, ï na Wuuö
Jwøk, aana cunnï ki køør
bëëtö mara na beer,
ki køør bëëtö mara na bëëda ni
dëëra waany nyïmï, ni bääta
bäŋ raay.
25 Wui Wuuö Jwøk, mëër marï ni
wø ba jøøl wø nyoothï nyoodhø
jï jø wø bëëdö ki bëët-mëër,
ni nyoothï bëëtö marï na näk
kare jï jø wø bëëdö ki bëëtö
ma kare.
26 Tac cwïny marï wø nyoothï
nyoodhø jï jø wø bëëdö ni
cwïnyge tar;
'ba ï wø bëëdö ni waŋï riek bäät
jø wø bëëtö marge ba tiir.
27 Jøøa no ocaarø wø kønyï kønyø;
'ba jø wø töödö, wïthge wø dwøgï
piny.
28 Wui Wuuö Jwøk, beeye ï ni wø
cïpi ki tar jïra;
ni beeye ï na Jwøa ni wø wiil
muudhö mara na tar.
29 Ki køør teek marï, a wø reŋŋa
baŋ jø wø ö baŋ twëër;
ni beeye ï na Jwøa ni wø mooc
aani ki teek mo päära yi kiir
mar nyïïmän ki gø.
30 'Ba ï na Jwøk, bäŋ gïn jøøŋŋi ri
bëëtö marï,
ni luubö marï adïëri;
niï bëëdö niï caala kwöt leny jï
jiy bëët mo wø kan rege buutï.
31 ?Aŋø, da jwøk mør këët mo caala
ïïni, ï na Wuuö Jwøk?
?A da ŋat mo teek mo caala ïïni,
ï na Jwøwa?
32 Beeye ï Jwøk ni wø tïïc aani ni
teek;
ni beeye ï wø tïïc bëëtö mara ni
bäŋ gïn jøøŋŋi ree.
33 Tieta akwathï ni tïmge ni jööt ni
caala tiet aŋer,
ni tïïyï aani naa cuŋŋa naa teek
kwöra perge leth na en bäät
thuuri.
34 Aana pwönynyï ki uutjïëth leny,
ni tïme ni løny jïra ki man
thöödha ka atheerø ma atum
mare tïïc ka nywïënyö ma
jwïël.
35 'Ba ï caala kwöt leny jïra ni wø
piem aani,
ni beeye ï wø jøl aani ki cer
cwïïï,
ni ö kønynyi marï ni put kara tïïc
ni dwøŋ.
36 Waŋjöö ajapï ni dwøŋ nyïma,
ni kära tiera cwaanyø.
37 Aani, køør nyïïmän 'moa aŋwiea
ni puta ge mak,
ni kära duu ŋääa këël mana ö
nyïïmänna na thumge.
38 Nyïïmän 'moa wïthge adïïra
møn, ni puta ge nyath na bäre,
ni tïme ni ba løny jïge ki man
öge maal këët;
ni putge bëëtö ni geno pädhö
tieta.
39 Ï na Wuuö Jwøk, aana mooyï ki
teek mo këëda ki gø ri leny,
ni ö jøøa ö maal bääta ni putï
wïthge dwøk piny jïra.
40 Ïïni, nyïïmänna atïïyï nee ŋäthge
luuge baŋa ni reŋge,
ni ö jøøa bëëdö ni män ki aani,
ni puta ge thöör.
41 'Ba kanya jwöŋge nee ge køny,
bäŋ ŋat mo okøny geni;
këël mana kwacge ïïni, ï na
Wuuö Jwøk, bäŋ gïn mo iï løø
jïge.
42 Køøre nø, gena puta nyath këël
mana tïmge ni caala tør mo
okwør jamø,
ni nyøra geni kaamar odhöönh
mo ena dï jöö.
43 Aana kønyï ceŋ jø powa moa
bëëdö ni gëëmö ki aani;
ni tïïyï aani nee wïth juurre
tïmge ni ena tiera;
këël wïth juurre mo kuua, ge
puta bëëtö ni ge bëënna aani.
44 Juurre mo path, a wø wøørge
wøørø ni dëëtge rïïŋö ki lwär,
ni kany wø cäänna geni, dwøra
wø wïnyge wïnynyö.
45 'Ba geni, bäätge opädhö, 
ni öge wøk yïth kiiri moge moa
no ogeerø ni teek ni dëëtge
kwanynyi.
46 Wui Wuuö Jwøk, ï nut niï kwøw
møn.
Pwøc en jïrï, ï na teek mara;
beerra man ö nyeŋŋï ni wïnye, ï
na Jwøk ni wø piem aani.
47 Beeye ï na Jwø wø cool kwöra
dëët nyïïmänna,
ni wø tïïc wïth juurre nee bëëtge
ni ena tiera.
48 Beeye ï thuwø ni wø køny aani
ceŋ nyïïmänna;
ni tïïyï jøøa ö maal bääta nee
bëëtge ni ena tiera;
ni kälï aani wøk ceŋ jø kwöri.
49 Wui Wuuö Jwøk, ï pwøa pwøø dï
wïth juurre,
ni wära ki duut naa pwøya nyeŋŋï.
50 Beeye ï wø køny aani, a na tïïyï
na nyeya;
ni ö mëërri marï na näk ba jøøl
ni putï gø nyooth jïra,
a na tïïyï nee wïïa thïïmmi ki
maaw niï røønya aani;
ni ö mëërri manøgø ni put bëëtö
ni nut kipera, a na Deebit en,
ni pïïe baŋ nyïïkwaaya ni ba cuŋ.
&Manøgø beeye duut mana cak Deebiti
ni pwøya Wuuö Jwøk ki køør pïëm
mana piemi ya Wuuö Jwøki ceŋ
nyïïmänne bëët, këël cer Cøøl.
@
*#Duut Mo Pwøca Jwøk Kiper Gïïa Tïïe Këël Gïïa Ceme
1 Maal cara ajiem Jwøk,
ni bëëdö ni nyøtha tïïe mo cere.
2 Dïcäŋ man nø bëëdö ni køpa
ajiem Jwøk jï dïcäŋ maya,
ni wäär man nø bëëdö ni nyøtha
tier ajiem manøgø jï wäär
maya.
3 Geni, ge bäŋ dhøkge mo ge
cäänö ki ge,
ni bäŋ luup mo caange mo wïnyö;
4 'ba döötge poot pïï dï piny bäre,
ni ö luupge ni këët teegi mo piny
bäre.
Jwøk atïïö ki kar bëëtö maal
kiper cäŋ,
5 ni tuul cäŋŋi wøk ki yie
kaamar ŋat nywöm mo ö wøk ka
yi øde,
ni ö wøk ni caala ŋat ŋwïëy mo
teek mo rïïŋi ni yie met.
6 Eni tuulö ki kare ni wø tuule ki
yie,
ni caath maal bäre këël kanyo
pïïe kany wø päth yie,
ni bäŋe gïn mo bøth ni ba
lëënhnhi.
7 Ciik Wuuö Jwøk tiir,
ni jwïëc dhaanhø wø døøye mo
nyään.
Luum Wuuö Jwøk di ŋäädhö,
ni ŋat wø poot bäŋ gïn mo ŋääe
wø di mooø ki leec wïc.
8 Ciik Wuuö Jwøk beege karge,
ni cwïny dhaanhø wø døøcge mo
met.
Gïïa cem Wuuö Jwøki bäŋ gïn
mo raac rege,
ni nyeŋ dhaanhø di jabø ni
døøcge ge mo tøŋ.
9 Ki man lwäär Wuuö Jwøk beeye
gïn mo beer,
ni beeye gïn mo bëëdö na bäre
bäre.
Luup ŋøl mo Wuuö Jwøk beege
adïëri,
ni ge bëëdö ni beyø karge bëët.
10 'Ba gïïögø bëët di manynyø døc
ni kaala man wø many warkey;
di manynyø møn ni kaala warkey
mana tøŋ døc.
Gïïögø bëët met døc ni kaala
maar kïc, 
ni met marge kaala ŋweeth maar
kïc ma tëëma.
11 Wui Wuuö Jwøk, ciik moï beege
ni wø kööm aani, a na laŋŋï;
ni näk mo geno gwøø, da gïn mo
dwøŋ mo duuge duuö.
12 ?'Ba aŋa ni maar bääyö mare
caar e keere?
Wui Wuuö Jwøk, wec gïïa baaa
ni kuua, ni wëënnï aani.
13 Män aani thuwø ki gïïa reyø nee
ba kama ki teek wïc mara;
kära tïmö ni aana laŋŋø mar gïïa
reyø.
Køøre nø, a bëëdö ni bäŋ ajäla
bääta,
ni dööŋa wøk ki bëët adhala kare
bäre.
14 Wui Wuuö Jwøk, ï ni wø kana
raa buutï, ni bee ï ni wø piem
aani,
beerra man ö luupa ka acaare
'moa
ni tïmge ni mïërö nyïmï.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Kwaca Jwøk Kiper Nyeya Nee Nyïïmän Bööte
1 Beerra man ö Wuuö Jwøki ni
wïny kwac marï kany wø näk
miï ena yïth gïï mo leth;
beerra man ö eni na Jwø Jeekap
ni koor ïïni.
2 Beerra man ö Wuuö Jwøki baŋï
ki kar bëëtö mare na en bäät
Kïn Dhayan,
ni køny ïïni ni mooc ï ki teek.
3 Beerra man ö Wuuö Jwøki ni par
wïïe ki muuce moï bëët,
ni put bëëtö ni yie met ko
olämme mo wø waaŋ bäre mo
wø cïpï.
4 Beerra man ö Wuuö Jwøki ni tïïc
gïï wø caarï bëët nee thurge
karge,
ni tïïe ka køør mana manynyï ki
cwïnyï.
5 Waani wa wär ki duut ni
yïthwa met kiper mano böötï
nyïïmännï,
ni tïŋwa bëëre mowa maal ki
nyeŋ Jwøø.
Beerra man ö Wuuö Jwøki ni
wëëk gïï wø pëënynyï baŋe
bëët thur karge.
6 'Ba ennø, ŋääa ni Wuuö Jwøk
dhaanhnhe na wï gø thïïmme
ki maaw ni røønya gø na nyeya
kønye kønyø,
ni ö Wuuö Jwøki ni wïny kwac
mare ki maal kar bëëtö mare
na en kur keere,
ni køny eni ki køny mo dwøŋ ki
køør teek mare.
7 Jø møøk ŋäätha jïëth leny mo wø
tut okwëënyi,
ni ö møga ni ŋääthge okwëënyi
mo leny;
'ba øøni, ø ŋäätha teek Wuuö
Jwøk, Jwøk marø.
8 Geni tietge ocwanyge ni päthge,
'ba øøni ø ööa maal ni cuŋŋö ni
ø teek.
9 Wui Wuuö Jwøk, køny nyeya nee
nyïïmän bööte;
wïny marwa kany wø kwacwa ïïni.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Pwøca Wuuö Jwøk Kiper Man Wø Tïïe Kiper Nyeya
1 Wui Wuuö Jwøk, nyeya yie atïmö
ni met ki køør teegï,
ni yie mïnni ka køør mana kønyï
eni.
2 Gïna manynye døc ki cwïnye
atïïyï jïre;
gïna kwaae kärï mänö ki eni.
3 Ïïna ö baŋe ni tïïï ki gïï mo beyø
jïre,
ni kïthï wïïe ka aduda mo tïïc ka
warkey.
4 Ïïna kwaae kiper nee bëëde ni
kwøw, ni cïpï gø jïre,
ni mooyï eni ki nïr kwøw mo
puta bëëtö na bäre bäre.
5 Ajiem mare atïmö ni dwøŋ døc ki
køør køny marï;
ena mooyï ka ajiem ki wödö
møn.
6 Ena tïïyï nee bëëde no ogwïëdhö
na bäre bäre,
ni døøyï yie mo met kiper man
wø nudï buute.
7 Nyeya bëëdö ni ŋäätha Wuuö
Jwøk;
'ba kiper mana ö Wuuö Jwøki,
Jwøa Dwøŋ ni en Maal, ni
mëëre ki nyeya ki mëër mo ba
jøøl,
eni na nyeya puta bëëtö kare ni
teek.
8 Ï na nyeya, nyïïmännï bëët magï
maaø;
jø wø män ki ïïni magï maaø
møn ki køør teek marï.
9 Kanyo nyoothï dëërï, geno
raanynyï kaawat man wø ö
maaci wø räänye;
ge raany Wuuö Jwøki raanynyø
ni thumge ki køør wëër mare ni
wø liel kaamar maac.
10 Nyïïge oraanynyï bäät piny na
bäre bäre;
këël nyïïkwaacge thuwø wïthge
odïïrï yïthakic jiy.
11 Këël nyïïmän moï doo cädö ki gïï
mo reyø kiperï,
ni tutge ki luubö, luummeca ba
thur kare jïge.
12 Geno thööyï ka athëëre,
ni døøge køørge.
13 Wui Wuuö Jwøk, bëëdï ni karï
dwøŋ ki køør teegï.
Waano wär ki dudi ni pwøcwa
ïïni kiper teek marï.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Kwaca Wuuö Jwøk Kiper Køny Mare
1 ?Wui Jwøk, Jwøa, aŋø ni weyï
aani en?
?Aŋø ni tïïyï karï ni bäär ni ba
kønyï aani en?
?Na aŋø ni ba kønyï aani kany
wø jwöŋa dëërï?
2 Wui, ï na Jwøa, a jwöŋö dëërï ki
dïcäŋ cooth,
'ba bäŋ gïn mo løgï jïra,
ni jwöŋa dëërï ki wäär thuwø, ni
dëëra ba jwöma ki jwøk.
3 'Ba ïïni, ïïna Jwøk miï ena kur keerï,
niï bëëdö ni jø Icriel pwøya ïïni.
4 Wëëkwa abëëdö ni ge ŋäätha ïïni;
ïïna ŋääthge møn, ni piemï geni.
5 Gena jwöŋö dëërï ni piemï geni;
ïïna ŋääthge, 'ba ŋäädhe marge
kär aay jaak.
6 'Ba aani, a paa dhaanhø; a röömi
ka twöŋö.
Aano taak jiyi, naa bëëdö naa
ege päädö.
7 Jø wø joot aani bëët a wø buuge
buuö,
ni lëëpge wø rwääge wøk ni
wïthge tuuŋge tuuŋŋö, ni köge,
8 «Eni kee Wuuö Jwøk ee ŋäädhö.
?Aŋø, Wuuö Jwøk ba køny eni
ŋø?
?Aŋø, ni näk mo Wuuö Jwøk yie
met ki eni, eni ba kønyi Wuuö
Jwøki aperŋø?»
9 'Ba ï na Wuuö Jwøk, beeye ïïni
na tïïc aani nee lwaarø ki aani,
ni gwøgï aani kanya ena köör mera.
10 Ki mana ö mera ni lwaare ki
aani, a ena cerï,
ni beeye ïïni na Jwøa ki mana
täge naa ena yi mera.
11 Wui Wuuö Jwøk, kär karï tïmö ni
bäär ki aani,
kiper gïï mo leth karge cään,
ni bäŋ ŋat mo køny aani.
12 Nyïïmänna moa thööth aana
cielge dïër,
ni caala man wø tïïc rwäth dhäki
moa teek mo jø Baacan.
13 Nyïïmänna atïmö ni caala ŋuu
mo dhee ee ŋaamø,
ni märö ni manynya man cam
dhaanhø.
14 Aana tïmö naa jääk døc,
ni ö nyeŋ cuuwa bëët ni panyge
rege,
ni puta lwäyö døc.
15 Cwaaga atal na bäre,
ni ö leeba ni neebøønhnha wøk,
ni tïïyï a kaamar dhaanhø mo
othøw.
16 Jiy mo tïïö ki gïï mo reyø
aana cielge dïër kaawat man wø
tïïc guuwi;
ceŋŋa ki tieta agurge.
17 Cuuwa bëët atïmö ni løny ki
kwaan jïra.
'Ba nyïïmänna bëëdö ni neeta
aani ni ge buua aani.
18 Abïïe moa en dëëra apääŋge
yïthakicge
ki køør nyuuthe mo wø tïïc ni
pätha baŋ ŋati man nø.
19 'Ba ï na Wuuö Jwøk, kär karï
tïmö ni bäär ki aani;
ï na pïëmi mara, laar rwänh
kuna kønyï aani.
20 Gwøk jwïëya naa ba 'näk ko
opëëllö,
ni gwøgï jwïëya ceŋ nyïïmänna.
21 Piem aani ceŋ nyïïmänna moøgø
ni caal ŋuuwe yøø;
piem aani møn ceŋ nyïïmänna
moøgø ni caal jööpe yøø mo
tukge beth.
22 Aani, nyeŋŋï caana caanø jï
nyïïmera ma jø Icriel,
ni pwøa ïïni kany wø dee acooŋ lam.
23 Uuni ni wø lwäär ki Wuuö Jwøk,
pwøyu Wuuö Jwøk;
uuni na nyïïkwaac Jeekap bëët,
jiemmu Wuuö Jwøk,
ni wøørru eni, u na nyïïkwaac
Icriel bëët.
24 Kiper eni ŋat mo ocaannø ba
taae wala ba kwiere,
ni täärnyïme ba kane ki gø,
'ba kany wø ö ŋatøgø wø kwac
eni, dwør gø di wïnynyö.
25 Wui Wuuö Jwøk, a wø mooyï
mooø ki teek man pwøa ïïni ki
gø dï acooŋ lam mo dwøŋ,
ni cïba gïïa kööŋa ki ge jïrï ni
nëënö jï jø wø lwäär ki ïïni.
26 Jøøa no ocaannø cämö ni jäŋge;
jø wø many Wuuö Jwøk, Wuuö
Jwøk opwøcge.
'Ba ennø, u bëëdö nou kwøw.
27 Jø bäät piny bëët wïthge ocaarge,
ni duuge baŋ Wuuö Jwøk.
Ni ö wïth tuŋi mo juurre bëët
ni wøørge eni.
28 Kiper Wuuö Jwøk beeye nyeya,
ni wïth juurre bëët ena cere.
29 Jøøa no okwär bäät piny bëët
geno cämö ni wøørge eni;
këël jøøa can bëët thuwø ni wø
karge cään ki thøø
cøŋge këëlge piny ni kuulge
wïthge piny nyïme,
ni beege jø wø rege ba løny køny
keerge ki teek marge.
30 Jiy moo nywøl yi nyïme obëëdö
ni tïnynya Wuuö Jwøk, 
ni ö jiyi ni caange gïre jï
beenhnhe moo ööi;
31 ni öge ni caange adïëri mare jï
jiy moa näk poot kär nywølø,
ni ge caana gïna tïïe kiree.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Nyootha Gø Ni Wuuö Jwøk Beeye Dïkwääy
1 Wuuö Jwøk beeye dïkwääy mara;
bäŋ gïn maa can ki gø.
2 A wø mooe mooø ki cam ni jäŋa,
naa bëëdö kaawat man wø bëët
dielli mo obut piny yi luum mo
pulli;
ni bwøth aani ki buut pïï mo tøŋ.
3 Jwïëya wø døøye mo nyään,
ni bwøth aani ki øtjöö mo beer
kiper nee nyeŋŋe pwøc.
4 Wui Wuuö Jwøk, këël a doo
cäädhö kany mo cøl ma kar
thøø,
bäŋ gïn mo lwäära lwäärö,
kiper ï nut buuta;
cwïnya wø cømï cømø kany wø
koorï aani,
kaawat man wø ö dïkwääy wø
koor dïëk ni cere da tøŋ ki
waragööy.
5 Wui Wuuö Jwøk, cam wø jiiŋŋï
jiiŋŋø jïra kaamar dhaanhø mo
pänhnha wëëllö,
ni wïïrï dëëra ki maaw,
ni ö awalli mara man wø
mädha ki gø ni tïme ni päŋ ni
manynya øc piny.
'Ba nyïïmänna, ge neeta aani,
naa ba løny ki kam jïge.
6 Wui Wuuö Jwøk, ka adïëri møn,
beenynyï ki mëër marï ni wø
ba jøøl
bëëdö ni løpa køøra yïth nïr
kwøw 'moa bëët,
ni puta bëëtö yi ødï na bäre bäre.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Pwøca Wuuö Jwøk Kiper Dööŋö Mare
1 Piny bäre ki jammi bëët moa en
yie beege mo Wuuö Jwøk,
këël jiy bëët mo bëëdö yie en.
2 Kiper eni piny acwää bäät näpa
døøŋŋø,
ni këël tier gø piny ni teek.
3 ?Aŋa ni løny jïre ki man eth bäät
Kïn Wuuö Jwøk?
?Na aŋa ni løny jïre ki man
cuŋŋe kar bëëtö mar Wuuö
Jwøk na en kur keere?
4 Beeye ŋat mo bëëdö ni tïïe moe
ka acaare moe beyø,
na ŋat mo cwïnye ba en køør gïn
mo patha adïëri,
ni ba kööŋ ni mare cwøk.
5 Teeŋ ŋatøgø gwïëth Wuuö Jwøki
gwïëdhö,
ni jïëyi ya Jwøki ni mare beer, ni
beeye Jwø wø piem eni.
6 Jiy mo caala teeŋ ŋatøgø beege
jø wø bëëdö ni manynya Wuuö
Jwøk,
ni wø many eni, eni na Jwø
Jeekap.
7 Wui dhøk kiiri, japu rou;
japu rou, u na dhøk kiiri moa
cääŋŋe,
kiper nee nyenynya näk ajiem
mare päl nee dunynye.
8 ?Aŋø, nyenynya näk ajiem mare
päl aŋa?
Beeye Wuuö Jwøk na teek na
dwøŋ,
ni bee eni na Wuuö Jwøk ni wø
nyooth teek mare kany wø näk
ri leny.
9 Wui dhøk kiiri, japu rou;
japu rou, u na dhøk kiiri moa
cääŋŋe,
kiper nee nyenynya näk ajiem
mare päl nee dunynye.
10 ?Aŋø, nyenynya näk ajiem mare
päl aŋa?
Beeye Wuuö Jwøk, eni na wïth
jammi bëët,
bee eni na nyenynya näk ajiem
mare päl.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Kwaca Jwøk Nee Raay Wëënne
1 Wui Wuuö Jwøk, a bëëdö na
acaara mara bäre ena baŋï,
2 naa bëëdö naa ŋäätha ïïni, ï na
Jwøk mara;
kär wïïa wëëk lääö,
ni ba wëëgï nyïïmänna ŋeethø
bääta.
3 Ka adïëri møn, jø wø raŋ jïrï
wïthge ba lääi,
'ba jø wø bëëdö ni kämö jaak
wïthge olääi.
4 Wui Wuuö Jwøk, nyooth jöörï
jïra,
ni pwönynyï aani ki man cäädha
jöörï.
5 Bwøth aani ki jöörï na näk adïëri
ni pwönynyï aani,
kiper bee ï na Jwø wø piem aani,
naa bëëdö naa raŋŋa jïrï cooth ki
yïth nïne bëët.
6 Wui Wuuö Jwøk, par wïïï ki met
ec marï,
ki mëër marï ni wø ba jøøl,
kiper beeye bëëtö marï cøøn ki
mana täge ya acääŋŋe cøøn.
7 Kär wïïï parï ki raay moa tïïa
naa poot thiinh, këël gïïa baaa;
Wui Wuuö Jwøk, lääŋ aani
ki køør mëër marï ni wø ba jøøl
ki beer marï.
8 Wuuö Jwøk beer ni mare thïïŋ;
kiper manøgønø, jø raay wø di
pwönynyö ki jöö mo beer.
9 Eni jøøa mwöl wø di bwødhø ki
jöö ma kare,
ni pwöny geni ki jööre.
10 Jöör Wuuö Jwøk beeye jöö ma
adïëri ni yie da mëër mo ba
jøøl
jï jø wø gwøk luumma tuude ki
gïïa caane.
11 Wui Wuuö Jwøk, wëën gïïa baaa
ki køør nyeŋŋï,
kiper raay 'moa thööth.
12 Ŋat wø lwäär ki Wuuö Jwøk
onyuunh Wuuö Jwøki ki jöö man
caadhe.
13 Eno bëëdö ni bëëtö mare bäre
beer,
ni tïm ŋøømmi ni ena ceŋ
nyïïkwaaye.
14 Wuuö Jwøk gïïa en cwïnye caane
caanø jï jø wø lwäär ki eni,
ni lam tier gïna näk ee tuudö
jïge.
15 Aani, a wø raŋŋa jï Wuuö Jwøk
cooth,
kiper eni tieta käle wøk ki ya
abïëp.
16 Wui Wuuö Jwøk, luu nyïmï baŋa
ni kønyï aani ki køør met ec
marï,
kiper aano dööŋ keera ni aano
caarø.
17 Gïï wø raany cwïnya athöönhnhö;
beerra man kälï aani wøk ki yïth
gïïa leth ni wø jwøra.
18 Raŋ caarø ki teek bëëtö mara,
ni wëënnï raay 'moa bëët.
19 Aŋø ni ba raŋï nyïïmän 'moa nø,
kiper gena tïmö ni ge thööth, 
ni mänge ki aani ki män mo
dwøŋ døc.
20 Koor aani ni kønyï aani;
kär wïïa wëëk lääö, kiper raa yaa
kan buutï.
21 Beerra man ö bëëtö mara na beer
na thïïŋ ni gwøk aani,
kiper a bëëdö naa raŋŋa jïrï.
22 Ï na Jwøk, køny jø Icriel
yïth gïïa leth bëët ni en bäätge.
&Manøgø beeye duut Deebit.
@
*#Duut Ŋat Mo Bëëtö Mare Kare Mo Kwaya Jwøk Kiper Nee Ŋunni
1 Wui Wuuö Jwøk, ŋun aani,
kiper a bëëdö ka bëëtö mo tiir,
naa bëëda naa ŋäätha ïïni, ï na
Wuuö Jwøk, ni cwïnya ba
wiila.
2 Wui Wuuö Jwøk, many yia ni
raŋï aani døc;
ni raŋï cwïnya ka acaara mara
bäre.
3 Kiper a bëëdö naa lääŋŋa mëër
marï ni wø ba jøøl,
naa cäädhi ka køør adïëri marï.
4 A bäŋ wø pï piny kanya ciel ki jiy
mo cara oballe,
naa ba cäädhi ki jø cwøk;
5 a män ka acooŋ jø wø tïïö ki gïï
mo reyø,
naa bäŋ wø pï piny kanya ciel ki
jø raay.
6 Aani, ceŋŋa lwøa lwøø naa
nyootha gø ni bäŋ raay cwïnya,
ni wïra deŋ gïn wø cïp olämme
bääte marï, ï na Wuuö Jwøk,
7 nee gïrï køba naa dwøga met ec,
naa cara tïïe moï bëët ni wø
rëëm ec.
8 Wui Wuuö Jwøk, yia met ki øtø
marï na näk kar bëëtö marï,
ni beeye kany wø joot ajiem marï
yie.
9 Kär a 'nägï ki jø raay na aciel,
ni ba raanynyï aani na aciel ki jø
wø nääö ki jiy,
10 ni beege jø wø tudö ki gïï mo
reyø,
ni wø kädi ki jammi mo wø cïp
ki piny.
11 'Ba aani, a poot cäädhi ka jöö
mana na adïëri;
put aani køny ki køør met ec marï.
12 Ennø, aana nø pïï kany mo leer;
ni bëëda naa pwøya Wuuö Jwøk
ki jø acooŋa na aciel.
&Manøgø beeye duut Deebit.
@
*#Duut Mar Ŋat Mo Lääŋŋa Wuuö Jwøk
1 Wuuö Jwøk beeye tar mara ni
beeye dïkunyi mara;
?aŋø, da ŋat mo daa lwäärö këët
nø?
Wuuö Jwøk bee eni ni wø gwøk
jwïëya;
?aŋø, da ŋat maa böö ki gø?
2 Kany wø ö jøøa reyø ni wø öge
baŋa,
ni beege nyïïmänna ki jø wø
caan aani,
kiper nee remma kønyge piny,
tietge wø cwanyge cwanynyø ni
päänhge.
3 Këël jø leny mo thööth a dege
ciel dïër,
a ba lwäyi;
këël leny doo tägö ni ööa baŋa,
a poot bëëdö ni jïra da ŋäädhe.
4 Da gïrpiny aciel mo yaa kwaaø
baŋ Wuuö Jwøk,
ni beeye gïnögø keere ni
manynya;
ni gïn manynya en beeye ki man
bëëda Øt Wuuö Jwøk
ki yïth nïr kwøw 'moa bëët,
kiper nee beeny Wuuö Jwøk
jooda,
naa bëëda naa lääŋŋa eni yi øt
lam mare.
5 Kiper kany wø näk da gïï mo leth
mo tägö,
a wø kane kanø kar kän mare;
a wø di kanø kar kän mare møn
yi øt lam mare.
A wø kïthe maal kar gwøk røk
kany mo ena bäät kïdi.
6 'Ba ennø, wïïa tïŋa maal bäät
nyïïmänna moa ciel aani dïër;
køøre aano cïpi ko olämme jï
Wuuö Jwøk yi øt lam mare,
naa kwöŋŋö ki met ec,
ni wära ki dudi naa pwøya Wuuö
Jwøk.
7 Wui Wuuö Jwøk, wïny dwøra
kany wø kwaa ïïni;
køny aani ni wïnynyï dwøra.
8 Kanya kööï, «Ni cayu aani,»
aana köö ki yi cwïnya, «Wui Wuuö
Jwøk, ï wø manynya manynyø.»
9 Kär täärnyïmï kanï ki aani.
Kärï wëër ni riemmï aani, a na
laŋŋï,
kiper beeye ï na dïkunyi mara.
Wui Jwøk, ï ni wø piem aani,
kär a wetï, ni ba weyï aani.
10 Këël wära ki mera a dege wiiø,
ï na Wuuö Jwøk, a lwørï lwørø.
11 Wui Wuuö Jwøk, pwöny aani ki
man caadha jöörï,
ni bwøthï aani ki jöö mo tiir,
kiper da jiy mo män ki aani.
12 Kär a cïp ceŋ jø wø caan aani,
kiper da tööte mo oö maal bääta,
ni ge manynya man tïïge ki gïn
mo raac dëëra.
13 Ennø, cwïnya da ŋäädhe
ni beeny Wuuö Jwøk daa neenø
kanyo pooda naa poot kwøw.
14 'Ba ï na dhaanh Jwøk, beerra
man bëëdï niï koora Wuuö
Jwøk,
ni bëëdï niï teek ni cwïnyï iï
maaø.
Adïëri møn, bëëdï niï koora
Wuuö Jwøk.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Kwaca Jwøk Kiper Køny
1 Wui Wuuö Jwøk, a cøøra nyeŋŋï;
ï na teek mara, kär ïthï dhïŋï ki
dwøra.
'Ba ni näk miï lïŋö niï ba cäänö
ki aani,
a tïmö kaamar jø wø ci yi bwörö.
2 Wïny kwac mara
kany wø jwöŋa dëërï kiper køny,
kany wø thaaŋa ceŋŋa maal
kuna näk da kar bëëtï na en kur
keere.
3 Kär a ŋøl wøk na aciel ki jø raay,
ni beege jø wø tïïö ki gïï mo
reyø,
ni wø cäänö kere ge cäänö ka
mëër,
'ba yïthge da gïï mo reyø.
4 Beerra man cunnï geni ki køør
tïïe moge,
ki køør raay moa tïïcge.
Cun geni ki køør gïïa tïïcge ki
ceŋge,
ni coolï ka køør mana no orømø
ki geni.
5 Geno raanynyï møn, ni ba dwøgï
bëëtö marge kare këët,
kiper mana näk ge ba cädö kiper
tïïe moï, ï na Wuuö Jwøk,
moa näk iï tïïö ki cerï.
6 Pwøc en jï Wuuö Jwøk, 
kiper kwac mara awïnynye.
7 Wuuö Jwøk beeye teek mara, ni
eni caala kwöt leny jïra;
eni wø ŋäädha ŋäädhö, ni køny aani.
Kiper manøgønø, cwïnya wø
tïmö ni met,
ni pwøa eni ki duuda.
8 Wuuö Jwøk beeye teek mar jiye,
ni eni bëëdö na dïkunyi mo teek
jï ŋat wø wï gø thïïmme ki maaw
ni wø røønye na nyeya.
9 Wui Wuuö Jwøk, piem jiy moï ni
gwïëthï geni;
bëëdï ni ïïna dïkwääy marge, ni
käärï geni cooth.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Jiemma Wuuö Jwøk Kiper Teek Mare
1 Jiemmu Wuuö Jwøk, uuni ni
bëëdö maal;
jiemmu Wuuö Jwøk ki køør ajiem
mare ki teek mare.
2 Jiemmu Wuuö Jwøk ka ajiem
mana näk orømø ki nyeŋŋe;
wøørru Wuuö Jwøk kiper eni ena
kur keere.
3 Dwør Wuuö Jwøk wïnyö bäät
näpa døøŋŋø,
ni ö dwøre, eni na Jwø ajiem, ni märe,
ni tïm dwøre, eni na Wuuö Jwøk,
ni wïnyö bäät näm bëët.
4 Dwør Wuuö Jwøk teek døc;
dwør Wuuö Jwøk wïnyö ni yie da
ajiem mo päl.
5 Dwør Wuuö Jwøk jenni moa
døøŋŋø di tøyø;
kare møn, Wuuö Jwøk jer lur
Libaanø moa døøŋŋø di tøyø.
6 Eni kïte mo Libaanø di jäŋö, ni
tïmge kaamar nyïïrøøe mo
bïëdö,
ni tïïc Kïn Ciriyön ni jäŋŋi
kaawat man wø bïët nyi jööbi.
7 Dwør Wuuö Jwøk daaŋ kaamar
agaackøth.
8 Dwør Wuuö Jwøk paap di jäŋö,
Wuuö Jwøk paap Kadëc di jäŋö.
9 Dwør Wuuö Jwøk jenni moa
døøŋŋø di jäŋö,
ni jaaŋ bäätge,
ni put jiyi bëët moa en yi øt lam
mare kwöŋŋö, ni köge,
na «Ajiem en jï Wuuö Jwøk.»
10 Ööny jwïïnynya dwøŋ ena cer
Wuuö Jwøk,
Ka adïëri møn, Wuuö Jwøk
bëëdö bäät wälu na nyeya na
bäre bäre.
11 Wuuö Jwøk wø cïpö ki teek jï
jiye.
Wuuö Jwøk jiye wø gwïëdhe
gwïëdhö, ni jïtge ki bëët-mëër.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Pwøca Jwøk Kiper Køny
1 Wui Wuuö Jwøk, nyeŋŋï tïŋa
maal, kiper aana kønyï,
ni kärï yïth nyïïmänna wëëk
mïnnö bääta.
2 Wui Wuuö Jwøk, ï na Jwøa, aana
jwöŋö dëërï kiper køny,
ni døøyï dëëra mo jööt.
3 Wui Wuuö Jwøk, jwïëya amänï
ki mana dee ci kar bëët jwïëc
jøøa no othøw.
Doo na aano ci yi bwörö cøøn,
'ba aana kwøwï.
4 U na cwïnynyu en køør Wuuö
Jwøk, wärru ki duut pwøc jï
Wuuö Jwøk,
ni pwøyu eni na en kur keere.
5 Kiper wëër mare beeye kany mo
thiinh keere,
'ba met yie bëëdö këël yïth nïr
kwøw bëët.
Ni näk mo da kïmmö, beeye
wäär aciel keere,
'ba noo tïme na amöölla,
kanynyø wø put ka joot.
6 Kanya bëëda ni bëëtö mara beer,
aana cädö,
«Ni bäŋ gïn tägi dëëra na bäre
bäre.»
7 Wui Wuuö Jwøk, ki køør met yiï,
aana tïïyï naa teek kaamar kïdi.
'Ba kanya kanï täärnyïmï ki aani,
cwïnya apädhö.
8 Wui Wuuö Jwøk, aana jwöŋö dëërï,
ni kwaa ïïni, ï na Wuuö Jwøk, ni
kööa,
9 «?Ni näk mo aano thøw ni cøøa
yi bwörö,
agïnaŋø noo duue jïrï?
?Aŋø, løny ki man ö ŋøømmi ni
pwøcge ïïni?
?A løny ki man caange adïëri marï?
10 Wui Wuuö Jwøk, wïny kwac mara,
ni kønyï aani ki køør met ec marï.
Wui Wuuö Jwøk, bëëdï ni ïïna
dïkunyi mara.»
11 Kïmmö mara adøøyï meeŋ mar
met ec;
kïmmö akälï wøk bääta,
ni døøyï yia mo met.
12 Kiper manøgønø, ï pwøa pwøø ni
ba lïŋa.
Wui Wuuö Jwøk, ï na Jwøa, ï
pwøa pwøø cooth.
&Manøgø beeye duut Deebit.
@
*#Duut Ŋäädhe Mar Ŋat Mo Ena Yïth Gïï Mo Leth
1 Wui Wuuö Jwøk, a bëëdö ni raa
yaa kan buutï;
kär wïïa wëëk lääö na bäre bäre.
Køny aani ki køør adïëri marï.
2 Wïny dwøra, ni laarï aani køny.
Bëëdï niï caala kïdi mo røk kana
yie,
niï caala kiir mo teek mo gëëŋa
aani,
3 Kiper ïïna teek mara, ni ïïna kar
gwøk røk mara.
Beerra man cäädhï maal ni
bwøthï aani kiper nee nyeŋŋï
pwøc.
4 Käl aani wøk ki ya abïëba cek
jiyi kipera,
kiper beeye ï na teek mara.
5 Wui Wuuö Jwøk, jwïëya acïba
cerï;
aana wïïlï wøk, ï na Jwø adïëri.
6 Wui Wuuö Jwøk, a män ki jø wø
wøør juu mo bäŋ gïn duuge,
'ba aani, a bëëdö naa ŋäätha ïïni.
7 Yia wø mïnnö ni kanynya ki køør
mëër marï ni wø ba jøøl,
kiper mana jootï caannø mara,
ni ŋäyï gïïa leth na pïï dëëra.
8 A kärï cïp ceŋ nyïïmänna,
'ba jöö ajapï jïra.
9 Wui Wuuö Jwøk, køny aani,
kiper bääta da gïï mo leth.
Nyeŋŋa awer ni ränyge ki jwøk,
ni ö dëëra ki jwïëya ni ränyge
thuwø.
10 Kiper nïr kwøw 'moa bëët thööra
naa kïmmö,
ni cwiiri 'moa thööra naa cooyø.
Teek mara aränynyö ki køør gïïa
reyø na tïïa,
ni ö rïŋ dëëra ni ränynye.
11 Aana tïmö naa di jøøŋŋø ki køør
nyïïmänna na thööth,
na ajøøŋ kaatha jø atuti mara
døc.
Jøøa ŋäc aani gena tïmö ni lwäär
ki aani ki køør ränynyö mara, 
ni tïm jiyi bëët mo wø joot aani
øtjöö ni rïŋö ki aani.
12 Wïth jiy awïl ki aani kaamar
dhaanhø mo othøw,
ni wø bäŋ gïn mo caar kipere
këët;
aana tïmö kaamar dak mo othøw.
13 Gïïa reyø na møŋ jiy mo thööthi
awïnynya,
ni bëët lwärri mo dwøŋ naa ee
ciel dïër.
Kanya bëëtge ni ge cuuŋö kipera,
gena tudö naa 'näkge nääö.
14 Wui Wuuö Jwøk, a ŋäätha ïïni,
naa wø köö, «Ni ïïna Jwøa.»
15 Gïï wø tägi dëëra bëët ena cerï;
køny aani ceŋ nyïïmänna ki ceŋ
jø wø caan aani.
16 Wëëk tac täärnyïmï rieny bääta,
a na dhaanhnhï,
ni piemï aani ki køør mëër marï
ni wø ba jøøl.
17 Wui Wuuö Jwøk, kär wïïa wëëk
lääö,
kiper a bëëdö naa cøøra nyeŋŋï.
Beerra man tïme ni lää wïth jøøa
reyø,
ni thøwge, ni bëët jwïëcge no
onikïïl kar bëët jwïëc jøøa no
othøw.
18 Beerra man twöc lëëp jø wø
cäänö ki tööt,
ni beege jø wø car atade dëët
jøøa beyø,
ni wø bëëdö ni ŋwöö ni ge jööŋö.
19 Wui Wuuö Jwøk, da gïï mo beyø
mo thööth
mo iï cïp piny kiper jø wø lwäär
ki ïïni,
ni beege jø wø kan dëëtge buutï,
ni gïïögø tïïyï ni nëënö jï jiy bëët.
20 Jøøgø wø kanï kanø buutï kany
mo ba joot,
nee gïïa tuut jiyi kiperge nee ba
pïïcge dëëtge.
Ge wø gwøgï gwøø kar kän marï,
niï mäna geni ki gïï mo reyø mo
wø käl lëëp jiy.
21 Pwøc en jï Wuuö Jwøk,
kiper kanya bëëda päänya näk
ociel dïër,
mëër mare ni wø ba jøøl
anyoodhe jïra ki jöö mo rëëma
ec.
22 Dïkwøŋ cwïnya abwøk, ni kööa,
«Ni kara atïmö ni bäär ki ïïni.»
'Ba kwac mara awïnynyï kanya
jwöŋa dëërï kiper køny.
23 Uuni bëët, u na cwïnynyu en
køør Wuuö Jwøk,
beerra man bëëdu nou mëër ki
Wuuö Jwøk.
Wuuö Jwøk bëëdö ni gwøga jøøa
näk marge adïëri;
'ba gïn wø rømi ki jø atöör tïïe
tïïö dëëtge.
24 U bëët ni wø ŋääth køny mar
Wuuö Jwøk,
bëëdu nou teek, ni cwïnynyu you
maaø.
&Manøgø beeye duut Deebit.
@
*#Duut Gwïëth Kiper Ŋat Mo Raay Moe Owiiø
1 Gwïëth en bäät ŋat mo raay moe
owiiø,
ni moa baae orïëbö.
2 Gwïëth en bäät ŋat mo bääyö
mare ba kwaan Wuuö Jwøki
bääte,
ni bëëdö ni bäŋ cwøk cwïnye.
3 Wui Wuuö Jwøk, kanya bëëda ni
bääyö mara kära caanø,
dëëra aput ränynyö ki køør
kïmmö mana bëëda naa
kïmmö ki gø cooth. 
4 Kiper waŋcäŋ ki wäär cerï atïmö
ni ena dëëra;
ni ö teek mara ni ränynye
kaamar luum man wø raany
cäŋ öörö.
5 Køøre bääyö mara acaana jïrï,
ni kära gïna raac na tïïa kanø;
aana köö, «Ni gïïa baaa caana
caanø jï Wuuö Jwøk.»
'Ba ki køør mana nø caana gø,
bääyö mara na dwøŋ aputï wec.
6 Kiper manøgønø, beerra man ö
jiyi bëët moa cwïnyge en køørï
ni kwacge ïïni kany bëëdï niï nut
en;
køøre, këël gïï mo leth doo öö
kaamar jwïïö mo raanynya
piny,
bäŋ gïn mo pïï bäätge.
7 Beeye ïïni ni wø kana raa buute,
ni bee ï ni wø koor aani yïth gïï
mo leth;
ni laga wø cielï cielø ki jø wø
wär ki dut køny.
8 Ï wø köö, ni «Ï pwönynya
pwönynyö
ni nyuunhnha ïïni ki jöö mana
diï cäädhö ki yie,
ni pwönynya ïïni thuwø ni waŋa
ena bäätï.
9 Kärï tïmö kaamar okweeny wala
gääŋŋö ni wø bäŋ gïn ŋääe,
ni wø tïïc ni maa piny ka kaw mar
dhee kiper nee bëëde buutï.»
10 Ŋat ma ŋat adhala wø jïtö ki gïï
mo leth mo thööth,
'ba ŋat wø ŋääth Wuuö Jwøk,
mëër mo ba jøøl ena bääte.
11 U ni bëëtö maru beer, bëëdu ni
yïthu met ni kanynyu ki køør
Wuuö Jwøk.
U ni cwïnynyu thïïŋ bëët, pwøyu
Wuuö Jwøk ni döötu ena maal
ni yïthu met.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Pwøca Jwøk Kiper Tïïe Moe
1 Wui, u ni maru beer, wärru ni
yïthu met jï Wuuö Jwøk;
pwøc mïërö ka ŋat mo mare
thïïŋ.
2 Pwøyu Wuuö Jwøk ki
thoom-othïënhö;
wärru ki dut pwøc jïre nou
pöödö ki thoom mo thøøli moe
apaar.
3 Wärru jïre ki duut mo nyään,
pwötu thøme ni nyeŋŋu reegø, ni
döötu ena maal.
4 Kiper luum Wuuö Jwøk thïïŋ,
ni tïïc mare bäre tïïe no
oŋäädhö.
5 Wuuö Jwøk yie met ki bëëtö mo
beer ki ŋøl ma kare,
ni piny bäre päŋ ki mëër mare ni
wø ba jøøl.
6 Wuuö Jwøk maal acwääe ki køør
dwøre,
ni cwääc gïïa en yie bëët ki jam
dhee.
7 Pï naama dwøŋ acooŋe kaamar
acooŋ beel,
ni cooŋ ge yïth kudi kaamar beel
mo ocooŋ yïth odïï.
8 Beerra man ö pinynyi bäre ni
lwäär Wuuö Jwøk;
beerra man ö jø bäät piny bëët ni
bëëtge ni yïthge othäŋŋö ki eni.
9 Kiper ena cäänö ki dwøre, ni put
piny cwääc ki gïïa en yie bëët,
ni ö mana caane ni thur kare.
10 Wuuö Jwøk acaara mar wïth
juurre di raanynyø;
eni acaac jiy wø tïïe tïïö nee ba
thurge karge.
11 'Ba acaara mar Wuuö Jwøk
bëëdö na bäre bäre,
ni ö acaare mo wø caare ni bëëtge ni
nut këël yïth beenhnhe bëët.
12 Gwïëth en bäät jø wø Jwøge
beeye Wuuö Jwøk,
jøøa näk ee jierø na moe.
13 Wuuö Jwøk wø räŋŋö ki maal ni
raŋ piny,
ni joot jiy bëët,
14 ni raŋ jøøa bëëdö bäät piny bëët
ni räŋŋi ka kar bëëtö mare.
15 Bee eni na cwääc cwïnyge bëët,
ni tïïe moge bëët ŋääe.
16 Nyeya bäŋ wø bøth ki thøø kiper
jø leny moe na thööth,
ni ŋat leny bäŋ wø bøth ki thøø
kiper teek mare.
17 Køny mar okweeny leny ba ŋääth,
ni eni bäŋ wø kunynyi kaper
teek mare na dwøŋ.
18 Ka adïëri møn, waŋ Wuuö Jwøk
ena bäät jø wø lwäär ki eni,
jø wø ŋääth mëër mare ni wø ba jøøl,
19 nee ge kønye cer thøø,
ni gwøk geni nee kwøwge kany
wø dee käc.
20 Øøni, ø bëëdö nøø raŋŋa jï Wuuö
Jwøk;
bee eni na dïkunyi marø, ni ena
kwöt leny jïïø.
21 Ka adïëri møn, met ec marø
joodø baŋe,
kiper ø ŋäätha nyeŋŋe na en kur keere.
22 Wui Wuuö Jwøk, beerra man ö mëërri
marï ni wø ba jøøl ni bëëde bäätwa,
kaawat man bëëde niï ewa ŋäädhö en.
@
*#Duut Mo Pwøca Jwøk Kiper Køny Mare
1 Wuuö Jwøk wø pwøa pwøø
cooth,
ni bëët pwøci dhaa man wø pwøa
eni ki gø.
2 Aani, Wuuö Jwøk pwøa pwøø
kiper gïïa tïïe;
beerra man ö jøøa canni ni
wïnyge gø ni mïn yïthge.
3 Beerra man jiemø Wuuö Jwøk na
aciel,
ni tïŋø nyeŋŋe maal ø bëët.
4 Wuuö Jwøk akwaaa, ni løk kwac
mara,
ni køny aani dhøk gïïa lwäära
bëët.
5 Jø wø raŋ jï Wuuö Jwøk,
täärnyïmge tïmö ni waany
ni ba lää wïthge këët.
6 Aani, kanya bëëda yïth gïï mo leth,
aana jwöŋö dëër Wuuö Jwøk,
ni ö Wuuö Jwøki ni wïny dwøra,
ni køny aani yïth gïïa leth bëët
na en dëëra.
7 Nyïïatwiet maal mo Wuuö Jwøk
rege wø cielge cielø
lak jø wø lwäär ki Wuuö Jwøk, ni
piemge geni.
8 Bel bëët Wuuö Jwøk, nee jootï
møn ni eni beer;
gwïëth en bäät ŋat wø kan ree
buute.
9 U na jic Wuuö Jwøk, lwäärru
Wuuö Jwøk,
kiper jø wø lwäär ki eni bäŋ gïn
cange.
10 Këël nyïï ŋuuwe ge wø cännö ni
'nägi ya käci,
'ba jø wø cac Wuuö Jwøk bäŋ gïn
mo cange ri moa beyø bëët.
11 Ööu, u na nyïïa, ni wïnynyu mara,
u pwönynya pwönynyö ki jöö
man lwäärru Wuuö Jwøk ki gø.
12 ?Aŋa dïïu ni cac kwøw,
na aŋa dïïu ni yie met ki man
bëëde ni kwøw ki cwiiri mo
thööth nee gïï mo beyø joode?
13 Beerra man ö ŋatøgø ni gwøk
leebe ki raay,
ni män dhee ki luup cwøk.
14 Beerra man ö ŋatøgø ni tïïc kare
ni bäär ki raay, ni tïïc gïna beer,
ni many bëët-mëër, ni caath køør
gø døc.
15 Nyeŋ Wuuö Jwøk ena bäät jøøa
beyø,
ni ïthe ee ciiø ki kwac marge.
16 Täärnyïm Wuuö Jwøk cøl ki jø
wø tïïc raay,
ni tïïc ge nee wïc ba par ki geni
bäät piny këët.
17 Kany wø ö jøøa beyø wø jwöŋge
kiper køny,
wïny Wuuö Jwøki wïnynyö,
ni køny geni yïth gïïa leth bëët
na pïï dëëtge.
18 Wuuö Jwøk kare cään ki jø wø
näk cwïnyge opädhö,
ni bëëdö ni køønynya geni.
19 Gïï mo leth mo thööth wø tägö
dëër ŋata beer,
'ba eni wø køny Wuuö Jwøki
kønyø yïth gïïögø bëët.
20 Wuuö Jwøk ŋatøgø wø gwøe
gwøø,
ni bäŋe cöönne aciel mo toor.
21 Jø wø tïïc raay 'näk raayi nääö,
ni ö jø wø män ki jøøa beyø ni
jääli.
22 Wuuö Jwøk jiye wø wïïle wøk,
ni bäŋe aciel mo di jäälö dëët jø
wø kan rege buute.
&Manøgø beeye duut mana cak Deebiti
kanya cøøk ree nyïm nyeya ma Abimëlëk
ni ena bøøl; ni riemmi ni put aay.
@
*#Duut Mo Kwaca Jwøk Ki Man Køny Dhaanhnhe Ceŋ Nyïïmänne
1 Wui Wuuö Jwøk, ŋäbï ki jø wø
ŋäbö ki aani,
ni këëdï ki jø wø këëdi ki aani.
2 Kwany kwöt leny marï,
ni ööï maal ni kønyï aani.
3 Lwør tøŋ marï ni këëdï ki jø wø
ŋwiec køøra,
niï nyootha gø jïra ni beeye ïïni
na dïkunyi mara.
4 Beerra man lää wïth jø wø many
man 'näkge aani, ni räny
nyeŋge;
beerra man kier wïth jø wø cädö
ki gïï mo reyø nee tïïcge dëëra,
ni riem ge.
5 Beerra man køøl ge kaamar lethø
mo okøøl jame,
ni beeye nyïïatwiel maal marï, ï
na Wuuö Jwøk, noo køøl geni.
6 Beerra man tïm jöörge na
muudhö ni da adipøødha,
ni ö nyïïatwiel maal marï, ï na
Wuuö Jwøk, ni ŋwiec køørge.
7 Kiper geni akupa acekge kipera
jaak,
ni kunyge ki buur kipera ki gïn
mo bäŋ tiere.
8 Beerra man räny ge ni cwöba
dëëtge,
ni päth akumma cekge keerge
bäätge,
ni päthge yi ränynyö.
9 Køøre nø, yia omïnni ki ïïni, ï na
Wuuö Jwøk,
ni kanynya kiper mana kønyï
aani.
10 Ni kööa ki cwïnya bäre,
ni «?Wuuö Jwøk, aŋa ni pääri ki
ïïni?
Beeye ïïni ni wø køny ŋata no
ocaannø cer ŋata teek døc ni
kaala eni,
ni køny ŋata no ocaannø na can
cer ŋat wø twier gø.»
11 Jiy mo caana luup mo patha
adïëri aö maal,
ni pëënyge aani ki luup mo kuua.
12 A wø duunge duunnö ki gïn mo
raac na kar mana beer,
ni thøøa ki pänh cwïny.
13 'Ba aani, kanya bëëtge ni ge tuu,
aana tïmö naa käära keeca na
abïï ki køør kïmmö mara
kiperge,
ni dwøga dëëra piny ni bëëda ni
aano kweer ki cam,
naa lämö ni wïïa yaa kuul piny.
14 Aana jwöŋö kaawat mana daa
jwöŋö kiper nyawatwa wala
coka,
naa bëëdö kaamar dhaanhø mo
jwøga menni,
ni wïïa yaa kuul piny naa kïmmö.
15 'Ba kanya jootge aani naa ena
yïth gïï mo leth,
yïthge amïnnö ni cooŋge røkge
kanya ciel;
jø wø tïïc gïï mo reyø
dëëtge adwalge kipera ni kuua,
ni bëëtge ni ge waya nyeŋŋa, ni
ba wecge.
16 Gena kwääk bääta ni ge ŋeethø,
ni kaacge lakge bääta.
17 ?Wui Wuuö Jwøk, a kany mo
nyïëdi nø noo bëëdï niï rääŋö
jaak?
Køny aani yïth gïïö ni leth ni wø
temge yøø,
ni gwøgï jwïëya ceŋ jiy moi ni
caal ŋuuwe ii.
18 Ï pwøa pwøø dï acooŋ jøøa
thööth,
ni pwøa nyeŋŋi dï lwaak.
19 Kär yïth nyïïmänna wëëk mïnnö
bääta,
jø wø män ki aani jaak.
Kär nyïïmänna tïïyï nee nyeŋge
niiŋge bääta,
jø wø män ki aani ki gïn mo bäŋ
tiere.
20 Kiper ge ba cäänö ki luum mëër,
'ba ge wø caana luum cwøk dëët
jø wø bëëdö jaak paac.
21 Gena kwöŋŋö bääta,
ni köge, ni «Wui, wui, ïïna
jootwa ki nyeŋwa kiree.»
22 'Ba ï na Wuuö Jwøk, gïnögø
ajootï; kärï lïŋö.
Wui Wuuö Jwøk, karï kär tïïyï ni
bäär ki aani.
23 Ö maal ni cwagï aani,
ni cäänï kipera, ï na Jwøk mara
ni bee ï na kwääya.
24 Wui Wuuö Jwøk, ï na Jwøk
mara, ŋun aani, ki køør adïëri
marï,
ni tïïyï ge nee yïthge ba mïnge
bääta.
25 Ge kär tïïyï nee cäänge ki
cwïnyge ni köge, ni «Gïna
manywa ajootwa.»
Ni ba tïïyï ge nee köge, ni «Ena
raanywa.»
26 Jøøa näk yïthge met ki gïna tägö
dëëra,
wïthge olääi ni räny nyeŋge bëët;
jøøa tïïc dëëtge ni døøŋŋø bääta,
lään wïc bëëde bäätge kaamar
abïï.
27 Jø wø yïthge met ki man ŋun
aani, wär kwöŋge ki met ec,
ni cäänge ni nøøcge nøøyø ni ge
köö, ni «Dwøŋŋa Wuuö Jwøk,
eni ni wø yie mïnni kany wø tïm
bëët dhaanhnhe ni beer.»
28 Køøre nø, adïëri marï køba købø,
ni bëëda naa pwøya ïïni cooth.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Cäänö Kiper Bëët Ŋat Raay Ki Bëët Jwøk
1 Raay cäänö cwïny ŋat raay,
ni Jwøk ba lwääre na bäre bäre.
2 Dëëre wø jieme jiemø keere ni
eni beer, 
'ba raay moe ba neete, ni eni ba
män ki geni.
3 Luup mo wø cur dhee reyø, ni
beege luup cwøk keerge,
ni wïïe oløny ni ba leer, ni bäŋ
gïn mo beer mo tïïe.
4 Kanyo en kar niine mare, eni
caara gïï mo reyø,
ni dëëre wø cïbe uutjïëthe mo
patha karge,
ni gïï mo reyø ba kwiere.
5 Wui Wuuö Jwøk, mëër marï ni
wø ba jøøl dwøŋ døc no okëët
maal,
na adïëri marï okëët nyeŋ pøøl.
6 Bëëtö marï na beer ruu kaamar
kïte moa døøŋŋø,
ni ŋøl marï ŋølï ni tiet luup iï
neenø døc
ni caala man wø many gïn mo
ena yi kut.
Wui Wuuö Jwøk, beeye ïïni ni
wø køny dhaanhø ki lääy.
7 Wui Wuuö Jwøk, mëër marï ni
wø ba jøøl pere leth døc.
Jiy rege wø kange tiet bwöpï.
8 Ge wø jäŋŋa yi ødï døc ki luup
moï,
ni cïpï met yiï na päl jïge kaamar
pï naam.
9 Jøøro mar pï kwøw ena baŋï,
ni tar jootwa ka køør tar marï.
10 Put mëëyï ni wø ba jøøl cïp jï
jøøa ŋäc ïïni,
ni nyoothï adïëri marï jï jøøa
marge thïïŋ.
11 Kär jø atöör wëëk atöör bääta,
ni ba tïïyï jø raay naa riemge
wøk.
12 Jø wø tïïc gïï mo reyø pädhö;
ge pädhö ni dhäthe jïge ki man
öge maal.
&Manøgø beeye duut Deebit na
näk dhaanh Wuuö Jwøk.
@
*#Duut Mo Pöö Kiper Bëëtö Mo Beer
1 Kär wïïï kierï ka acaara kiper
bëët jøøa reyø;
ni ba keeyï per bëët jø raay.
2 Kiper ge laara ränynyö kaamar
luum mo otal,
ni närge kaamar omarø mo obäp.
3 Bëëdï niï ŋäätha Wuuö Jwøk, ni
tïïyï gïï mo beyø,
ni bëëdï yïth ŋøøpu ni ïïna ŋat
mo oŋäädhö.
4 Bëëdï ni yiï met ki Wuuö Jwøk,
køøre ïïno mooe ki gïïo manynyï
ki cwïnyï.
5 Cïp dëërï jï Wuuö Jwøk;
ni ŋääthï eni, køøre mare otïïe.
6 Eni bëëtö marï na beer otïïe ni
nëënö kaamar tar,
ni tïm bëëtö marï na näk kare
ni nëënö kaa man wø neen
gïrpiny ki dhöör.
7 Bëëdï ni ïïno göök ri Wuuö Jwøk,
ni raŋŋï jïre ni cwïnyï iï cïp
piny;
kär wïïï kierï ka acaara kiper ŋat
wø jape thöönhnhi ki køør tïïe
moe,
ŋat wø tïïc gïï wø caare na reyø.
8 Män riï ki gootø ni kwierï wëër,
kär wïïï kierï ka acaara, kiper
acaara duua gïï mo reyø.
9 Kiper jø wø tïïc gïï mo reyø ŋøla
wøk,
'ba jø wø raŋ jï Wuuö Jwøk,
ŋøøm cøøa jïge.
10 Ki kany mo thiinh ŋat raay tïmö
ni ba joot këët;
ni këël kare diï manynyø døc, eni
ba jootï. 
11 'Ba jøøa mwöl ŋøøm cøøa jïge,
ni mïn yïthge ki køør bëëtö
marge na beer.
12 Ŋat raay cädö ki jöö man tïïe ki
gïn mo raac dëër ŋata beer,
ni kaac lage bäät gø.
13 'Ba Wuuö Jwøk ŋeethø bäät ŋat
raay,
kiper ŋääe ni cäŋ ränynyö mar
ŋat raay kare cään.
14 Jø raay opëëlle moge wø wöthge
wøk,
ni niitge athëëre moge,
kiper nee jøøa no ocaannø ki
jøøa can nee 'näkge,
ki jøøa näk bëëtö marge thïïŋ.
15 'Ba opëëlle moge døøa dëëtge keerge,
ni ö atummi moge ni tøcge.
16 Beerra bëët ŋata mare beer ni
jape nøk,
ni kaala bëët kwärö mar jøøa
thööth ni wø tem raay.
17 Kiper Wuuö Jwøk teek mar jø
raay raanynye raanynyø,
'ba jøøa beyø gwøe gwøø.
18 Wuuö Jwøk bëët jøøa marge
thïïŋ ŋääe,
ni ö ŋøømmi ni bëëtge na moge
na bäre bäre.
19 Kany wø näk mo piny raac, öölö
ba pïï bäätge,
ni kany wø näk mo da käc, cam
dagø jïge mo rømø.
20 'Ba jø raay ränynyö,
ni tïm nyïïmänni mo Wuuö Jwøk
kaamar luum pwöla ni wø laar
talø,
ni rwäänyge kaamar jïrö ni wø
maayi.
21 Ŋat raay wø mäyö, 'ba eni ba
cudö,
'ba ŋata beer wø cïpö ki køør
bäth ec mare.
22 Jøøa no ogwïëth Wuuö Jwøki,
ŋøøm cøøa jïge,
'ba moa näk ee cienø, ŋøle wøk.
23 Bëët dhaanhø wø wëëga Wuuö
Jwøki thur kare,
ni tïm yi Wuuö Jwøki ni met ki
bëët gø.
24 Këël eni doo pädhö, ba pädhi ki
pänh ränynyö,
kiper cere mak Wuuö Jwøki
maaø.
25 Ki mana täga thïnhö, këël mana
jala ennø,
a kär jïtö ki ŋat mo beer mo
owiiø;
këël obwöre moe mo kwääö ki
caammi, bäŋgø thuwø.
26 Eni bëëdö ni cwïnye bäth, ni jape
wø wëëge mac cooth,
ni ö jiyi ni gwïëdhi ki køør
nyïïkwaaye.
27 Tïïc karï ni bäär ki raay, ni tïïyï
gïna beer,
køøre nø, ïïno bëëdö na bäre
bäre.
28 Kiper Wuuö Jwøk yie met ki ŋøl
ma kare.
Jøøa näk cwïnyge ena køøre ba
wiie;
ge gwøe gwøø na bäre bäre,
'ba wäät jøøa reyø ŋøle wøk.
29 Jøøa beyø ŋøøm cøøa jïge,
ni bëëtge yie na bäre bäre.
30 Ŋata beer cara luup leec wïc,
ni luup mo wø ŋøle ni wø cur
dhee beege karge.
31 Eni ciik Jwøk bëëdö cwïnye,
ni bëëde ni tiere ba cwanynye.
32 Ŋata raac bëëdö ni lepa ŋata
beer, 
ni caya man 'näk gø.
33 'Ba Wuuö Jwøk ŋata beer ba wii
cer ŋatøgø,
ni eni ba wëëk jääl kanyo ŋøl
luumme.
34 Bëëdï niï raŋŋa jï Wuuö Jwøk, ni
caathï jööre.
Karï otïïe ni dwøŋ, ni ö ŋøømmi
ni cige jïrï,
ni jootï jø raay ni geno ŋøl wøk.
35 Ŋat raay dagø mo yaa joodø mo
ogäy mo jiy ee dïïmö,
ni caala jaath mo dwøŋ mo piny
ee maaø.
36 'Ba na tïme na køøre cään, ena
rwäänyö, ni tïme ni tøør kaace
këët;
'ba kanya manynya gø, eni kära joodø.
37 Raŋ ŋat mo bäŋ ajäla bääte, ni neenï
ŋata näk bëëtö mare thïïŋ,
kiper ŋat wø bëëdö ki bëët-mëër
jïtö ki nyïïkwaaye.
38 'Ba jø wø tïïc raay, wïthge di
dïïrö na bäre bäre,
ni ö nyïïkwaacge ni ŋøli wøk.
39 Wuuö Jwøk beeye ni wø piem
jøøa beyø,
ni teek marge wø jootge baŋe kany
wø dee gïï mo leth mo pïï bäätge.
40 Ni beeye Wuuö Jwøk ni wø køny
geni ni wø piem geni,
ni käl geni wøk ceŋ jø raay, ni
kwøw geni,
kiper mana kange dëëtge buute.
&Manøgø beeye duut Deebit.
@
*#Duut Kwac Mar Ŋat Mo Cwïnye Opädhö Ki Raay Moe
1 Wui Wuuö Jwøk, kär a joogï ni
marï wëër ki aani,
ni ba wëërï kanyo pwönynyï
aani.
2 Kiper athëëre moï anø pï dëëra,
ni thielï aani piny ki cerï.
3 Dëëra ajïtö ki täw ki køør wëër
marï,
ni tïm dëëra ni ba jööt ki køør
raay 'moa.
4 Kiper raay 'moa wïïa akaalge;
ni tïmge ni peek døc ni caala tëër
mo ba løny ki tïëtö.
5 Ŋwiili 'moa, na jooda ki køør gïïa
tïïa ki bøøl mara,
ajïtö ki tuut ni ŋwääge.
6 A cäädhi ni aano gääŋ,
naa bëëdö naa kïmmö cooth.
7 Kiper dëëra waŋŋi bäre,
ni dëëra man bäre da täw.
8 Dëëra atïmö ni bäth bäre ni
ränynye,
ni bëëda naa cooyø ni cwïnya
opädhö.
9 Wuuö Jwøk, gïn manynya en
ŋäyï,
ni cooyø mara wïnyö jïrï.
10 Wenynya atïmö ni pärö, ni ö
teeki mara ni aae dëëra,
ni ö nyeŋŋa ni tïmge ni ba nëënö
këët.
11 Nyïïawääta ki jø wø mëër ki aani
karge atïïcge ni bäär ki aani
kiper ŋwiili moa en dëëra,
këël tuuŋwa kiree karge atïïcge
ni bäär ki aani thuwø.
12 Jø wø cac man 'näkge aani
abëëbe moge wø cekge ciiø
kipera,
ni ö jø wø many man tïïcge gïï
mo leth dëëra ni cäänge kiper
naa raanyge,
ni ge tudö ki luup ki piny cooth.
13 'Ba aani, raa atïïa naa caala
dhaanhø ma miiŋ, naa ba
wïnyö, 
ni tïma naa caala dhaanhø mo
bäŋ dhee mo ba cäänö.
14 Ka adïëri møn, aana tïmö naa
caala dhaanhø mo ba wïnyö,
mo bëëdö ni ba pïëmö kiper
dëëre.
15 'Ba bee ï na Wuuö Jwøk, ni wø
jïre raŋŋa,
ni bee ï na Wuuö Jwøk, Jwøk
mara, noo løk mara.
16 Kiper aana lämö ni kööa, ni
«Jø wø tïïc dëëtge ni døøŋŋø
bääta,
kär yïthge mïnnö kany wø
cwaanya tiera.»
17 Ennø, kara atïmö ni cään ki man
pädha,
naa bëëdö naa rämö cooth.
18 Aani, raay 'moa køba købø;
aana tïmö naa kïmmö kiper gïïa
baaa.
19 Nyïïmän 'moa dëëtge jööt ni ge
teek,
ni jø wø män ki aani ki gïn mo
bäŋ tiere thööth.
20 Jø wø duu gïn mo raac na kar
gïna beer,
ge män ki aani kiper mana
caadha køør bëëtö mo beer.
21 Wui Wuuö Jwøk, kär a weyï;
wui ï na Jwøk mara, kär karï
tïïyï ni bäär ki aani.
22 Wui Wuuö Jwøk, ï na dïkunyi
mara,
laar rwänh baŋa kuna kønyï
aani.
&Manøgø beeye duut Deebit
mana par wï Jwøk ki gø.
@
*#Duut Mo Nyootha Gø Ni Dhaanhø Nïre Nøk Bäät Piny
1 Aana cädö ni kööa, ni «Dëëra
gwøa gwøø ki gïno caana,
kiper nee leeba ba bääye.
A bëëdö ni dhaa yaa gwøø,
kany wø nut jø raayi buuta.»
2 Aana bëëdö naa lïŋö jaak naa ba
luubö;
'ba lïŋŋö mara bäŋ gïn mo ee
kønyø,
ni ö pänh cwïnynyi mara ni
cääth nyïme.
3 Yia acwat døc,
ni cwat ec mara kadhi ka kanya
cäda.
Køøre aana lämö ni kööa,
4 «Wui Wuuö Jwøk, beerra man
pwönynyï aani kiper aŋuun
kwøw mara,
ki kwään nïne moo beeda,
nee ŋääa ni nïr kwøw 'moa ba
kän wøk ki kany mo bäär.
5 Neenï, nïr kwøw 'moa atïïyï ni
nøk,
ni tïm nïne moo beeda ni bäŋ
karge ki baŋï.
Adïëri møn, dhaanhø ni bëëdö ni
kwøw en caala jamø jaak.
6 Adïëri møn, bëët dhaanhø caala
tïpö,
ni dijal mar jiy bäŋ gïn duue
møn;
dhaanhø jammi wø cooŋe cooŋø
kiper dëëre, 'ba ŋato käl ge
kuue.
7 «?'Ba ennø, ï na Wuuö Jwøk,
agïnaŋø noo dööŋ këët nø?
Aani, a ŋäätha ïïni.
8 Køny aani yïth raay 'moa bëët;
kär a wëëk jøøa näk bäŋ wïthge
naa jøøŋge.
9 A bëëdö naa ba luubö, ni dhaa ba
jaala,
kiper bee ïïni na tïïc gïïögø bëët.
10 Kär a jäälï këët,
kiper aana tïmö naa manynya
thøø ki køør pöödö marï.
11 Dhaanhø wø joogï jooø niï
pwönynya gø kiper raay moe, 
ni raanynyï gïï wø mëëre ki geni
kaawat man wø tïïc alweela;
ka adïëri møn, dhaanhø caala
jamø jaak.
12 «Wui Wuuö Jwøk, wïny lam
mara,
ni cegï ïthï ko oduuru mara;
kär ïthï dhïŋï ki jwøk mara.
Kiper a bëëdö buutï naa caala
dhaanhø mo path,
naa bëëdö ni aana wëëllö kaawat
mana bëët kwäya bëët.
13 Wec a turu, kiper nee yia mïnne
kany poode naa poot kär thøw
en.»
&Manøgø beeye duut Deebit.
@
*#Duut Mo Ŋäätha Jwøk Kiper Køny Mare
1 Aana bëëdö naa raŋŋa jï Wuuö
Jwøk;
køøre ïthe aciie ni wïny oduuru
mara.
2 Ni tuut aani wøk ki yi buur mo
raac,
ni käl aani wøk ki yo odhöönh;
ni cïp a bäät kïdi,
ni kïth aani kany mo bäŋ gïn mo
pïï dëëra yie.
3 Dhaa acäŋŋe ki duut mo nyään,
na man wø pwøa eni ki gø, eni
na Jwøk marø.
Gïïa tïïe oneen jiy mo thööthi ni
lwäcge,
ni tïmge ni ge ŋäätha Wuuö Jwøk.
4 Gwïëth en bäät ŋat wø ŋääth
Wuuö Jwøk,
ŋat wø ba raŋ jï jø atöör,
jø wø gaa wøk køør luup mo
patha adïëri.
5 Wui Wuuö Jwøk, ï na Jwøk
mara,
ïïna tïïö ki gïï mo thööth mo
rëëma ec,
niï lääŋŋa waani cooth.
Bäŋ ŋat mo röömi ki ïïni.
Këël a doo köö ni gïr gïïa tïïyï
caana caanø,
tïmö ni thööth døc ni ba løny ki
caan.
6 Wui Wuuö Jwøk, yiï ba met ki
muuce mo beel ko olämme mo
wø cïp;
këël olämi man wø waaŋ bäre ko
olämme mo wø cïp kiper raay,
ï kär pëëö kiperge;
'ba aana mooyï ki ïdhi nee marï
wïnynya.
7 Køøre aana köö, na «A nut ennø,
kaawat mana no ogöörö yi Wëël
Jwøk kipera.
8 Ïïni na Jwøk mara, yia met ki
man tïïa mana manynyï;
ciik moï ena cwïnya.»
9 Luup moa met kiper køny marï
akøba dï acooŋ lam mana dwøŋ.
Wui Wuuö Jwøk, ŋäyï naa kär
lïŋö ki car luupögø.
10 Aani luum køny marï kära mooŋø,
'ba adïëri marï ki pïëm man wø
piemï jiy ki gø akøba.
Aani mëër marï ni wø ba jøøl ka
adïëri marï
kära kanø ya acooŋ lam mana
dwøŋ.
11 Wui Wuuö Jwøk, kär bäth ec
marï mänï ki aani,
beerra man ö mëërri marï ni wø
ba jøøl, ka adïëri marï
ni bëëtge ni gwøga aani.
12 Kiper gïïa reyø mo ba løny ki
kwaan, aana cielge dïër;
gïïa baya aana makge,
ni tïïcge aani naa ba räŋö;
gena tïmö ni thööth døc ni kaala
jïëc wïïa, 
ni ö cwïnya ni pädhe.
13 Wui Wuuö Jwøk, beerra man
piemï aani.
Wui Wuuö Jwøk, laar rwänh
kuna kønyï aani.
14 Jøøa many man 'näkge aani,
beerra man lää wïthge ni kier
wïthge bëët.
Jøøa yïthge met ki caannø mara
beerra man riem geni ni räny
nyeŋge.
15 Beerra man ö jø wø buu aani
ni bwøk cwïnyge ki køør lään
wïc marge.
16 'Ba jø wø cac ïïni bëët
beerra man mïn yïthge ki ïïni ni
kanyge,
ni ö jø wø yïthge met ki køny marï
ni cäänge ni nøøcge nøøyø ni ge
köö, ni «Dwøŋŋa Wuuö Jwøk!»
17 'Ba aani, aano caannø naa bëëdö
naa can;
'ba ï na Wuuö Jwøk, beerra man
lääŋŋï aani.
Bee ï ni wø køny aani, ni bee ï ni
wø piem aani;
Wui ï na Jwøk mara, kärï ruu.
&Manøgø beeye duut Deebit.
@
*#Duut Lam Mar Ŋat Mo Tuu Mo Manynya Køny
1 Gwïëth en bäät ŋat wø cädö
kiper ŋata can.
Eno køny Jwøki kany wø näk da
gïï mo leth mo tägö.
2 Eno gwøk Wuuö Jwøki, nee
bëëde ni kwøw,
ni tïme no ogwïëdhö dï poge,
ni eni ba cïp ceŋ nyïïmän moe.
3 Wuuö Jwøk bëëdö buute kany wø
näk mo eni tuu,
ni ö Wuuö Jwøki ni riem täw, ni
døøc dëër gø mo jööt.
4 'Ba aani, aana köö, ni «Wui Wuuö
Jwøk, aana bääyö dëërï;
'ba bääth yiï ki aani ni kønyï täw mara.»
5 Nyïïmänna wø cäänö ki gïï mo
reyø kipera, ni köge,
ni «?Thøøe wäne nø, nee nyeŋŋe
rwäänye?»
6 Kany wø dee ŋat mo lïïmmö
baŋa, eni wø caana luup cwøk,
ni cwïnye cooŋa raay kipera;
'ba kany wø ci wøk, nyeŋŋa wø
waae waaø.
7 Jø wø män ki aani bëët, ge wø
møŋŋa gïra,
ni ge caara gïn mo raac kipera, ni köge,
8 «Ena mak täwi mo raac døc ki
køør rääö mare,
ni eni ba ö maal këët.»
9 Këël nyawatwa kiree na näk yaa ŋäädhö,
ŋat wø cam kwöna, aana cääbe ki tiere.
10 'Ba ï na Wuuö Jwøk, bääth yiï ki aani,
ni dwøgï teek dëëra kare kiper
nee kwöra coola.
11 'Ba na ö nyïïmänna na kärge
aani böötö ennø,
aŋääa ni yiï omïnnö ki aani.
12 'Ba aani, a wø kønyï kønyø kiper
adïëri mara,
ni cïbï aani buutï na bäre bäre.
13 Pwøc en jï Wuuö Jwøk, Jwø Icriel,
na bëëdö kanya poode ni piny poot kär
cwääö, këël na bäre bäre.
Kare møn, enøgønø.
&Manøgø beeye duut Deebit.
@
*#Duut Lam Mar Ŋat Mo Cwïnye Opädhö Ni Manynya Wuuö Jwøk
1 Kaawat man wø ö röönna mo
onäk riewi wø many pïï,
aani thuwø a wø bëëdö naa
manynya ïïni, ï na Jwøk.
2 Aani, dëëra da riew kiper Jwøk,
Jwøa kwøw.
?A yi wäne nø noo ööa naa
cuŋŋa nyïm Jwøk?
3 A bëëdö naa jwöŋö cooth
waŋcäŋ ki wäär,
ni tïm pï nyeŋŋa na cam mara,
kany wø bëët jiyi ni jøøŋŋa aani
cooth, ni ge köö,
ni «?Jwøk marï age?»
4 Cwïnya wø pädhö kany wø para
wïïa ki gïïa wara tïïa,
ni beeye kanya wara cøøa ki
lwaak mo päl
ni bwødha geni Øt Jwøk,
ni wa kwöŋŋö ki met ec ni wa
wär ki dut pwøc,
ni wa cämö ka ajwöma ni waana
lwaak mo päl.
5 ?'Ba aperŋø ni bëëda ni cwïnya
opädhö?
?Na aperŋø ni bëëda ni wïïa ree
ee kierø en?
Beerra man raŋŋa jï Jwøk, ni
bëëda naa pwøya eni,
eni na dïkunyi mara.
6-7 Wui ï na Jwøk mara, cwïnya
apädhö kany, tier Naam
Jördan,
kany bëëda ni aana wëëllö yie en,
ni para wïïa ki ïïni.
Aana mooyï ki pänh cwïny møn,
ni ö gïï mo lethi ni päthge bääta
kaamar naam mo pänhnhö,
ni lwör kaamar pïï mo wø
löönynyi ki bäät Kïn Armön ki
Kïn Midhaar,
ni löönyge yi Naam Jördan.
8 'Ba Wuuö Jwøk mëër mare ni wø
ba jøøl wø nyoodhe nyoodhø
jïra ki waŋcäŋ,
ni wära ki duut jïre ki wäär,
naa lama Jwøk ni wø kwøw aani.
9 A lämö jï Jwøk eni na teek mara,
ni kööa,
na «?Aperŋø na wïl wïïï ki aani?
?Na aperŋø ni bëëda naa kïmmö
en
kiper gïïa leth na tïïc nyimän?»
10 Ajøøŋ mana tïïc nyïïmänni 'moa
dëëra
atïmö ni caala ŋwellø mo onieŋ
døc dëëra,
kany wø bëëtge ni ge jøøŋŋa aani
cooth, ni ge köö,
ni «?Jwøk marï age?»
11 ?'Ba aperŋø ni bëëda ni cwïnya
opädhö?
?Na aperŋø ni bëëda ni wïïa ree
ee kierø en?
Beerra man raŋŋa jï Jwøk, ni
bëëda naa pwøya eni,
eni na dïkunyi mara ni beeye
Jwøk mara.
&Manøgø beeye duut wäät Köra.
@
*#Duut Mo Kwaca Jwøk Kiper Køny
1 Wui Jwøk, ŋun aani, ni cwagï
aani ceŋ jø wø ba wøør ïïni,
ni kälï aani wøk ceŋ jø cwøk ki
ceŋ jø wø wïthge reyø;
2 kiper beeye ïïni na Jwøk ni wø
kana raa buute.
?Aperŋø ni kwierï aani en?
?Na aperŋø ni bëëda naa kïmmö
en
kiper gïïa leth na tïïc nyimän?
3 Beerra man jääŋŋï tar marï ka
adïëri marï, kiper naa bwøthge,
ni kïthge aani bäät kïnnï na en
kur keere na näk kar bëëtö
marï. 
4 Køøre nø, aano ci kany wø en gïn
wø cïp olämme bääte marï yie,
ï na Jwøk,
ni ööa baŋï, ï ni wø mooc aani ki
met ec mo päl døc,
ni pwøa ïïni ki thoom, ï na Jwøk
mara.
5 ?'Ba aperŋø nø ni bëëda ni
cwïnya opädhö?
?Na aperŋø ni bëëda ni wïïa ree
ee kierø en?
Beerra man raŋŋa jï Jwøk, ni
bëëda naa pwøya eni,
eni na dïkunyi mara ni beeye
Jwøk mara.
@
*#Duut Mo Pëënynya Jwøk Kiper Mana Ŋøl Køny Mare
1 Wui Jwøk, luup moa caan
kwäcwa jïwa awïnywa
ni beege gïïa tïïyï yïth nïra
beetge ya acääŋŋe cøøn.
2 Ïïni ki dëërï kiree wïth juurre
ariemï wøk,
ni këëllï tiet kwäcwa piny;
ni tïïï dëët wïth juurre ki gïï mo
leth,
ni tïïyï kwäcwa nee ge nyaacge.
3 Geni, piny kär ci jïge kiper jap
leny moa en ceŋge,
ni ge kär käädhö kiper teek
marge,
'ba beeye kiper teek marï ki leec
nyïmï,
kiper ï mëër ki geni.
4 Ïïna nyeya mara, ni bee ï na
Jwøk mara,
dïïm wø cïpa ïïni jïwa, wa jø dhi
øt Jeekap.
5 Nyïïmän mowa riemwa riemmø
ki køørï,
ni böötwa jø wø ö maal bäätwa
ki nyeŋŋï.
6 Kiper a ba ŋäädhö ko opëëllö
mara,
ni jap leny 'moa ba ŋäädha naa
dege kønyø.
7 'Ba beeye ïïni na køny waani ceŋ
nyïïmän mowa,
ni lääï wïth jø wø män ki waani.
8 Wui Jwøk, wa bëëdö ni wa jïëmö
ki nyeŋŋï cooth,
ni wa bëëdö ni wa pwøya nyeŋŋï
na bäre bäre.
9 'Ba kawaane waana kwierï ni lääï
wïthwa,
niï ba cii ki jø leny mowa baŋ
leny.
10 Waana tïïyï nee wa reŋwa
ŋäthwa ki nyïïmän mowa,
ni twierge jammi mowa.
11 Waana cïpï nee wa ŋarge kaamar
dïëk,
ni keethï waani dï wïth juurre.
12 Jiyï agathï ni gätge jööt jaak,
ni kanya dwøgï ge pwödhö bäŋ
gïn ege duuö.
13 Waana tïïyï ni waana jø jøøŋ jø
atuti mowa,
ni tïïyï wa na gïr ŋeethø na gïr
tuuk jï jøøa en buutwa.
14 Waana tïïyï na gïr aŋaada dï
wïth juurre,
ni tïmwa ni waana gïr abuua jïge.
15 Cooth a bëëdö ni aano päädö,
naa bëëdö ni wïïa olääö
16 ki luup jø wø jøøŋ waani ki jø wø
jany waani,
ki jø wø män ki waani, ki jø wø
raŋ waani ka agääde.
17 Gïïögø bëët apïï bäätwa,
'ba wïthwa kär wïl ki ïïni,
ni luumma tuutï ki waani kärwa
kaalø.
18 Cwïnywa kär døø cään,
ni wa kär gaa wøk jöörï.
19 'Ba waana raanynyï kany mo
raac,
ni kïthï waani kany mo cøl ma
kar thøø.
20 ?Aŋø, ï na Jwøk marwa, doo na
wïthwa owïl ki ïïni,
ni thaaŋwa ceŋwa baŋ jwøk mør
mo path,
21 ba diï ŋääö?
Kiper jap wø en cwïny bëët ŋäyï.
22 'Ba beeye kiperï ni bëëtwa ni wa
di nääŋŋö cooth,
ni waano tïmö kaamar dïëk mo
di ŋarø en.
23 Päyï, ï na Wuuö Jwøk. ?Ï butï
kiper ŋø?
Ö maal, kär wa kwierï na bäre bäre.
24 ?Aperŋø ni kanï täärnyïmï en?
?Na aperŋø ni wïl wïïï ki caannø
marwa ki bëëtö marwa ni teek
en?
25 Waana nø ränynyö ni nø päthwa
yi tør,
ni yïthwa ogääbö ki ŋøøm.
26 Ö maal ni kønyï waani,
ni wïïlï waani wøk ki køør mëër
marï ni wø ba jøøl.
&Manøgø beeye duut wäät Köra.
@
*#Duut Nywöm Mar Nyeya
1 Aana cääö ki duut mo beer ki
cwïnya bäre,
naa cäŋŋa nyeya;
ni tïm leeba ni caala peen mar
ŋat göör mo waŋe riek døc.
2 Ï na nyeya, wøp mar kïdö marï
kaala mar jiy bëët,
ni luup mo wø ö wøk ki dhiï met,
kiper mana näk ïïno gwïëth
Jwøki na bäre bäre.
3 Ïïni na teek, twöö opëëllö marï
pierï,
niï nyootha ajiem marï ki wödö
marï.
4 Beerra man cäädhï niï aa kuna
böötï jiy ni ïïna nyeya mo
owøørø,
nee adïëri ki bëët mööl ki bëëtö
mo beer nee nyaacge,
ni tïïï ki tïïe mo rëëma ec ki køør
teek marï.
5 Dhøk athëëre moï opaaø ni beth,
ni ge wø pïïa bäät weny mo
nyïïmän moï,
ni ö wïth juurre ni päthge tietï.
6 Ï na Jwøk,
wälu marï bëëdö na bäre bäre,
na athøra mar kwär ena cerï,
niï bëëdö niï ŋøla luup ki ŋøl ma
kare.
7 Ï mëër ki bëëtö mo beer niï män
ki raay;
kiper manøgønø, Jwøk ni beeye
Jwøk marï ïïna mooe ki met ec
ni mïn yiï niï kaala nyeye møga
bëët.
8 Abïïe moï bëët ŋwääö ni met ki
riia;
ni jø wø pöödö ki thøme yiï wø
tïïcge tïïö ni met
yi øt nyec mo oŋwaŋŋø ki tuk
lïëy.
9 Nyïï nyeye dagø dï mään moa
näk owøørø ni wø en buutï,
ni bäät cwïïï gwanynyø cuŋŋö
yie ni dëëre päŋ ki warkey mo
käla Öpïr.
10 Ï na gwanynyø, wïny mara, ni
cegï ïthï, ni lääŋŋï gø;
beerra man wïl wïïï ki jø pou ki
tuuŋ wäru,
11 køøre nyeya yie omïnni ki mïërö
marï.
Wøør eni, kiper ena kwäärö
marï.
12 Jic Tayar ïïno jeethge, 
ni ö jøøa näk okwär ni mwøthge
ïïni.
13 Nyi nyeya mano tïmö ni
gwanynyø ennø mïërö døc,
ni dëëre da abïï mo ree da warkey.
14 Ni kïthi baŋ nyeya ni dëëre da
abïï kït,
ni ö nyïïakuue moa näk lwöp
moe na caath køøre
ni kïthi baŋ nyeya thuwø;
15 ni ge bwøth ka met ec ki kanynyø,
ni dønyge øt nyec.
16 Ïïni na nyeya, wäätï oläw kar
kwäcge,
ni røønyï geni na kwääri mo bäät
piny bäre.
17 Nyeŋŋï otïïa ni ŋäc ki yïth
beenhnhe bëët;
kiper manøgønø, jiy obëëdö ni
pwøya ïïni na bäre bäre.
&Manøgø beeye duut wäät Köra, na
cakge kiper nywöm mar nyeya.
@
*#Duut Mo Nyootha Gø Ni Jwøk Beeye Kar Kan Røk
1 Jwøk beeye kar kan røk marø ni
ena teek marø,
ni eni kare cään ni wø laara
kunynyö kany wø näk da gïï
mo leth.
2-3 Kiper manøgønø, këël piny doo
tïmö ni jäŋŋi,
ni ö kïte ni leeŋge rege dï naama
dwøŋ;
ni ö pïïe ni lwörge ni neekum ki
bööyö,
ni ö kïte ni jäŋge rege ka athaga
mare,
ø ba doo lwäyö.
4 Da naam mo døøya yïth jiy mo
met yi pääny mar Jwøk,
ni beeye kar bëëtö mana en kur
keere mar Jwøa Dwøŋ ni en
Maal.
5 'Ba Jwøk ena dï päänyögø, ni
bëët päänyögø ni ba ränynyi,
ni päänyögø wø laar Jwøki ka
køny.
6 Wïth juurre atïïö ko okiera, ni ö
akwömmi ni päthge;
køøre Jwøk mare acaane, ni tïm
dëëtge ni rïïŋö.
7 Wuuö Jwøk, eni na wïth jammi
bëët, ena buutø,
eni na Jwø Jeekap bee eni ni wø
kanø røø buute.
8 Ööu ni neennu tïïe mo Wuuö
Jwøk,
eni na tïïc gïï mo rëëma ec bäät
piny.
9 Lenye wø jooe jooø bäät piny
bäre,
ni tøy athëëre ni ŋør tøøŋi,
ni waaŋ jïëth leny mo wø tut
okwëënyi.
10 'Ba Jwøk aköö, ni «Lïŋu nø, ni
ŋäyu gø ni aana Jwøk.
Kara tïmö ni dwøŋ dï wïth juurre,
ni tïm kara ni dwøŋ bäät piny bäre.»
11 Wuuö Jwøk, eni na wïth jammi
bëët, ena buutø,
eni na Jwø Jeekap, bee eni ni wø
kanø røø buute.
&Manøgø beeye duut wäät Köra.
@
*#Duut Mo Nyootha Gø Ni Dwøŋŋa Jwøk
1 Wui u na jiy bëët, paŋŋu ceŋŋu,
ni kwöŋŋu ni yïthu met jï Jwøk.
2 Kiper Wuuö Jwøk na dwøŋ ni en
maal, di lwäärö;
ena nyeya mana dwøŋŋa eni bäät
piny bäre.
3 Wïth juurre abööte jïwa,
ni tïïc geni ni ge ena thäc tietwa.
4 Waana jëënne ki paac mo bëëtwa
yie,
ni tïme na gïr ajiem jïwa, wa na
nyïïkwaac Jeekap na mëëre ki
geni.
5 Wuuö Jwøk aci maal bäät wälle,
ni jiy kwöŋŋö ki met ec, ni ge
kudhö ki tuŋi.
6 Wärru ki dut pwøc jï Jwøk,
wärru ki dut pwøc;
Wärru dut pwøc jï nyeya marø,
wärru dut pwøc;
7 kiper Jwøk beeye nyeny bäät
piny bäre;
wärru dut pwøc mo ocaaø ni
beyø.
8 Jwøk bëëdö na nyeya bäät wïth
juurre bëët;
Jwøk bëëdö bäät wälu mare na
en kur keere.
9 Kwääri mo wïth juurre dëëtge
acooŋge kanya ciel,
ni tïmge na jic Jwø Eeberam;
kiper kwääri mo bäät piny bäre,
gena mo Jwøk,
ni eni na Jwøk, kare dwøŋ døc.
&Manøgø beeye duut wäät Köra.
@
*#Duut Mo Pwøca Wuuö Jwøk Jwø Dhayan
1 Wuuö Jwøk dwøŋ, no orømø ki
pwøc døc,
yi pääny mare na en bäät kïnne
ma Dhayan na en kur keere.
2 Kïn Dhayan bäär ni mïërö,
ni piny bäre yie met ki gø,
ni beeye na geer pääny mar
nyenynya dwøŋ bääte.
3 Jwøk bëëdö dï kiir na no ogeerø
ni teek mar päänyögø,
ni ree ee nyoodhø ni bee eni na
kar gwøk røk.
4 Ka adïëri møn, nyeye rege
adwalge kanya ciel,
ni cäänhge na aciel nee Kïn
Dhayan tukge.
5 'Ba kanya neenge gø, yïthge
athäŋŋö,
ni lwäcge, ni bwøkge,
6 ni miel dëëtge kaace,
ni pïïc gïn mo leth dëëtge, ni
tïmge kaamar dhaagø mo
ogøøc mäc lwaarri.
7 Gena raanynyï kaamar baabuure
mo Tarcëc,
na raany atuunna mana dwøŋ.
8 Ka teeŋ mana wïnynyø gïna tïïc
Jwøki,
aputø joot ennø no otägö
yi pääny mare, eni na Jwøk
marø, eni na wïth jammi bëët.
'Ba päänyögø gwøk Jwøki gwøø
na bäre bäre.
9 Wui ï na Jwøk, waana cädö kiper
mëër marï ni wø ba jøøl
ni wa ena øt lam marï.
10 Wui Jwøk, ka teeŋ mana ŋäc
nyeŋŋï bäät piny bäre,
jø bäät piny bëët pwøya ïïni thuwø,
kiper bëëtö marï na beer.
11 Jøøa bëëdö bäät Kïn Dhayan
beerra man mïn yïthge,
ni mïn yïth mïëc Juuda thuwø ki
ŋøl marï.
12 U na jic Jwøk, caathu deŋ
Dhayan ni wïrru lage,
ni kwaannu uut koor moe;
13 raŋŋu kiire døøc,
ni neennu kwör lenye moa teek,
kiper nee caannu jï beenhnhø
mano ööi.
14 Man beeye Jwøk,
ni beeye Jwøk marø na bäre bäre,
ni bëëdö ni bwøtha øøni na bäre
bäre.
&Manøgø beeye duut wäät Köra.
@
*#Duut Mo Nyootha Bøøl Mar Jø Wø Ŋääth Kwär Marge
1 Dïbwör bäre, beerra man
wïnynyu gïn.
Cegu ïthu, u bëët, u ni bëëdö
bäät pinyi en,
2 u na kwöru døøŋŋø ki u na
kwöru bäŋgø,
ki jiy moa can ki moa näk okwär
bëët.
3 A cäänö naa caana luup leec wïc,
na acaare 'moa tiet luup
nyoothge nyoodhø.
4 Aani, ïtha ciia ciiø ki pwöc leec wïc,
kiper nee tier gø caana ki yi duut
mano wära ki thoom.
5 ?Aŋø, a lwäya kiper ŋø kany wø
dee gïï mo leth,
kany wø ö raayi mo jø wø gëëmö
ki aani wø cielge aani dïër?
6 Jøøgø, ge ŋäätha kwär marge,
ni ge wø töödö kiper jap kwär
moge na thööth.
7 'Ba bäŋ dhaanhø mo løny jïre ki
man wïïl jwïëye wøk,
wala cïpa gät jwïëye jï Jwøk,
8-9 kiper nee bëëde ni kwøw na bäre
bäre,
ni ba thøw;
kiper gät jwïëy teek døc,
ni bäŋ gïn rømi ki gø.
10 Kiper ŋäc jøwi bëët ni këël jøøa
näk wïthge leer, ge thøw,
ni jøøa näk wïthge ba leer ki moa
näk wïthge bäŋ acaara bëët ge
poot thøw thuwø,
ni dööŋ jap kwär moge jï jø
møøk.
11 Bwör moge bëëdö na uudi moge
na bäre bäre,
ni bëëtge na kwör bëëte moge
këël yïth beenhnhe moo ööi
bëët;
ni ö pwöthi moa näk nyeŋge ege
caa rege ni dööŋge wøk.
12 Këël dhaanhø okwär, eni ba ruu;
eni caala lääy mo thøw jaak.
13 'Ba aŋuun bëët jøøa näk ŋäätha
oballe,
ki jøøa caath køørge ni wø jïëc
luupge beeye en:
14 ge thøw kaamar dïëk jaak, na
aŋuun bëëtö marge beeye yi
bwörö,
ni tïm thøøe na dïkwääy
marge;
ni tïmge ni ge ena tiet jøøa näk
marge thïïŋ kanyo ruu øwi,
ni tïmge ni bäŋ kar bëëtö jïge
këët,
ni ö dëëtge ni ränyge yi bwörö.
15 'Ba aani, jwïëya wïïl Jwøki wøk
cer teek thøø,
ni kïth aani baŋe.
16 Käru lwäyö ki dhaanhø kany wø
kwäre,
kany wø tïm jap paare ni
thööth.
17 Kiper kanyo thøøe, bäŋ gïn mo
kääre noo aae;
eni ba ci piny ki jap paare na
aciel.
18 Këël eni doo bëëdö ni pwøya
dëëre keere kany bëëde ni
kwøw en,
ni jiy pwøya eni kiper kwär
mare,
19 eni poot cøøa kanya ci kwäye yie,
jøøa näk tar ba jootge këët.
20 Dhaanhø mo okwär mo ba cädö,
caala lääy mo thøw jaak.
&Manøgø beeye duut wäät Köra.
@
*#Duut Mo Jwøk Jääla Jø Wø Raany Lam Marge Ki Køør Bëëtö Marge
1 Wuuö Jwøk, Jwøa teek, acäänö,
ni cwøl jø bäät piny bëët,
ni tägi ka jï løø kur tuul-cäŋ,
ni pïïe jï løø kur pänh-cäŋ.
2 Jwøk ree wø nyoodhe ka bäät
Dhayan,
paana näk wøp ni mïërö døc.
3 Eni na Jwøk marø öö, ni ba
nikïïl,
ni ööi ni nyïme da maac mo
räänyö,
ni buute da atuunna mo dwøŋ.
4 Ni cwøl maal, ni cwøl piny,
kiper nee luup jiye ŋøle buutge.
5 Ni kööe, ni «Cuuŋu jiy 'moa
buuta kany moa näk cwïnyge
ena køøra,
jøøa jïëy ki man tutge ki luubö
ki aani,
na twöc luummögø ki køør
olämi.»
6 Maal gïr beeny Jwøk caane
caanø,
kiper Jwøk ki dëëre beeye dïŋut
luup.
7 Jwøk aköö, ni «Uuni na jiya,
wïnynyu gïn caana en;
uuni na jø Icriel, mara caana
caanø dëëtu;
aana Jwøk, ni beeye aani na
Jwøk maru.
8 U ba jääla kiper olämme mou mo
wø cïpu;
olämme mou mo wø waaŋ mo
wø cïpu nut nyïma cooth.
9 'Ba aani, a ba jïëy ki man käda ki
rwädhe mo wø käl baŋu,
wala nywø ateea mo wø kälu ki
dï pïïth.
10 Kiper lääc paap bëët beege 'moa,
ki dhäk ki dïëk moa en yïth
pwöle mo ba kwaan.
11 Weny moa en paap bëët ŋääa,
këël lääy moø ni en yi pwöla bëët
yøø beege 'moa.
12 'Ba doo na aano 'näk käci, ba daa
caana jïïu,
kiper piny beeye mara ki gïïö ni
en yie bëët yøø.
13 ?Aŋø, a wø cämö ki rïŋ rwädhe,
naa wø mädhö ki rem atëëe?
14 Cïpu pwøc no olämi jïra, a na Jwøk,
ni cïpu gïïa kööŋŋu ki ge jïra, a
na Jwøa Dwøŋ ni en Maal.
15 Ni cwøllu aani kany wø näk mo
u ena yïth gïï mo leth;
u kønya kønyø ni wøørru aani.»
16 'Ba Jwøk aköö jï ŋat raay,
na «?A teega ŋø ni en jïrï ni wø
caanï ciik 'moa en,
naa teega ŋø ni en jïrï ni maaï
luumma tuuda ki jiya dhiï en?
17 Kiper ï män ki man pwöny ïïni,
ni luupa iï leeŋ ŋääï.
18 Ni kany wø jootï kuu, tïïyï tïïö
na nyawadu,
niï wø dwätö ki jø luuy.
19 Dhiï atïmö ni kwel ki caan gïï
mo reyø,
ni tïm leebï ni cara cwøk.
20 Ï wø bëëdö ni ïïno pï piny niï
jøøŋŋa coku,
niï wø waya nyeŋ ŋata lwaar
meru ki gø kiree.
21 Gïïögø bëët atïïyï, 'ba aana lïŋö jaak;
ki jïrï naa caala ïïni.
'Ba ennø, ï jääla jäälö, ni caana
gïïa tïïyï na aciel aciel ni
nyeŋŋø yøø kemø.
22 «'Ba ennø, wïnynyu gïn, uuni ni
taak Jwøk en;
'ba ni näk mo ba wïnynyu, u
raanynya raanynyø, ni tïme ni
bäŋ ŋat køny uuni.	
23 Ŋat wø cïp pwøc no olämi jïra
wøøra aani,
ni ööa ni nyoodha køny mara
jïre, eni ni wø jiiŋ bëëtö mare
na kare.»
&Manøgø beeye duut mar Acaap.
@
*#Duut Kwac Mar Ŋat Mo Cwïnye Opädhö Nee Raay Moe Wëënni
1 Wui Wuuö Jwøk, wëën aani
ki køør mëër marï ni wø ba
jøøl.
Wec moa baaa ni raanynyï geni
ki køør mëër marï na päl.
2 Pïny gïna baaa wøk cwïnya,
ni døøyï dëëra mo waany ki gïna
baaa.
3 Kiper gïïa baaa ŋääa,
naa lääŋŋa bääyö mara cooth.
4 Beeye ïïni keerï na bääya dëëre,
ni tïïa gïna raac nyïmï,
kiper manøgønø, luummï na
caanï beeye adïëri,
ni bäŋ ajäla bäätï ki køør luummï
na ŋølï.
5 Adïëri møn, aana ŋat bääö ki
mana nywøl a cøøn,
ni tägi ka kanya ŋiiny aani yi
mera.
6 Adïëri møn, ï mëër ki ŋat mo
cwïnye thïïŋ;
ni bee ï ni wø pwöny aani nee
tiet luup cige cwïnya.
7 Wec gïna baaa, naa tïma naa
waany,
ni pïnyï bääyö mara wøk yi
cwïnya, nee dööŋe ni waany.
8 Køny aani naa jïta ki met ec ki
kanynyø,
ni døøyï pänh cwïny mara met
ec.
9 Cïp cwïnyï piny ki gïïa baaa,
ni raanynyï geni bëët.
10 Wui Wuuö Jwøk, beerra man
tïïyï cwïnya ni tøŋ,
ni døøyï jwïëya mo nyään, nee
cwïnya bëëde ni ena køørï
cooth.
11 Kär a riem wøk buutï,
ni ba lwørï jwïëyï na en kur
keere bääta.
12 Dwøk met ec mara kare, man wø
ööi ki køør køny marï;
ni døøyï wïïa mo jööt, naa tïma
naa tïïya mana manynyï.
13 Køøre aani, jø wø dhal ciigï
pwönynya pwönynyö ki jöörï,
ni ö jø wø bääö ni luuge rege
baŋï.
14 Wui Jwøk, ï na pïëmi mara,
wëën aani kiper ajäl rem
dhaanhø mana kønynya piny;
køøre aano wär ki duut ni yia
met naa pwøya beenynyï.
15 Wui Wuuö Jwøk, beerra man japï
dhaa,
naa cääna naa pwøya ïïni.
16 Wui Wuuö Jwøk, yiï ba mïnni ko
olämi man wø waaŋ;
doo na yiï met ko olämi, a doo
cïpö.
17 Kiper olämi man wø manynyï
beeye cwïny mo opädhö.
Wui Wuuö Jwøk, dhaanhø mo
cwïnye pädhö kiper bääyö
mare, ba taagï.
18 Ki køør met ec marï,
beerra man tïïï ki gïï mo
beyø jï Dhayan, ni beeye
Jerucalem,
ni cäŋï kiir mare geerrø.
19 Køøre nø, yiï otïmö ni met ko
olämme moa näk karge,
ni mïn yiï ko olämme mo wø
waaŋ bäre;
kar kaace nø, rwädhe otïmö ni di
cïbö bäät gïn wø cïp olämme
bääte marï. 
@
*#Duut Mo Jääla Ŋata Raac Ni Wø Ŋwöö
1 Nyie, ï ni wø köö niï teek!
?Aŋø ni ŋwöï kiper gïna raac na
tïïyï dëët jic Jwøk en?
2 Cooth ï caara luup aranya.
Leebï beth ni caala muuc,
ïïni ni wø tïïc cwøk.
3 Ï mëër ki gïn mo raac ni kaala
mana beer,
niï mëër ki tööt ni kaala adïëri.
4 Yiï met ki luup aranya bëët,
ni ïïna ŋat cwøk.
5 'Ba Jwøk ïïno raanynye na bäre
bäre,
ï di maaø ni tuut ïïni wøk ki yi
ødï,
ni puth ï wøk kar bëët jøøa kwøw.
6 Gïïögø ojoot jøøa bëëtö marge
beer, ni putge lwäyö,
ni ŋeethge bäätï ni köge,
7 ni «Raŋ ŋat mo Jwøk käre tïïö na
kany kan dëëre yi gø,
ni eni bëëdö ni ŋäätha jap kwär
moa thööth na en jïre,
ni ö teek mare ni cääth maal ki
køør gïna raac na tïïe.»
8 'Ba aani a caala jaath mo oløth
mo ena Øt Jwøk,
naa bëëdö cooth naa ŋäätha
mëër mar Jwøk ni wø ba jøøl.
9 Wui Jwøk, ï pwøa pwøø na bäre
bäre,
kiper gïna tïïyï.
Aani, man näk maa ŋäätha ïïni
caana caanø nyïm jiy mo
cwïnyge ena køørï,
kiper ïïna Jwøk mo beer.
@
*#Duut Mo Cäänö Kaper Rääö Mar Jø Raay
1 Jiy mo wø cäänö ki cwïnyge, ni
«Bäŋ Jwøk», gena bøøre.
Gena jiy mo oränynyö, ni ge
temma gïï mo reyø,
ni bäŋ ŋat mo tïïö ki gïn mo beer.
2 Jwøk aräŋŋö ki maal ni raaŋa
bëët jø bäät piny,
ni ge raaŋe kaper nee jïte ki mo
wïïe leer,
mo manynya eni, eni na Jwøk.
3 'Ba ge bëët, geno nø gaa wøk,
ni geno nø tïmö ni ge reyø bëët,
ni bäŋgø mo tïïö ki gïn mo beer,
këël dhaanhø aciel kiree, bäŋgø
na bäre bäre.
4 ?Aŋø, jøø ni tïïö ki gïï mo reyø
yøø bäŋ gïn mo ŋäcge,
ni camge jap jiya kaawat man wø
cam møø jaak en,
ni nyeŋ Jwøk ba cwølge?
5 'Ba kaace ge tïmö ni ge lwäär døc
ki lwär mo ge poot kär lwäyö ki
gø cøøn,
kiper Jwøk nyïïmän mou cuu
moge keethe keethø,
Ni lääu wïthge, kiper geno kwier
Jwøki.
6 Beerra man ö Jwøki ni wø bëëdö
Dhayan ni piem jiye ma jø
Icriel,
ni ö jø Icrielli, ni beege
nyïïkwaac Jeekap, ni mïn
yïthge kanyo ö Jwøki noo dwøk bëëtö
marge kare.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Kwaca Jwøk Kiper Nee Nyïïmän Bööte
1 Wui Jwøk, køny aani ki køør
nyeŋŋï,
ni ŋunnï aani ki køør teek marï.
2 Wui Jwøk, wïny lam mara,
ni cegï ïthï ki luup mo wø cara.
3 Kiper juurre rege anø thïïŋge
dëëra,
ni ö jøøa no ogäy ni cacge man
raanyge jwïëya,
jø wø bäŋ gïn caarge kiperï, ï na
Jwøk.
4 Adïëri møn, Jwøk beeye dïkunyi
mara,
ni bee eni ni wø en jwïëya cere.
5 Nyïïmänna ocunne kiper gïïa
reyø na tïïcge,
ni raany geni, kiper mare adïëri.
6 Wui Wuuö Jwøk, olämi cïba cïbö
jïrï ki met ec,
ni pwøa nyeŋŋï, kiper ï beer.
7 Kiper aana kønyï yïth gïïa leth
bëët,
ni jooda nyïïmänna ni geno
böötö.
&Manøgø beeye duut Deebit,
mana caae kanya ö jø Dhip na
öge kuna caange gø jï Cøøl, ni
«Deebit ree ee kan buutwa.»
@
*#Duut Mo Cäänö Kaper Ŋata Døø Dëër Nyawatge
1 Wui Jwøk, wïny lam mara,
ni ba taagï kwac mara.
2 Cek ïthï ni wïnynyï mara.
Wïïa ree ee cwödhö ka acaara, ni
ö wïïa ni kier ree,
3 ki dööt nyïïmänna,
ki jøøa reyø ni wø thiel aani
piny;
kiper gena kän bääta ki gïï mo
leth,
ni gootge ni mänge ki aani.
4 Cwïnya apädhö ki pädhö mo
dwøŋ døc,
ni lwäya ki lwäc thøø.
5 A bëëdö naa lwäär ni dëëra
kwanynyi,
ni ö lwärri mo dwøŋ døc ni bööt
aani.
6 Ni kööa ki cwïnya, ni «Doo na
jïra da bwöm kaamar akuuru
ennø,
a doo määta kanymør naa jïta ki
jwöm.
7 Ka adïëri møn, a doo reŋŋa kany
mo bäär,
ni bëëda dï paap jaak.
8 A doo laar läät kany kana raa
yie,
nee kara tïme ni bäär ki geni ni
wø räänyö kaawat man wø tïïc
jamø ka atuunna.»
9 Wui Wuuö Jwøk, raany acaare
moge, ni pääï dhøkge,
kiper gïï mo leth ki lenye ajooda
ni tägö dï pääny.
10 Waŋcäŋ ki wäär ge bëëdö ni ge
wïdö dï kiir mar pääny,
ni beeye kany wø bëëdö ni temma
gïï mo leth ki jap rääö yie,
11 na aranya ena yie kiree,
këël ŋwöny jiy ki cwøk, ba aay dï
uutjïëthe moe.
12 Doo na beeye nyimänna na jøøŋ
aani,
doo løny jïra ki man jïënya
luumme;
doo na beeye ŋat mo män ki aani
na tïïc dëëre ni dwøŋ bääta,
doo løny jïra ki man kana raa ki
gøøni.
13 'Ba beeye ï na näk röömi ki aani
kiree,
ŋato näk aano dwätö ki gøøni,
na nyawatwa mana ŋäcwa
cwïnywa ki gø,
14 ni wara wääwa ki waac mo met
ki gø na aciel,
ni wara cääthwa Øt Jwøk ki gø
na aciel ni wa ena dï lwaak mo
dwøŋ.
15 Beerra man cwöp thøøe dëët
nyïïmänna,
ni leeŋ ge yi bwörö ni ge poot
kwøw;
kiper raay atïmö ni bëëdö kany
wø bëëtge yie.
16 'Ba aani, Wuuö Jwøk cwøla
cwølø,
ni ö eni ni køny aani.
17 A wø lämö naa jwöŋö
ka abøøya ka amöölla ki dhöör,
ni ö eni ni wïny dwøra.
18 Këël na bëëde ni da jiy mo
thööth mo män ki aani,
eni, a käle wøk ni bäŋ gïn mo
otägö dëëra
ki yi leny mano këël ki aani.
19 Jwøk, ni beeye na wää pinynyi
cøøn,
lam mara di wïnynyö ni jääl geni;
kiper gena jiy mo bëëtö marge ba
wiilge,
ni ge ba lwäär ki Jwøk.
20 Nyawatwa aöö maal bäät jøøa
bëëdö ki bëët-mëër ki eni,
ni raany gïna tuude ki geni.
21 Luumme jööm ni kaala maar
dhieŋ,
'ba cwïnye poot caara leny.
Luupe pøøth ni kaala maaw,
'ba bëëdö ni beth kaamar
opëëllö.
22 Gïna peek na en bäätï cïp cer
Wuuö Jwøk,
køøre ï kønye kønyø;
eni, ba løny jïre ki man wëëk ŋat
mo mare adïëri pädhö.
23 'Ba ïïni na Jwøk, jiy mo wø nääö
ki jiy, ki jø cwøk,
geno tïïyï nee laarge thøø ni nïne
moge poot kär päŋ.
'Ba aani, a bëëdö naa ŋäätha ïïni.
&Manøgø beeye duut Deebit.
@
*#Duut Mar Ŋat Mo Ŋäätha Jwøk Kiper Nyïïmänne
1 Wui Wuuö Jwøk, køny aani ki
køør mëër marï,
kiper da jiy mo caanna aani,
naa ege öölö cooth ki leny.
2 Nyïïmänna atïmö ni thööth,
ni ge bëëdö ni ge caanna aani cooth,
ni ge manynya leny ki aani ni ge
töödö.
3 'Ba kany wø lwäya,
a wø bëëdö naa ŋäätha ïïni.
4 Bee ï Jwøk ni wø luumme pwøa,
ni bee ï Jwøk ni wø ŋäädha naa
ba lwäyi.
?Aŋø, dhaanhø jaak, agïnaŋø noo
tïïe dëëra?
5 Cooth dhaa kat jiyi katø,
ni gïï wø caarge bëët kipera
beege gïï mo reyø.
6 Dhøkge wø tuutge tuudö, ni lepge aani;
køør tieta wø raŋge raŋŋø,
ni ge koora aani naa 'näkge.
7 Wui Wuuö Jwøk, jääl jøøgø ki
køør gïna baacge,
ni raanynyï geni ki wëër marï.
8 Kwöra wïïra yïthge bëët ŋäyï;
beerra man kanï pï nyeŋŋa yi
wïlli marï, niï caara kïmmö
mara. 
?Aŋø, gïïa tägö dëëra bëët paa iï
göörö yi wëëlö marï?
9 'Ba dïcäŋ wø kwaa ïïni,
nyïïmänna wø puta døø
ŋäthge.
Ŋääa møn ni ï na Jwøk, ï ena
kura.
10 Bee ï Jwøk ni wø luumme pwøa;
bee ï Wuuö Jwøk ni wø luumme
pwøa møn;
11 bee ï Jwøk ni wø ŋäädha naa ba
lwäyi.
?Aŋø, dhaanhø jaak, agïnaŋø noo
tïïe dëëra?
12 Wui Wuuö Jwøk, gïïa kööŋa ki
geni bëët na en bääta otïïa jïrï,
ni cïpa jïrï ko olämme mo dwøk
met ec.
13 Kiper aana piemï cer thøø,
ni cømï tieta naa ba pädha,
naa cäädha nyïmï, ï na Wuuö
Jwøk,
yi tar mar kwøw.
@
*#Duut Mo Ŋäätha Jwøk Kiper Køny
1 Wui Jwøk, køny aani, køny canna,
kiper raa yaa kan buutï.
Dëëra kana tiet bwöpï
këël mano ö gïna lethi noo
pöödhe.
2 A jwöŋö dëër Jwøa Dwøŋ ni en
Maal,
Jwø wø tïïc jammi bëët nee
thurge karge jïra.
3 Eni køny di jääŋŋö ki maal ni
køny aani,
ni jook jø wø thiel aani piny.
Jwøk mëër mare ni wø ba jøøl ka
adïëri mare di jääŋŋö.
4 Aani, a caala dhaanhø mo ena dï
ŋuuwe,
naa bëëdö dï jiy mo owär kaamar
cwëënyi,
ni beege nyïïmänna ni wø lakge
beth ni caala tøøŋi ka athëëre,
ni lëëpge beth ni caala opëëllö.
5 Wui Jwøk, ï bëëdö ni karï dwøŋ døc,
na ajiem marï ena bäät piny bäre.
6 'Ba nyïïmänna, abïëp anø cekge
kipera,
ni ö cwïnya ni pädhe.
Gena kunyö ki buur mo dwøŋ
øtjööra,
ni ö geni ki dëëtge ni päthge yie.
7 Wui Jwøk, a bëëdö ni cwïnya ena
køørï;
cwïnya bëëdö ni ena køørï møn,
naa wär ki dudi naa pwøya ïïni.
8 Päyï, ïïni na jwïëya,
ni päyu, u na thøme 'moa;
aani, øw nyïïa nyïïö nee laar
ruuö ki duuda.
9 Wui Wuuö Jwøk, met ec duua
duuö jïrï dï jiy bëët,
ni wära ki dut pwøc jïrï dï wïth
juurre.
10 Kiper mëër marï ni wø ba jøøl
dwøŋ døc no okëët maal,
na adïëri marï okëët nyeŋ pøøl.
11 Wui Jwøk, ï bëëdö ni karï dwøŋ døc,
na ajiem marï ena bäät piny bäre.
&Manøgø beeye duut Deebit mana
caae kanya reeŋe ni ŋwieya
Cøøl, ni kan ree øt kïdi.
@
*#Duut Mo Kwaca Jwøk Nee Jøøa Reyø Jääle
1 ?Aŋø, uuni na kwääri, u ŋudö
møn ki ŋøl mana näk adïëri? 
?A luup jiy ŋøllu ŋølø na karge?
2 Jïre bäär, kiper u caara gïï mo
reyø ki yïth cwïnynyu,
nou tïïö ki ceŋŋu ki gïï mo reyø
bäät piny.
3 Jøøa reyø, ki mana nywøl ge
cøøn, ge bëëdö ni geno gaa
wøk, ni ge cara tööt;
geno bääyö cøøn ki mana öge
wøk ki yïth mëëkge.
4 Dhøkge reyø ni caala cïm mar
thwöl,
ni ge caala olwierø ni wø dhïŋ
ïthe, ni tïïc dëëre na miiŋ,
5 kiper nee dööt jø wø tuuk ki
thwöre nee ba wïnynye,
këël jøøgø nyeŋge doo reegø
nidïï, döötge ba wïnyge.
6 Wui Jwøk, tøc lak jøøa reyø.
Wui Wuuö Jwøk, tëëŋ lwönni
moge wøk, ge ni caal ŋuuwe
yøø.
7 Beerra man rwäänyge kaamar pïï
mo oøyø,
ni tïm athëëre moge ni bäŋ tøøŋi
wïthge kany wø thööthge.
8 Beerra man tïmge kaamar
nyilaal mo onimany ec,
ni tïmge kaamar nyilaal mo
obwön wøk,
mo cäŋ käre joodø.
9 Jwøk jøøgø pudhe wøk kaamar
acïrra kany mo kärge dïëdö,
ni raany geni ki køør wëër mare.
10 Ŋata beer yie omïnni kanyo joot
gø ni kwör di coolø,
ni lwøk tiete ki rem jøøa reyø.
11 Køøre jiy oköö, ni «Ka adïëri
møn, jøøa beyø da gïn mo beer
mo jootge joodø møn;
kare møn, Jwøk nutö ni ŋudö
bäät piny.»
&Manøgø beeye duut Deebit.
@
*#Duut Mo Kwaca Jwøk Nee Dhaanhnhe Pieme Ceŋ Nyïïmän
1 Wui, ï na Jwøk mara, piem aani
ceŋ nyïïmänna;
gwøk aani ceŋ jø wø ö maal
bääta.
2 Piem aani ceŋ jø wø tïïö ki gïï
mo reyø,
ni gwøgï aani ceŋ jø wø many
'näk ki jiy.
3 Wui Wuuö Jwøk, ka adïëri møn,
jøøa bäätge teek, geno nø mør
piny jööra;
ni ge manynya man tïïge ki gïï
mo leth dëëra,
ni paa kiper ni da gïn mo yaa
baaø wala raay mo yaa tïïö.
4 Aani bäŋ gïn mo yaa baaø,
'ba ge wø laara reŋ kuna jiiŋge
dëëtge kipera.
Ï na Jwøk, ö maal ni raŋï gïna
tägö dëëra, ni kønyï aani.
5 Wui Wuuö Jwøk, Jwø Icriel, ï na
wïth jammi bëët,
päyï ni jäälï wïth juurre bëët;
jø wø kaam gïï mo reyø kär
wëënnï.
6 Jøøgø, wø tïme na abøøya, ge wø
duuö,
ni ge ŋärö kaamar guu,
ni wïrge dï pääny.
7 Luup mo reyø wø dhääge wøk
jaak,
ni dhøkge beth kaamar opëëllö,
kiper ge köö ki cwïnyge, na
«?Aŋa ni wïny gø?»
8 'Ba ïïni na Wuuö Jwøk, ï ŋeethø
bäätge,
ni taagï gïr wïth juurre bëët.
9 Ï na teek mara, a bëëdö naa
raŋŋa jïrï, 
kiper bee ïïni na kar gwøk røk
jïra.
10 Jwøk ni wø mëër mare ba jøøl
obwödhö nyïma,
ni tïïc aani nee nyïïmänna jooda
ni geno böötö.
11 'Ba ï na Wuuö Jwøk, ni bee ï na
kwöt leny marwa,
kär ge 'nägï, kiper kanymør wïth
jiya wïl;
tïïc ge nee ge thääcge ki køør teek
marï, ni dwøgï wïthge piny.
12 Beerra man cegï ge ka atöör
marge,
ki raay mo dhøkge ki luup mo wø
cur dhøkge,
ki luup tööt mo wø carge, ka
acïëni marge.
13 Beerra man thöörï geni ki wëër,
nee bäŋe gøøni mo dööŋ këët,
kiper nee ŋäc bäät pinynyi bäre
ni Jwøk beeye kwäärö bäät
nyïïkwaac Jeekap.
14 Jøøgø, wø tïme na abøøya, ge wø
duuö,
ni ge ŋärö kaamar guu,
ni wïrge dï pääny.
15 Ge wø wïïrö ni ge caya cam,
ni ŋurge kany wø näk mo ge kär
jäŋ.
16 'Ba aani, aano wär ki duut kiper
teek marï,
ni yia met ka amöölla ni dwøra
ena maal,
naa wär kaper mëër marï ni wø
ba jøøl,
kiper ïïna bëëdö na kar gwøk røk
jïra,
na kar kan røk kany wø dee gïï
mo leth dëëra.
17 Wui ï na teek mara, a wär ki
duut jïrï naa pwøya ïïni,
kiper ï bëëdö na kar gwøk røk
jïra, ï na Jwøk,
ni wø nyooth mëër marï ni wø ba
jøøl jïra.
@
*#Duut Mo Kwaca Jwøk Nee Jiye Pieme
1 Wui Jwøk, waana kwierï,
ni raanynyï waani;
ïïna bëëdö ni ïïno gootø ki
waani;
'ba ennø, dwøk bëëtö marwa
kare.
2 Dïjäŋ piny atïïyï møn, ni ö
pinynyi ni kaaŋŋe;
'ba cäŋ kwöra kaaŋŋø mwönnö,
kiper piny atïmö ni muuŋŋö.
3 Wa na jiyï, waana mooyï ki bëëtö
mo teek,
ni mooyï wa ki køøŋ nyïïomøki
mo na maathwa gø waana put
bøømmø.
4 'Ba ïïna cïpö ki bëëra na nyuudhi
jï jø wø lwäär ki ïïni,
kiper nee dëëtge cooŋge na aciel
lage kiper adïëri marï.
5 Wïny marwa ni piemï waani ki
køør teek badï,
kiper nee waani na mëërï ki geni
nee wa piem.
6 Jwøk acäänö ni ena kar bëëtö
mare na en kur keere, ni kööe,
«Ŋøøp Cekam pääŋŋa pääŋŋö ni
mïn yia,
ni pääŋŋa ŋøøp Goor Cuköt
thuwø.
7 Ŋøøp Gelät beege 'moa, ni ö ŋøøp
Maneeca ni näkge 'moa thuwø;
jø tuuŋ Ipariem perge leth ni
caala cöör nywïënyö mara,
ni jø tuuŋ Juuda beege jø wø kïth
ciik 'moa bäät tïïc. 
8 'Ba jø Möap caala gïn wø lööga
yie,
ni ö warø mara ni leeŋa gø yi po
jø Ëdöm,
ni kwöŋŋa bäät jø Pilitin ni
dwøra ena maal kanyo bööta
geni.»
9 ?Wui Jwøk, aŋa noo mooc aani
ki teek naa dønynya yi pääny
mana teek,
noo bwøth aani naa këëda ki jø
Ëdöm?
10 ?Wui Jwøk, aŋø, waana kwierï
møn ennø,
niï ba ci baŋ leny këët ki jø leny
mowa?
11 Køny waani ceŋ nyïïmän,
kiper køny mar dhaanhø bäŋ gïn
mo duue
12 Teek dïïm ojootwa baŋ Jwøk,
ni bee eni noo bööt nyïïmän
mowa.
&Manøgø beeye duut Deebit mana
caae kanya këëde ki jø Aram-Naarim
ki jø Aram-Dhöba, ni ö Jöapi ni
døøe ni 'näk jø Ëdöm ma kume
apaar kurriiø yi Goor Acäbö.
@
*#Duut Mo Kwaca Jwøk Nee Dhaanhe Gwøe
1 Wui Jwøk, wïny oduuru mara,
ni cegï ïthï ki lam mara.
2 Aani, a cøøra ïïni kany bëëda ni
kara bäär ki paac en,
ni cwïnya opädhö.
Kan aani buutï, ï na teek,
3 kiper ï wø bëëdö na kar kan røk
jïra,
ni nägï kar gwøk røk jïra kiper
nyïïmänna.
4 Tïïc aani naa bëëda kar bëëtö
marï na bäre bäre,
ni kana raa tiet bwöpï.
5 Ï na Jwøk, gïïa kööŋa ki ge ri
lam awïnynyï,
ni gïï wø cïpï jï jø wø lwäär ki
ïïni acïpï jïra.
6 Meet nïr kwøw mo nyeya,
ni këët cwiiri moe ri beenhnhe
moo ööi.
7 Beerra man bëët nyeya na bäre
bäre nyïmï, ï na Jwøk,
ni gwøgï eni ki køør mëër marï
ni wø ba jøøl ka adïëri marï.
8 Køøre aano wär ki duut naa
pwøya nyeŋŋï cooth,
nee gïïa kööŋa ki geni tïïa ki yïth
nïne bëët.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Ŋäätha Køny Mar Jwøk
1 Aani, a bëëdö naa raŋŋa jï Jwøk
keere naa lïŋö,
kiper køny mara ööi ka baŋe.
2 Bee eni keere na teek mara na
dïkunyi mara,
ni ena kar gwøk røk jïra, ni tïm
cwïnya ni ba bööi këët.
3 ?Aŋø, u bëët, a këël kany mo nyïëdi
nø noo bëëdu nou tuuŋŋa dhaanhø,
ki man raanynyu gø, kaamar kiir
mo dëëre ee nyaaŋø wala kal
mo nhønhnhi?
4 Man wø caarru keere beeye ki
man gøøu dhaanhø piny kare
na näk eno wøørø yie,
ni yïthu wø met ka caan tööt,
ni u wø gwëëdhö ka dhøgu, 'ba u
cïënö ki cwïnynyu.
5 Aani, a doo bëëdö naa raŋŋa jï
Jwøk keere naa lïŋö,
kiper a bëëdö naa ŋäätha eni.
6 Bee eni keere na teek mara na
dïkunyi mara,
ni ena kar gwøk røk jïra, ni tïm
cwïnya ni ba bööi këët.
7 Køny mara ka ajiem mara jooda
baŋ Jwøk,
ni teek mara ki kar kan røk mara
beeye Jwøk.
8 Dïbwör bäre, bëëdu nou ŋäätha
eni cooth,
ni kälu gïïa en cwïnynyu wøk
jïre;
kiper Jwøk beeye kar kan røk
marø.
9 Jø bäät piny bëët caala jam dhøk
jaak;
këël jøøa kwörge døøŋŋø ki moa
kwörge bäŋgø bëët, bäŋ karge.
Ni näk mo ge kïtha bäät gïr røm,
ge ba peek;
këël mo rwöpa ge bëët cøøn,
jööt marge kaala jööt mar jam
dhøk.
10 Kär jöör møt ŋääthu,
ni ba ŋääthu jammi mo jootu ka
køør kwal.
Ni näk jap kwär otïmö ni thööth
jïïu, kär cwïnynyu këëllu
køørge.
11 Jwøk acäänö yie aciel,
ni luup moa wïnynya beege luup
ariiø mo perge leth,
ni beege ni teek ena cer Jwøk,
12 ni mëër man wø ba jøøl käla baŋe.
Kiper ïïni na Wuuö Jwøk,
ŋati man nø wø cunnï cunnö ki
køør tïïe moe.
&Manøgø beeye duut Deebit.
@
*#Duut Ŋat Mo Lääŋŋa Jwøk
1 Wui Jwøk, beeye ïïni na Jwøk
mara; a wø manynya køørï.
A bëëdö naa manynya ïïni
kaawat man wø manynya pïï
ni aano 'näk riewi.
A bëëdö naa lääŋŋa ïïni paap,
kany ni bëëdö no otal ni bäŋ
pïï yie en.
2 Jïrï araŋa kar bëëtö marï na en
kur keere,
kiper nee teek marï ka ajiem
marï jooda.
3 Ï pwøa pwøø ki dhaa,
kiper mëër marï ni wø ba jøøl
letha pere ki kwøw;
4 a bëëdö naa pwøya ïïni ki yïth
nïr kwøwa bëët,
ni thaaŋa ceŋŋa maal naa lama
ïïni.
5 Yia atïmö ni met kaamar dhaanhø
mo ojäŋ ki cam mo met,
ni wära ni yia met naa pwøya ïïni.
6 Kany wø para ïïni naa ena kar
niine mara,
ï lääŋŋa lääŋŋö ki dï wäär bäre.
7 A wär ki dudi ni yia met tiet bwöpï,
kiper ï bëëdö na dïkunyi mara,
8 A bëëdö ni aano göök dëërï,
naa iï jølø ki cer cwïïï.
9 'Ba jø wø many man raanyge
jwïëya,
ge cøøa piny tiet ŋøøm.
10 Geno cïp ceŋ jøw 'näk geni ko
opëëlle,
ni tïmge na cam jï odïï.
11 'Ba nyeya yie omïnni ki Jwøk,
ni ö jø wø kööŋ ŋëët Jwøk bëët
ni kanyge;
'ba jø wø cäänö ki tööt, dhøkge
omec.
&Manøgø beeye duut Deebit mana
caae kanya en dï paap Juuda.
@
*#Duut Mo Kwaca Jwøk Nee Dhaanhnhe Kønye Ceŋ Nyïïmän
1 Wui Jwøk, wïny dwøra ki gïï
cäda kiperge ii; 
køny aani naa ba lwäya ki nyïïmänna.
2 Gwøk aani ki gïï wø tuut jøøa
reyø kipera,
ni gwøgï aani ceŋ jø wø tïïö ko okiera,
3 jø wø lëëpge ege paa ni beth ni
caala opëëllö,
ni wø lëëpge coony baŋ dhaanhø
kaamar athëëre.
4 Ge caala jiy mo omøør piny mo
ge thööya ŋat mo mare adïëri,
jø wø laar dhaanhø thööyö ni ge
ba lwäär.
5 Dhøkge wø tuutge tuudö nee gïï
mo reyø tïïcge na aciel,
ni cäänge ki man cïïge ka abïëp,
ni ge cädö ki cwïnyge ni bäŋ ŋat
joot geni.
6 Ge cädö ki man tïïge ki gïn mo raac,
ni tïïcge ka køør riek waŋ marge,
kiper acaara mar dhaanhø ki gïïa
en cwïnye ba joot.
7 'Ba geno këër Jwøki ka atheerø mare,
ni put dëëtge jïtö ki ŋwiili.
8 Luup moge odwøk Jwøki wïthge,
ni kïth ge yi ränynyö,
ni ö jø wø joot geni bëët ni buuge
geni.
9 Køøre jiy bëët otïmö ni lwäär;
ni ö gïna tïïc Jwøki ni køpge gø,
ni cätge kiper tïïe moe.
10 Ŋata mare beer yie omïnni ki
Wuuö Jwøk,
ni kan dëëre buute,
ni ö jøøa cwïnyge thïïŋ bëët ni kanyge.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Cäänö Kaper Gïï Wø Beyø Ni Wø Tïïc Jwøki
1 Wui Jwøk, jiy wø bëëdö ni ge
pwøya ïïni Dhayan, 
ni ö gïïa kööŋge ki ge ni cïpge ge
jïrï.
2 Ïïni ni wø wïny lam,
dhaanhø bäre ööa baŋï.
3 Raay atïmö ni manynya man
böötge waani,
'ba ïïni gïïa bacwa awëënnï.
4 Gwïëth en jï ŋat wø jierï ni wø
kälï buutï
kiper nee bëëde kar bëëtö marï.
Wa puta jäŋö ki japa beyø na en
yi ødï,
ni beeye kar bëëtö marï na en
kur keere.
5 Wui Jwøk, ï na dïkunyi marwa,
lam marwa wø løgï løø jïwa ki
køør adïëri marï,
ki køør tïïe moï ni wø rëëm ec.
Beeye ïïni ni wø ŋääth jø bäät
pinyi bëët,
këël moa en kwör mo bäyö løø
näpa døøŋŋø løøga.
6 Beeye ïïni na cwääc kïte ki teek
marï,
niï nyootha teek marï.
7 Beeye ïïni ni wø jook lwör mar
näpa døøŋŋø,
ni wø jook athage moge, ni
nigebäc;
këël okiera mar jiy wø joogï jooø.
8 Jiy mo wø bëëdö kwör mo bäyö,
ge lwäyö ki nyuuthe moï moa
näk rëëma ec.
Jø wø bëëdö jï løø kur tuul-cäŋ
ki jï løø kur pänh-cäŋ,
geno tïïyï niï pwøcge ni döötge
ena maal.
9 Piny wø liimï liimø ni jääŋŋï
køth,
ni tïïyï ŋøøm ni beyø ni jammi
ciek yie.
Näm moï wø pääŋï pääŋö ki pïï;
ni cïpï caammi jï jiy, 
moa näk iï nø jiiŋŋø kiperge.
10 Kwöra näk opuurö wø jwøyï
jwøø,
ni päärï wïth ŋøøm ni röömi,
ni døøŋï gø ki køth ni tïme ni
jööm,
ni gwïëthï gïï wø tuy yie.
11 Ki yi cwiir cooth ï wø cïpö ki
caammi mo beyø mo wø ciek,
ni ö orööge ni päŋge ki caammi
ni tïmge ni ge øya piny jöö
jaak.
12 Pwöla otuy ki luum mo pulli,
ni tïm thuuri ni mïërö ni ec met
ki ge.
13 Ni tïm pwöla ni päŋ ki dïëk,
ni røm gøli bëët ki beel,
ni ö jiyi ni kwöŋge ni ge wär ki
dudi ni yïthge met.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Pwøca Jwøk Kiper Gïïa Tïïe
1 U ni en bäät piny bäre, pwøyu
Jwøk ni döötu ena maal ni mïn
yïthu.
2 Wärru ki dudi nou jiema nyeŋŋe,
ni cïpu pwøc jïre ni wøørru eni.
3 Caannu jï Jwøk, ni «Tïïe moï
rëëma yïth jiy.
Ki køør teek marï na dwøŋ døc,
nyïïmän moï dëëtge atïmö ni
kwanynyi nyïmï.
4 Jø bäät piny bëët ï wøørge
wøørø,
ni wärge ki dut pwøc jïrï,
ni ge pwøya nyeŋŋï.»
5 Ööu ni neennu gïïa tïïc Jwøki,
ni beege tïïe mo rëëma ec moa
tïïe dï jiy.
6 Naama dwøŋ apääŋŋe ki dï gø,
ni dööŋe no otal,
ni put jiyi ŋut løøga ki piny jaak.
Kiper manøgønø, beerra man
mïn yïthø ki eni.
7 Eni bëëdö na wïth jiy na bäre
bäre ki køør teek mare,
ni nyeŋŋe ena bäät wïth juurre;
'ba ennø, kär dee jø ageem mo
tïŋa wïthge maal bääte.
8 Dïbwör bäre, pwøyu Jwøk marø,
nee pwøc man wø pwøyu eni ki
gø wïnynyi.
9 Bee eni ni wø gwøk øøni nøø
bëëdö ni ø kwøw,
ni bee eni ni wø ba wëëk tietø
ceec.
10 Wui Jwøk, waana päärï,
kaawat man wø twøn gwel-bïrö
kany wø leenyi, nee mana beer
joot.
11 Waana kïthï kar twöc,
ni kïthï bäätwa ki tëër mo peek.
12 Jiy awëëgï wääth bäätwa,
ni cørwa dï maac ni cääthwa yïth
pïï;
'ba waana kälï wøk ni cïbï wa
kar bëëtö mo beer.
13 Aani, a ööa yi øtø marï naa käädö
ko olämme mo wø waaŋ bäre,
ni cïba gïïa kööŋa ki ge jïrï,
14 ni beege moa näk yaa caanø ki
dhaa
kanya ena yïth gïï mo leth.
15 Lääy moa no olør ocïba jïrï no
olämme mo wø waaŋ bäre,
mo noo waaŋi, jïrö puta nitul,
ni beege nyöök rööm, ki rwädhe,
ki nyöök atëëe.
16 U wø lwäär Jwøk bëët, ööu,
wïnynyu gïn,
kiper nee gïna tïïc Jwøki jïra
caana jïïu.
17 Aana jwöŋö dëëre,
ni pwøa eni ki dhaa.
18 Doo na raay 'moa poot bëëdö ni
yaa maa cwïnya, 
Wuuö Jwøk lam mara bäŋa dee
wïnynyö;
19 'ba ka adïëri møn, Jwøk kwac
mara awïnynye,
ni leŋ dwøra kanya läma.
20 Pwøc en jï Jwøk,
eni na kär kwier man wïny lam
mara,
ni käre mëër mare ni wø ba jøøl
paanyø bääta.
@
*#Duut Mo Cäänö Kaper Man Ö Jiyi Bëët Ni Pwøcge Jwøk
1 Beerra man ö Jwøki ni nyooth met
ec mare jïwa ni gwïëth waani,
ni wëëk tac täärnyïme rieny bäätwa,
2 ni ö jööre ni tïme ni ŋäc bäät piny,
ni tïm kønynyi mare ni ŋäc dï
wïth juurre bëët.
3 Wui Jwøk, beerra man ö jiyi ni
pwøcge ïïni;
beerra man ö jiyi bëët ni pwøcge ïïni.
4 Beerra man mïn yïth juurre ni
wärge ni yïthge met,
kiper luup jiy wø ŋølï na adïëri,
ni bwøthï wïth juurre moa en
bäät piny.
5 Wui Jwøk, beerra man ö jiyi ni
pwøcge ïïni;
beerra man ö jiyi bëët ni pwøcge ïïni.
6 Ŋøøm aduunnö ki caammi;
Jwøk, ni beeye Jwøk marø,
bëëdö ni gwïëtha øøni.
7 Jwøk ø gwïëdhe gwïëdhö,
ni ö jø bäät pinynyi bëët ni
lwäcge ki eni.
@
*#Duut Mo Pwøca Jwøk Kiper Gïïa Tïïe
1 Beerra man ö Jwøki maal, ni
keeth nyïïmänne,
ni ö jø wø män ki eni ni bwøkge
nyïme.
2 Wui Jwøk, keeth geni kaawat
man wø ö jame wø keeth jïrö.
Beerra man räny jøøa reyø
nyïmï,
kaawat man wø ö gage wø leenyi
maaci.
3 'Ba beerra man ö jøøa bëëtö
marge beer ni mïn yïthge,
ni kanyge nyïm Jwøk,
ni bëëtge ni met ec marge
okadhø.
4 Wärru jï Jwøk, ni pwøyu nyeŋŋe
ki dudi;
wärru jïre ni döötu ena maal, eni
ni wø cäädhi ki bäät pøøl,
ni kanynyu nyïme, eni na Wuuö
Jwøk.
5 Jwøk ni wø bëëdö kar bëëtö
mare na en kur keere
bee eni na wää kïïe, ni bee eni ni
wø gwøk määr thuunhnhi.
6 Jwøk dhaanhø mo owii kur keere
wø di mooø ki paac.
Jø twöc wø käle wøk ni mooc
geni ki bëëtö mo beer;
'ba jø ageem bëëdö yi ŋöömö mo
raac.
7-8 Wui Jwøk, Jwø Icriel, kanya
bwödhï nyïm jiyï,
niï cäädha dï paap,
kanya pïïyï bäät Kïn Caynay,
piny ajïtö ki dïjäŋ piny,
ni ö køthi ni pädhe.
9 Wui Jwøk, køth mo dwøŋ ajääŋŋï,
ni dwøgï ŋøøpï na näk oränynyö
karge,
10 ni ö jiy moï ni jïtge ki kar bëëtö.
Wui Jwøk, jøøa can amooyï ki
køør beer marï.
11 Wuuö Jwøk mare acaane, ni put
nyïïmänni bwøk;
ni ö apoole mo thööth ni køpge
dwørøgø ni met enøgø, 
12 ni köge, ni «Nyeye ki jø leny
moge abwøk ni reŋge.»
Ni ö määnni moa dööŋ paac ni
pääŋge jammi moa twier.
13 Këël na bëët määrögø ni ge
bëëdö dhi lwaaga,
gena tïmö ni ge mïërö ni ge caala
akuuru mo bwöpe orïëbö ki
gïn mo ŋwaŋŋi,
mo okwöre moe orwødhø ki
warkey.
14 'Ba kanya ö Jwøa en teeki cere ni
keeth nyeye kaace,
bäät Kïn Jaalmön agääbö bäre ki
jammi moa dööŋ piny.
15 Kïdi mana teek beeye Kïn
Baacan,
kïnna näk wïthe thööth.
16 ?Aŋø, ï na kïnna wïthe thööth,
aperŋø ni räŋï ka agääde en,
niï raŋŋa kïnna jier Jwøki na kar
bëëtö mare?
Adïëri møn, Wuuö Jwøk ki dëëre
bëëdö kaace na bäre bäre.
17 Jïëth leny mo Jwøk mo wø tut
okwëënyi
thööth døc ni ba thum ki kwaan,
ni Wuuö Jwøk ena dïge kaawat
mana bëëde kar bëëtö mare na
en kur keere bäät Kïn Caynay.
18 Ï na Wuuö Jwøk, ïïna aa maal
bäät Kïn Dhayan,
ni jiy moa no omaaø ri leny pieyï
pieyø,
ni lwørï gïïa cïp jïrï yïthakic jiy,
këël moa cïp jø ageemmi thuwø,
ni putï bëëtö kaace.
19 Pwøc en jï Wuuö Jwøk,
eni ni wø käär øøni ki yïth nïne
bëët,
ni bee eni na pïëmi marø.
20 Jwøk marø beeye Jwøk mo
kunyö,
ni bee eni na Wuuö Jwøk ni wø
wëëk dhaanhø bødhø cer thøø.
21 'Ba Jwøk wï nyimän mare di gøø
ni keethe,
këël wï ŋat wø bëëdö ni nøøya
raay moe.
22 Wuuö Jwøk aköö,
ni «Ge duua duuö ki yi Baacan,
ni duua geni ki yïth kudi mo
naama dwøŋ,
23 kiper nee tietu lwøgu ki rem
nyïïmän mou,
ni ö guuwi mou thuwø ni jïtge ki
remø mo gatge gadø.»
24 Wui Jwøk, thaabuur marï ajoot jiyi,
ni beeye thaabuur marï, ï na
Jwøk mara, ï na nyeya mara,
ni jiy cøøa kar bëëtö marï na en
kur keere.
25 Jø wø wär, bwödhö nyïm,
ni ö jø wø pöödö ki thøme ni
enge køørge,
ni ö nyïïakugo pöödö ka anëët ni
enge lakge.
26 Pwøyu Jwøk dï acooŋa mo dwøŋ;
pwøyu eni na Wuuö Jwøk, uuni
na nyïïkwaac jø Icriel.
27 Tuuŋ Benjamen na thiinh nutö
kaace ni bwödhö eni;
ni kwääri mo jø tuuŋ Juuda ki jiy
moge,
ki kwääri mo jø tuuŋ Dhebulan
ki mo jø tuuŋ Naptali, ge nut
kaace thuwø.
28 Wui Jwøk, jääŋ teek marï,
ni nyoothï teek marï kaawat
mana tïïyï kiperwa dïkwøŋ.
29 Nyeye oböönh baŋï ki jammi
Øt Jwøk marï na dwøŋ na en
Jerucalem.
30 Jook Ijep ni caal lääy mo bëëdö
yïth oböödhi enø,
ni joogï nyeye mo wïth juurre ki
jiy moge ni wø caal rwädhe ki
nyïïrøøe yøø,
këël kanyo leeŋge dëëtge piny
nyïmï ni cïpge gwet ajwäk; 
keeth wïth juurre mo wø yïthge
met ki leny.
31 Cuumme oööi ki Ijep,
ni ö Ithiöpia ni laar cere thaaŋ
baŋ Jwøk.
32 Uuni na mïëc bäät piny, wärru jï
Jwøk;
wärru ki dut pwøc jïre, eni na
Wuuö Jwøk.
33 Wärru jïre, eni ni wø cäädhi ki
maal, ni beeye maal na nut
cøøn.
Ennø, eni cäänö ni jïre da teek.
34 Jiemmu Jwøk kiper teek mare,
eni na en ajiemmi mare bäät jø
Icriel,
na näk teek mare okëët maal.
35 Wui Jwøk, ï di lwäärö kar bëëtö
marï na en kur keere;
eni na Jwø Icriel ki dëëre, teek
wø cïbe cïbö jï jiye.
Pwøc en jï Jwøk.
&Manøgø beeye duut Deebit.
@
*#Duut Ŋat Mo Jwöŋö Dëër Jwøk Kiper Køny
1 Wui Jwøk, køny aani,
kiper a caala dhaanhø mo pïï
onø këët cwaage.
2 Aana niŋac yo odhöönh,
ni bäŋ kany këëla tiera yie.
Aana pïï dï naam kanya päŋ,
ni ö naammi ni mwøny aani.
3 A bëëdö ni aano ööl naa jwöŋö
cooth,
ni cwaaga orööy.
Ni ö nyeŋŋa ni talge jöö
naa raŋŋa jïrï, ï na Jwøk mara.
4 Jiy mo män ki aani ki gïn mo
bäŋ tiere jaak thööth døc,
ni kwäänge kaala jïëc wïïa,
ni jø wø many aani naa 'näkge
jaak beege jiy mo teek;
aana wëëkge cool jammi mo kära
kwalø.
5 Wui Jwøk, beeye ï ni ŋäc rääö
mara,
ni gïïa baya bëët paa okanø ki
ïïni.
6 Wui Wuuö Jwøk, ï na wïth jammi
bëët,
kär wïth jø wø raŋ jïrï lääi ki
køøra;
Wui Jwø Icriel,
kär nyeŋ jøøa many ïïni ränynyö
ki køøra.
7 Aani, ajøøŋ mana jøøŋ a ki gø,
ajïënya kiperï,
ni tïm wïïa ni laay døc.
8 Aana tïmö ni aana jur jï tuuŋwa,
ni tïma naa path jï nyïïmera;
9 kiper mana bëëda ni remø mara
otwak kiper øtø marï,
ni ö ajøøŋ mar jø wø jøøŋ ïïni ni
pänh bääta.
10 Kanya bëëda naa jwöŋö naa
wödö ki cam,
gïnögø atïmö na ajøøŋ dëëra.
11 Kanya røøa keeca dëëra na abïï
kiper pänh cwïny mara,
aana tïmö na gïr abuua jïge.
12 Jø wø pï piny bura wø cäänö ka
nyeŋŋa,
ni ö jø meerø ni jalge aani ki
duut.
13 'Ba aani, a wø lämö jïrï, ï na
Wuuö Jwøk,
kany wø näk ma kare ni wø
manynyï.
Wui Jwøk, wïny lam mara ki køør
mëër marï na päl ni wø ba jøøl,
ni kønyï aani ki køør adïëri marï.
14 Käl aani wøk ki yo odhöönhi ni
ena yie en,
naa ba naŋac yie;
køny aani ceŋ nyïïmänna,
ni kälï aani wøk ki yi naama
päŋ. 
15 Køny aani naa ba mwøny
naammi,
ni kønyï aani naa ba käl jwïëe,
ni ba wëëgï dhi buur dïïr bääta.
16 Wui Wuuö Jwøk, wïny lam mara
ki køør mëër marï na beer ni
wø ba jøøl,
ni luuï nyïmï baŋa ki køør bäth
ec marï na dwøŋ.
17 Kär täärnyïmï kanï ki aani, a na
laŋŋø marï,
kiper a ena yïth gïï mo leth;
beerra man laarï lam mara
wïnynyö.
18 Nyänh buuta ni wïïlï aani wøk,
naa wïïlï wøk ka ceŋ nyïïmänna.
19 Gïï wø jøøŋ aani ki ge bëët ŋäyï,
këël lään wïc mara ki räny nyeŋ
mara ŋäyï thuwø,
ni nyïïmänna bëët nëënö jïrï.
20 Ajøøŋ cwïnya araanynye,
ni tïma kaamar dhaanhø mo tuu;
ni rääŋa ki dhaanhø mo cwïnye
pädhi kipera, 'ba bäŋgø mo
yaa joodø,
ni rääŋa ki jiy mo cøma cwïnya,
'ba bäŋgø thuwø.
21 Aana moocge ki gïn mo keec ni
beeye cam jïra;
Kanya ö riewi na 'näk aani, aana
moocge ki køøŋ nyïïjenni mo
wac nee maadha.
22 'Ba beerra man tïm cam marge
na abïëp mo maga geni,
ni tïm bëët-mëër marge ni caala
akupa mo duua ränynyö
bäätge.
23 Beerra man tïm nyeŋge no
onijïïm ni bäŋ gïn nëëni jïge,
ni tïm cuu pïth moge ni
nhønhnhi na bäre bäre.
24 Kïth ajäla marï bäätge,
ni ö wëërri marï na dwøŋ døc ni
pïïe bäätge.
25 Beerra man tïm twïër marge ni
ba beet,
ni bäŋe dhaanhø mo bëëdö yïth
oduŋkaare moge.
26 Kiper dhaanhnhï na näk iï
pwödö acäŋge caannø,
ni ö eni na dëëre mooyï ki gïn
mo leth ni cäŋge dëër gø
mooyø ki rääm.
27 Cäŋ bäät ajäla marge meetø ka
ajäla mør;
ge kär jïëyï ni marge beer.
28 Beerra man gööp nyeŋge wøk yi
wëël kwøw;
ni ö nyeŋge ni ba göörï kanya
aciel ki jøøa beyø.
29 'Ba aani, aano caannø naa bëëdö
naa rämö;
wui Jwøk, beerra man kønyï aani
ni gwøgï aani.
30 Nyeŋ Jwøk pwøa pwøø ki duut,
ni tïŋa nyeŋŋe maal ki køør man
wø dwøga met ec jïre.
31 Ni beeye gïn wø tïïc yi Wuuö
Jwøk ni met
ni kaala dhieŋ man wø cïp no
olämi,
wala rwaath mo dwøŋ.
32 Kanyo jooti ya jøøa canni, yïthge
omïnni;
'ba uuni ni wø cac Jwøk, beerra
man jïtu ki cøm cwïny.
33 Kiper Wuuö Jwøk luum jøøa can
di wïnynyö,
ni luum jiye moa näk otwöö ba
taae.
34 Beerra man ö maalli ki piny ni
pwøcge eni,
ki näpa døøŋŋø këël ki gïï wø
bëëdö yïthge bëët.
35 Kiper Jwøk jø Dhayan di kønyø,
ni cäŋ päänye mo Juuda tïïyö
nee geer,
ni ö jiyi ni bëëtge kaace ni bëët
ŋøøpøgø na moge.
36 Ni dööŋ ŋøøpøgø jï nyïïkwaacge,
ni ö geni ni wø mëër ki eni ni
bëëtge yie.
&Manøgø beeye duut Deebit.
@
*#Duut Ŋat Mo Kwaya Jwøk Nee Eni Køny Ceŋ Nyïïmänne
1 Wui Jwøk, beerra man piemï
aani,
Wui Wuuö Jwøk, laar rwänh
kuna kønyï aani.
2 Jøøa many man 'näkge aani,
beerra man lää wïthge ni kier
wïthge.
Jøøa yïthge met ki caannø mara,
beerra man riem geni ni räny
nyeŋge.
3 Beerra man ö jø wø buu aani
ni bwøk cwïnyge ki køør lään
wïc marge.
4 'Ba jø wø cac ïïni bëët,
beerra man mïn yïthge ki ïïni ni
kanyge,
ni ö jø wø yïthge met ki køny
marï
ni cäänge ni nøøcge nøøyø, ni ge
köö,
ni «Dwøŋŋa Jwøk; dwøŋŋa Jwøk!»
5 'Ba aani, aano caannø naa can;
'ba ï na Jwøk, laar rwänh baŋa.
Bee ï ni wø køny aani, ni bee ï ni
wø piem aani;
Wui Wuuö Jwøk, kärï ruu.
&Manøgø beeye duut Deebit
mana par wï Jwøk ki gø.
@
*#Duut Ŋat Ma Jaal Mo Kwaaya Køny
1 Wui Wuuö Jwøk, a bëëdö ni raa
yaa kan buutï;
kär wïïa wëëk lääö na bäre bäre.
2 Køny aani ki køør adïëri marï, ni
piemï aani.
Wïny dwøra ni piemï aani.
3 Bëëdï ni ïïna kïn gwøk røk man
wø reŋŋa bääte cooth;
ni cïpï ki dwøl kiper naa køny,
kiper ïïna teek mara, ni ïïna kar
gwøk røk mara.
4 Wui, ï na Jwøk mara, køny aani
ceŋ jø raay,
ceŋ jø wø tïïö ki gïï mo reyø ni
wø bëëdö no ogäy.
5 Wui Wuuö Jwøk, beeye ï ni wø
ŋäädha,
ni bee ï na ŋäädha ki mana täga
thïnhö.
6 Bee ï ni wø käär aani ki mana
täge ki kanya nywøl aani,
ni beeye ïïni na tïïc aani nee
lwaarø ki aani.
Aani, a bëëdö naa pwøya ïïni
cooth.
7 Aana tïmö ni aana nyuudhi jï jiy
mo thööth,
'ba beeye ïïni ni teek ni wø gwøk
aani.
8 Ï pwøa pwøø ki cwïnya bäre,
ni bëëda naa jiema ïïni ki yïth
nïne bëët.
9 A kär jarï këël ni bëëda ni aana
jaal en,
ni ba wiiï aani kur keera këël ni
bëëda ni bäŋ teek dëëra en.
10 Kiper nyïïmänna aløny ni ge
cäänö kipera,
ni ö jø wø many aani naa 'näkge
ni tuutge dhøkge,
11 ni köge, «Kee ena nø wec Jwøki;
reŋŋu køøre ni magu gø,
kiper bäŋ ŋat mo piem eni këët.»
12 Wui Jwøk, kär karï tïïyï ni bäär
ki aani;
wui, ï na Jwøk mara, laar rwänh
kuna kønyï aani. 
13 Beerra man lää wïth nyïïmänna
ni dïïr wïthge,
ni ö jø wø many tïïö ki gïn mo
leth dëëra ni jøøŋ geni ni räny
nyeŋge.
14 'Ba aani, a bëëdö naa raŋŋa jïrï
cooth,
ni ö pwøci man wø pwøa ïïni ki
gø ni meet ree.
15 Aani, a bëëdö naa cara gïr adïëri
marï,
naa cara gïr pïëm man wø piemï
jiy ki gø ki yïth nïne bëët,
këël na bëëtge ni thööth ni kaala
moa ŋääa.
16 Wui Wuuö Jwøk, a tägö ki man
caana gïïa tïïyï ki køør teek
marï,
ni bëëda naa cara gïr adïëri marï
keerï.
17 Wui Jwøk, aana tägï ki
pwönynyö naa poot thiinh,
ni bëëda naa poot køpa gïïa tïïyï
na näk rëëma ec këël dïcäŋi
en.
18 Wui Jwøk, kär a weyï,
këël ni bëëde ni aana jaal ni wïïa
da lwaar en,
kiper nee gïr teek marï køba jï
beenhnhø man ki moo ööi
bëët.
19 Wui Jwøk, adïëri marï dwøŋ døc
no okëët maal,
ïïni na tïïc gïïa døøŋŋø.
?Wui Jwøk, aŋa ni röömi ki ïïni?
20 Ïïni na tïïc aani nee gïï mo
thööth mo leth pïïcge bääta,
aano cäŋï mooyø ki kwøw,
ni duuï aani wøk ki dhi bwörö.
21 Wödö man wøør aani ki gø
omeetï,
ni cäŋï cwïnya cømmø.
22 'Ba aani, a pöödö ki thoomothïënhö
jïrï, ï na Jwøk mara,
naa pwøya ïïni kiper adïëri marï,
ni wära ki dut pwøc jïrï ki yi
thoom-othïënhö,
ï na en kur keere na Jwø Icriel.
23 Aano wär ni yia met ni dwøra
ena maal,
naa pwøya ïïni,
naa wär ka cwïnya bäre kiper
mana piemï aani.
24 Tïïe moï moa na adïëri ocaana ki
yïth nïne bëët,
kiper jøøa many gïn mo leth nee
tïïcge dëëra
wïthge alääö ni räny nyeŋge.
@
*#Duut Lam Kiper Nyeya
1 Wui Jwøk, nyooth ŋøl marï na
beer jï nyeya,
ni nyoothï adïëri marï jïre, eni
na o nyeya.
2 Beerra man ö eni ni ŋøl luup jiyï
na adïëri,
ni ŋøl luup jiyï moa no ocaannø
ki ŋøl mo beer.
3 Beerra man jït jiyi ki bëët-mëër,
ni ciek ŋøømmi, ni kwär jiyi,
ni jït paaci ki bëëtö mo beer.
4 Beerra man ö nyeya ni ŋun jøøa
no ocaannø,
ni piem obwöre mo jøøa can,
ni raany ŋat wø many man thiel
jiy piny.
5 Beerra man ö jiyi ni lwäärge ïïni
këël kanyo poot cäŋŋi ki dwääy
ni nut bäät piny,
këël mano këët røk beenhnhe
bëët moo ööi.
6 Beerra man tïm ööny nyeya ni
caala ööny køth
mo jwøya piny, ni tïïc luum ni
pulli,
ni caala køth mo dwøŋ mo jwøya
piny bäre.
7 Beerra man ö adïëri ni nyaae
yïth nïro beede ni ena nyeya, 
ni ö bëët-mëër ni nyaae këël
kanyo poot dwääyi ni nut bäät
piny.
8 Beerra man bëët pinynyi ni ena
cere,
ni tägi ka jï løø kur tuul-cäŋ këël
jï løø kur pänh-cäŋ,
ni cäŋ tägö ki Naam Upareeti
këël cuŋ piny.
9 Beerra man ö jø wø bëëdö paap
ni dwøkge kööthge piny nyïme,
ni ö nyïïmänni moe ni këëlge
cøŋge yi tør.
10 Beerra man ö nyec Tarcëc ki
nyec jø wø bëëdö bäät naama
dwøŋ
ni cïpge ka ajwäk jïre,
ni ö nyec Cïïba ki nyec Ceba ni
böönhge baŋe.
11 Beerra man ö nyeye bëët ni
dwøkge kööthge piny nyïme,
ni ö wïth juurre bëët ni tïnyge
eni.
12 Kiper eni ŋata can di piemø kany
wø jwöŋe dëëre,
këël ŋata no ocaannø ki ŋata näk
bäŋ dïkunyi jïre.
13 Ni cwïnye wø pädhö kiper ŋata
jïre bäŋ teek ki ŋata can,
ni kwøw geni.
14 Eni jøøgø wø pieme piemø ceŋ jø
wø thiel geni piny ki ceŋ jøøa
no ogäy,
ni bëëde ni per jwïëcge leth jïre.
15 Beerra man bëëde ni eni kwøw
cooth,
ni ö warkeyi mar Cïïba ni mëëgi
eni.
Beerra man läm jiyi kipere
cooth,
ni bëëde ni ge gwïëtha eni ki
yïth nïne bëët.
16 Beerra man jït ŋøømmi ki bëëlö
mo päl këël wïth kïte,
ni ö wïth beelli ni bëëtge ni tuuŋ
jame tuuŋŋö kaamar jer bäät
Kïn Libaanø,
ni nyaac jiyi yïth päänye bëët
kaamar luum mo ena yi pwöla.
17 Beerra man bëët nyeŋ nyeya ni
ŋäc na bäre bäre,
ni wïny nyeŋŋe dï jiy kanyo
poode ni cäŋ poot nut ni rieny.
Beerra man ö jiyi ni gwïëdhi ki
køøre,
ni ö wïth juurre bëët ni köge ni
eno gwïëdhö.
18 Pwøc en jï Wuuö Jwøk, Jwø Icriel;
na näk bee eni keere ni wø tïïc
gïï mo rëëma ec.
19 Pwøc en jïre, ni put nyeŋŋe
bëëdö no ojiemø na bäre bäre;
ni ö ajiemmi mare ni pääŋ piny
bäre.
Kare møn, enøgønø.
20 Man beeye aŋuun dut lam mo
Deebit o Jeci.
&Manøgø beeye duut mana
cak jï Cølöman.
@
*#Duut Mo Nyootha Aŋuun Bëët Jøøa Reyø Ki Bëët Dhaanh Jwøk
1 Ka adïëri møn, Jwøk mëër ki jø
Icriel,
ni beege jøøa cwïnyge thïïŋ.
2 'Ba aani, kara acäännö ki man
pädha,
ni tïma naa caala dhaanhø mo
cäädha yo othwørø.
3 Kiper aana tïmö naa këëö kiper
bëët jø atöör,
kanya jooda geni, ge na jøøa
reyø, ni geno kwär.
4 Kiper geni bäŋ gïn mo jwørge;
ge bëëdö ni dëëtge jööt jaak ni
ge teek.
5 Ge kär ööl kaamar jiy møga,
ni bäŋ gïn mo leth mo pïï dëëtge.
6 Kiper manøgønø, atöör atïïcge na
gïr ajiem
kaamar tii mo otwöö cwaak,
ni tïm dïwïti kaamar abïï mo ege
røø dëëtge.
7 Nyeŋge okwöt ki lørø,
ni gïï wø reyø wø caarge ki
cwïnyge thööth.
8 Ge bëënna abuua ni ge cara luup
mo reyø,
ni ge töödö ni ge manynya gø
nee jiy møga thielge piny.
9 Dhøkge cara luup mo reyø dëër
Wuuö Jwøk ni en maal,
ni ö lëëpge ni carge luup atöör dï
piny bäre.
10 Ni ö jø Jwøki ni døøge cään
baŋge
ni putge jïëy ki marge.
11 Ni kö jø atöörri, na «?Aŋø, Jwøk
da gïn mo ŋääe kiper bëëtö
marwa?
?Aŋø, da leec wïc jï Jwøa Dwøŋ
ni en Maal?»
12 Neennu nø mø, jø raay beege yøø
nø;
cooth bëëtö marge jööt jaak, ni
kwärö marge cäätha nyïme.
13 'Ba aani, ka adïëri møn, cwïnya
adøøya mo waany ki gïn mo
oballe jaak,
ni bëëda ki bëëtö mo beer kiper
gïn mo bäŋ tiere jaak.
14 Kiper gïï mo leth atïmö ni pïï
dëëra cooth,
ni bëëda naa jøøya gïï mo leth ki
yïth nïne bëët.
15 'Ba aani, gïnögø kära caanø.
Wui Jwøk, doo na yaa caanø,
mara doo tïmö naa dwøga
ŋäädhe mar jiyï cään.
16 'Ba kanya pooda naa poot kär ci
Øt Jwøk,
naa cädö kiper nee tier
luummögø jooda,
atïmö ni teek jïra ki man jooda gø;
17 'ba na cøøa Øt Jwøk,
aŋuun bëëtö marge ajooda.
18 Ka adïëri møn, ge cïbï kwör mo
cëëö,
ni leeŋï ge yi ränynyö.
19 Ge laara ränynyö ki kany mo
thiinh,
ni thumge na bäre bäre ki køør
gïï mo leth mo opïï dëëtge.
20 Wui Wuuö Jwøk, kaawat man wø
ö dhaanhe wø taak lääk kanyo
pääe,
ïïni thuwø ge taagï taaø kanyo
ööï maal bäätge.
21 Kanya bëët cwïnya ni keec,
ni yia raac,
22 aana bëëdö ni bäŋ gïn mo ŋääa
ni wïïa bäŋgø,
ni tïma naa caala lääy nyïmï.
23 'Ba ennø, ajooda naa poot bëëdö
ka ïïni,
ni cer cwïïa iï maaø,
24 naa bwøthï ka ri pwöc moï;
køøre nø, aano pänhnhï ni jïta
buutï ka ajiem.
25 ?Wui Wuuö Jwøk, aŋa ni ŋäädha
maal këët?
?Patha ïïni?
Bäŋ gïn mør mo manynya bäät
piny,
'ba beeye ïïni keerï.
26 Løny ki man ö rïŋ dëëra ni
ränynye, ni päth cwïnya,
'ba ï na Jwøk, ï poot bëëdö ni
ïïna teek mara,
ni bëëdï ni ïïna kura na bäre bäre.
27 'Ba ka adïëri møn, jø wø jäth
karge ki ïïni, ränynyö, 
ni dïïrï wïth jø wø dhal luummï.
28 'Ba aani, bëëtö mo beer wø jooda
buut Jwøk,
ni dëëra wø kana buute, eni na
Wuuö Jwøk,
nee luum tïïe moe bëët caana.
&Manøgø beeye duut mar Acaap.
@
*#Duut Mo Kwaca Jwøk Nee Nyïïmän Moa Raany Øtø Mare Jääle
1 ?Wui Jwøk, aperŋø ni putï wa
kwier na bäre bäre en?
?Aperŋø ni gootï ki waani na
dïëgï en?
2 Par wïïï ki jiyï moa piemï cøøn,
jøøa wïïlï wøk nee tïmge na jiyï.
Par wïïï ki Kïn Dhayan kanya
bëëdï yie.
3 Ööï ni cäädhï niï raŋŋa øtø marï
na näk oränynyö na bäre;
nyïïmän gïïa en øtø marï na en
kur keere araanyge bëët.
4 Nyïïmännï akwöŋŋö ki met ec
kar ødï kanya wara røømmï
yie ki jiyï,
ni cwöthge bëëre moge piny na
nyuuthe.
5 Ni tïmge kaamar jiy mo ŋøda jen
piny yi lul,
6 ni ö jenni moa näk otieŋø yi øtø
marï
ni kaaŋge ge ki lïge ki guduume.
7 Øtø marï na en kur keere
awaaŋge na bäre,
ni tïïcge kar bëëtö marï na ŋäc
nyeŋŋï yie ni ba waany.
8 Gena cäänö ki cwïnyge ni köge,
ni «Dïïmø geni na bäre bäre.»
Ni öge ni waaŋge uut acook Jwøk
bëët moa en dï paac bäre.
9 Nyuuthe moa cïp Jwøki jïwa ba
jootwa nïri,
ni tïme ni bäŋ nyikuŋ Jwøk dïwa
këët,
ni bäŋ dhaanhø dïwa mo ŋäc
ruuö mar gïïa leth na tägö.
10 ?Wui Wuuö Jwøk, a këël kany
mo nyïëdi nø noo bëët
nyïïmänni ni buuö?
?Aŋø, ge puta bëëtö ni ge jøøŋŋa
ïïni na bäre bäre?
11 ?Aperŋø ni bëëdï ni cerï na teek
iï kut köörï jaak en?
Beerra man kerï riï ni raanynyï
geni.
12 'Ba ï na Jwøk, ï bëëdö ni ïïna
nyeya mara cøøn,
niï wø bëëdö ni marï køny bäät
piny bäre.
13 Ïïni, pï naama dwøŋ apääŋŋï ki
teek marï,
ni nyathï wïth lääc naama dwøŋ
tiet pïï.
14 Ïïni, Lëëwatan, lääna wïthe
thööth, anyathï,
ni wëëgï gø lääc paap nee camge.
15 Ïïni, jøør ki näm awëëgï kwödö,
ni taalï näpa wara bëëdö ni
kwödö cooth.
16 Ïïni, waŋcäŋ beeye marï, ni wäär
poot na marï thuwø,
ni beeye ïïni na cïp cäŋ ki dwääy
kwörge.
17 Nyeŋ kee mo bäät piny bëët tïïya
ïïni,
ni öörö ki cwiir tïïya ïïni thuwø.
18 Wui Wuuö Jwøk, par wïïï ka
abuua mar nyïïmän,
ka ajøøŋ mar bøøre ni wø taak
ïïni.
19 Kär jwïëc jiyï na jägö kaamar
akuyi wëëk nyïïmän moge,
ni ba bëëdï ki kany mo bäär ni wïïï
owïl ki jwïëc jiyï na no ocaarø.
20 Cäŋ wïïï caarrø kiper luubö
mana tuutï ki waani,
kiper kwöra näk muudhö dï paac
päŋ ki jiy mo tïïö ki gïï mo
reyø.
21 Kär jøøa näk odïïmö duuö ni
wïthge olääö,
'ba beerra man ö jøøa no ocaarø ki
moa näk oööl ni pwøcge nyeŋŋï.
22 Wui Jwøk, ö maal ni caanï
luummï,
ni parï wïïï ki gïn ö bøøre ni
bëëtge ni ge jøøŋŋa ïïni cooth
en.
23 Kär luup nyïïmännï taagï,
kiper dïŋaŋ mar jø wø ö maal
bäätï wïnyö cooth.
&Manøgø beeye duut mar Acaap.
@
*#Duut Mo Pwøca Jwøk Kiper Ŋøl Mare Na Näk Kare
1 Wui Jwøk, wa pwøya ïïni;
wa pwøya ïïni møn, kiper karï
cään ki waani;
ni ö jiyi ni køpge tïïe moï na näk
rëëma ec.
2 Jwøk aköö, ni «Kanyo tïme na
kanya näk yaa jierø,
luup ŋøla ŋølø na karge.
3 Kanyo leeny pinynyi ki jiy moa
en yie bëët,
beeye aani noo tïïc gø nee cuŋŋe
ni teek.
4 Aana köö jï jø ŋwøc, ni ‹Käru
ŋwöö›,
ni kööa jï jøøa reyø, ni ‹Kär
wïthu tïŋu maal.
5 Kär wïthu tïŋu maal,
ni ba cäänu nou ŋaya ŋutu.› »
6 Kiper dööŋ-kar dhaanhø ba käl
jï løø kur tuul-cäŋ wala jï løø
kur pänh-cäŋ,
ni ba käl paap thuwø.
7 'Ba beeye Jwøk keere ni wø ŋøl
luup,
ni wø dwøk maya piny ni tïŋ
maya maal.
8 Kiper cer Wuuö Jwøk da athöönh
ajäla,
ni yie da køøŋø mo keec mo onø
twaaø,
ni cïp gø nee maath jøøa reyø mo
bäät piny bäre,
këël alage moe bëët.
9 'Ba aani, gïr Jwø Jeekap okøba
cooth,
ni wära ki duut pwøc jïre.
10 Jwøk teek mar jøøa reyø bëët
raanynye raanynyø,
'ba teek mar jøøa beyø meede
meedø.
&Manøgø beeye duut mar Acaap.
@
*#Duut Mo Pwøca Jwøk Kiper Teek Mare
1 Jwøk ŋäc dï Juuda,
ni nyeŋŋe bëëdö ni dwøŋ dï Icriel.
2 Øtø mare ena Calem, 
ni beeye kar bëëtö mare bäät Kïn
Dhayan.
3 Kaace athëëre mo nyïïmän atøye,
ni tøc kööt leny, ko opëëlle, ki
jap leny bëët.
4 Ï na Jwøk, ï bëëdö ni ïïno rieny,
na ajiem marï kaala ajiem kïte
mo wø bëëdö na bäre bäre.
5 Jø wø bëëdö ni teeka geni nyïm
leny, japge akäl,
ni putge thøø,
ni bäŋe gïn mo oløny jïge ki tïïc
këët.
6 Wui Jwø Jeekap, ki køør mana
mänï geni, 
okwëënyi ki jïëth leny mo wø
tutge adööŋ ni cuŋŋö jaak.
7 Beeye ï keerï, ï na Jwøk, na doo
lwäärö.
?Aŋa ni løny jïre ki man cuŋŋe
nyïmï kany wø wëërï?
8 Luum ŋøl acaanï niï ena maal,
ni ö jø bäät pinynyi bäre ni
lwäcge ni lïŋge.
9 'Ba kanya ööï maal niï ŋøla luup,
jøøa can moa en bäät piny
apiemï.
10 Ka adïëri møn, këël wëër mar jiy
tïmö ni duua pwøc jïrï,
ni tïm aŋuun wëërri ni ena cerï.
11 Kööŋŋu jï Wuuö Jwøk, eni na
Jwøk maru,
ni tïïyu gïïa kööŋŋu kiperge jïre.
Beerra man ö wïth juurre moa
karge cään ki eni
ni böönhge nyïme, eni na doo
lwäärö.
12 Eni bäät kwääri di bäädhö,
ni ö nyec bäät pinynyi ni lwäärge
eni.
&Manøgø beeye duut mar Acaap.
@
*#Duut Mo Cøma Cwïny Ki Køør Tïïe Mo Jwøk
1 A jwöŋö dëër Jwøk kiper køny,
ni dwøra yaa tïŋ maal, ni wïny
mara.
2 Kany wø ena yïth gïï mo leth, a
bëëdö naa kwaaya Wuuö Jwøk,
ni ki wäär ceŋŋa thaaŋa baŋe
naa ba jwöm;
'ba cwïnya adhäthö ki cøm.
3 Wïïa apara ki Wuuö Jwøk, ni
puta guyö;
ni cäda, ni ö bääta ni pädhe.
4 Nyeŋŋa amäne ki niine,
ni ö cwïnya ni pädhe,
ni tïm cäänö ni ba løny jïra.
5 A cädö kiper nïne moa cääŋŋe,
këël kiper cwiiri moa no
opöödhö cøøn.
6 Ki wäär bäre a bëëdö naa cädö,
ni cäda ki yi cwïnya ni pëënynya
dëëra keera;
7 ni kööa, na «?Aŋø, Wuuö Jwøk ø
kwiere kwierø na bäre bäre?
?Eni yie ba mïnni ki øøni këët?
8 ?Mëër mare ni wø ba jøøl
rwäänyö na bäre bäre?
?A luumma kööŋe ki gø wiie wiiø
na bäre bäre?
9 ?Wïïe wïl ki tïï met ec mare?
?A mëër mare awiile ki wëër?»
10 Ni kööa, ni «Jwøa Dwøŋ ni en
Maal teek mare akane ki aani,
ni beeye ni bëëda naa kïmmö en.»
11 Wui Wuuö Jwøk, wïïa opara ki
gïïa tïïyï;
ka adïëri møn, wïïa opara ki gïïa
näk rëëma ec na tïïyï cøøn.
12 A cädö kiper gïïa tïïyï bëët,
ni cäda kiper tïïe moï na døøŋŋø.
13 Wui Jwøk, jöör bëëtö marï ena
kur keere;
?a Jwøe mane ni dwøŋ ni caal
ïïni na Jwøwa?
14 Ïïna Jwø wø tïïö ki gïï mo rëëma
ec,
ni wø nyooth teek mare dï jiy.
15 Jiyï awïïlï wøk ki teek badï,
ni beege nyïïkwaac Jeekap ki
nyïïkwaac Jocep.
16 Wui Jwøk, ïïna joot pï naama
dwøŋŋi;
ïïna joot pï naama dwøŋŋi, ni
tïmge ni dhulli ki lwär,
ni tïm kudi moe ni wälli.
17 Pøøl apädhö na køth mo dwøŋ,
ni ö maalli ni märe,
ni ö agaackøthi ni keethge
kaamar athëëre.
18 Dwør määc køth marï awïnyö ki
ya atuunna, 
ni ö malø mare ni meeny bäät
piny,
ni tïm pinynyi ni kwanynyi ni
jäŋŋi.
19 Øtjöö marï cøra dï naama dwøŋ,
niï cäädhi ka kwöra päŋ,
ni kwör tietï ba joot.
20 Jiyï abwøthï kaamar pïïth dïëk,
ni ge ena cer Modhe ka Aran.
&Manøgø beeye duut mar Acaap.
@
*#Duut Mo Lamma Jöö Mana Ö Jwøki Na Käär Jiye Ki Gø
1 Wui jø powa, cegu ïthu, ni
wïnynyu pwöc mara,
ni këëllu ïthu piny ki luumma.
2 Aani, gïïa tägö lama lamø jïïu,
ni beege gïïa näk tietge okanø
cøøn,
3 gïïa näk yøø wïnynyö na ŋääø,
na no ocaan kwäyø jïïø.
4 Gïïögø ba døø mooŋø ki
nyïïkwaayø;
'ba pwøc man wø pwøc Wuuö
Jwøk ki gø døø caanø jï
beenhnhe moo ööi,
këël gïr teek mare ki tïïe moe na
näk rëëma ec.
5 Wuuö Jwøk luumme acaane, ni
cïp ciik moe
jï jø Icriel, ni beege nyïïkwaac
Jeekap,
ni kööm kwäyø ki ge nee obwöre
moge pwönyge ki ge,
6 nee ŋäc beenhnhe moo ööi,
ni beege obwöre moo nywøl
cään,
nee läwge caan jï obwöre moge
thuwø;
7 kiper nee ge bëëtge ni ge ŋäätha
Jwøk,
ni ge gwøga ciik moe,
ni ba wïl wïthge ki tïïe moe;
8 nee ge ba tïmge kaamar kwäcge
na wïnni na näk gena jø
ageem,
na näk cwïnyge ba en køør
adïëri,
na näk cwïnyge kär nieŋ køør
Jwøk.
9 Jø Ipariem, na wara bëëde, gena
jiy mo ŋäc leny ka athëëre,
'ba dïcäŋa këëtge gena riemmi.
10 Luumma tuut Jwøki ki geni
kärge gwøø,
ni kweerge ki man cääthge ki
køør ciik moe,
11 ni wïl wïthge ki tïïe moe,
ki gïïa näk rëëma ec na nyoodhe
jïge.
12 Ena tïïö ki gïï mo rëëma ec nyïm
kwäcge,
yi pwöl Dhöän na en yi ŋööm
Ijep.
13 Pï naama dwøŋ apääŋŋe,
ni wëëk jiy pöödhö ki yie,
ni tïïc pïï nee cuŋge ni tïmge
kaamar ageela.
14 Gena bwødhe ki pöölö ki dïcäŋ,
ni bwøth geni ki tac maac ki wäär.
15 Kïte moa en paap akaaŋŋe,
nee jiye mooe ki pïï mo thööth
mo caala pï naama dwøŋ.
16 Pïï atïïe nee kwönge wøk ki yi
kïdi,
ni wëëk ge kwödö kaamar pï
naam.
17 'Ba gena bëëdö ni ge poot tïïö ki
raay dëëre,
ni ge poot gëëmö dï paap ki eni
na Jwøa Dwøŋ ni en Maal.
18 Jwøk apäänyge ki cwïnyge bäre,
ni ge pëënynya cam mana lääŋge
keere.
19 Gena cäänö dëër Jwøk, ni köge,
na «?Aŋø, løny jï Jwøk ki man
cïpe ki cam dï paap kany?
20 Ka adïëri møn, kïdi agøøe, ni ö
pïïyi wøk,
ni tïm pïïyi ni kwödö;
?a møø nø, løny jïre thuwø ki
man cïp gø,
ni løny jïre thuwø ki man cïpe ki
rïŋö jï jiye?»
21 'Ba kanya ö Wuuö Jwøki na wïny
gïnögø, ena wëër døc;
ena wëër ki wëër mo dwøŋ ki jø
Icriel,
ni tïm wëërri mare ni liel kaamar
maac dëëtge, ge na nyïïkwaac
Jeekap,
22 kiper Jwøk kärge ŋäädhö,
ni kärge pïëm man piem geni ki
gø ŋäädhö.
23 'Ba eni maal aköömme,
ni jap dhøk uudi mo gø,
24 ni jääŋ møø mana cwøl ni meena
bäätge kaamar køth nee
camge,
ni mooc ge ki cam mo käla maal.
25 Ni ö jiyi ni camge muunni mo
nyïïatwiet maal,
ni beeye cam mana päl na jääŋ
Jwøki jïge.
26 Jam jï løø kur tuul-cäŋ atïïe nee
kwönne ki maal,
ni bwøth jam jï løø tier-piny ki
teek mare,
27 ni kööla lwaa wenyø bäätge na
cam, ni päl kaamar tør,
ni kwäänge caala nyeŋ akwöny
deŋ näpa døøŋŋø,
28 ni wëëk geni pänh dï twïër marge,
kwör bëëte moge, këël deŋŋe
bäre.
29 Ni ö geni ni cämge ni jäŋge døc,
kiper gïna lääŋge acïp Jwøki jïge.
30 'Ba kanya poode ni ge poot kär
jøøm ki cam,
ni ceŋge poot ena dhøkge,
31 wëëc Jwøk aput ö bäätge,
ni 'näk jø møøk moa dëëtge teek
rege,
ni beege wøpe moa no ojierø dï
Icriel.
32 'Ba këël na bëëde ni gïïögø bëët
otïïö,
ge poot tïïö ki raay,
ni kärge jïëy ki Jwøk,
këël na bëëde ni gïïa näk rëëma
ec moa tïïe ege joodø.
33 Kiper manøgønø, nïr kwøw
moge atïïe nee laarge pöödhö
kaamar jam dhøk,
ni tïm aŋuun cwiiri moge na
ränynyö.
34 'Ba kanya ö Jwøki na 'näk geni,
gena tïmö ni ge manynya eni,
ni duuge baŋe ni ge caya eni døc,
35 ni parge wïthge ni Jwøk beeye
teek marge,
ni bee eni na dwøŋ ni en maal na
pïëmi marge.
36 'Ba ena cøøkge ki dhøkge jaak,
ni ö lëëpge ni bëëtge ni cara tööt
dëëre,
37 ni bëëtge ni cwïnyge ba en
køøre,
ni kärge luubö mana tuude ki
geni gwøø.
38 'Ba eni gïïa bacge awëënne ki
køør bäth yie,
ni käre geni raanynyø,
ni kwier wëër ki kwöre mo
thööth,
ni käre wëër mare nyoodhø ki
pälle bäre;
39 kiper wïïe acaare ki man näk mo
gena jiy jaak,
ni ge caala jamø man wø pöödhi
ni ba duui këët.
40 A kwöre adïï na bëëtge ni ge
gëëmö ki eni,
ni moocge eni ki kïmmö dï
paap!
41 Jwøk apäänyge kwöre mo
thööth,
ni cwaatge yi gø, eni na Jwø
Icriel na en kur keere.
42 Wïthge awïl ki teek mare mana
tïïe
dïcäŋ mana käl geni wøk yie
ceŋ jøøa thiel geni piny,
43 kanya ööe na tïïc nyuuthe moe
ki gïï mo rëëma ec
yi pwöl Dhöän na en yi ŋööm
Ijep;
44 ni tïïc pï näm moge na remø,
ni tïme ni bäŋ pïï mo maathge.
45 Ena jääk bäätge ki lwaa lwaŋŋø
mo cama geni,
ko ogwäle mo raanynya poge.
46 Ni wëëk beekge adïtwie nee
camge,
ni cïp gïïa puurge jï bäänyö.
47 Ni raany omøki moge ki pey,
ni raany olämmi moge ki köö.
48 Pey awëëk päth bäät dhäk moge
nee thøwge,
ni ö pïïth lääc paac moge ni
gøøyi ya køthi.
49 Wëër mare na liel kaamar maac,
ka ajäla mare, ki gïï mo leth
ajääŋŋe bäätge
ki ri nyïïatwiet maal mo wø
räänyö.
50 Øtjöör wëër mare ajabe,
ni käre thøø mänö ki man pïïe
bäätge,
ni 'näk geni ki täw mo leth,
51 ni beege kaai bëët moa näk
cwøw na en Ijep,
na kwøŋ jø Ijepi nywøl yïth mïëc
nyïïkwaac Kaam, na täkge
nyöödö ki ge.
52 'Ba eni jiye abwøth wøk kaamar
rööm,
ni gwøk geni dï paap kaamar
pïïth rööm.
53 Gena bwødhe ni ee gwøø ni
tïmge ni ge ba lwäär,
'ba nyïïmän moge acam naama
dwøŋŋi.
54 Køøre jiye akäl yi ŋöömme na en
kur keere,
paana en bäät kïte na maae ki
teek bade.
55 Wïth juurre ariem wøk nyïm
jiye,
ni røm ŋøøpge ni pääŋ ge jïge
ni tïme na moge,
ni wëëk jiye ma wïth tuŋi mo jø
Icriel bëëtö kwöra bëët jøøgø
yïthge.
56 'Ba geni, gena gëëmö ki Jwøa
Dwøŋ ni en Maal, ni ge
päänynya gø,
ni kärge ciik moe gwøø,
57 ni ge bëëdö ni cwïnyge ba en
køøre ni marge cwøk kaamar
wëëkge,
ni tïm bëëtö marge no okööm,
ni caala atheerø mo ree ee
täpö.
58 Jwøk atïïcge nee goote ki køør
kwör lam moa tïïcge bäät
thuuri,
ni wëëkge eni këëyö ki køør gïï
lam moge moa tieŋge.
59 Kanya ö Jwøki na joot gïïögø,
ena put wëër,
ni kwier jø Icriel,
60 ni wec kar bëëtö mare na en
Cëëlö,
ni beeye oduŋkaara mana bëëde
yie dï jiy.
61 Ni tïïc acanduk man wø nyooth
luumma tuude ki jiy nee käl
nyïïmänni,
na näk beeye nyuudhi mar teek
mare ka ajiem mare.
62 Ena wëër ki jiy moe,
ni wëëk geni nyïïmän moge ni
'näk geni ko opëëllö.
63 Wøpe moge athum ri leny,
ni tïme ni bäŋ duut nywöm mo
løøa bäät nyïïakuue moge.
64 Ni ö dïlämme moge ni nääi ko
opëëllö,
ni dhäth määr thuunhnhi ki
kïmmö.
65 Køøre Wuuö Jwøk aö maal
kaamar dhaanhø mo päya yïth
niine,
ni tïme kaamar dhaanhø mo teek
mo twäädö ri køøŋø.
66 Ni riem nyïïmän moe,
ni lää wïthge na bäre bäre.
67 Jø tuuŋ Ipariem, ni beege
nyïïkwaac Jocep, akwiere,
ni käre poge jierø na kar bëëtö
mare.
68 'Ba beeye jø tuuŋ Juuda na jiere,
ki Kïn Dhayan na mëëre ki gø na
en poge;
69 ni geer øt lam mare na en kur
keere bäät gø
na kany mo ojiemø,
ni geer gø ni teek kaamar piny
ni wø bëëdö na bäre bäre.
70 Eni dhaanhnhe ma Deebit ajiere,
ni käl wøk ka yi lwaaŋ dïëk.
71 Ena cwøl Jwøki kanya bëëde ni
kwaaya rööm ki nyïïge moa
näk dhøøth,
nee tïme ni ena dïkwääy jï jiye
ma jic Jeekap,
ni beege jiye ma jø Icriel.
72 Ni ö Deebiti ni kwaac geni ki
cwïny mo thïïŋ,
ni bwøth geni ki køør leec wïïe.
&Manøgø beeye duut mar Acaap.
@
*#Duut Mo Kwaca Jwøk Kiper Räny Jerucalem
1 Wui Jwøk, juurre paarï atukge,
ni raanyge øt lam marï na en kur
keere,
ni tïïcge gø ni ba waany,
ni tøkge Jerucalem.
2 Rïk dëët jiyï acïpge jï wec maal
na cam,
ni cïpge rïk dëët jiyï na cwïnyge
en køørï jï lääc paap.
3 Rem moge akønyge piny kaamar
pïï dï Jerucalem bäre,
ni bäŋ ŋat mo koony geni.
4 Waana tïmö na gïr ajøøŋ jï wïth
juurre moa en deŋwa,
ni ŋeethge bäätwa ni buuge wa.
5 ?Wui Wuuö Jwøk, a këël kany
mo nyïëdi noo poodï niï wëër?
?Naa këël kany mo nyïëdi nø noo
bëët cwïnyï ni keec no oäpö
kaamar maac?
6 Kïth wëër marï bäät wïth juurre
moa näk ï kucge,
ni beege mïëri moa näk nyeŋŋï
ba cøørge;
7 kiper geni waana thöörge, wa na
jø po Jeekap,
ni raanyge kar bëëtö marwa.
8 Kär gïïa reyø na tïïc kwäcwa kïth
bäätwa;
'ba beerra man laarï mëër marï
nyooth jïwa,
kiper waano dwøk piny døc.
9 Køny waani, ï na Jwø wø piem
waani,
ni piemï waani ni wëënnï raay
mowa,
kiper nee nyeŋŋï jïte ka ajiem.
10 ?Aŋø, juurre doo köö møn na age
Jwøge?
Beerra man coolï kwör rem jiyï
na øc piny,
nee ŋäc wïth juurre, ni jootwa gø
thuwø.
11 Beerra man wïnynyï cooyø mar
jø twöc;
ni gwøgï jøøa näk thøø oŋøl
bäätge ki køør teek badï na
dwøŋ.
12 Wui Wuuö Jwøk, dwøk ajøøŋ
mar wïth juurre moa en deŋwa
bäätge kwöre abïriiø,
ni beeye ajøøŋ mana jøøŋge ïïni
ki gø.
13 Køøre waani na jiyï, ni wø
kwaayï kaamar pïïth dïëk moï,
ï pwøcwa pwøø cooth,
ni caanwa gïr pwøc marï jï
beenhnhe bëët.
*#Manøgø beeye duut mar Acaap.
@
*#Duut Mo Kwaca Jwøk Nee Bëët Jiye Dwøk Kare
1 Wui Jwøk, cek ïthï, ï na dïkwääy
mar jø Icriel,
ï ni wø bwøth jiyï ma nyïïkwaac
Jocep kaamar pïïth dïëk.
Rienyï ni nyoothï riï,
ïïni ni wø nyooth ajiem nyec marï
ki yïthakic nyïïatwiet maal moa
cwøl ni kirubëlli.
2 Nyooth teek marï jï jiyï ma tuuŋ
Ipariem ki tuuŋ Benjamen ki
tuuŋ Maneeca,
ni ööï ni piemï waani bëët!
3 Wui Jwøk, dwøk bëëtö marwa
kare,
ni wëëgï tac täärnyïmï rieny
bäätwa,
nee wa jïtwa ki køny.
4 Wui Wuuö Jwøk, ï na wïth jammi
bëët,
?a këël kany mo nyïëdi noo bëëdï
ni ïïno gootø,
ni lam marwa, wa na jiyï, ba
wïnynyï?
5 Waana tïïyï nee wa jwöŋwa, ni
tïm pï nyeŋwa na cam jïwa,
ni maathï waani ki pï nyeŋ mo
thööth døc.
6 Waana tïïyï na gïn läär wïth
juurre moa en deŋwa,
ni ö nyïïmänni mowa ni ŋïërge
bäätwa.
7 Wui Jwøk, ï na wïth jammi bëët,
dwøk bëëtö marwa kare,
ni wëëgï tac täärnyïmï rieny
bäätwa,
nee wa jïtwa ki køny.
8 Omøk apudhï wøk ki yi Ijep,
ni tøøï gø yi ŋöömma riemï wïth
juurre wøk yie.
9 Kare apuurï ni jiiŋŋï gø,
ni ö lweete ni këët piny døc ni
mac piny bäre.
10 Mïëya en bäät kïte atïmö ni ena
tier tïpö mare;
këël jenni moa døøŋŋø aume.
11 Bääte alaak këël mana pïïe bäät
naama dwøŋ,
jï løø kur pänh-cäŋ,
ni ö bääte møga ni pïïcge bäät
Naam Upareeti,
jï løø kur tuul-cäŋ.
12 ?A ennø, aperŋø nø na nyaaï kal
mare piny,
ni tïme ni jø wø cur kaace bëët
pøna nyïïe en?
13 Këël kule bëëdö ni raanynya gø,
ni bëët lääc paapi ni cama gø.
14 Wui Jwøk, ï na wïth jammi bëët, 
wa kwaya ïïni, cäŋ täärnyïmï luu
baŋwa;
räŋŋï ki maal ni raŋï piny,
ni neenï jï omøk man,
15 ni beeye omøk mana piithï ki
teek badï,
na caal wäädï na jierï na marï.
16 Ena waaŋ nyïïmänni ki maac ni
ŋøtge gø piny.
'Ba ennø, raany geni ki køør wëër
marï.
17 'Ba beerra man bëët cerï bäät jiyï
na jierï,
na mooyï ki teek niï tïnyge.
18 Køøre nø, wa ba døø ŋäthwa
këët.
Beerra man cäŋ wa mooyø ki
kwøw,
nee nyeŋŋï cøørwa.
19 Wui Wuuö Jwøk, ï na wïth jammi
bëët,
dwøk bëëtö marwa kare,
ni wëëgï tac täärnyïmï rieny
bäätwa,
nee wa jïtwa ki køny.
&Manøgø beeye duut mar Acaap.
@
*#Duut Mo Cäänö Kaper Beeny Jwøk Ki Teek Wïc Mar Jiye
1 Wärru ki dudi ki met ec jï Jwøk
na näk teek marø,
ni kwöŋŋu ni yïthu met jïre, eni
na Jwø Jeekap.
2 Jøllu duut døc,
ni pwötu odööla ki thøpothïënhö
mo döötge met.
3 Tuuŋ wär koothu kany wø päär
dwääyi,
ni koothu gø kanyo en dwääyi
tar,
dïcäŋ man wø wøørø na jwøk.
4 Kiper man beeye ciik kiper jø
Icriel,
ni beeye mana ŋøl Jwø Jeekapi.
5 Gïnögø atïïe na ciik kiper jø
Icriel
kanya tïïc gïn mo leth dëët jø Ijep.
'Ba aani, dwøl mo poot kuua
cøøn awïnynya, mo köö,
6 ni «Tëër akäla wøk bäätu,
ni käla u wøk ki yi tïïc mo teek.
7 Kanya enu yïth gïïa leth, uuna
cwötö ni kønya uuni,
ni løøa mara jïïu ki yi pöölö mo
märö,
ni päänynya uuni buut pï Meriba.
8 «Wui, u na jiya, wïnynyu mara
nou köömma.
?Wui, u na jø Icriel, luubö mara
owïnynyu gø wäne nø?
9 Kär dee jwøk mo path mo bëëdö
yïthakiyu,
ni bäŋe jwø jur mo wøørru.
10 Beeye aani na Wuuö Jwøk na
Jwøk maru
na käl uuni wøk ki yi ŋööm Ijep.
'Ba ennø, ŋaammu dhøgu nou
caama.
11 «'Ba jiya ma jø Icriel dwøra kärge
wïnynyö;
gena kweer ki luumma.
12 Køøre gena wiia ki teek wïc
marge,
nee ge cääthge ki uutjïëthe moa
manyge jaak.
13 «Jiya ma jø Icriel, doo na ge
wïnynya mara cøøn,
ni dege køøra caadhø,
14 nyïïmänge daa laara dïïm,
ni daa jøøa thiel geni piny
raanynyø.
15 Ni ö jøøa män ki aani, a na Wuuö
Jwøk, ni dege kööthge dwøk
piny ki lwär nyïma,
ni ö ajäla marge ni put bëëtö
bäätge na bäre bäre.
16 'Ba uuni, u na jiya, u daa caamø
ki beel ma liil,
ni wëëga uuni jäŋö ki maar kïc
man wø käl yi kïdi.»
&Manøgø beeye duut mar Acaap.
@
*#Duut Mo Jääla Jø Wø Ŋudö Ki Ŋøl Mo Patha Kare
1 Jwøk aöö ni pï piny dï acooŋa
mare,
ni ŋøl luup yïthakic dïŋut luup,
ni kööe,
2 na «?A këël kany mo nyïëdi nø
noo ŋudu ki ŋøl mo patha kare,
nou bëëdö nou jëënyö nou ena
kur jøøa reyø?
3 'Ba ennø, ŋunnu jøøa jïge bäŋ
teek ki moa näk kïïe,
ni tïïyu mana beer jï jøøa no
ocaannø ki moa näk bäŋ
jammi jïge.
4 Kønynyu jøøa jïge bäŋ teek ki
moa can,
ni piemmu geni ceŋ jøøa reyø.»
5 Bäŋ gïn mo ŋäcge ni tier luubö
ba kwanyge,
ni ge bëëdö ni ge cäädha yi
muudhö jaak;
ni tïm pinynyi ni raac.
6 Jwøk aköö, ni «U bëët uuna wääta,
a na Jwøa Dwøŋ ni en Maal,
ni uuni thuwø, uuna juu.
7 'Ba u thøw kaawat man wø thøw
jiyi,
ni thøwu kaawat man wø thøw
kwääri.»
8 Wui Jwøk, ö maal ni ŋølï luup
piny,
kiper wïth juurre bëët beege moï.
&Manøgø beeye duut mar Acaap.
@
*#Duut Mo Kwaca Jwøk Nee Nyïïmänne Raanynye
1 Wui Jwøk, kärï lïŋö këët,
ni ba bëëdï ni ïïno nidut;
wui Jwøk, kärï bëëdö jaak!
2 Kiper ennø, nyïïmännï atïïö ko
okiera,
ni tïŋge wïthge maal.
3 Ki køør riek waŋ marge, ge cädö
ki jöö man raanyge jiyï ki gø,
ni tutge ki luup kiper jiyï moa
näk iï gwøø.
4 Ni köge, ni «Ööu nee poge
raanynyø,
nee bäŋe nyeŋ Icriel mo di cwølø
këët.»
5 Kiper dhøkge adwalge na aciel
bëët,
ni tutge ki luubö kiperï;
6 ni jøøgø beege jø Ëdöm ki jø
Icmiel,
ki jø Möap ki jø Agri,
7 ki jø Gëbal ki jø Amön ki jø
Amalëk,
ki jø Pilitin ki jø wø bëëdö Tayar;
8 këël jø Aciria thuwø adwätö ki
geni,
ni tïmge na køny mo dwøŋ jï
nyïïkwaac Løøt. 
9 Ennø, tïïc teeŋ gïna tïïyï dëët jø
Midien dëëtge,
ni tïïyï gø kaawat mana tïïyï
dëër Cicara ki Jabin bäät naam
Kicön,
10 jøøa raanynyi Endör,
na tïmö kaamar wëëyö mo oker
piny.
11 Tïïc kwääri moge ni caala Orëëp
ki Dhëëp,
ni tïïyï nyeye moge ni caala
Jeeba ki Jalmuuna,
12 jøøa köö, ni «Kälø ŋöömma näk
mar Jwøk,
nee tïme na marø.»
13 Wui, ï na Jwøk mara, tïïc
geni kaamar tør mo käära
apwøyaweerø,
ni tïïyï geni kaamar lethø mo
kwør jame kwørø.
14 Thöör geni kaawat man wø ö
maaci wø thöör paap,
kaawat man wø ö maaci wø
waaŋ bäät kïte.
15 Riem geni ka atuunna marï mano
jääŋŋï bäätge,
ni døøyï geni mo lwäär ki jamø
marï na teek.
16 Wui Wuuö Jwøk, lää wïthge,
kiper niï cacge.
17 Beerra man lää wïthge ni lwäcge
na bäre bäre,
ni dwøk wïthge piny ni ränyge.
18 Beerra man ŋäcge gø ni beeye ï
keerï, ï na Wuuö Jwøk,
na näk Jwøa Dwøŋ ni en Maal
bäät piny bäre.
&Manøgø beeye duut mar Acaap.
@
*#Duut Ŋat Mo Lääŋŋa Ciin Kar Bëët Wuuö Jwøk
1 Wui Wuuö Jwøk, ï na wïth jammi
bëët,
yia met ki kar bëëtö marï!
2 Cwïnya lääŋŋa gø døc ki man
cøøa yi kal marï,
naa kwöŋŋö ki met ec ki cwïnya
bäre jïrï, ï na Jwøa kwøw.
3 Wui Wuuö Jwøk, ï na wïth jammi
bëët,
këël adiit thuwø jïtö ki kany gëët
yie,
ni ö agweeci ni gëën ree ki øtø
mo nyööt yi gø
mo kare cään ki gïn wø cïp
olämme bääte marï,
ï na nyeya mara ni nägï Jwøk
mara.
4 Gwïëth en jï jø wø bëëdö ødï,
ni ge bëëdö ni ge pwøya ïïni
cooth.
5 Gwïëth en jï jø wø joot teek
marge baŋï,
jø wø cwïnyge caar ciin bäät Kïn
Dhayan.
6 Kany wø pööth jøøgø ki yie ya
agäm Baka na näk otal,
kaace wø puta jïtö ki pïï,
ni ö køthi ni put kaace mooc ka
aguule.
7 Ni ö teek marge ni cääth nyïme,
këël mano joot geni nyïm Jwøk
bäät Kïn Dhayan.
8 Wui Wuuö Jwøk, ï na wïth jammi
bëët,
wïny lam mara,
ni cegï ïthï ki mara, ï na Jwø
Jeekap.
9 Wui Jwøk, neen jï ŋat wø caal
kwöt leny marwa,
ŋata näk iï jierø na tïïyï nee wïïe
thïïmmi ki maaw.
10 Beerra eni jïra ki man bëëda dï
kal marï ki dïcäŋ aciel,
ni kaala man bëëda kany mør ki
nïne ma kuma.
Ni theemma man cuŋŋa dhi kal
marï,
ki man bëëda yïth uudi mo jøøa
reyø.
11 Wuuö Jwøk caala tac cäŋ,
ni caala kwöt leny jï jiye.
Wuuö Jwøk cïpö ki met ec ka
ajiem;
bäŋ gïn mo beer mo mäne ki
jøøa marge thïïŋ.
12 Wui Wuuö Jwøk, ï na wïth jammi
bëët,
gwïëth en jï ŋat wø bëëdö ni
ŋäätha ïïni.
&Manøgø beeye duut mar wäät Köra.
@
*#Duut Mo Kwaca Jwøk Nee Bëët Jiye Dwøk Kare
1 Wui Wuuö Jwøk, met ec anyoothï
yi ŋöömmï,
ni dwøgï bëët jic Jeekap kare.
2 Gïïa bac jiyï awëënnï,
ni buŋï raay moge.
3 Wëër mana wëërï ki gø aweyï,
ni kwierï wëër marï ni wø liel
kaamar maac.
4 Wui Jwøk, ï na pïëmi marwa,
dwøk bëëtö marwa kare,
ni weyï gootø marï ki waani.
5 ?Aŋø, ï puta bëëtö ni ïïno wëër ki
waani na bäre bäre?
?A wëër marï, poot bëëdö na
bäre bäre këël yïth beenhnhe
bëët moo ööi?
6 ?Aŋø, wa ba cäŋï mooyø ki kwøw,
nee wa na jiyï, yïthwa mïnge ki
ïïni?
7 Wui Wuuö Jwøk, nyooth mëër
marï ni wø ba jøøl jïwa,
ni piemï wa.
8 Aani, ïtha ciia ciiø ki mano caan
Wuuö Jwøki,
ni beeye luum bëët-mëër mano
caane jï jiye, jøøa cwïnyge en
køøre;
'ba beerra man ba døøge øtjöör
bøøl.
9 Ka adïëri møn, eni jøøa lwäär ki
eni pute ka piem,
ni ö ajiemmi mare ni bëëde yi
ŋöömö marø.
10 Mëër man wø ba jøøl ki bëët
adïëri rööpö na aciel,
ni ö bëët bëënynyö ki bëët-mëër
ni dwätge.
11 Bëët adïëri tägö bäät piny,
ni ö bëënynyö ni ööe ki maal ni
ö piny.
12 Ka adïëri møn, Wuuö Jwøk gïïa
beyø di cïbö,
ni ö ŋöömö marø ni ciee ki caammi.
13 Bëënynyö mare bwödhö nyïme,
ni tïm køør tiete na jöö.
&Manøgø beeye duut mar wäät Köra.
@
*#Duut Mo Kwaca Jwøk Kiper Køny
1 Wui Wuuö Jwøk, cek ïthï ki kwac
mara ni løgï gø,
kiper aano caannø naa bëëdö naa
can.
2 Gwøk jwïëya, kiper cwïnya ena
køørï.
Wui, ï na Jwøk mara, køny
dhaanhnhï ni wø ŋääth ïïni.
3 Wui Wuuö Jwøk, bëëdï ni cwïnyï
bäth ki aani,
a ni wø kwac ïïni cooth ki yïth
nïne bëët.
4 Wui Wuuö Jwøk, døøc cwïny
dhaanhnhï mo met,
kiper a bëëdö na acaara mara
bäre ena baŋï.
5 Wui Wuuö Jwøk, ïïna Jwøk mo
beer,
ni jiy wëënnï wëënnö;
Mëër marï ni wø ba jøøl päl jï jø
wø cøør nyeŋŋï.
6 Wui Wuuö Jwøk, cek ïthï ki lam
mara,
ni wïnynyï kwac man wø kwääa
ki gø.
7 Kany wø ena yïth gïï mo leth,
bee ï wø cwøla,
kiper bee ï wø løk mara.
8 Wui Wuuö Jwøk, bäŋ Jwøk mo
caala ïïni røk juu,
ni bäŋ tïïe mo caala tïïe moa
tïïyï.
9 Wui Wuuö Jwøk, wïth juurre
moa cwääyï bëët oööi,
ni wøørge ïïni, ni jiemge nyeŋŋï.
10 Kiper ï dwøŋ niï tïïö ki gïï mo
rëëma ec,
ni beeye ï na Jwøk keerï.
11 Wui Wuuö Jwøk, pwöny aani ki
jöör bëëtö marï,
naa cäädha ki køør adïëri marï.
Mooc aani ki cwïny aciel naa
bëëda naa lwäära ïïni.
12 Wui Wuuö Jwøk, ï na Jwøk mara,
ï pwøa pwøø ki cwïnya bäre,
ni bëëda naa jiema nyeŋŋï na
bäre bäre.
13 Kiper mëër marï ni wø ba jøøl na
nyoothï jïra dwøŋ;
jwïëya amänï ki mana dee ci kar
bëët jwïëc jøøa no othøw.
14 Wui Jwøk, jø okiera aö maal
bääta,
ni ö jø kwöri ni cacge jwïëya nee
raanyge,
jøøa näk bäŋ gïn caarge kiperï.
15 'Ba ï na Wuuö Jwøk, ïïna Jwø
wø yie bäth wø nyooth met ec
mare jï jiy;
ï ba laar wëër,
ni mëër marï ni wø ba jøøl ka
adïëri marï päl.
16 Luu riï baŋa ni nyoothï met ec
marï jïra;
cïp teek marï jï dhaanhnhï
ni piemï aani, a na o dhaaŋ wø
tïny ïïni.
17 Mooc a ki nyuudhi mo nyootha
beenynyï,
nee jøøa män ki aani nee wïthge
lääge
kanyo jootge gø naa iï kønyø,
ni jïta ki cøm cwïny baŋï, ï na
Wuuö Jwøk.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Jiemma Pääny Jwøk Ma Jerucalem
1 Wuuö Jwøk pääny mare ageer
bäät Kïn Dhayan na en kur
keere.
2 Eni mëër ki Jerucalem, na no
ogeer bäät kïnnögø,
ni kaala kwör bëëte mo wø bëët
nyïïkwaac Jeekapi yïthge bëët.
3 Wui, ï na pääny Jwøk,
gïï mo duua ajiem di carø kiperï.
4 Wuuö Jwøk aköö, ni «Ki røk wïth
juurre moa ŋäc aani,
Reeyap na näk Ijep ki Babiløn
beege noo kwaana.
Ni ö jø Pilitin ki jø Tayar ki jø
Ithiöpia
ni købi ni ge nywølla
Jerucalem.»
5 Luubö mano caan jiyi kiper
Dhayan beeye
ni ŋati en ki ŋatøce nywølla yie;
ni ö Jwøa Dwøŋ ni en Maal ki
dëëre ni këël tier gø piny ni
teek.
6 Kanyo ö Wuuö Jwøki noo göör
nyeŋ wïth juurre piny, eni köö,
ni «Jø paani nø ki jø paani nø
nywølla Dhayan.»
7 Ni ö jø wø wär ki dudi ki jø wø
kudhö ko opele bëët ni köge,
ni «Ï na pääny Jwøk, gïï wø
manywa bëët jootwa baŋï.» 
&Manøgø beeye duut mar wäät Köra.
@
*#Duut Ŋat Mo Ena Yi Ränynyö Mo Kwaaya Jwøk Kiper Køny
1 Wui Wuuö Jwøk, Jwø wø piem
aani,
a bëëdö naa jwöŋö dëërï ki dïcäŋ
ki wäär.
2 Beerra man wïnynyï lam mara,
ni cegï ïthï ko oduuru mara,
3 kiper gïïa leth na nø jwøra atïmö
ni thööth,
ni tïm kar jwïëya ni cään ki ciin
kar bëët jwïëc jøøa no othøw.
4 A caala dhaanhø mo okwaan
dëët jøw mo okoony yi bwörö,
ni tïma kaamar dhaanhø mo bäŋ
teek jïre.
5 Aana tïmö naa caala dhaanhø
mo owii dï jøøa no othøw,
ni tïma naa caala jøøa no onääö
na no okoony yi bwörö,
na näk ge ba lääŋŋï këët,
jøøa näk ïïno pääö ki geni.
6 A caala dhaanhø mo iï leeŋ yi
buur mo bäär mo raac,
kanya cøl tiet ŋøøm.
7 Wëër marï atïmö ni dwøŋ bääta,
ni ö athaŋ wëër marï ni muun
aani.
8 Jøøa näk waano ŋïyö ki geni
karge atïïyï ni bäär ki aani,
ni tïïyï aani na gïn mo yïthge
raac ki gø.
A caala dhaanhø mo otwöö, ni
bäŋ gïn mo løny ki tïïc jïra.
9 Aana cøør ki køør gïïa leth na pïï
dëëra.
Wui Wuuö Jwøk, a cøøra ïïni ki
yïth nïne bëët,
ni ceŋŋa yaa thaaŋø jïrï.
10 ?Aŋø, ï poot tïïö këët ki gïï mo
rëëma ec jï jøøa no othøw?
?A jwïëc jøøgø ööa maal ni
pwøcge ïïni?
11 ?Aŋø, mëër marï ni wø ba jøøl
gïre di caanø yi bwörö?
?A gïr adïëri marï, di købø kar
ränynyö?
12 ?Aŋø, gïïa näk mo rëëma ec ni
wø tïïyï di ŋääö yi muudhö?
?A beer marï di ŋääö kar wïl wïc?
13 'Ba aani, a wø bëëdö naa jwöŋö
dëërï kiper køny, ï na Wuuö
Jwøk,
ni lam mara wø pïï baŋï ka
aruunnø cooth.
14 ?Wui Wuuö Jwøk, aperŋø na
kwierï aani,
ni kanï täärnyïmï ki aani en?
15 Ki mana täga thïnhö, a bëëdö ni
aano caannø
ni kara cään ki thøø.
Aana ööl døc ki køør gïïa leth na
näk duua lwär na jwøra cerï,
ni puta ränynyö ki køørge.
16 Wëër marï aliel bääta kaamar
maac,
ni ö gïïa leth na näk duua lwär
na kälï bääta ni raanyge aani.
17 A ege ciel dïër cooth kaamar
jwïïö,
ni mwønyge aani na bäre bäre.
18 Ŋat wø mëëra ki gø jaak ki ŋat
ma nyawatwa karge atïïyï ni
bäär ki aani,
ni dööŋ muudhö keere ni beeye
ŋata näk waano ŋïyö ki gø.
&Manøgø beeye duut mar wäät Köra
mana cak Ëmanni nyï Edhera.
@
*#Duut Mo Cäänö Kaper Luumma Tuut Wuuö Jwøki Ki Jø Icriel
1 Wui Wuuö Jwøk, a bëëdö naa
wär ki dudi na bäre bare kiper mëër marï ni wø ba jøøl,
ni caana gïr adïëri marï ki dhaa
nee ŋäc beenhnhe bëët.
2 Kiper ŋääa ni mëër marï ni wø
ba jøøl bëëdö na bäre bäre,
ni ö adïëri marï ni bëëde na bäre
bäre kaamar maal.
3 Wui Wuuö Jwøk, ïïna köö, ni
«Aana tudö ki luubö ki ŋata
näk yaa jierø,
ni beeye dhaanhnha ma Deebit
na kööŋa jïre.»
4 Ni kööï jïre, ni «Tier nyec mar
nyïïkwaayï këëlla piny na bäre
bäre,
ni bëët wälu marï ni nut këël yïth
beenhnhe bëët.»
5 Wui Wuuö Jwøk, ïïno pwøc
maalli kiper gïïa näk rëëma ec
na tïïyï,
ni pwøc ïïni ki køør adïëri marï
ya acooŋa mar nyïïatwiet
maal.
6 ?Aŋa ni pääri ki Wuuö Jwøk
maal,
na aŋa ni teek ni röömi ki Wuuö
Jwøk dï nyïïatwiet maal?
7 Jwøk di lwäärö ya acooŋ
nyïïatwiet maal;
eni di lwäärö døc ni kaala geni,
ge na en buute bëët.
8 ?Wui Wuuö Jwøk, ï na wïth
jammi bëët,
aŋa ni teek ni caal ïïni?
Wui Wuuö Jwøk, ï bëëdö ni marï
adïëri cooth.
9 Teek athaŋ naama dwøŋ ena cerï,
ni kany wø kwöt athaga mare,
joogï jooø, ni cuŋŋe.
10 Ïïni, Reeyap ni beeye Ijep
araanynyï,
ni raanynyï kaamar gïn mo di
nääö,
ni keethï nyïïmän moï ki teek
badï.
11 Maal beeye marï, ni bëët pinynyi
na marï thuwø;
bäät piny bäre ki gïïa en yie bëët
cwääya ïïni.
12 Wï-piny ki tier-piny cwääya ïïni,
ni ö Kïn Tabör ki Kïn Armön ni
kwöŋge ki nyeŋŋï ni yïthge
met.
13 Badï bëëdö ni teek,
ni teek badï dwøŋ døc.
14 Bura marï cuŋŋa ri bëënynyö ki
ŋøl ma kare,
ni mëër man wø ba jøøl ka adïëri
bwödhö nyïmï.
15 Wui Wuuö Jwøk, gwïëth en jï jø
wø ŋäc kwöŋŋö jïrï ki met ec,
jø wø cäädhi ni tar marï ena
bäätge!
16 Ge bëëdö ni ge kanynyø cooth ki
nyeŋŋï,
ni tïm kwörge ni døøŋŋø ki køør
beer marï.
17 Kiper ajiem marge ki teek marge
wø jootge baŋï,
ni teek marge wø meeta ïïni ki
køør met ec marï.
18 Kiper nyeya marwa ni wø gwøk
waani ena cerï, ï na Wuuö
Jwøk,
ï na Jwø Icriel na en kur keere.
19 Ï na Wuuö Jwøk, dïcäŋ aciel ïïna
cäänö ki yïth lääk
jï nyïïkuk Jwøk moï moa näk
cwïnyge ena køørï, ni kööï,
ni «Ŋat leny mo teek mo yaa
jierø dï jiy,
akønya ni tïŋa gø maal;
20 ni beeye dhaanhnha ma Deebit
na manynya na jooda,
na tïïa nee wïïe thïïmmi ki maaw
mara na en kur keere.
21 Teek mara obëëdö bääte,
ni tëënne ki køør teek bada.
22 Bäŋ nyimän mo cwöti ka ajwäk
bääte,
ni eni ba thiel jøøa reyø piny.
23 Jø wø män ki eni dïïma dïïmö
nyïme,
ni puta ge raanynyø.
24 Adïëri mara ki mëër mara ni wø
ba jøøl oen bääte,
ni jïte ki teek ki køør nyeŋŋa.
25 Teek nyec mare tägö ki bäät
naama dwøŋ,
ni këët bäät Naam Upareeti.
26 Aano cøøre ni kööe, ni ‹Ïïna
wära,
ni nägï Jwøk mara na teek ni wø
piem aani.›
27 Eno tïïa na lwiidhø,
ni tïme na nyeya mana dwøŋŋa
eni bäät piny.
28 Mëër mara ni wø ba jøøl otïïa
nee bëëde bääte na bäre bäre,
ni ö luumma tuutwa ki gø ni
bëëde ni ba cuŋ.
29 Tier nyec mar nyïïkwaaye këëlla
piny na bäre,
ni ö wälu mare ni bëëde na bäre
bäre kaamar maal.
30 «Ni näk mo jøw käl dëëre pwöc
'moa wecge wiiø,
ni ba cääthge køør luup ŋøl 'moa,
31 ni bacge ciik 'moa,
ni ba gwøkge luup moa cema
geni ki ge,
32 aani, a ööa baŋge ka ajäla mo
teek, ni jääla geni ki køør raay
moa tïïcge,
naa dwøga gïïa bacge wïthge.
33 'Ba mëër mara ni wø ba jøøl ba
paanya bääte,
ni ba wiia gïna kööŋa kipere.
34 A ba gaa wøk ki ri luumma
tuuda,
ni ba wiila luubö mo yaa nø
caan.
35 Kiper aano nø kööŋ ri bëëtö
mara na en kur keere,
naa ba cäänö ki tööt jï Deebit.
36 Nyec mar nyïïkwaaye bëëdö na
bäre bäre,
ni ö wälu mare ni bëëde nyïma
na bäre bäre kaamar cäŋ,
37 ni put bëëtö na bäre bäre kaamar
dwääy
na no oŋäädhö na nyuudhi
maal.»
38 'Ba ï na Wuuö Jwøk, ŋata jierï na
tïïyï nee wïïe thïïmmi ki maaw
aleeŋï wøk ni kwierï gø,
ni tïm wëërri marï ni dwøŋ
bääte.
39 Luumma tuutï ki dhaanhnhï
araanynyï,
ni leeŋï aduda mare yi tør.
40 Kiir mare bäre anyaaï piny,
ni raanynyï kwör gwøk røk moe
moa teek.
41 Ni ö jø wø pöödhi ki jöö bëët ni
twierge jammi moe,
ni tïm wïth juurre moa en deŋŋe
ni buua eni.
42 Jø wø män ki eni awëëgï tëënnö,
ni tïïyï nyïïmän moe bëët nee
yïthge mïnge.
43 Dho opëëllö mare adøøyï mo
pööl,
ni kärï eni wëëk cuŋŋö ri leny.
44 Ajiem mare awëëgï ränynyö,
ni leeŋï wälu mare yi tør.
45 Ena laarï wëëk jalø jaak,
ni døøyï wïïe mo laay døc.
46 ?Wui Wuuö Jwøk, a këël kany
mo nyïëdi nø?
?Aŋø, ï bëëdö ni riï iï kanø na
bäre bäre?
?A këël kany mo nyïëdi nø noo
bëët wëërri marï ni liel kaamar
maac?
47 Caar wïïï kiper nïr kwøw 'moa
moo beeda.
?Aŋø, jiy cwääyï jaak kaper gïn
mo bäŋ tiere?
48 ?Aŋø, da ŋat mo bëëdö ni kwøw
cooth ni thøø ba joode?
?A da ŋat mo løny jïre ki man käl
dëëre wøk cer teek thøø?
49 ?Wui Wuuö Jwøk, age mëër marï
ni wø ba jøøl na nut cøøn,
na kööŋï ki gø jï Deebit ki køør
adïëri marï?
50 Wui Wuuö Jwøk, caar wïïï ka
ajøøŋ mana pïï bääta, a na
dhaanhnhï,
ki jwør mana jwøra ajøøŋ bäre
mar wïth juurre ki yi cwïnya,
51 ni beeye ajøøŋ mana ö nyïïmänni
moï na jööŋge ki gø,
ni ge jøøŋŋa ŋata jierï na tïïyï
nee wïïe thïïmmi ki maaw,
ni eni jøøŋge kwör wø cäädhe
yïthge bëët.
52 Pwøc en jï Wuuö Jwøk na bäre
bäre.
Kare møn, enøgønø.
&Manøgø beeye duut mar
Ëtan nyï Edhera.
@
*#Duut Mo Nyootha Nïr Jwøk Ki Nïr Dhaanhø
1 Wui Wuuö Jwøk, ï bëëdö na kar
bëëtö marwa cøøn
ki yïth beenhnhe bëët.
2 Kanya poode ni kïte poot kärï
cwääö,
ni piny thuwø ki gïïa en yie poot
kärï tïïö,
ï nut cøøn ni ïïna Jwøk,
ni bëëdï ni ïïna Jwøk na bäre
bäre.
3 Jiy wø dwøgï yi ŋöömö, kany wø
kööï,
ni «Uuni na wäät jiy, døøu yi
ŋöömö.»
4 Kiper ki baŋï, cwiiri ma kuma
laara pöödhö
kaamar dïcäŋa wääre na pöödhö,
ni caala yïth caae mo nøk mo wø
koor dhaanhe ki wäär.
5 Jiy wø laarï ka käl, ni thøwge,
ni ge caala luum ni wø tuy ni ba
ruu.
6 Luum këël doo tuy ni ŋøøe ni
mïërö,
laara närö ni tale.
7 Kiper waana thum ki thøø ki
køør wëër marï,
ni ö wëërri marï ni känne ki lwär
mo päl bäätwa.
8 Gïïa bacwa apeedhï nyïmï,
ni ö moa tïïcwa ni kuc jiyi ni
joodi ki yi tar marï.
9 Kiper nïr kwøw mowa bëët
pöödhö ni wëër marï poot ena
bäätwa,
ni laar cwiiri mowa thumö
kaamar jamø man wø kuuth
wøk ki dhøk.
10 Kanymør cwiic kwøw mowa jïtö
ki pïërabïriiø,
'ba ni näk dëël poot teek,
kanymør pïï ri pïërabära,
'ba gïï wø joot dhaanhe ni wø
tööde kiperge yïth cwiiyøgø
yøø,
duua öölö ki bëëtö mo leth jaak,
kiper cwiiri mowa laara pöödhö,
ni ö jwïëcwa ni rwäänyge.
11 ?Aŋa ni ŋäc teek wëër marï,
ni lwäär ïïni ka teeŋ mana di
wëërri marï lwäärö?
12 Pwöny waani nee nïr kwøw
mowa kwaanwa,
nee wa jïtwa ki leec wïc.
13 ?Wui Wuuö Jwøk, a këël kany
mo nyïëdi nø noo bëëdï niï wëër ki waani?
Dwøk cwïnyï piny ni päth cwïnyï
ki gïrwa, wa na laaŋe moï.
14 Kany wø päcwa ka amöölla,
wëëk wa jäŋö ki mëër marï ni wø
ba jøøl,
kiper nee yïthwa mïnge ni
kanywa
ki yïth nïr kwøw moo beetwa
bëët.
15 Tïïc yïthwa ni met ki nïne mo
thööth
mo röömi ki nïne moa mooyï wa
ki rääm yïthge,
ni wëëgï yïthwa mïnnö ki cwiiri
mo thööth
mo röömi ki cwiiri moa jootwa
gïïa leth yïthge.
16 Beerra man nyoothï tïïe moï
jïwa, wa na laaŋe moï,
ni nyoothï ajiemï jï obwöre mowa.
17 Wui Wuuö Jwøk, beerra man ö
met yiï ni bëëde bäätwa,
ni wëëgï gïï wø tïïcwa ki ceŋwa
thur karge jïwa.
Adïëri møn, jap wø tïïcwa ki
ceŋwa, tïïyï nee thurge karge.
&Manøgø beeye duut mana cak
Modhe, dhaanh Jwøk, ni mare lam.
@
*#Duut Kiper Gwøk Ŋat Mo Ŋäätha Jwøk
1 Ŋat wø kan ree buut Jwøa Dwøŋ
ni en Maal
obëëdö tïm Wuuö Jwøk na en
teeki jïre.
2 A wø cäänö jï Wuuö Jwøk, ni
kööa,
ni «Bee ï ni wø kana raa buutï,
ni bee ï na kar gwøk røk kipera,
ni bee ï na Jwøa ni wø ŋäädha.»
3 'Ba ï na dhaanh Jwøk, beeye
Wuuö Jwøk ni wø käl ïïni wøk
ki ya abïëp mo ocek ŋat mørri,
ni køny ïïni yi teeŋ täw mo leth
mo kännö ki thøø.
4 Ïïno gwøe tiet bwöpe,
ni tïmge na kar kan røk jïrï,
ni ö adïëri mare ni tïme ni caala
kwöt leny mo gëëŋa ïïni.
5 Ïïno tïmö niï ba lwäär ki gïï mo
di lwäärö ki ge ki wäär,
këël tøŋ miï di thöörö ki gø ki
dïcäŋ.
6 Niï ba lwäär ki täw mo tägö dëët
jiy ki wäär,
këël täw mo leth mo nyaga paac
bäre ki dïcäŋ,
ï ba lwäyi ki gø.
7 Këël jiy ma kuma doo thøw
buutï,
ni ö kume apaar ni thøøge bäät
cwïïï,
bäŋ gïn mo guta ïïni na bäre.
8 Ïïno rääŋö ki waŋï jaak,
ni jootï gïno tïïc dëët jøøa reyø.
9 'Ba Wuuö Jwøk, Jwøa Dwøŋ ni
en Maal, na näk kar kan røk
jïra,
kiper mana bëëde ni iï nø tïïc na
kar bëëtö jïrï,
10 bäŋ gïn mo raac mo pïï bäätï,
ni bäŋe gïn mo leth mo ö paarï.
11 Kiper nyïïatwiet maal moe
oköömme kiperï,
nee ï koorge ki uutjïëthe mo wø
caathï bëët.
12 Ïïno jølge maal ki ceŋge,
kiper nee tierï ba cwaanyï ri kïdi.
13 Ïïno cäädhi ni ethï bäät ŋuu ni
nyøønï olwierø,
këël ŋuu mo dwøŋ wala onyaaŋ
onyørï ki tietï jaak.
14 Wuuö Jwøk aköö, ni «Teeŋ
ŋatøgø, kiper mana mëëre ki
aani,
eno käla wøk yi gïna raac, ni gwøa eni kiper mana ŋäc aani.
15 Ni kany wø kwac aani, mare løøa
løø jïre,
ni bëëda ki eni kany wø näk da
gïï mo leth.
Eni kønya kønyø ni jiema gøøni.
16 Eni wëëga bëëtö ki cwiiri mo
thööth ni mïn yie,
ni nyoodha køny mara jïre.»
@
*#Duut Mo Pwøca Jwøk Kiper Tïïe Moe Na Beyø
1 Wui Wuuö Jwøk, beeye gïn mo
beer ki man pwøc ïïni,
ni beeye gïn mo beer thuwø ki
man pwøc nyeŋŋï ki dudi, ï na
Jwøa Dwøŋ ni en Maal,
2 ni caan gïr mëër marï ni wø ba
jøøl ka amöölla cooth,
ni køp gïr adïëri marï ki wäär,
3 ni wär na duut mo pwöt ka
thøp-othïënhö,
ki thøme moa näk thøøthge
opaarri na näk döötge met.
4 Kiper ï na Wuuö Jwøk, yia
adøøyï mo met ki køør tïïe
moï,
ni wära ki dudi ni yia met kiper
tïïe moa tïïyï ki cerï.
5 Wui Wuuö Jwøk, tïïe moï
døøŋŋø,
na acaare moï døøŋŋø døc!
6 'Ba gïn mo tiere ba kwany ŋat
mo bäŋ wïc,
mo tiere ba joot bøølli, beeye en:
7 Jøøa reyø, këël ge doo løth
kaamar luum ni kwärge,
ge poot ränynyö na bäre bäre;
8 'ba ï na Wuuö Jwøk,
ï puta bëëtö ni karï dwøŋ na bäre
bäre.
9 Ka adïëri møn, ï na Wuuö Jwøk,
nyïïmännï ränynyö;
nyïïmännï ränynyö na bäre bäre,
ni ö jø wø tïïö ki raay bëët ni
keethge.
10 'Ba aani, aana mooyï ki teek mo
caala teek jööbi;
aana wïïrï ki maaw mo nyään.
11 Räny nyïïmänna ajooda ki waŋa,
ni wïnynya gïr pädhö mar jøøa
reyø na ö maal bääta.
12 Jøøa beyø løth kaamar twöö,
ni tïmge ni døøŋŋø kaamar
jaath mana dwøŋ na en yi lur
Libaanø.
13 Ge wø piith yi kar Wuuö Jwøk,
ni løthge dï kal mare, eni na
Jwøk marø.
14 Jøøgø, këël cwiiri moge doo tïmö
ni thööth, ge poot bëëdö ni ge
kännö ki nyïëdi,
ni bëëtge ni ge løth cooth ni ge
ba tal;
15 gïïögø nyootha gø ni Wuuö Jwøk
mare thïïŋ.
Bee eni na teek mara, ni bäŋ gïn
lääŋ ri bëëtö mare na bäre bäre.
&Manøgø beeye duut man
wø wär ki cäŋ Jwøk.
@
*#Duut Mo Cäänö Kaper Teek Mar Wuuö Jwøk
1 Wuuö Jwøk bëëdö na nyeya,
na ajiem ee røø dëëre kaamar
abïï,
ni teek mo dwøŋ ena cere.
Adïëri møn, piny acïp kare ni
teek ni ba dak.
2 Wui Wuuö Jwøk, wälu marï ocïp
kare ni teek ki mana täge ya
acääŋŋe cøøn,
niï nut dïkwøŋ cøøn.
3 Wui Wuuö Jwøk, athage mo näpa
døøŋŋø atïmö ni päl, 
ni lwörge ni döötge ena maal.
4 'Ba Wuuö Jwøk ni en maal teeka
eni,
teeka eni ki näpa døøŋŋø moø ni
lwör yøø,
ni teek mare kaala teek athage
moge.
5 Wui Wuuö Jwøk, ciik moï bëëdö
karge ni ba dak,
ni bëëtö mana en kur keere rømi
ka ødï na bäre bäre.
@
*#Duut Mo Kwaca Jwøk Nee Kwör Jiye Coole
1 Wui Wuuö Jwøk, ï na Jwø wø
cool kwöri,
ï na Jwø wø cool kwöri, rienyï.
2 Ö maal, ï ni wø ŋøl luup mo bäät
piny;
ni cunnï jø atöör ki moo rømø ki
gïïa bacge.
3 ?Wui Wuuö Jwøk, a këël kany
mo nyïëdi nø
noo bëët jøøa reyø ni yïthge met
jaak?
4 Geni luumge päl, ni ge cara luup
atöör,
ni bëëtge ni ge jeemma dëëtge
keerge, ge na jø raay bëët.
5 Wui Wuuö Jwøk, jiyï athielge piny,
ni caange geni, ge na näk thöögï.
6 Määr thuunhnhi ki jøøa path wø
'näkge nääö;
këël kïïe thuwø 'näkge nääö.
7 Ni ge wø köö, ni «Gïn ba nëëni jï
Wuuö Jwøk,
ni bäŋ gïn mo caare kipere, eni
na Jwø Jeekap.»
8 U ni bäŋ wïdhi en, beerra man
wïnynyu gø.
?Aŋø, tiet luup okwanynyu gø
wäne, u na bøøre en?
9 ?Aŋø, eni na cïp ïdhi, eni ba
wïnyö?
?A eni na cwääc nyeŋ, eni ba
nëënö?
10 ?A eni ni wø kööm wïth juurre, u
ba jooe?
Bee eni ni wø pwöny jiy nee jïtge
ki leec wïc.
11 Wuuö Jwøk acaac dhaanhø ŋääe,
ni ŋääe na acaac dhaanhø caala
jam dhøk jaak.
12 Wui Wuuö Jwøk, gwïëth en jï ŋat
wø köömmï,
ni wø pwönynyï ki ciik moï,
13 niï cïba cwïnye piny yïth gïïa
leth,
këël kanyo koony buur ni ceka
jøøa reyø.
14 Kiper Wuuö Jwøk jiye ba wiie;
ni ba wete, ge na näk thööge.
15 Kiper luum ŋøl ocäŋ tïmö ni
thïïŋ,
ni ö jøøa cwïnyge thïïŋ bëët ni
jïëcge gø.
16 ?Aŋa noo ö maal noo cwak aani
ki jøøa reyø?
?Na aŋa noo cuŋŋi løøa noo gëëŋ
aani ki jø wø tïïc gïï mo reyø?
17 Doo na Wuuö Jwøk kär bëëdö na
dïkunyi mara,
jwïëya doo laar tïmö ni ena kany
mo bäŋ dwøl yie.
18 Wui Wuuö Jwøk, kanya cäda naa
manynya pädhö,
mëër marï ni wø ba jøøl aana
jøle.
19 Kany wø tïm acaare 'moa ni
thöönhnhö cwïnya,
cwïnya wø døøyï mo met ki køør
man wø cømï cwïnya.
20 ?Aŋø, løny jï dïŋut luup moa reyø
ki man dwätge ki ïïni,
jø wø tïïc gïï mo reyø ki køør ciik
mo wø kälge wøk? 
21 Geni dhøkge wø dwalge dwalø
bäät ŋat mo mare beer,
ni ŋølge thøø bäät ŋat mo bäŋ
gïn mo ee baaø.
22 'Ba Wuuö Jwøk bëëdö na kar
gwøk røk mara,
ni bee eni na Jwøk mara na teek
ni wø kana raa buute.
23 Eni gïïa bacge odwøk wïthge,
ni raany geni kiper gïïa reyø na
tïïcge;
Wuuö Jwøk, Jwøk marø, ge di
raanynyø.
@
*#Duut Mo Köömma Jiy Nee Jwøk Pwøcge
1 Ööu nøø wärø ki dudi jï Wuuö
Jwøk ni yïthø met,
ni kwöŋŋø ni yïthø met jïre, eni
na teek ni wø piem øøni.
2 Beerra man cøø nyïme ni ø
pwøya eni,
ni wärø dut pwøc jïre ni döötø
ena maal.
3 Kiper Wuuö Jwøk beeye Jwøk
mana dwøŋ,
ni ena nyeya mana dwøŋ mo
kaala juu bëët.
4 Ki mana täge ki tiet ŋøøm kuya,
këël mana këët wïth kïte, ena
cere.
5 Naama dwøŋ beeye mare, kiper
bee eni na cwääc gø,
ni kwöra no otal tïïya eni ki cere.
6 Ööu ni kuullø wïthø piny ni
wøørø eni,
ni këëlø cøŋŋø piny nyïme, eni
na Wuuö Jwøk na cwääc øøni.
7 Kiper bee eni na Jwøk marø,
ni øøna jiye ni wø kwaaye
kaamar pïïth dïëk moe;
øøna dïëk moe møn, ni ø ena
cere.
Dïcäŋi, beerra man wïnynyu
dwøre mana caane na kööe,
8 ni «Kär cwïnynyu døøyu mo teek
kaawat mana tïïc kwäyu Meriba,
ni beeye gïna tïïcge dïcäŋöca
Maca dï paap,
9 kanya ö kwäyu na päänyge aani.
Aana päänyge, këël na bëëtge ni
tïïe 'moa ege joodø.
10 Aana bëëdö ni cwïnya oränynyö
ki beenhnhøce ki cwiiri ma
pïëraŋween,
ni kööa, ni ‹Gena jiy mo cwïnyge
bëënna bääö jaak,
ni jöör bëëtö mara poot ba
kwanyge.›
11 Kiper manøgønø, aana kööŋ
kanya wëëra, ni kööa,
ni ‹Jwöm mana daa cïbö jïge ba
jootge na bäre bäre.› »
@
*#Duut Mo Pwøca Wuuö Jwøk Ni Wø Ŋøl Luup Na Adïëri
1 Wärru jï Wuuö Jwøk ki duut mo
nyään;
wärru jï Wuuö Jwøk, u na jø bäät
piny bëët.
2 Wärru jï Wuuö Jwøk, ni pwøyu
eni,
ni caannu luumma met mar køny
mare ki yïth nïne bëët.
3 Køpu ajieme jï wïth juurre bëët,
ni køpu tïïe moe moa näk rëëma
ec jï jiy bëët.
4 Kiper Wuuö Jwøk dwøŋ, no
orømø ki pwøc døc,
eni di lwäärö ni kaala juu bëët.
5 Kiper juu bëët mo wïth juurre
beege juu mo oballe jaak,
'ba Wuuö Jwøk bee eni na cwääc
maal.
6 Wödö ka ajiem joota baŋe;
ni ö teeki mare ki beenynye ni
joodi øt lam mare.
7 Jiemmu Wuuö Jwøk, u na wïth
tuŋi bëët mo bäät piny bäre;
jiemmu Wuuö Jwøk ki køør ajiem
mare ki teek mare.
8 Jiemmu Wuuö Jwøk ka ajiem mo
orømø ki nyeŋŋe;
kännu ki muuce, ni ööu dï kal
mar øt lam mare.
9 U jø bäät piny bëët,
wøørru Wuuö Jwøk kiper eni ena
kur keere,
ni ööu nyïme ni dëëtu kwanynyi.
10 Caannu jï wïth juurre bëët, ni
kööu,
ni «Wuuö Jwøk bëëdö na wïth
jammi bëët.
Piny acïp kare ni teek, ni ba løny
ki daak.
Wuuö Jwøk luup mo jiy bëët di
ŋølø ni tiir.»
11 Beerra man mïn yïth gïïa en
maalli,
ni ö gïïa en bäät pinynyi ni
kanyge;
beerra man lwör naama dwøŋŋi
ni kanynye, ki gïïa en yie bëët.
12 Beerra man ö pwöthi ni kanyge,
ki gïïa en yïthge bëët.
'Ba kar kaace thuwø, jer paap
bëët yïthge omïnni
ni wärge ki dudi nyïm Wuuö Jwøk,
13 kiper eni cäädha jöö,
ni ööa kuna ŋøl luup mo piny.
Eni luup jø piny di ŋølø na kare,
ni ŋøl mo jiy bëët ki køør adïëri
mare.
@
*#Duut Mo Pwøca Jwøk Kiper Tïï Nyec Mare Na Teek
1 Wuuö Jwøk bëëdö na nyeya;
beerra man ö jø pinynyi ni mïn
yïthge,
ni ö mïëri moa en kwöra bäyö ni
kanyge.
2 Pøøl ki muudhö mo cøl ena
cielge dïër;
bura mare cuŋŋa ri bëënynyö ki
ŋøl ma kare.
3 Maac mo liel bwödhö nyïme,
ni thöör nyïïmän moe kwöra
enge yïthge bëët.
4 Malø mare piny di meenyø bäre,
ni ö pinynyi ni tïme ni kwanynyi.
5 Kïte leeny kaamar gaga nyïm
Wuuö Jwøk,
eni na wää pinynyi bäre.
6 Gïr beenynye caan maalli caanø,
ni ö ajieme ni neeni wïth juurre
bëët.
7 Jøw bëët mo wø wøør gïï lam
moa näk otieŋø, wïthge olääi,
ni beege jø wø töödö kiper juu
mo oballe;
'ba nyïïatwiet maal bëët, ge wø
bëëdö ni ge wøøra eni.
8 Wui Wuuö Jwøk, gïr ŋøl marï
awïny jø Dhayan ni mïn yïthge,
ni ö mïëc Juuda ni kanyge.
9 Kiper beeye ïïni na Wuuö Jwøk
na karï dwøŋ bäät piny bäre,
ni karï dwøŋ døc niï kaala juu bëët.
10 Uuni ni wø mëër ki Wuuö Jwøk,
männu ki gïï mo reyø;
eni jø wø cwïnyge en køøre
jwïëcge di gwøø,
ni piem geni ceŋ jøøa reyø.
11 Tar di meenyø jöör jøøa beyø,
ni mooc jø wø cwïnyge thïïŋ ki
met ec.
12 U na maru beer, bëëdu ni yïthu
met ki Wuuö Jwøk,
ni pwøyu nyeŋŋe na en kur keere.
@
*#Duut Mo Köömma Gïïa En Bäät Piny Bëët Nee Jwøk Pwøcge
1 Wärru jï Wuuö Jwøk ki duut mo
nyään, kiper ena tïïö ki gïï mo rëëma ec;
ki køør teek bade na en kur
keere, ena käädhö.
2 Wuuö Jwøk pïëm mare man wø
piem jiy ki gø anyoodhe nee
ŋäc,
ni nyooth bëënynyö mare jï wïth
juurre.
3 Wïïe kär wïl ki man nyooth mëër
mare ni wø ba jøøl
ka adïëri mare jï jø dhi øt Icriel;
ni ö pinynyi bäre ni joot pïëm
mar Jwøk marø.
4 U na jø bäät piny bëët, kwöŋŋu jï
Wuuö Jwøk ki met ec;
putu dut pwøc jøl døc ni wärru
ni yïthu met.
5 Wärru ki dut pwøc jï Wuuö Jwøk
nou pöödö ki thøme,
ni wärru ni pwötu ni you jiiŋŋø
ni met.
6 Kwöŋŋu ki met ec nyïm Wuuö
Jwøk, eni na nyeya,
ni koothu dipiire ki tuk lääy.
7 Beerra man lwör naama dwøŋŋi
ni kanynye, ki gïïa en yie bëët,
këël piny ki jø wø bëëdö yie bëët.
8 Beerra man ö nämmi ni mïn
yïthge,
ni ö kïte ni wärge na aciel ki dut
met ec nyïm Wuuö Jwøk,
9 kiper eni cäädhö jöö ni ööa kuna
ŋøl luup mo piny.
Eni luup jø piny di ŋølø na kare,
ni ŋøl luup jiy ni tiir.
@
*#Duut Mo Pwøca Wuuö Jwøk Kiper Eni Ena Kur Keere
1 Wuuö Jwøk bëëdö na nyeya;
beerra man tïm jiyi bëët ni
dëëtge kwanynyi.
Eni ajiem nyec mare wø nyoodhe
nyoodhø
ki yïthakic nyïïatwiet maal moa
cwøl ni kirubëlli;
beerra man ö pinynyi ni tïme ni
jäŋŋi.
2 Wuuö Jwøk kare dwøŋ Dhayan,
ni dwøŋŋa kare bäät wïth juurre
bëët.
3 Beerra man pwøcge nyeŋŋe na
dwøŋ ni wø lwäärö ki gø;
bee eni na en kur keere.
4 Wui Wuuö Jwøk, ï na nyenynya
teek, ï mëër ki ŋøl luup ma
kare;
ŋøl luup mo thïïŋ atïïyï nee
bëëde ni nut,
ni nyoothï adïëri ki ŋøl luup ma
kare po nyïïkwaac Jeekap.
5 Tïŋu nyeŋ Wuuö Jwøk maal, eni
na Jwøk marø,
ni wøørru eni kanya näk køøm
tiete;
bee eni na en kur keere.
6 Modhe ka Aran, këël Camiel
thuwø, ge ena dëët dïlämme
moe,
ni ö geni ni cøørge nyeŋŋe.
'Ba kanya cøørge nyeŋŋe, eni na
Wuuö Jwøk, eni marge aløøe
jïge.
7 Ena cäänö ki geni ni eni ena yi
pöölö mo ree ee wenyø;
gïïa ceme jïge agwøkge,
këël ciik moa cïbe jïge.
8 Wui Wuuö Jwøk, ï na Jwøk
marwa, marge aløgï jïge,
ni bëëdï ni ïïna Jwøk miï wëënna
geni,
'ba gïïa bacge adwøgï wïthge.
9 Tïŋu nyeŋ Wuuö Jwøk maal, eni
na Jwøk marø,
ni wøørru eni bäät kïnne na en
kur keere, 
kiper Wuuö Jwøk, Jwøk marø,
ena kur keere.
@
*#Duut Mo Köömma Jiy Nee Jwøk Pwøcge
1 U ni en bäät piny bäre,
pwøyu Wuuö Jwøk ni döötu ena
maal ni mïn yïthu.
2 Tïnynyu Wuuö Jwøk ni yïthu
met,
ni ööu nyïme nou wär ki dudi ni
döötu ena maal.
3 Wär ŋäyu ni Wuuö Jwøk ki dëëre
beeye Jwøk.
Bee eni na cwääc øøni, ni øøna
moe;
øøna thööge, ni ø caala pïïth
dïëk moe ni wø kwaaye.
4 Dønyu ki dhi kal mar øt lam
mare nou dwøga met ec jïre,
ni pwøyu eni dï kal mare.
Dwøgu met ec jïre, ni pwøyu eni.
5 Kiper Wuuö Jwøk beer,
ni mëër mare ni wø ba jøøl
bëëdö na bäre bäre,
na adïëri mare nut cooth ki yïth
beenhnhe bëët.
@
*#Duut Mo Nyeya Caana Bëëtö Mano Bëëde Ki Gø
1 Wui Wuuö Jwøk, ï pwøa pwøø ki
duut,
naa wär kiper mëër mo ba jøøl ki
ŋøl luup ma kare.
2 Aani, a poot bëëdö ni cwïnya ena
jöör adïëri.
?A yi wäne nø noo ööï baŋa?
A poot bëëdö ni bëëtö mara thïïŋ
ki jø paara.
3 A ba jïëy ki gïn mo raac,
naa män ki tïï jø wø gaa wøk,
ni tïïe moge a ba gutge.
4 Bëëtö mo ba tiir kwiera kwierø,
ni bëëda ni kara bäär ki raay.
5 Ŋat wø waac nyeŋ watge ki piny
raanynya raanynyø,
naa ba jïëy ki ŋat mo cwïnye da
atöör mo jiy ee taaø ki waŋe.
6 A bëëdö naa jïëya jøøa näk
marge adïëri dï paac,
kiper nee ge bëëtge ki aani.
Eni ni wø cäädhi ki jöö mo thïïŋ
otïmö na ŋat mo tïnynya aani.
7 Ŋat wø tïïö ki tïï cwøk ba bëëdö
paara,
ni ŋat wø car tööt ba bëëdö
buuta.
8 Ka amöölla cooth jøøa reyø
moa en dï paac wø raanynya
raanynyø,
kiper nee jø wø tïïc gïï mo reyø
bëët käla wøk dï pääny Wuuö
Jwøk.
&Manøgø beeye duut Deebit.
@
*#Duut Lam Mar Ŋat Mo Ocaannø Mo Manynya Køny
1 Wui Wuuö Jwøk, wïny lam mara;
beerra man pïïc kwaci mara baŋï.
2 Kär täärnyïmï kanï ki aani
kany wø ena yïth gïï mo leth.
Cek ïthï ki mara,
ni laarï mara løk kany wø cwøla
ïïni.
3 Kiper nïr kwøw 'moa wø laara
maayø kaamar jïrö,
ni tïm dëëra bäre ni waŋŋi.
4 Bääta apädhö ni tïma naa caala
luum mo obäp,
ni gïr cam ba lääŋŋa.
5 Ki køør cooyø mara na päl,
aana dwat ni tïma na cöö keere.
6 Aana tïmö kaamar wenyø mo
onoorø dï paap, ni tïma naa caala tula mo bëëdö
wï paac.
7 A bëëdö naa juudö,
naa caala wenyø mo bëëdö ee
keere wï øtø.
8 Nyïïmänna bëëdö ni jøøŋŋa aani
cooth ki yïth nïne bëët,
ni ö jø wø päät aani ni tïïcge
nyeŋŋa na gïr acïëni.
9-10 Ki køør wëëyï na pällö bääta,
aana kwanyï ni wetï aani wøk,
ni tïma naa cama bur,
ni ö pï nyeŋŋa ni bëëde ni øøya
yi gïn wø maadha.
11 Nïr kwøw 'moa aløny ni maayø
kaamar tïm abøøya,
ni tïma kaamar luum mo obäp.
12 'Ba ï na Wuuö Jwøk, ï bëëdö na
nyeya na bäre bäre,
ni bëët nyeŋŋï ni ŋäc këël yïth
beenhnhe bëët.
13 Ïïno ö maal ni päth cwïnyï ki gïr
Dhayan,
kiper ennø beeye kany mo orømø
ki man nyoothï met iï jïre,
kiper kanya wäŋŋi apäŋ.
14 Kiper ka adïëri møn, jiyï poot
mëër ki Dhayan, pääny mana
no oränynyö,
ni cwïnyge opädhö ki gïr ŋøøm
moa dööŋ wï paac manøgø.
15 Wïth juurre bëët otïmö ni lwäär
ki nyeŋ Wuuö Jwøk,
ni ö nyec bäät piny bëët ni
lwäcge ka ajiem mare.
16 Kiper Wuuö Jwøk Dhayan cäŋe
ka geerrø,
ni ööe ka ajiem mare.
17 Eni lam mar jøøa can di wïnynyö,
ni kwac marge ba taae.
18 Beerra man göör luummi piny
kiper beenhnhe moo ööi,
kiper nee geni na näk poot
kär nywølø nee Wuuö Jwøk
pwøcge;
19 ni luummeca beeye en:
Wuuö Jwøk alwïthö piny ni eni
ena maal kar bëëtö mare na en
kur keere,
ni raŋ bäät piny ni eni ena maal,
20 kiper nee cooyø mar jø twöc wïnynye,
nee jøøa näk thøø onø ŋøl bäätge
päde.
21 Køøre nyeŋ Wuuö Jwøk okøp jiyi
Dhayan, ni beeye Jerucalem,
ni ö pwøci mare ni caani yie,
22 kanyo ö tiet mïëri ki wïth juurre
noo cooŋge rege na aciel
ni ge wøøra Wuuö Jwøk.
23 'Ba aani, Wuuö Jwøk aana tïïe
naa jääk naa poot thiinh,
ni døøc nïr kwøw 'moa mo nøk.
24 Køøre aana köö, ni «Wui, ï na
Jwøk mara,
kär jwïëya laar käl ni cwiiya poot nøk;
ïïni, ï bëëdö niï kwøw ki yïth
beenhnhe bëët.
25 Dïkwøŋ cøøn piny acwääyï,
ni tïïyï maal ki cerï.
26 Gïïögø bëët ränynyö, 'ba ïïni, ï
dööŋ karï.
Ge ränynyö bëët kaamar abïï,
ni wiilï geni kaawat man wø wiil
abïï dëël,
ni wet ge.
27 'Ba ïïni, ï poot bëëdö na karï karï,
ni cwiiri moï ba thum.
28 Wäät jiyï obëëdö ni kwøw,
ni ö nyïïkwaacge ni këët tietge
piny nyïmï.»
&Manøgø beeye duut lam mar ŋat mo
ocaannø, kanya bëëde ni jääk, ni käl
luumma en cwïnye wøk jï Wuuö Jwøk.
@
*#Duut Mo Pwøca Jwøk Kiper Mëër Mare
1 Aani Wuuö Jwøk pwøa pwøø ki
cwïnya bäre, ni pwøa eni na en kur keere ni
dëëra yaa cïbö jïre bäre.
2 Wuuö Jwøk pwøa pwøø ki
cwïnya bäre,
ni ba wïl wïïa ki tïïe moe bëët na
beyø.
3 Beeye Wuuö Jwøk ni wø wec gïïa
baaa bëët,
ni wø køny täwe moa en dëëra
bëët.
4 Bee eni ni wø käl aani wøk cer
thøø,
ni wø nyooth bäth ec ki mëër mo
ba jøøl jïra.
5 Bee eni ni wø tïïc aani nee gïï
mo beyø tïmge ni dagø jïra
ki yïth nïr kwøw 'moa bëët,
ni tïïc teek mara ni nyään
ni tïma naa teek kaamar
odhuuth.
6 Wuuö Jwøk wø tïïya tïïc ma
adïëri,
ni ŋun jøøa näk othiel piny bëët.
7 Acaare moe anyoodhe jï Modhe,
ni nyooth tïïe moe jï jø Icriel.
8 Wuuö Jwøk yie bäth ni mëër ki
jiy;
eni ba laar wëër, ni mëër mare
päl ni ba jøøl.
9 Eni ba bëëdö ni jääla øøni cooth,
ni wëër mare thuwø ba bëëdö na
bäre bäre.
10 Eni kär kännö bäätø ka ajäla mo
orømø ki raay moø,
ni käre øøni cunnö ki gïn mo
orømø kiper moa baaø.
11 Kaawat man bëët maalli ki piny
ni dwøŋ en,
Wuuö Jwøk mëër mare ni wø ba
jøøl dwøŋ døc bäät jø wø lwäär
ki eni.
12 Ka teeŋ man bëëde en ni yïthakic
kur tuul-cäŋ
ki kur pänh-cäŋ bäär,
Wuuö Jwøk gïïa baaø akäl wøk
ni tïïc karge ni bäyö ki øøni.
13 Ka teeŋ man wø bëët wää
obwöre ni yie ee bäädhö ko
obwöre moe,
Wuuö Jwøk bëëdö ni yie ee
bäädhö ki jø wø lwäär ki eni.
14 Kiper eni cwääc marø ŋääe,
ni wïïe wø di caarø ki man näk
mo øøna tør jaak.
15 Nïr kwøw mo dhaanhø caala nïr
luum;
dëër dhaanhø wø døøŋŋø ni
mïërö kaamar luum mo oløth
yi pwöla.
16 'Ba luum, kany wø kwön jame
bääte, puta ränynyö,
ni put kare rwäänyö na bäre
bäre.
17 'Ba Wuuö Jwøk mëër mare ni wø
ba jøøl
bëëdö na bäre bäre bäät jø wø
lwäär ki eni,
ni ö adïëri mare ni bëëde ni nut
bäät nyïïkwaacge,
18 ni beege jø wø gwøk gïna tuude
ki geni,
ni wïthge ba wïl ki man kïthge
gïïa ceme bäät tïïc.
19 Wuuö Jwøk tier wäl nyec mare
ee nø këël piny maalø,
ni eni bëëdö na wïth jammi bëët.
20 Pwøyu Wuuö Jwøk, u na
nyïïatwiet maal moe,
uuni na teek ni wø kïth luumme
bäät tïïc,
ni wø wïny dwøre man wø caane.
21 Pwøyu Wuuö Jwøk, u na lwaae
moe bëët ni en maal,
uuni ni wø tïny eni nou tïïya mo
wø manynye.
22 Beerra man ö gïïa cwääc Wuuö
Jwøki bëët ni pwøcge eni
kwöra enge yïthge bëët,
ni beeye bäät piny bäre na en
cere. 
'Ba aani, Wuuö Jwøk pwøa pwøø
ki cwïnya bäre.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Pwøca Wuuö Jwøk Kiper Tïïe Moe Bëët
1 Aani Wuuö Jwøk pwøa pwøø ki
cwïnya bäre.
Wui Wuuö Jwøk, ï na Jwøk
mara, karï dwøŋ døc;
wödö ka ajiem na en jïrï iï røø
dëërï kaamar abïï.
2 Tar iï rïëp dëërï kaamar aleeŋŋa,
ni maal iï peerø kaamar oduŋkaara.
3 Wuuö Jwøk paare ee geer maal,
ni tïïc pøøl na jääy mare,
ni cäädhi ka bäät jamø.
4 eni jamø wø di jääŋŋö na
nyïïatwiel mare,
ni tïïc agaackøth na gïr tïïc mare.
5 Piny acwääe ni këël tiet gø piny
ni teek,
nee bëëde na bäre bäre ni ba
nëëŋŋi.
6 Wui Wuuö Jwøk, naama dwøŋ
apeedhï bäät piny kaamar abïï,
ni ö pïïyi ni macge wïth kïte.
7 Kanya joogï geni, gena døøk,
ni putge mølø kanya määr dwørï.
8 Wïth kïte anyänh maal, ni dööŋ
agäm-kïte piny,
ni dööŋ pïïyi kwöra näk iï jiiŋŋø
kiperge.
9 Ïïna tïïö ki kee mo ba løny ki
man kaali ya nämmi,
nee piny ba cäŋge mayø këët.
10 Wuuö Jwøk pï jøøro wø wëëge
kwödö ki yïth agäm-kïte,
ni muulge ki yïthakic kïte.
11 Ni ö lääyi bëët ni jïtge ki pïï mo
maathge,
ni jït ogwari ki pïï mo riemma
riew marge.
12 Wec maal wø bëëdö bäät pïïögø,
ni bëëtge ni ge lweelli bäät jenni.
13 Wuuö Jwøk køth wø jääŋŋe
jääŋŋö bäät kïte ni eni ena
maalø,
ni ö gïïa en bäät piny ni jäŋge ki
cam ki køør man wø tïïe.
14 Wuuö Jwøk luum wø wëëge twöö
kiper lääy,
ni gïï wø duunni ki cam wø
wëëge twöö jï dhaanhø,
nee dhaanhø jïte ki cam ri gïï wø
ciek yïth ŋøøm;
15 ni jïte ki køøŋø mo døøya yie mo
met,
ki maaw mo tïïya täärnyïme ni
lem,
ki cam ni wø cïpi ki teek dëël.
16 Jer lur Libaanø na piith Wuuö
Jwøki
wø di jwøø ki pïï na karge.
17 Weny wø gëëdö ki uudi bäätge,
ni ö ajaae ni jïtge ki kwör bëëte
bäät jera døøŋŋø.
18 Kïte moa bäyö bëëdö na kar
bëëtö jï adëëlli,
ni ö kwöra no okaaŋŋø røk kïte
ni tïmge na kar kan røk jï
athinaaki.
19 Wuuö Jwøk dwääy atïïe nee
cwiir pääŋŋe,
ni ö cäŋŋi ni ŋäc kany wø pädhe
yie.
20 Muudhö wø jääŋŋe jääŋŋö, ni
tïm pinynyi na wäär,
ni ö lääc paapi bëët ni täkge ki
ööny wøk;
21 ni ö ŋuuwe ni märge ni ge
manynya gïï camge,
ni cam marge man wø cacge käla
baŋ Jwøk.
22 'Ba kany wø tuul cäŋŋi ge tägö ki
døøn kwörge, 
ni butge piny kwör bëëte moge.
23 Køøre dhaanhø wø aa baŋ tïïc
mare,
ni tïïc tïïe moe këël kanyo päth
cäŋŋi.
24 Wui Wuuö Jwøk, gïïa tïïyï thööth
døc kiree.
Gïïögø bëët tïïyï ka køør leec wïc
marï,
ni ö gïïa cwääyï bëët ni pääŋge
piny bäre.
25 Naama dwøŋ nut, ni bëëdö ni
dwøŋ ni kany mo päl ee maaø,
ni yie da gïï mo kwøw mo
døøŋŋø ki mo therø mo
kwäänge ba thum.
26 Ni baabuure wø cäädha yie,
ni Lëëwatan, lääna dwøŋ na
cwääyï,
nut yi naam kaace ni tuuk yie.
27 Gïïögø bëët raŋŋa jïrï,
kiper nee caapge cïpï jïge ki yïth
kwöra näk karge.
28 Kany wø cïpï cam jïge, lwørge
lwørø,
ni jäŋge ki caammi mo met kany
wø japï cerï jïge.
29 Kany wø paanyï täärnyïmï, dëëtge
wø puta tïmö ni kwanynyi;
ni kany wø lwørï jwïëcge, ge thøw,
ni putge døø yi ŋöömö.
30 Møøk wø cäŋ ka cwääyö kany wø
jääŋŋï jwïëyï bäätge,
ni cäŋï bäät piny tïïyö ni nyään.
31 Beerra man ö ajiem mar Wuuö
Jwøk ni bëëde na bäre bäre.
Beerra man ö Wuuö Jwøki ni
mïn yie ki tïïe moe.
32 Wuuö Jwøk bäät piny di raŋø, ni
tïm pinynyi ni jäŋŋi,
ni gut kïte, ni putge duuŋ ki jïrö.
33 Aani, a wär ki duut jï Wuuö Jwøk
kany pooda naa poot kwøw en,
ni wära thuwø ki dut pwøc jï
Jwøa kany pooda naa nut bäät
piny.
34 Beerra man tïm acaare 'moa ni
kännö ki met ec jï Wuuö Jwøk;
aani thuwø a bëëdö ni yia met
ki eni.
35 Beerra man thum jø raayi bäät
piny,
ni bäŋe jø wø tem gïï mo reyø
mo joot këët.
Aani Wuuö Jwøk pwøa pwøø ki
cwïnya bäre.
Alëluya, pwøc en jï Wuuö Jwøk.
@
*#Duut Mo Cäänö Kaper Gïïa Tïïc Wuuö Jwøki Kiper Jiye
1 Dwøgu met ec jï Wuuö Jwøk, ni
pwøyu nyeŋŋe,
ni caannu tïïe moe nee wïny
wïth juurre.
2 Wärru jïre, wärru dut pwøc jïre,
ni caannu tïïe moe bëët na näk
rëëma ec.
3 Jiemmu nyeŋŋe na en kur keere;
beerra man mïn yïth jø wø cac
Wuuö Jwøk.
4 Cayu Wuuö Jwøk ki teek mare,
ni manynyu eni cooth.
5-6 U na nyïïkwaac dhaanhnhe ma
Eeberam,
u na nyïïkwaac Jeekap na näk ee
jierø,
caarru wïthu ki gïïa näk rëëma
ec na tïïe,
këël ŋïïce moe ki luup ŋøl moa
caane ki dhee.
7 Eni na Wuuö Jwøk, beeye Jwøk
marø;
ŋøl luup mare ena bäät piny
bäre.
8 Eni luumma tuude di lääŋŋö na
bäre bäre, ni bëëde ni luumma caane di
lääŋŋö këël yïth beenhnhe ma
kume,
9 ni beeye luumma tuude ki
Eeberam,
na kööŋe kiper gø jï Aydhak.
10 Ni cäŋ gø tuutö ki Jeekap, ni
beeye Icriel,
nee bëëde na bäre bäre,
11 na kööe, ni «Ŋööm Keenan
omëëga ïïni,
ni tïme na kur nyïïkwaayu.»
12 Kanya bëëtge ni kwäänge nøk,
ni ge nøk døc ni gena wëëlle yi
ŋöömmögø,
13 ni ge wïïrö tiet mïëri,
ni ge cøøa paac man nø ki baŋ
jøøi nø,
14 ge käre wëëk dhaanhø mør nee
ge thiel piny;
nyeye aköömme kiperge, ni kööe,
15 ni «Jiya na näk yaa jierø kär
gutu,
ni ba tïïu dëëtge ki gïï mo leth,
ge na nyïïkuk 'moa.»
16 Kanya ö Wuuö Jwøki na käl käc
paac mana bëëtge yie,
ni wëëk caammi moge thumö
bëët,
17 eno nø jääk Ijep ki dhaanhø
nyïmge dïkwøŋ,
ni beeye Jocep, na kwøŋ dwøk
pwödhö na laŋŋø.
18 Eni tiete atwöc ko oguudi,
ni maai piny ki nywïëny.
19 'Ba eni, kanya poode ni luumma
caan Wuuö Jwøki poot kär
thur kare,
luummögø abëëdö na gïr päärö
dëëre.
20 'Ba nyeny Ijep ajäägö ni käl eni
wøk øt twöc,
ni bee eni na wïth jiy na pät
Jocep.
21 Eni Jöcep atïïe na ŋat käär
akwöma,
ni tïïc eni na wïth jammi moe
bëët,
22 nee cuumme moe köömme
kaawat man wø manynye,
nee jø døøŋŋø moe pwönynye
nee jïtge ki leec wïc.
23 Køøre Icriel thuwø, ni wø cwøl ni
Jeekap, aö Ijep,
ni bëëde na wëëllö kaace yi
ŋööm Kaam.
24 Ni ö Wuuö Jwøki ni wëëk jiye ma
jø Icriel nyaay,
ni tïïc geni ni teek ni kaala
nyïïmän moge.
25 Eni cwïny jø Ijep awiile ni tïmge
ni ge män ki jiye,
ni tïïge ka atade dëët jiye.
26 Eni dhaanhnhe ma Modhe
ajääŋŋe,
ni jääŋ Aran thuwø na näk ee
jierø.
27 Geni nyuuthe moe atïïcge dï jø
Ijep,
ni tïïcge gïï mo rëëma ec kaace
yi ŋööm Kaam.
28 Eni muudhö ajääŋŋe ni tïm
pinynyi ni cøl,
ni kärge luumme kwierø.
29 Eni pïï mo jø Ijep awiile ni tïme
na remø,
ni wëëk rec moge thøø.
30 Dï paac marge agääbö ko ogwaal
bäre,
këël kwör niine moa en paan
dwøŋ.
31 Ena cäännö, ni ö nyuuwi dï poge
bäre,
ni cäŋ cäännö, ni put lwaa
lwaŋŋø öö ni päl.
32 Pey ajääŋŋe bäätge na kar køth,
ni ö maalli ni male dï poge bäre.
33 Ni raany omøki ko olämmi moge
moa piithge,
ni kaaŋ jenni moa en dï poge.
34 Ena cäännö, ni put bäänyö öö, 
ni beeye bäänyö mo kwäänge ba
thum.
35 Ni camge gïïa no otuy bëët poge,
ni thöörge gïïa no ociek yi
ŋöömö marge.
36 Eni kaai bëët moa näk cwøw dï
poge ma Ijep anääe,
ni beege moa kwøŋ jø Ijepi nywøl
na nyooth gø ni ge nyöödö.
37 Køøre eni jø Icriel abwøth wøk
ni ge käädö ki warkie ki
gwet-bïrö;
'ba kanya cääthge, bäŋ dhaanhø
aciel dïge mo obøømmø.
38 Kanya aac jø Icrielli, jø Ijep
yïthge amïnnö,
kiper mana bëëtge ni geno lwäyö
ki gïïa tïïc Jwøki dëëtge ki
køørge.
39 Eni pöölö apeere na tïpö bäätge,
ni tïïc maac nee liele jïge ki
wäär.
40 Gena pëëö, ni känne jïge ka
ajwëëyi,
ni wëëk ge jäŋö ki møø mo käla
maal.
41 Eni kïdi akaae ni mul pïïyi wøk,
ni kwöt kwöra no otal kaamar
naam.
42 Eni wïïe kär wïl ki luumma en
kur keere na tuude,
ni beeye luumma tuude ki
dhaanhnhe ma Eeberam.
43 Eni jiye abwøth wøk ni yïthge
met,
ni kwöŋge ki met ec, geni na näk
ee jierø.
44 Eni ŋøøp wïth juurre amëëk geni,
ni lwørge gïïa tïïc jøøgø ki öölö
marge
ni tïmge na moge,
45 kiper nee ciik moe gwøkge,
ni kïthge gïïa ceme bäät tïïc.
Alëluya, pwøc en jï Wuuö Jwøk!
@
*#Duut Mo Cäänö Kaper Køny Mar Jwøk Këël Na Bëët Jø Icrielli Ni Ge Gëëmö
1 Alëluya, pwøc en jï Wuuö Jwøk!
Dwøgu met ec jï Wuuö Jwøk,
kiper eni beer,
ni mëër mare ni wø ba jøøl
bëëdö na bäre bäre.
2 ?Aŋa ni løny jïre ki man caan
gïïa tïïc Wuuö Jwøki ki teek
mare?
?Na aŋa ni løny jïre ki man pwøc
eni ki pwøc mana dii pwøø ki
gø?
3 Gwïëth en jï jø wø many ŋøl ma
adïëri,
jø wø tïïc mana näk kare cooth.
4 Wui Wuuö Jwøk, kär wïïï wïl ki
aani kanyo nyoothï met iï jï jiyï;
ö baŋa ni piemï aani,
5 kiper nee kwärö mar jiyï na näk
iï jierø neena,
nee yia mïnne ki jiyï na aciel,
nee ï jiemwa na aciel ki jiyï na
näk thöögï.
6 Waani, waana tïïö ki raay,
kaawat mana tïïc kwäcwa,
ni bëëtwa ki bëëtö mo paa kare,
ni tïïwa ki gïï mo reyø.
7 Kanya bëët kwäcwa Ijep,
tïïe moï ni wø rëëm ec kärge
lääŋŋö,
ni mëër marï na päl ni wø ba
jøøl, ge kär cädö kiper gø;
'ba gena gëëmö ki ïïni, ï na Jwøa
Dwøŋ ni en Maal, kanya enge
bäät Naama Kwaar.
8 'Ba ka adïëri møn, Wuuö Jwøk
gena pieme kiper nyeŋŋe,
ni nyootha teek mare, 
9 kanya kööm Naama Kwaar ni tale,
ni bwøth geni ki kanya päŋ
dïkwøŋ, ni cääthge kere ge
caatha paap mo otal.
10 Kanyøgø gena pieme ceŋ jøøa
män ki geni,
ni käl geni wøk ceŋge.
11 Ni ö naammi ni cam jøøgø,
ni bäŋe aciel mo odööŋ.
12 Køøre ge na jiye, luup moe
aŋääthge,
ni wärge ki duut ni ge pwøya eni.
13 'Ba wïthge alaar wïlö ki tïïe moe,
ni kärge pwöc mare koorø.
14 Ni tïmge ni ge lääŋŋa yïthge dï
paap,
ni päärge Jwøk.
15 Gïna pëënyge acïbe jïge,
'ba dëëtge amooe ki täw mo leth.
16 Kanya enge twïër dï paap, gena
bëëdö ni yïthge keec ki Modhe
ka Aran,
Aran ŋata no ocïp kur keere na
mar Wuuö Jwøk.
17 Ni ö pinynyi ni jap ree ni mwøny
dïbwöthe moge ma Daathan ka
Abiram,
ni dïïr ree bäätge ki jø mïëcge
bëët.
18 Ni ö maaci ni waaŋ jøøa dwal
dëëtge ki jøøgø,
ni put jøøgø ni reyø yøø thöör.
19 Jø Icriel gena lëënyö ki warkey
ni tïïcge gø na nyirøøa tier Kïn
Körëp,
ni wøørge gïnögø ni ege leenyø
na gïn lam enø.
20 Geni Jwøk na näk ajiem marge
awiilge
ki gïna tïïcge ni caala dhieŋ ni
wø cam luum jaak.
21 Geni wïthge awïl ki Jwøk na
piem geni,
na tïïc gïï mo døøŋŋø Ijep,
22 ni beege gïïa näk rëëma ec na
tïïe kaace yi ŋööm Kaam,
ki gïïa thääŋ ec na tïïe bäät
Naama Kwaar.
23 Køøre Jwøk aköö ni ge di
raanynyø;
'ba Modhe, na näk ee jierø,
aci yïthakicge ki Jwøk,
nee wëër mar Jwøk paanye
bäätge, nee ge ba raanynye.
24 Geni luumma caan Wuuö Jwøki
kärge ŋäädhö,
ni taakge rege ki jøøa en yi
ŋöömma mïërö.
25 Gena bëëdö ni ge ŋurö yïth
oduŋkaare moge,
ni kärge dwør Wuuö Jwøk
wïnynyö.
26 Køøre ena kööŋ jïge,
ni ge wëëge thumö ki thøø dï
paap,
27 ni wëëk nyïïkwaacge keethø dï
wïth juurre,
ni thumge ki thøø tiet mïëri.
28 Geni cwïnyge aløøge baŋ jwøa
cwøl ni Baal-Pëëgör,
ni camge olämme moa cïp jï juu
mo bäŋ jwïëy dëëtge,
29 ni tïïcge Wuuö Jwøk nee goote ki
køør gïïa tïïcge,
ni ö Jwøki ni jääl geni ki täw mo
leth.
30 'Ba Piniac aö maal ni dier
luummögø,
ni put täwi cuŋŋö.
31 Ni jïëc eni ni mare beer këël yïth
beenhnhe bëët moo ööi
ki køør gïna tïïe.
32 Geni Wuuö Jwøk atïïcge nee
wëëre bäät pï Meriba,
ni ö Modhe ni jïte ka ajäla ki
køørge;
33 kiper cwïny Modhe adøøcge mo
keec,
ni cääne ki luup mo käre caarø.
34 Geni wïth juurre moa bëëdö
Keenan kärge nääö,
këël na bëëde ni geno kööm
Wuuö Jwøki ni jøøgø 'näkge.
35 'Ba røkge ajääpge ki wïth juurre
moøgø,
ni kwanyge bëëtö marge.
36 Ni wøørge gïïa no otieŋø ni wø
lam jøøgø,
ni tïm lammi manøgø na abïëp
kiperge.
37 Wäätge ki nyïïge aŋaalge no
olämme jï juu mo piny,
38 ni kønyge rem jiy piny mo bäŋ
gïn mo ege baaø,
ni beege rem wäätge ki nyïïge,
na ŋaalge no olämme jï gïïa no
otieŋø ni wø lam jø Keenanni,
ni tïm ŋöömö marge ni ba waany
ki køør remø.
39 Ni tïm dëëtge ni ba waany ki
køør tïïe moge,
ni tïmge kaamar kääpe ki køør
gïïa tïïcge.
40 Wëër mar Wuuö Jwøk aliel
kaamar maac bäätge, ge na
jiye,
ni männe ki geni, ge na näk
thööge.
41 Ni cïp geni ceŋ wïth juurre,
ni tïmge ni ge ena tietge, ge na
jøøa män ki geni.
42 Gena thiel nyïïmänni moge piny,
ni tïmge ni ge ena tietge.
43 Geni, gena køny Wuuö Jwøki
kwöre mo thööth,
'ba gena tïmö ni marge ageem ki
køør gïï wø carge,
ni nigeŋac yïth raay moge.
44 'Ba kanya ö Wuuö Jwøki na wïny
oduuru marge,
leth bëëtö marge aneene,
45 ni par wïïe ki luumma tuude
kiperge,
ni dwøk cwïnye piny ki køør
mëër mare na päl ni wø ba
jøøl;
46 ni tïïc cwïny jøøa mak geni ki
tøŋ ni bäth ki geni.
47 Wui Wuuö Jwøk, ï na Jwøk
marwa, piem waani,
ni lemï waani yïthakic wïth
juurre,
kiper nee nyeŋŋï na en kur keere
pwøcwa,
ni jiemwa ïïni kany wø pwøcwa
ïïni.
48 Pwøc en jï Wuuö Jwøk, Jwø
Icriel,
ki mana täge cøøn, këël bäre
bäre.
Beerra man kö jiyi bëët, ni
«Beeye kare!»
Alëluya, pwøc en jï Wuuö Jwøk!
@
*#Duut Mo Pwøca Wuuö Jwøk Kiper Køny Mare
1 Dwøgu met ec jï Wuuö Jwøk,
kiper eni beer,
ni mëër mare ni wø ba jøøl
bëëdö na bäre bäre.
2 Beerra man ö jøøa wïïl Wuuö
Jwøki wøk yïth gïïa leth
ni caange met ec marge na
enøgønø,
3 ni beege jøøa cooŋe ki tiet mïëri
bëët,
na käl jï løø kur tuul-cäŋ ki jï løø
kur pänh-cäŋ,
ki moa käl wï-piny ki tier-piny.
4 Møøk dïge atïmö ni thääyö dï
paap kany mo bäŋ pïï yie,
ni kärge jöör pääny mana dege
bëëdö yie joodø.
5 Käc ki riew bäre atïmö ni päl
dëëtge,
ni ö dëëtge ni ŋiir piny.
6 Kanya cwat yïthge ki öölö, Wuuö
Jwøk akwacge,
ni ö Wuuö Jwøki ni käl geni wøk
yïth gïïa leth na enge yïthge.
7 Gena bwøth Wuuö Jwøki ki jöö
mo tiir,
kiper nee ge cige pääny mana
dege bëëdö yie.
8 Beerra man ö jøøgø ni dwøkge
met ec jï Wuuö Jwøk
kiper mëër mare ni wø ba jøøl,
ki gïïa näk rëëma ec ni wø tïïe
jï jiy.
9 Kiper ŋata no onäk riewi
amaadhe ki pïï ni røme,
ni wëëk ŋata no onäk käci jäŋö
ki cam mo met.
10 Møøk dïge abëëdö yi muudhö mo
cøl ma kar thøø,
ni geno twöö ko oguudi ni bëëtö
marge leth,
11 kiper mana kwierge luupa caan
Jwøki,
ni taakge pwöc moe, eni na
dwøŋ ni en maal.
12 Wïthge adwøk Wuuö Jwøki piny
ki tïïc mo teek,
ni tïm dëëtge ni dhønhnhi ni bäŋ
ŋat mo køny geni.
13 Kanya cwat yïthge ki öölö, Wuuö
Jwøk akwacge,
ni ö Wuuö Jwøki ni käl geni wøk
yïth gïïa leth na enge yïthge.
14 Gena käl Wuuö Jwøki wøk ki yi
muunhnha cøl na näk kar thøø,
ni cööt oguudi moa näk geno
twöö ki ge.
15 Beerra man ö jøøgø ni dwøkge
met ec jï Wuuö Jwøk
kiper mëër mare ni wø ba jøøl,
ki gïïa näk rëëma ec ni wø tïïe
jï jiy.
16 Kiper eni dhøk uut twöc moa näk
tïïc ka nywïëny atoor piny,
ni tøc dïdëëte mo nywïëny na
thäŋi.
17 Møøk dïge moa wïthge teek,
bëëtö marge atïmö ni leth
kiper mana dhalge luum Jwøk ni
tïïge ki gïï mo reyø.
18 Cwïnyge atïmö ni cøl ki caammi
bëët,
ni tïm karge ni cään ki thøø.
19 Kanya cwat yïthge ki öölö, Wuuö
Jwøk akwacge,
ni ö Wuuö Jwøki ni käl geni wøk
yïth gïïa leth na enge yïthge.
20 Wuuö Jwøk dwøre acaane ni
dwøk dëëtge karge,
ni køny geni yi ränynyö marge.
21 Beerra man ö jøøgø ni dwøkge
met ec jï Wuuö Jwøk
kiper mëër mare ni wø ba jøøl,
ki gïïa näk rëëma ec ni wø tïïe
jï jiy.
22 Beerra man cïpge ko olämme
thuwø ni ge dwøga met ec,
ni caange tïïe moe ni döötge ena
maal.
23 Møøk dïge mo wø cäädhi dï
naama dwøŋ ki baabuure,
ni wø bëëdö ni marge tïïc bäät
naama dwøŋ,
24 tïïe mo Wuuö Jwøk na näk rëëma
ec
ni wø tïïe bäät naamøgø ajootge
døc.
25 Kiper dwøre acaane, ni put
atuunna mo dwøŋ kwönnö,
ni ö athaga ni tïme ni päl.
26 Gena leeŋ athaga maal ni cäŋ
geni duu piny,
ni päth cwïnyge na bäre bäre ki
køør gïna raac na tägö.
27 Gena tïmö ni ge bøømmø kaamar
dhaanhø mo omeer,
ni tïm riek waŋ marge ni bäŋ
kare.
28 Kanya cwat yïthge ki öölö, Wuuö
Jwøk akwacge,
ni ö Wuuö Jwøki ni käl geni wøk
yïth gïïa leth na enge yïthge.
29 Atuunna ajooe ni cuŋŋe,
ni ö athaga ni lïŋe.
30 Yïthge amïnnö kanya ö naammi
na neekïïl,
ni ö Wuuö Jwøki ni bwøth geni
këël mana pïïcge dhi waath
mana manyge.
31 Beerra man ö jøøgø ni dwøkge
met ec jï Wuuö Jwøk
kiper mëër mare ni wø ba jøøl,
ki gïïa näk rëëma ec ni wø tïïe
jï jiy.
32 Beerra man tïŋge nyeŋŋe maal dï
acooŋ paac bäre,
ni pwøcge eni kany wø ö jø
døøŋŋø wø cooŋge dëëtge yie.
33 Wuuö Jwøk näm ataale ni tïm
kwörge na tëën,
ni taal kwör wø kwön pïïyi ki
yïthge;
34 ni tïïc ŋøøp wø cïpi ki cam na
ŋøøp acäbö mo bäŋ gïn mo tuy
yie.
Gïïögø atïïe ki køør rääö mar
jøøa bëëdö yi ŋöömmögø.
35 Kany ma tëën atïïe na kany mo
yie da näm,
ni tïïc ŋøøpa näk otal na kwör
wø kwöt pïïyi ki yïthge.
36 Jøøa no onäk käci awëëk bëëtö
kaace,
ni gëëtge ki pääny mo bëëtge yie.
37 Ni purge ki pwöth, ki pwöth
omøki,
ni jïtge ki caammi mo thööth.
38 Gena gwïëth Wuuö Jwøki, ni
tïmge ni thööth,
ni tïïc dhäk moge ni thööth.
39 'Ba kwään jiy wø tïmö ni nøk ni
døø wïthge piny
ki køør caannø ki bëëtö mo leth
ki kïmmö man wø kïmge ki gø.
40 Ni ö Wuuö Jwøki ni bëëde ni
kwääri ee taaø jaak,
ni wëëk geni thääyö dï paap mo
bäŋ øtjöö mo joot yie.
41 'Ba jøøa can wø poot käle wøk ki
yi ränynyö marge,
ni meet geni ni tïmge ni thööth
kaamar pïïth dïëk.
42 Gïïögø neen jøøa beyø neenø ni
mïn yïthge,
ni ö jøøa reyø ni bëëtge ni
dhøkge ege miiø.
43 Ŋata näk wïïe leer, beerra man
kïth gïïögø cwïnye,
ni bëëde ni lääŋŋa mëër mar
Wuuö Jwøk ni wø ba jøøl.
@
*#Duut Mo Pwøca Jwøk Ni Kwaca Eni Kiper Køny
1 Wui Jwøk, a bëëdö ni cwïnya ena
køørï;
naa wär ki dudi naa pwøya ïïni
ki cwïnya bäre.
2 Päyu, u na thøme 'moa!
Aani, øw nyïïa nyïïö nee laar
ruuö ki duuda.
3 Wui Wuuö Jwøk, met ec duua
duuö jïrï dï jiy bëët,
ni wära ki dut pwøc jïrï dï wïth
juurre.
4 Kiper mëër marï ni wø ba jøøl
dwøŋ døc no okëët maal,
na adïëri marï okëët nyeŋ pøøl.
5 Wui Jwøk, ï bëëdö ni karï dwøŋ
døc,
na ajiem marï ena bäät piny
bäre.
6 Wïny mara ni piemï aani ki køør
teek badï, kiper nee aani na mëërï ki gø naa
piem.
7 Jwøk acäänö ni ena kar bëëtö
mare na en kur keere, ni kööe,
«Ŋøøp Cekam pääŋŋa pääŋŋö ni
mïn yia,
ni pääŋŋa ŋøøp Goor Cuköt
thuwø.
8 Ŋøøp Gelät beege 'moa, ni ö
ŋøøp Maneeca ni näkge 'moa
thuwø;
jø tuuŋ Ipariem perge leth ni
caala cöör nywïënyö mara,
ni jø tuuŋ Juuda beege jø wø kïth
ciik 'moa bäät tïïc.
9 'Ba jø Möap caala gïn wø lööga
yie,
ni ö warø mara ni leeŋa gø yi po
jø Ëdöm,
ni kwöŋŋa bäät jø Pilitin ni
dwøra ena maal kanyo bööta
geni.»
10 ?Wui Jwøk, aŋa noo mooc aani
ki teek naa dønynya yi pääny
mana teek,
noo bwøth aani naa këëda ki jø
Ëdöm?
11 ?Wui Jwøk, aŋø, waana kwierï
møn ennø,
niï ba ci baŋ leny këët ki jø leny
mowa?
12 Køny waani ceŋ nyïïmän,
kiper køny mar dhaanhø bäŋ gïn
mo duue
13 Teek dïïm wø jootwa baŋ Jwøk,
ni bee eni noo bööt nyïïmän
mowa.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Kwaca Jwøk Nee Kwör Coole Dëët Nyïïmän
1 Wui Wuuö Jwøk, ï ni wø pwøa,
kärï lïŋö,
2 kiper jøøa reyø ki jø cwøk
dhøkge ena raa,
ni ge kïtha bääta ki luup tööt.
3 Aana cielge dïër ki luup män,
ni bëëtge ni dhøkge ena dëëra ki
luup mo bäŋ tietge.
4 Këël na bëëda naa mëër ki geni, gena
duu raa ni kïthge bääta ki luup;
'ba aani, a bëëdö naa lämö.
5 Gena tïmö ni ge duua gïn mo
raac baŋa na kar gïna beer,
ni duuge män na kar mëër mana
mëëra ki geni.
6 Wui Wuuö Jwøk, cuumï ki dïŋut
luup mo raac bäät ŋata kïth
bääta ki luup,
ni ö nyimän mar ŋata kïth bääta
ki luup ni kïth bäät gø ki luup
kar løøk.
7 Kanyo ŋøl luumme, beerra man
jääl eni,
ni tïm lammi mare ni duua raay
bääte.
8 Beerra man tïm nïr kwøwi moe
ni nøk,
ni ö kare ni lwøri ya ŋat mørri.
9 Beerra man tïm obwöre moe ni
bäŋ wääge,
ni tïm cïïe na cï thøø.
10 Beerra man thääy obwöre moe ni
ge kwääö,
ni bëëtge ni ge määnyö ni tïm
karge ni bäär ki wï poge.
11 Beerra man ö ŋat pïïdö ni käl
japa en jï gø bëët,
ni ö jøøa pathi ni twierge japa
joode ki køør öölö mare.
12 Beerra man ba jïte ki ŋat mo
nyootha mëër jïre,
ni bäŋe ŋat mo cwïnye pädhi
kiper obwöre moe kanyo
dööŋge ni bäŋ wääge.
13 Beerra man dït wïïe,
ni put nyeŋŋe rwäänyö yi
beenhnhø mano ööi.
14 Beerra man ö Wuuö Jwøki ni paac
wïïe ki raay moa tïïc kwäye,
ni ö bääyö mar menni ni ba
wëënni.
15 Beerra man bëët Wuuö Jwøki ni
raŋŋa raay mo gø cooth,
ni rwääny nyeŋŋe bäät piny, ni
bäŋe ŋat mo par wïïe ki eni.
16 Kiper eni wïïe käre caarø ki man
nyooth mëër;
'ba ena tïmö ni caanna jøøa no
ocaarø ki moa can,
ki moa näk cwïnyge opädhö, këël
mano thøwge.
17 Eni bëëdö ni yie met ki man cien
dhaanhø,
'ba acïëni ööa bääte;
ni eni bëëdö ni yie ba met ki
man gwïëth dhaanhø,
'ba gwïëth otïmö ni kare bäär ki
eni.
18 Eni acïëni ee røø dëëre kaamar
abïï,
ni ci dëëre kaamar pïï,
ni twaa yi cöönne kaamar maaw.
19 Beerra man ö acïëni ni bëëde
dëëre kaamar aleeŋŋa man wø
kääre,
ni tïme kaamar kaw man wø
twöö piere cooth.
20 Beerra man tïm gïïögø bëët na
gïïo tïïc Wuuö Jwøki dëët jøøa
kïth bääta ki luup,
jøøa car gïï mo reyø dëëra.
21 'Ba ï na Wuuö Jwøk, ïïni na
kwäärö mara,
beerra man tïïï ki gïn mo beer
kipera nee nyeŋŋï pwøc;
ni piemï aani ki køør mëër marï
na beer ni wø ba jøøl.
22 Kiper aano caannø naa bëëdö
naa can,
naa bëëdö ni cwïnya opädhö na
bäre bäre.
23 Aani, a rwäänyö kaamar tïm
abøøya,
ni jar aani wøk kaamar twöŋö.
24 Wïth cøŋŋa atïmö ni nhønhnhi ki
køør mana kweera ki cam,
ni dwada ni tïma ni aana cöö.
25 Aana tïmö na gïr ajøøŋ jï
nyïïmän 'moa,
ni kany wø neenge aani, wïthge
wø putge ka kiinynyø.
26 Wui Wuuö Jwøk, ï na Jwøk
mara, køny aani;
piem aani ki køør mëër marï ni
wø ba jøøl.
27 Beerra man ö pïëmmi manøgø ni
ŋäyi ya nyïïmänni 'moa ni käla
baŋï,
ni beeye ïïni ki dëërï, ï na Wuuö
Jwøk, na tïïc gø.
28 Geni, marge acïëni, 'ba ïïni, marï
gwïëth;
kanyo öge maal bääta, wïthge
olääi,
'ba a na dhaanhnhï, aano bëëdö
ni yia met.
29 Beerra man räny nyeŋ jø wø kïth
bääta ki luup,
ni bëët lään wïci dëëtge kaamar
abïï.
30 Aani Wuuö Jwøk pwøa pwøø ki
cwïnya bäre,
ni pwøa eni dï acooŋ jøøa
thööth.
31 Kiper eni cuŋŋa kur ŋata can,
nee jwïëc gø pieme ceŋ jø wø ŋøl
thøø bääte.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Cäänö Kaper Teek Mano Cïp Jwøki Jï Kwääc Deebit
1 Wuuö Jwøk aköö jï Kwäärö mara,
ni «Pï bäät cwïïa,
këël mano tïïa nyïïmän moï na
køøm tietï.»
2 Wuuö Jwøk teek kwär marï
otïïe nee nyaae ni tägi ka yi
Dhayan,
ni bëëdï ni nyïïmän moï ena
tierï.
3 'Ba dïcäŋ wø këëdï ki nyïïmän
moï,
jiyï wø puta ö maal ki met ec;
ni ö wøpe moï ni öge baŋï ka
ajiem mo dwøŋ,
ni ge thööth ni ge caala thööy
mo amöölla.
4 Wuuö Jwøk anø kööŋ, ni mana
caane ba wiile këët, na kööe,
ni «Ï bëëdö ni ïïna dïlämi na bäre
bäre,
niï caala Melkidhedek.»
5 Wui Wuuö Jwøk, kwäärö ena
bäät cwïïï,
eni, dïcäŋo wëëre, wïth nyeye di
nyadhø.
6 Eni luup wïth juurre di ŋølø,
ni tïïc piny ni päŋ ki dëët jiy mo
othøw,
ni nyath wïth kwääri mo tiet
mïëri mo thööth.
7 Eno mäthi ki pïï yi waŋ mo ena
deŋ jöö;
køøre nø, dïïm otïmö ni ena jïre.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Pwøca Wuuö Jwøk Kiper Bëëtö Mare
1 Alëluya, pwøc en jï Wuuö Jwøk.
Aani Wuuö Jwøk pwøa pwøø ki
cwïnya bäre
dï jøøa marge thïïŋ ni wø dwäti
na aciel,
ni pwøa eni thuwø dï acooŋa
bäre.
2 Tïïe mo Wuuö Jwøk døøŋŋø døc,
ni ö jøøa yïthge met ki tïïe
moøgø ni lääŋge geni.
3 Tïïe moe duua wödö ka ajiem jïre,
ni ö adïëri mare ni bëëde na bäre
bäre.
4 Eni wïth jiy apare ki tïïe moe ni
wø rëëm ec.
Wuuö Jwøk yie bäth ni mëër ki
jiy.
5 Jø wø lwäär ki eni wø di caamø,
ni ö luumme na näk ee tuudö
cøøn
ni bëëde ni lääŋŋa gø na bäre
bäre.
6 Teek mare anyoodhe jï jiye ki ri
tïïe moe,
kanya cïp ŋøøp juurre jï jiye.
7 Gïï wø tïïe bëët beege adïëri ni
näkge karge,
ni ciik moe bëët beege gïï mo
oŋäädhö.
8 Ni ge bëëdö karge na bäre bäre,
no otïïc Wuuö Jwøki ki jöö ma
adïëri mo thïïŋ.
9 Wuuö Jwøk jiye akønye ni wïïl
geni wøk;
ena tudö ki luubö ki geni mo
bëëdö na bäre bäre.
Wuuö Jwøk nyeŋŋe ena kur
keere ni di lwäärö.
10 'Ba tier leec wïc mana dïkwøŋ
beeye ki man lwäär Wuuö
Jwøk,
ni jø wø caath køør ciik moe, tier
gïna beer ŋäcge.
Pwøc en jï Wuuö Jwøk na bäre
bäre.
@
*#Duut Mo Cäänö Kaper Bëëtö Mano Joot Ŋat Wø Lwäär Jwøk
1 Alëluya, pwøc en jï Wuuö Jwøk!
Gwïëth en jï ŋat wø bëëdö ni
lwäära Wuuö Jwøk,
ŋat wø bëëdö ni yie met ki ciik
moe.
2 Eni kunhnhe otïmö ni teeka eni
dï piny,
ni ö beenh jøøa marge thïïŋ ni
gwïëdhi.
3 Eni paare jïtö ki jammi ni kwäre,
ni ö bëëtö mare na beer ni bëëde
na bäre bäre.
4 Eni bëëdö na tar mo meenya
muudhö jï jøøa marge thïïŋ;
ni bëëde ni mëër ki jiy, ni mare
beer.
5 Otïmö ni beer jï ŋat wø mëër ki
jiy ni wø wëëk jape mac;
ni wø tïïc tïïe moe ki jöö ma
kare.
6 Eni ba pädhi na bäre bäre;
eni na beer gïre di lääŋŋö cooth.
7 Eni cwïnye ba bwøk kany wø
wïny gïï mo leth mo otägö;
cwïnye ee maaø ni bëëdö ni
ŋäätha Wuuö Jwøk.
8 Eni cwïnye maae maaø ni ba
lwäyi,
këël mano joot gïna manynye
dëët nyïïmän moe no othur
kare.
9 Eni wø cïpö ni yie met jï jøøa can,
ni ö bëëtö mare na beer ni bëëde
na bäre bäre;
eno jïti ki teek ni wøør eni.
10 Bëët ŋatøgø ojoot ŋata raaci ni
goote,
ni kaac lage ni put bääte pädhö;
ni ö gïï wø many jø raayi ni
ränyge.
@
*#Duut Mo Pwøca Jwøk Kiper Man Wø Køny Jøøa Can
1 Alëluya, pwøc en jï Wuuö Jwøk!
Pwøyu Wuuö Jwøk, u na jiye;
pwøyu nyeŋ Wuuö Jwøk.
2 Beerra man pwøc nyeŋ Wuuö
Jwøk,
ki man bëëde ennø, këël bäre
bäre.
3 Beerra man pwøc nyeŋ Wuuö
Jwøk,
ki mano täge ki jï løø kur tuulcäŋ
këël jï løø kur pänh-cäŋ.
4 Wuuö Jwøk kare dwøŋ bäät wïth
juurre bëët,
na ajiem mare dwøŋ no okëët
maal.
5 ?Aŋa ni pääri ki Wuuö Jwøk, eni
na Jwøk marø?
Bee eni ni wø bëëdö maalø,
6 ni bee eni ni wø dwøk dëëre piny
nee japa en maal ki moa en piny
raŋŋe.
7 Eni jøøa can wø tïŋe maal ki yi
tør,
ni tïŋ jøøa näk oööl maal ki wï bur,
8 ni cïp geni kanya ciel ki kwääri,
jøøa no ocuumö na wïth jiye.
9 Eni dhaagø ma bwøc wø mooe
mooø ki paare,
ni tïme na mii obwöre ni bëëde
ni yie met.
Alëluya, pwøc en jï Wuuö Jwøk!
@
*#Duut Mo Cäänö Kaper Ööny Jø Icriel Wøk Ki Ijep
1 Jø Icriel, ni beege jø dhi øt Jeekap,
kanya öge wøk Ijep po jøøa
dhøkge path,
2 Juuda atïmö na kar bëëtö mo ena
kur keere jï Wuuö Jwøk,
ni bëët jø Icrielli bëët ni ena cere.
3 'Ba kanya ö jø Icrielli na jooti ya
Naama Kwaarri, Naama Kwaar
areeŋø, ni ö Naam Jördan ni døø ŋääe.
4 Thuuri atïmö ni pärö kaamar
nyïïrööm,
ni ö kïte ni tïmge ni pärö kaamar
nyöök rööm.
5 ?Wui Naama Kwaar, aŋø, ïïno
tïmö nidïï, ni reŋï en?
?Wui Naam Jördan, aŋø ni døøï
ŋääï en?
6 ?Wui, u na thuuri, aŋø ni päru
kaamar nyïïrööm en?
?Wui, u na kïte, aŋø ni päru
kaamar nyöök rööm en?
7 Wui, ï na piny, tïmï niï jäŋŋi
nyïm Wuuö Jwøk,
eni na Jwø Jeekap,
8 na wëëk pïï kwön wøk ki yi kïdi,
ni tïme na puul,
na tïïc kïnna teek na kany wø
kwön pïïyi wøk ki yie.
@
*#Duut Mo Pwøca Wuuö Jwøk, Eni Na Jwøka Eni Keere
1 Wui Wuuö Jwøk, kär tïmö ni
jiemma waani;
kär tïmö ni jiemma waani,
'ba beerra man tïme ni jiemma
nyeŋŋï
kiper mëër marï ni wø ba jøøl ka
adïëri marï.
2 Aperŋø ni kö wïth juurre en,
ni «?Jwøk marge en kaa?»
3 'Ba Jwøk marø møn, ena maal,
ni eni tïïya man wø met yie ki
gø.
4 'Ba gïï wø lam wïth juurre wø
tïïc ka warkey ki gwel-bïrö,
ni beege gïï mo tïïya jiyi ki ceŋge.
5 Gïïögø jïge da dhøgi, 'ba ge ba
luubö;
ni jïge da nyeŋŋi, 'ba ge ba
nëënö.
6 Jïge da ïdhi, 'ba ge ba wïnyö;
ni jïge da ummi, 'ba bäŋ gïn mo
ŋwääcge.
7 Jïge da ceŋ, 'ba bäŋ gïn mo mulge;
ni jïge da tiel, 'ba ge ba cäädhi;
ni bäŋ dwøl mo tuny wøk ki
cwäkge.
8 Jøøa tïïc geni otïmö ni bäŋ teek
jïge ni caala geni,
këël jøw bëët mo wø ŋääth geni.
9 Wui, u na jø Icriel, ŋääthu Wuuö
Jwøk;
bee eni na dïkunyi maru ni ena
kwöt leny jïïu.
10 Wui, u na jø dhi øt Aran, 
ŋääthu Wuuö Jwøk;
bee eni na dïkunyi maru ni ena
kwöt leny jïïu.
11 Uuni ni wø lwäär ki Wuuö Jwøk,
ŋääthu Wuuö Jwøk;
bee eni na dïkunyi maru ni ena
kwöt leny jïïu.
12 Wuuö Jwøk lääŋŋa øøni; ø di
gwïëdhö;
ø di gwïëdhö, ø na jø Icriel,
ni gwïëth jø dhi øt Aran.
13 Wuuö Jwøk jø wø lwäär ki eni di
gwïëdhö,
ni beege moa kwörge bäŋgø ki
moa kwörge døøŋŋø bëët.
14 Beerra man ö Wuuö Jwøki ni
wëëk uuni nyaay,
uuni ko obwöre mou bëët.
15 Beerra man ö Wuuö Jwøki ni
gwïëth uuni,
eni na cwääc maal ki piny.
16 Maal beeye mar Wuuö Jwøk,
'ba piny ee cïbö jï jiy.
17 Jøøa no othøw Wuuö Jwøk ba
pwøcge,
ni beege jøøa no oci kany mo
bäŋ dwøl yie.
18 'Ba øøni, Wuuö Jwøk pwøø pwøø,
ki man bëëde ennø, këël bäre
bäre.
Alëluya, pwøc en jï Wuuö Jwøk!
@
*#Duut Mo Pwøca Wuuö Jwøk Kiper Mana Køny Dhaanhnhe Cer Thøø
1 Aani, a mëër ki Wuuö Jwøk
kiper dwøra wø wïnynye
wïnynyö kany wø kwaa eni.
2 Eni cøøra cøørø ki yïth nïr kwøw
'moa bëët,
kiper mana cek ïthe ki mara.
3 Aana bëëdö ni aano ciel thøø
dïër kaamar dhaanhø mo
omeenø ki thøøl,
ni ö räämmi mana caal mana en
kar bëët jwïëc jøøa no othøw
ni ö bääta,
ni lwäya, ni päth cwïnya.
4 Køøre nyeŋ Wuuö Jwøk acwøla,
ni kööa,
ni «Wui Wuuö Jwøk, a kwaya
ïïni, kwøw aani!»
5 Wuuö Jwøk bëëdö ni mëër ki jiy
ni mare beer,
ni eni na Jwøk marø met ec mare
wø nyoodhe nyoodhø.
6 Wuuö Jwøk jøøa näk gïn tïïcge
kucge di gwøø;
kanya bëëda ni aano dwøk piny,
aana kønye.
7 Wui, cwïnya, døø piny, kärï pärö,
kiper Wuuö Jwøk atïïö ki gïï mo
beyø jïra.
8 Ï na Wuuö Jwøk, jwïëya akälï
wøk cer thøø,
ni pooyï pï nyeŋŋa,
ni tïïyï tieta nee nigethïk naa ba
pädha.
9 Aano bëëdö naa caatha køør
Wuuö Jwøk
kanyo pooda naa poot kwøw.
10 Aana bëëdö ni cwïnya da
ŋäädhe,
këël na bëëda ni aano köö ni
aano caannø døc.
11 Aani, cwïnya abwøk,
ni kööa ni jiy bëët tööte.
12 ?Agïnaŋø noo tïïa jï Wuuö Jwøk
na kar gïïa beyø bëët na tïïe jïra?
13 Aani, køøŋ nyïïomøki ocïba ki
ya athöödhi na muuy jï Wuuö
Jwøk
naa pwøya eni kiper mana piem
aani.
14 Gïïa kööŋa kiperge jï Wuuö Jwøk
ocïba ni jiye bëët nutö.
15 Wuuö Jwøk thøø mar jiye jwøre
jwørø.
16 Wui Wuuö Jwøk, ka adïëri møn,
aana dhaanhnhï;
aana dhaanhnhï møn, ni aana o
dhaaŋ wø tïny ïïni;
aana pädï wøk ki yi thøø.
17 Olämi mar dwøk met ec ocïba
jïrï,
ni cwøla nyeŋŋï, ï na Wuuö
Jwøk.
18 Gïïa kööŋa kiperge jï Wuuö Jwøk
ocïba ni jiye bëët nutö,
19 ni wa ena dï kal mar Øt Wuuö
Jwøk,
na en dï Jerucalem.
Alëluya, pwøc en jï Wuuö Jwøk!
@
*#Duut Mo Köömma Jiy Bëët Nee Wuuö Jwøk Pwøcge
1 U na wïth juurre bëët, pwøyu
Wuuö Jwøk;
u na dïbwör bäre, pwøyu eni;
2 kiper Wuuö Jwøk mëër ki øøni ki
mëër mo dwøŋ mo ba jøøl,
ni ö adïëri mare ni bëëde na bäre
bäre.
Alëluya, pwøc en jï Wuuö Jwøk!
@
*#Duut Mo Pwøca Jwøk Kiper Gïïa Tïïe Ki Køør Beenynye
1 Dwøgu met ec jï Wuuö Jwøk,
kiper eni beer,
ni mëër mare ni wø ba jøøl
bëëdö na bäre bäre.
2 Beerra man kö jø Icrielli,
ni «Mëër mare ni wø ba jøøl
bëëdö na bäre bäre.»
3 Beerra man kö jø dhi øt Aranni,
ni «Mëër mare ni wø ba jøøl
bëëdö na bäre bäre.»
4 Beerra man kö jø wø lwäär ki
Wuuö Jwøk,
ni «Mëër mare ni wø ba jøøl
bëëdö na bäre bäre.»
5 Aana jwöŋö dëër Wuuö Jwøk
kanya ena yïth gïï mo leth,
ni wïny mara ni mooc a ki bëëtö
mo beer.
6 Wuuö Jwøk ena kura naa ba
lwäyi.
?Aŋø, dhaanhø jaak, agïnaŋø noo
tïïe dëëra?
7 Wuuö Jwøk ena kura, ni beeye
dïkunyi mara;
kiper manøgønø, nyïïmänna
jooda joodø ni geno böötö.
8 Beerra eni ki man bëët dhaanhe
ni ree ee kan buut Wuuö Jwøk,
ki man bëëde ni eni ŋäätha
dhaanhø.
9 Beerra eni ki man bëët dhaanhe
ni ree ee kan buut Wuuö Jwøk,
ki man bëëde ni eni ŋäätha
kwääri.
10 Wïth juurre bëët aana cielge dïër,
'ba ki køør nyeŋ Wuuö Jwøk gena
raanynya.
11 Aana cielge dïër, aana cielge dïër
møn;
'ba ki køør nyeŋ Wuuö Jwøk gena
raanynya.
12 Aana cielge dïër kaawat man wø
tïïc kïci,
'ba gena nibäc kaamar maa
koodhi,
ni raanynya geni ki køør nyeŋ
Wuuö Jwøk.
13 Gena nyänh bääta døc ni tïma
naa many ka böötö,
'ba Wuuö Jwøk aana kønye.
14 Wuuö Jwøk beeye teek mara, ni
bee eni na cäŋŋa ki duut,
ni tïme na pïëmi mara.
15 Kwöŋŋö man wø kwöŋŋö ki met
ec kiper pïëm man wø piem jiy
ki gø en,
wïnyö yïth oduŋkaare mo jic
Wuuö Jwøk, ni jøw köö,
ni «Wuuö Jwøk bade teek ni
këëdö ki leny mo teek;
16 Wuuö Jwøk teek bade dwøŋ døc;
Wuuö Jwøk bade teek ni këëdö ki
leny mo teek.»
17 Aani, a ba thøw, 'ba a bëëdö naa
kwøw,
ni cara tïïe mo Wuuö Jwøk.
18 Wuuö Jwøk aana pwönynye døc
ki pwöc mo leth,
'ba a käre wëëk thøø.
19 Japu dhøk käälle jïra mo wø
døny jic Wuuö Jwøki ki yïthge,
kiper naa dønya ki yïthge,
nee met ec dwøga jï Wuuö Jwøk.
20 Man beeye dhi kal mar Øt Wuuö
Jwøk,
man wø døny jic Wuuö Jwøki ki
yie.
21 Wui Wuuö Jwøk, met ec duua
duuö jïrï kiper mana wïnynyï
mara,
ni tïmï ni ïïna pïëmi mara.
22 Kïdi mana kwier dïgëëte
atïmö na kïn gøøt mana pere
letha eni na mak øtø;
23 gïnögø beeye gïna tïïc Wuuö
Jwøki,
na tïmö na gïn mo rëëma ec ki
nyeŋŋø.
24 Dïcäŋi beeye dïcäŋ mana cïp
Wuuö Jwøki kur keere;
beerra man kanynyø ni mïn
yïthø ki gø.
25 Wui Wuuö Jwøk, wa kwaya ïïni,
piem waani;
wui Wuuö Jwøk, wa kwaya ïïni,
nee gïï wø tïïcwa thurge karge.
26 Gwïëth en jï ŋato ööi ki nyeŋ
Wuuö Jwøk!
Wa gwïëtha uuni ki yi Øt Wuuö
Jwøk.
27 Wuuö Jwøk beeye Jwøk møn,
ni bee eni na mooc øøni ki tar.
Olämme moo cïp dïcäŋ man wø
wøør Jwøk yie wär twöyu ki
thøøli,
ni kälu geni buut gïn wø cïp
olämme bääte.
28 Beeye ï na Jwøk mara, met ec
duua duuö jïrï;
beeye ï na Jwøk mara, nyeŋŋï
tïŋa maal.
29 Dwøgu met ec jï Wuuö Jwøk,
kiper eni beer,
ni mëër mare ni wø ba jøøl
bëëdö na bäre bäre.
@
*#Duut Mo Pwøca Jwøk Kiper Ciik Moe
1 Gwïëth en bäät jø wø bëëtö
marge thïïŋ,
jø wø cäädhi ki køør ciik mo
Wuuö Jwøk.
2 Gwïëth en bäät jø wø gwøk ciik
Wuuö Jwøk,
ni wø many eni ki cwïnyge bäre.
3 Jøøgø bäŋ gïn mo raac mo tïïcge,
'ba ge caatha jööre.
4 Wui Wuuö Jwøk, pwöc moi acïpï
nee gwøkwa na karge.
5 Gïna manynya keere beeye ki
man bëëda
naa gwøga ciik moï cooth.
6 Kany wø cäda kiper ciik moï,
wïïa ba lääy.
7 Kanyo kwanya luup ŋøl moï na
näk adïëri,
ïïno pwøa ki cwïny mo thïïŋ.
8 Aani, ciik moï gwøa gwøø;
kär a weyï na bäre bäre.
9 ?Aŋø, wøpe bëëtö marge
ogwøkge gø nidïï?
Bëëtö marge ogwøkge ki køør
luummï.
10 Ï yaa manynyø ki cwïnya bäre;
kär a wëëk gaan wøk ki ri ciik
moï.
11 Luummï yaa kan cwïnya,
kiper naa ba bääya dëërï.
12 Wui Wuuö Jwøk, pwøc en jïrï;
pwöny aani ki ciik moï.
13 Luup ŋøl moï bëët
wø køba købø ki dhaa.
14 A wø bëëdö ni yia met ki man
cäädha køør ciik moï,
naa caala dhaanhø mo yie
omïnnö ki jap kwärö.
15 A wø cädö bäät pwöc moï,
ni bëëda naa lääŋŋa jöörï.
16 A bëëdö ni yia met ki ciik moï,
ni wïïa ba wïl ki luummï.
17 Tïïï ki gïï mo beyø jïra, a na
dhaanhnhï,
naa bëëda naa kwøw ni gwøa
luummï.
18 Jap nyeŋŋa,
nee gïïa näk rëëma ec ri pwöc
moï nee jooda.
19 Aani, a bëëdö ni aana wëëllö
bäät pinyi en;
kär ciik moï kanï ki aani.
20 Cwïnya bëëdö ni ena køør luup
ŋøl moï,
naa bëëdö naa lääŋŋa geni ki
yïth nïne bëët.
21 Jø okiera, na no ocienø, wø joogï
jooø,
jø wø gaa wøk ki ri ciik moï.
22 Daak ajøøŋ ka ataa bääta,
kiper ciik moï yaa gwøø.
23 Këël ni näk kwääri bëëdö ni ge
waya nyeŋŋa,
a na dhaanhnhï, a poot bëëdö
naa cädö bäät ciik moï.
24 Met ec wø jooda ka ri ciik moï,
ni beeye geni ni wø pwöny aani.
25 Aano ränynyö naa bëëdö yi tør;
'ba cäŋ a mooyø ki kwøw ki køør
luummï.
26 Gïïa tïïa bëët acaana, ni løgï
mara jïra;
pwöny aani ki ciik moï.
27 Mooc aani ki leec wïc, nee tiet
pwöc moï kwanya,
naa cäda kiper tïïe moï na näk
rëëma ec.
28 Aani bääta apädhö ki kïmmö;
døøc a mo teek ki køør luummï.
29 Tïïc aani ni kara bäär ki bëët
tööt,
ni pwönynyï aani ki ciik moï ki
køør mëër marï.
30 Aani jöör adïëri yaa jierø,
ni cwïnya yaa cïp køør luup ŋøl
moï.
31 Wui Wuuö Jwøk, a bëëdö ni aano
göök ri ciik moï;
kär dee ŋat lää wïïa.
32 Aano cäädhi køør ciik moï
kiper mana tïïyï cwïnya ni leer.
33 Wui Wuuö Jwøk, pwöny aani ki
man cäädha køør ciik moï,
nee gwøa na bäre bäre.
34 Mooc aani ki leec wïc, nee ciik
moï gwøa,
ni bëëtge ni yaa gwøø ki cwïnya
bäre.
35 Bwøth aani ki jöör ciik moï,
kiper a bëëdö ni yia met ki ge.
36 Løø cwïnya køør ciik moï,
ni paa køør jap kwär.
37 Män nyeŋŋa ki raŋ gïï mo oballe
jaak,
ni cäŋï a mooyø ki kwøw ki køør
luummï.
38 Wëëk luummï thur kare jïra, a na
dhaanhnhï,
kiper niï lwäär.
39 Daak ajøøŋ bääta mana lwäära ki
gø,
kiper luup ŋøl moï beege karge.
40 Ka adïëri møn, a bëëdö naa
lääŋŋa pwöc moï;
cäŋ a mooyø ki kwøw ki køør
adïëri marï.
41 Wui Wuuö Jwøk, beerra man
nyoothï mëër marï ni wø ba
jøøl jïra,
ni piemï aani ki køør luummï.
42 Køøre nø, a jïtö ki gïn mo løøa
løø jï jø wø jøøŋ aani,
kiper luummï yaa gum cwïnya.
43 Kär luum adïëri daagï dhaa,
kiper a ŋäätha luup ŋøl moï.
44 Ni ö ciiki moï ni bëëde naa
gwøga geni,
ni gwøa geni na bäre bäre;
45 ni bëëda naa cäädhi ka kany mo
leer,
kiper man wø bëëda naa
manynya pwöc moï.
46 Ciik moï ocaana jï nyeye,
ni wïïa ba laay.
47 Aani, a bëëdö ni yia met ki ciik
moï,
na mëëra ki geni.
48 A bëëdö naa wøøra ciik moï na
mëëra ki ge,
ni bëëda naa cädö bäätge.
49 Par wïïï ki luumma caanï jïra, a
na dhaanhnhï,
ni beeye luumma mooyï aani ki
ŋäädhe ki køøre.
50 Gïn wø cøm cwïnya kany wø ena
yïth gïï mo leth beeye en:
a wø mooyï mooø ki kwøw ki
køør luummï.
51 Jø atöör bëëdö ni buua aani døc
kiree,
'ba a bäŋ wø gaa wøk ki ri ciik moï.
52 Wui Wuuö Jwøk, a bëëdö naa
lääŋŋa luup moa ŋølï ya
acääŋŋe cøøn,
ni bëëtge ni ge cøma cwïnya.
53 Yia aliel døc kaamar maac ki jø
raay,
ge na kwier ciik moï.
54 Ciik moï bëëdö na dudi jïra,
kany bëëda yie en ni aana wëëllö.
55 Wui Wuuö Jwøk, a wø bëëdö naa
lääŋŋa nyeŋŋï ki dï wäär,
ni bëëda naa gwøga ciik moï.
56 Bëëtö mara beeye en:
a bëëdö naa gwøga pwöc moï.
57 Wui Wuuö Jwøk, beeye ï na kura;
aana kööŋ ki man gwøa luupï.
58 A kwaya ïïni ki cwïnya bäre;
nyooth mëër marï jïra ki køør
luummï.
59 Aana cädö kiper bëëtö mara;
køøre raa aløøa ki man cäädha
køør ciik moï.
60 Aana laar läät bäät ciik moï,
naa kär ruu ki man gwøa ge.
61 Jøøa reyø aana cekge ka abïëp,
'ba wïïa kär wïl ki ciik moï.
62 Ki dhöör wäär a wø ööa maal
naa dwøga met ec jïrï
kiper luup ŋøl moï na näk adïëri.
63 Aana nyawat jø wø lwäär ki ïïni
bëët,
jø wø caath køør pwöc moï.
64 Wui Wuuö Jwøk, mëër marï ni
wø ba jøøl, piny päŋ ki gø
bäre;
pwöny aani ki ciik moï.
65 Wui Wuuö Jwøk, ïïna bëëdö niï
tïïya gïï mo beyø jïra, a na
dhaanhnhï,
ki køør luummï.
66 Pwöny aani nee wïïa tïme ni leer,
nee gïna beer ki gïna raac jiera,
kiper a bëëdö naa ŋäätha ciik
moï.
67 Kanya pooda ni gïïa leth kära
jwørø, aano gaa wøk;
'ba ennø, a bëëdö ni luummï yaa
gwøø.
68 Wui Wuuö Jwøk, ï beer ni tïïe
moï beyø;
pwöny aani ki ciik moï.
69 Jø atöör aana rwøthge jaak ki
luup tööt,
'ba a bëëdö naa gwøga pwöc moï
ki cwïnya bäre.
70 Ge bëëdö ni cwïnyge teek,
'ba aani, a bëëdö ni yia met ki
ciik moï.
71 Mana jwøra gïï mo leth atïmö na
gïn mo beer kipera,
kiper nee ciik moï kwanya.
72 Ciik moa caanï ki dhiï perge leth
jïra,
ni kaala warkey ki gwet-bïrö mo
ba kwaan.
73 Aana cwääyï ki cerï ni këëllï
tiera piny;
mooc a ki leec wïc nee ciik moï
kwanya.
74 Jø wø lwäär ki ïïni, bëëtö mara
ojootge ni mïn yïthge,
kiper a ŋäätha luummï.
75 Wui Wuuö Jwøk, ŋääa ni luup
ŋøl moï beege karge,
ni ŋääa ni marï beeye adïëri na
wëëgï aani jwør gïï mo leth.
76 Beerra man ö mëërri marï ni wø
ba jøøl ni cøm cwïnya,
ki køør luummï na caanï jïra, a
na dhaanhnhï.
77 Beerra man nyoothï mëër marï
jïra, kiper naa kwøa,
kiper yia mïnni ka ciik moï.
78 Beerra man lää wïth jø atöör,
kiper na katge dhaa ki jap tööt;
'ba aani, a bëëdö naa cädö bäät
pwöc moï.
79 Beerra man ö jø wø lwäär ki ïïni
ni duuge baŋa,
jø wø ŋäc ciik moï.
80 Beerra man gwøa ciik moï ki
cwïnya bäre,
nee wïïa ba lääe.
81 Aana ööl naa koora man piemï
aani;
'ba a poot bëëdö naa ŋäätha
luummï.
82 Waŋa atal jöö køør luummï,
ni kööa, na «?A yi wäne noo cømï
cwïnya?»
83 Këël na tïma kaamar opïr pïën
mo oraany jïrö,
wïïa kär wïl ki ciik moï.
84 ?A këël kany mo nyïëdi nø noo
bëëda, a na dhaanhnhï, naa
kurö?
?Na yi wäne noo ŋølï luup bäät
jø wø caan aani?
85 Jø atöör gena kunyö ki buri
kipera,
jø wø ba caath køør ciik moï.
86 Ciik moï bëët beege adïëri;
køny aani, kiper aana caange ki
luup tööt.
87 Dööŋŋa kany mo thiinh ki man
'näkge aani bäät piny,
'ba aani pwöc moï kära wiiø.
88 Cäŋ a mooyø ki kwøw ki køør
mëër marï ni wø ba jøøl;
køøre ciik moï gwøa gwøø.
89 Wui Wuuö Jwøk, luummï tiere
okëët piny maal,
ni bëëdö na bäre bäre.
90 Adïëri marï bëëdö ni nut yïth
beenhnhe bëët;
piny acïbï kare ni teek, ni put
bëëtö kare.
91 Ki køør luup ŋøl moï, jammi
bëët bëëdö kwörge këël dïcäŋi
ennø,
kiper jammi bëët bëënna ïïni.
92 Doo na a kär bëëdö ni yia met ki
ciik moï,
a doo ränynyö ki gïïa jwøra na
leth.
93 Aani wïïa ba wïl ki pwöc moï na
bäre bäre,
kiper aana cäŋï mooyø ki kwøw
ki køørge.
94 Aana dhaanhnhï; piem aani,
kiper man wø bëëda naa
manynya pwöc moï.
95 Jøøa reyø koora aani nee jwïëya
raanyge,
'ba a bëëdö naa cädö bäät ciik
moï.
96 Ajooda ni jammi bëët da cuŋge,
'ba ciik moï bëëdö na bäre bäre.
97 Wui Wuuö Jwøk, yia met ki ciik
moï døc,
naa bëëdö naa cädö bäätge ki
yïth nïne bëët.
98 Ciik moï a wø moocge mooø
ki leec wïc mo kaala mar
nyïïmänna,
kiper ciik moøgø nutö buuta
cooth.
99 Aana tïmö ni wïïa leer naa kaala
dïpööye 'moa bëët,
kiper mana bëëda naa lääŋŋa
gïïa caanï.
100 Wïïa atïmö ni leer ni kaala wïth
jøøa døøŋŋø,
kiper pwöc moï yaa gwøø.
101 Raa yaa mänö ki jïëth bëëtö moa
reyø bëët,
kiper nee luummï gwøa.
102 A kär gaa wøk ki ri luup ŋøl moï,
kiper beeye ïïni ki dëërï na
pwöny aani.
103 Luummï bëëdö ni met jïra døc,
ni bëëde ni ŋweeth dhaa ni kaala
maar kïc.
104 Leec wïc wø jooda joodø ki køør
ciik moï;
kiper manøgønø, a män ki jïëth
tööt bëët.
105 Wui Wuuö Jwøk, luummï caala
lamba mo meenya nyïma,
ni bëëde ni caala tar mo meenya
jööra.
106 Aano nø kööŋ kiper naa cäädha
køør luup ŋøl moï na näk
adïëri,
naa puta bëëtö naa tïïya geni
cooth.
107 Wui Wuuö Jwøk, aana cännö døc;
'ba cøm cwïnya ki køør luummï.
108 Wui Wuuö Jwøk, wïny luumma
man wø pwøa ïïni ki gø,
ni pwönynyï aani ki køør luup
ŋøl moï.
109 A bëëdö yïthakic kwøw ki thøø
cooth,
'ba wïïa bäŋ wø wïl ki ciik moï.
110 Jøøa reyø aana cekge ka abïëp,
'ba a kär gaa wøk ri pwöc moï.
111 Gïïa caanï atïmö na 'moa na bäre
bäre,
kiper beeye geni ni wø døøc
cwïnya mo met.
112 Cwïnya acïba køør ciik moï,
kiper nee gwøa na bäre bäre këël
aŋuun kwøw mara.
113 A män ki jiy mo wïdö yïthakic
acaare ariiø,
'ba a mëër ki ciik moï.
114 Beeye ïïni ni wø kana raa buute,
ni beeye ï na kwöt leny mara;
naa bëëdö naa ŋäätha luummï.
115 U jø wø tïïc gïï mo reyø, daagu
rou buuta,
kiper nee ciik mo Jwøk mara nee
gwøa.
116 Jøl aani ki køør luummï, kiper
naa kwøa,
ni kär niï wëëga ŋäädhe mara
duunnö ki lään wïc bääta.
117 Jøl aani, kiper naa piem,
nee ciik moï wøøra cooth.
118 Jø wø gaa wøk bëët ri ciik moï
kwierï kwierø,
kiper cwøk moge bäŋ gïn duue.
119 Jøøa reyø bäät piny bëët wø wetï
wøk kaamar juu;
kiper manøgønø, a mëër ki ciik
moï.
120 Dëëra atïmö ni kwanynyi kiper
mana lwäya ki ïïni,
naa bëëdö naa lwäär ki luup ŋøl
moï.
121 Aani luup wø ŋøla ŋølø na karge,
naa tïïya adïëri;
kär a wiiï ceŋ jø wø thiel aani
piny.
122 Gwøk aani, a na dhaanhnhï, naa
jïta ki bëëtö mo beer;
män jø atöör naa ba thielge piny.
123 Waŋa atal jöö naa koora pïëm
marï,
ki luummï na beer.
124 Gïïo tïïyï jïra, a na dhaanhnhï,
tïïyï ki køør mëër marï ni wø ba
jøøl,
ni pwönynyï aani ki ciik moï.
125 Aana dhaanhnhï; mooc aani ki
leec wïc,
kiper nee tiet ciik moï nee ŋääa.
126 Wui Wuuö Jwøk, beeye kar tïïc
marï gø ennø,
kiper jiy ciik moï aŋølge.
127 'Ba ka adïëri møn, aani a mëër ki
ciik moï,
ni kaala warkey, këël warkey
mana tøŋ.
128 Kiper manøgønø, a bëëdö ni aano
jïëy ni pwöc moï bëët beege
karge,
ni bëëda naa män ki jïëth tööt
bëët.
129 Ciik moï rëëma ec;
kiper manøgønø, geni gwøa gwøø.
130 Ki man kwany tiet luupï cïpö ki
tar,
ni cïpö ki leec wïc jï jøøa näk
poot bäŋ gïn ŋäcge.
131 A bëëdö ni aano wär ni dhaa yaa
ŋaamø,
naa lääŋŋa ciik moï.
132 Luu wïïï baŋa ni nyoothï mëër
marï jïra,
kaawat man wø tïïyï jï jø wø
mëër ki ïïni.
133 Bwøth aani ki køør luummï,
naa ba bööt raayi.
134 Käl aani wøk ceŋ jø wø thiel jiy
piny,
kiper nee pwöc moï gwøa.
135 Wëëk tac täärnyïmï rieny bääta,
a na dhaanhnhï en,
ni pwönynyï aani ki ciik moï.
136 Pï nyeŋŋa bëëdö ni lwöra piny
kaamar pï naam,
kiper jiy bëëdö ni ciik moï ba
gwøkge.
137 Wui Wuuö Jwøk, ï bëëdö ni marï
beer,
ni luup ŋøl moï thïïŋ.
138 Ciik moa cïpï beyø,
ni beege ciik ma adïëri døc.
139 Aana këëyö na bäre bäre,
kiper mana ö nyïïmänna na
wecge luummï.
140 Luummï tøŋ ni caala gïn mo
otwønø,
ni bëëda, a na dhaanhnhï, naa
mëër ki gø.
141 A bëëdö ni kara thiinh ni aano
taaø,
'ba wïïa ba wïl ki pwöc moï.
142 Bëënynyö marï beeye bëënynyö
mo bëëdö na bäre bäre,
ni ciik moï beege adïëri.
143 Gïï mo leth aö bääta, ni bëëda
naa rämö,
'ba a poot bëëdö ni yia met ki
ciik moï.
144 Ciik moï bëëdö na adïëri na bäre
bäre;
mooc aani ki leec wïc naa bëëda
naa kwøw.
145 Wui Wuuö Jwøk, a jwöŋö dëërï
ki cwïnya bäre; wïny mara;
aani ciik moï gwøa gwøø.
146 A jwöŋö dëërï; piem aani;
aani ciik moï gwøa gwøø.
147 A wø ööa maal ni øw poodi ni
kwaa ïïni,
naa ŋäätha luup moï.
148 Nyeŋŋa lwieny ki wäär bäre,
naa bëëdö naa cädö bäät luup
moï.
149 Wui Wuuö Jwøk, wïny dwøra ki
køør mëër marï ni wø ba jøøl,
ni cäŋï a mooyø ki kwøw ki køør
luup ŋøl moï.
150 Jø wø caath køør gïï mo reyø,
gena nyänhnhö;
geni karge bäyö ki ciik moï.
151 Wui Wuuö Jwøk, ï bëëdö ni karï
cään,
ni ciik moï bëët beege adïëri.
152 Kanya kwanya ciik moï kany mo
bäär,
aŋääa ni tietge okëët piny na
bäre bäre.
153 Neen caannø mara ni kønyï aani,
kiper wïïa bäŋ wø wïl ki ciik moï.
154 Ŋun aani ni piemï aani,
ni cäŋï a mooyø ki kwøw ki køør
luummï.
155 Jøøa reyø karge bäär ki pïëm
man wø piem jiy ki gø,
kiper ciik moï ba manyge.
156 Wui Wuuö Jwøk, mëër marï
dwøŋ;
cäŋ a mooyø ki kwøw ki køør
luup ŋøl moï.
157 Jø wø caan aani ki jø wø män ki
aani thööth,
'ba a bäŋ wø gaa wøk ki ri ciik
moï.
158 Jø wø tïïö ki gïï mo reyø ki piny
raŋŋa naa ba many dëëtge,
kiper luummï bäŋ wø gwøkge.
159 Wui Wuuö Jwøk, raŋ mëër man
mëëra ki pwöc moï ki gø en;
cäŋ a mooyø ki kwøw ki køør
mëër marï ni wø ba jøøl.
160 Luup moï bëët beege adïëri;
luup ŋøl moï na beyø bëët bëëdö
na bäre bäre.
161 Kwääri a caange caannø ki gïn
mo bäŋ tiere,
'ba a bëëdö naa wøøra luupï ki yi
cwïnya.
162 Yia wø mïnni ka luummï
kaawat man wø mïn yi ŋat mo o
ojïtö ki jap twëër mo thööth.
163 A män ki tööt, ni yia raac ki gø døc;
'ba a mëër ki ciik moï.
164 Ï wø pwøa pwøø ki kwöre abïriiø
ki yi cäŋ
kiper luup ŋøl moï na beyø.
165 Jø wø mëër ki ciik moï, jïge da
jwöm mo päl ki cwïnyge,
ni ge bëëdö ni bäŋ gïn mo
cwaany tietge.
166 Wui Wuuö Jwøk, a bëëdö naa
koora ïïni naa piemï,
naa bëëdö naa kïtha ciik moï
bäät tïïc.
167 A bëëdö naa gwøga ciik moï,
naa mëër ki geni døc.
168 A bëëdö naa gwøga pwöc moï ki
ciik moï,
kiper bëëtö mara bäre ŋäyï.
169 Wui Wuuö Jwøk, beerra man
wïnynyï oduuc kwac mara;
mooc aani ki leec wïc ki køør
luummï.
170 Beerra man wïnynyï kwac mara,
ni piemï aani ki køør luummï.
171 Beerra man ö dhaa ni pwøc ïïni,
kiper man wø pwönynyï aani ki
ciik moï.
172 Beerra man wära ki duut kiper
luummï,
kiper ciik moï bëët beyø.
173 Beerra man bëëdï ni riï iï jiiŋŋø
ki man kønyï aani,
kiper pwöc moï yaa jierø.
174 Wui Wuuö Jwøk, a bëëdö naa
lääŋŋa ïïni naa piemï;
met ec wø jooda ka ri ciik moï.
175 Beerra man bëëda naa kwøw
kiper nee ï wø pwøa,
ni bëët luup ŋøl moï ni køønynya
aani.
176 Aana bëëdö naa thääyö kaamar
diel mo orwäänyö,
many aani, a na dhaanhnhï,
kiper wïïa bäŋ wø wïl ki ciik
moï.
@
*#Duut Mo Kwaca Jwøk Nee Dhaanhnhe Pieme
1 Aana jwöŋö dëër Wuuö Jwøk
kanya ena yïth gïï mo leth,
ni ö eni ni wïny mara.
2 Wui Wuuö Jwøk, piem aani ceŋ
jø wø car tööt,
ki ceŋ jø wø car cwøk.
3 ?Uuni ni wø car cwøk,
gïno tägi dëëtu ŋäyu?
Gïno tägi dëëtu beeye en:
4 Athëëre mo ŋat leny mo dhøkge
beth
ki cuk mo wärri mo ba laar thøø
opïï dëëtu.
5 Bëëtö mara atïmö ni leth,
ni tïme keda a bëëdö dï jø Möcak
ki jø Këdar.
6 Aana bëëdö ki kany mo bäär
dï jø wø män ki bëët-mëër.
7 Aani a manynya bëët-mëër,
'ba kany wø cääna kiper bëëtmëër,
ge manynya leny.	
&Manøgø beeye duut wääth man
wø wär ni jøw iitha thuur ni
jøw cøøa Øt Wuuö Jwøk.
@
*#Duut Mo Nyootha Gø Ni Beeye Wuuö Jwøk Ni Wø Koor Jiye
1 A wø lwïthö ni neena kïte;
?aŋø, køny mara wø käl kaa ŋø?
2 Køny mara wø käla baŋ Wuuö
Jwøk,
eni na cwääc maal ki piny.
3 Eni tierï ba wëëk ceec;
eni ni wø koor ïïni ba nanni.
4 Eni ni wø koor jø Icriel ba nanni,
ni eni bäŋ wø buti.
5 Wuuö Jwøk beeye ni wø koor
ïïni;
Wuuö Jwøk beeye na gëëŋi marï.
6 Ï ba 'näk cäŋŋi ki dïcäŋ,
ni bäŋ gïn mo raac mo tägi dëërï
ki dï wäär.
7 Wuuö Jwøk ï di koorø dhøk gïï
mo reyø bëët;
eni jwïëy moï di koorø.
8 Wuuö Jwøk ï di koorø kany wø
aaï wøk paarï
ki kany wø duuï paarï,
kaa man bëëde ennø, këël bäre
bäre.
&Manøgø beeye duut wääth man
wø wär ni jøw iitha thuur ni
jøw cøøa Øt Wuuö Jwøk.
@
*#Duut Mo Kwaca Jwøk Kiper Nee Jerucalem Bëëde Ki Bëët-Mëër
1 Yia atïmö ni met kanya kö jiyi ki
aani,
ni «Waa cøø Øt Wuuö Jwøk.»
2 Wui Jerucalem, wa nut ennø,
ni wa cuŋŋö dhi kiir marï.
3 Jerucalem ogeerø na pääny
mo dwala jiy na aciel,
4 ni beeye kany wø ci wïth tuŋi mo
jø Icriel yie,
ni beege wïth tuŋi mo Wuuö
Jwøk,
nee met ec dwøkge jï Wuuö
Jwøk,
ki køør ciik mana no ocaanø jïge.
5 Ni beeye kanya en wälu mar dhi
øt Deebit yie,
ni nyeya bëëdö bääte ni ŋøla luup.
6 Lämu kiper Jerucalem nee bëëde
ki bëët-mëër.
Ï na Jerucalem, jø wø mëër ki
ïïni, ge jïtö ki bëëtö mo beer.
7 Jø wø bëëdö yi kiir marï, ge jïtö
ki bëët-mëër,
ni bëët jiyi no ogwøø yi kiir marï
na teek.
8 A cädö kiper nyïïmëëga ki
nyïïawäätwa,
ni kööa, ni «Ï na Jerucalem, bëëtmëër
en jïrï.»
9 Bëënynyö marï manynya
manynyø,
kiper nee Øt Wuuö Jwøk, Jwøk
marø, nee bëëde.
&Manøgø beeye duut Deebit, ni beeye
duut wääth man wø wär ni jøw iitha
thuur ni jøw cøøa Øt Wuuö Jwøk.
@
*#Duut Mo Kwaca Wuuö Jwøk Kiper Mëër Mare
1 Ïïni ni wø bëëdö maal,
nyeŋŋa ataa maal baŋï.
2 Kaawat man wø ö jø tïïci wø
neetge cer kwäärö marge,
kaawat man wø ö dhaaŋ tïïci wø
neet cer nyijø wø tïnynye,
waani thuwø, wa neeta jïrï, ï na
Wuuö Jwøk, Jwøk marwa,
këël mano nyoothï mëër marï jïwa.
3 Nyooth mëër marï jïwa, wui Wuuö
Jwøk, nyooth mëër marï jïwa,
kiper ajøøŋ mar jiy atïmö ni päl
bäätwa.
4 Waano ööl døc ka abuua mar
jøøa no ojäŋ,
ka ajøøŋ mar jø atöör.
&Manøgø beeye duut wääth man
wø wär ni jøw iitha thuur ni
jøw cøøa Øt Wuuö Jwøk.
@
*#Duut Mo Pwøca Jwøk Kiper Na Piem Jiye Ceŋ Nyïïmän
1 Doo na paa Wuuö Jwøk na en kurø,
u jø Icriel, u doo köö na ennø,
2 ni «Doo na paa Wuuö Jwøk na en
kurø,
kar kaace jøøa määnynyö baŋø,
3 na näk yïthge oliel kaamar maac
ki øøni,
ø dige løønyø ni ø nëënö.
4 Kar kaace ø doo tïmö kaamar jiy
mo okøøl jwïïe,
ni di wïthø dïdö kaamar jiy mo
omwøny naammi,
5 ni døø tïmö kaamar jiy mo okøøl
odhänynyi.»
6 Pwøc en jï Wuuö Jwøk,
na kär ø wëëk geni nee ø jeecge
ki lakge.
7 Øøna päär wøk ceŋge kaamar
wenyø mo pär wøk ka ya abïëp
mo ocek ŋat dwaarri;
abïëp atoor, ni päärø wøk.
8 Køny marø wø käla baŋ
Wuuö Jwøk,
eni na cwääc maal ki piny.
&Manøgø beeye duut Deebit, ni beeye
duut wääth man wø wär ni jøw iitha
thuur ni jøw cøøa Øt Wuuö Jwøk.
@
*#Duut Mo Cäänö Kaper Man Wø Ö Jwøki Wø Gwøk Jiye
1 Jø wø bëëdö ni cwïnyge ege gum
Wuuö Jwøk, ge bëëdö ni ge
caala Kïn Dhayan,
ni wø bëëdö kare na bäre bäre ni
ba dak.
2 Kaawat man bëët kïte ni
Jerucalem ege ciel dïër en,
Wuuö Jwøk jiye ee ciel dïër,
kaa man bëëde ennø, këël bäre
bäre.
3 Akwöma mo ena ceŋ jøøa reyø
ba ruu yïth ŋøøpa cïp Wuuö
Jwøki jï jøøa beyø,
kiper nee jøøa beyø tïïe mo reyø
ba kwanyge.
4 Wui Wuuö Jwøk, tïïï ki gïn mo
beer jï jøøa beyø,
jø wø bëëdö ni cwïnyge thïïŋ.
5 'Ba jø wø gaa uutjïëthe moa reyø,
geno riem Wuuö Jwøki wøk na
aciel ki jø wø tïïc gïïa reyø.
Bëët-mëër oen bäät jø Icriel.
&Manøgø beeye duut wääth man
wø wär ni jøw iitha thuur ni
jøw cøøa Øt Wuuö Jwøk.
@
*#Duut Mo Pwøca Jwøk Kiper Mana Dwøk Jiye Poge
1 Kanya ö Wuuö Jwøki na duu jø
Dhayan  moa no omaaø ki tøŋ,
waana tïmö kede marwa lääk.
2 Kar kaace waana ŋeethø ki
ŋeethø mo dwøŋ døc,
ni kwöŋwa ki met ec.
'Ba kar kaace wïth juurre aköö,
ni «Wuuö Jwøk atïïö ki gïn mo
dwøŋ kiper jø Dhayan.»
3 Wuuö Jwøk atïïö ki gïn mo dwøŋ
kiperwa møn,
ni tïm yïthwa ni met.
4 Wui Wuuö Jwøk, cäŋ bëëtö
marwa dwøk kare,
kaawat man wø ö køthi wø pääŋ
yïth näpa no otal.
5 Jø wø pïïdhö ni pï nyeŋge øya
piny,
geno kääö ni yïthge met.
6 Ŋat wø ci wøk baŋ pïïdhö ni jwöŋö
ni käära köödhi mo piidhe,
oduu paayø ni yie met, ni käära
ŋaaŋe.
&Manøgø beeye duut wääth man
wø wär ni jøw iitha thuur ni
jøw cøøa Øt Wuuö Jwøk.
@
*#Duut Mo Cäänö Kaper Jammi Moa Beyø Mo Wø Cïp Wuuö Jwøki
1 Ni näk mo øtø ba geera Wuuö
Jwøki,
jø geer ööla dëëtge jaak;
ni näk mo pääny ba koora Wuuö
Jwøki,
ŋat koor ööla dëëre jaak.
2 U këël dou mööla wøk ka
amöölla cøøn,
ni tïïu këël dhöör wäär kiper nou
jïtu ki jammi,
u ööla rou jaak,
kiper Wuuö Jwøk jø wø mëëre ki
geni wø di mooø ki niine.
3 Ka adïëri møn, Wuuö Jwøk bee
eni ni wø mooc jiy ko obwöre,
mo nywøl ka ec, ni cïbe na
gwïëth.
4 Obwöre mo wø nywøl dhaanhe
ni eni poot thiinh laara
kunynyö dëëre,
ni caala athëëre mo ena cer ŋat
leny.
5 Meta yi ŋat mo jïre da obwöre
mo thööth.
Teeŋ ŋatøgø nø, eni ba bööti
kany wø cääne ki nyïïmän moe
kar løøk.
&Manøgø beeye duut Cølöman, ni beeye
duut wääth man wø wär ni jøw iitha
thuur ni jøw cøøa Øt Wuuö Jwøk.
@
*#Duut Mo Cäänö Kaper Gwïëth Man Wø Joot Ŋat Wø Bëëdö Ni Lwäära Wuuö Jwøk
1 Gwïëth en jï jiy bëët mo wø
bëëdö ni ge lwäära Wuuö
Jwøk,
ni beege jø wø caath jööre.
2 Ki køør tïïc mano tïïyï, ïïno jïti ki
cam,
ni mïn yiï, ni tïm bëëtö marï ni
beer.
3 Cïïï otïmö kaamar jaath mo
duunnö ki nyïëdi paarï,
ni tïm obwöre moï ni thööth ya
akaaŋ.
4 Ka adïëri møn, manøgø beeye
gwïëth,
beeye gwïëth man wø joot ŋat wø
bëëdö ni lwäära Wuuö Jwøk.
5 Wuuö Jwøk ïïno gwïëdhe ki yi
Dhayan,
ni jootï bëëny Dhayan, eni na
Jerucalem, ki yïth nïr kwøw
moï bëët.
6 Obwöre moo nywøl nyïïï jootï
joodø.
Bëët-mëër oen bäät jø Icriel.
&Manøgø beeye duut wääth man
wø wär ni jøw iitha thuur ni
jøw cøøa Øt Wuuö Jwøk.
@
*#Duut Mo Kwaca Jwøk Nee Jø Wø Män Ki Dhayan Raanynyi
1 Ø jø Icriel, ø doo köö na ennø,
ni «Øøna caanni døc ki mana täk
paaci cøøn.»
2 Ka adïëri møn, øøna caanni døc
ki mana täk paaci cøøn,
'ba ø kär böötö.
3 Øøna tïmö kaamar jiy mo
opwödö,
mo dïŋäthge ocöötö, kaamar
pwödhö mo okwuö.
4 'Ba Wuuö Jwøk beer;
øøna päde ceŋ jøøa reyø.
5 Jø wø män ki Dhayan,
beerra man døøge ŋäthge ni
wïthge olääö.
6 Beerra man tïmge ni caala luum
mo otuy wïth uudi,
ni wø laar talø ni poot kär
døøŋŋø;
7 ni wø ba løny ki nyaar,
ni wø ba twöc na wïc.
8 'Ba jø wø cør buutge, kär nee ge
köö,
ni «Gwïëth Wuuö Jwøk en bäätu.»
Ni ba köge thuwø, ni «Wa gwïëtha
uuni ki nyeŋ Wuuö Jwøk.»
&Manøgø beeye duut wääth man
wø wär ni jøw iitha thuur ni
jøw cøøa Øt Wuuö Jwøk.
@
*#Duut Mo Ŋäätha Wuuö Jwøk Kiper Køny Mare
1 Wui Wuuö Jwøk, a kwaya ïïni,
kiper a ena yïth gïï mo leth døc.
2 Wui Wuuö Jwøk, wïny dwøra,
ni cegï ïthï ki kwac mara.
3 ?Wui Wuuö Jwøk, doo na ï bëëdö
niï kwara gïïa näk obøth,
aŋa na doo maar cuŋŋö nyïmï ni
ree bäŋ ajäla?
4 'Ba ï wø bëëdö niï wëënna jiy,
kiper nee bëëtge ni ge wøøra ïïni.
5 A bëëdö naa koora Wuuö Jwøk ki
cwïnya bäre,
ni luumme yaa ŋäädhö.
6 A bëëdö naa koora Wuuö Jwøk ki
cwïnya bäre,
ni kaala man wø ö jø koorri wø
manyge øw nee laar ruuö;
adïëri møn, dïkuye moøgø yaa
kaalø ki koor.
7 'Ba u na jø Icriel, bëëdu nou
ŋäätha Wuuö Jwøk,
kiper mëër mo ba jøøl joota baŋ
Wuuö Jwøk,
ni køny mo dwøŋ ena baŋe.
8 Eni jø Icriel owïïl wøk
yïth gïïa bacge bëët.
&Manøgø beeye duut wääth man
wø wär ni jøw iitha thuur ni
jøw cøøa Øt Wuuö Jwøk.
@
*#Duut Ŋat Mo Ŋäätha Wuuö Jwøk Ni Cwïnye Ee Cïp Piny
1 Wui Wuuö Jwøk, bäŋ atöör
cwïnya,
ni jiy kära raŋ piny;
ni aani, wïïa kära kierø ki tïï gïï
mo døøŋŋø mo teek
mo kaala acaara mara.
2 'Ba cwïnya yaa cïp piny ni aano
nikïïl,
naa caala nyilaal mo omänö ki
caak,
mo bëëdö kö menni ni cwïnye ee
cïp piny.
3 Wui, u na jø Icriel, bëëdu nou
ŋäätha Wuuö Jwøk,
kaa man bëëde ennø, këël bäre
bäre.
&Manøgø beeye duut Deebit, ni beeye
duut wääth man wø wär ni jøw iitha
thuur ni jøw cøøa Øt Wuuö Jwøk.
@
*#Duut Mo Cäänö Kaper Leth Per Dhayan
1 Wui Wuuö Jwøk, kär wïïï wïl ki
Deebit,
ki gïïa leth bëët na pïï dëëre,
2 ki gïna kööŋe ki gø jïrï, ï na
Wuuö Jwøk,
ï na Jwø Jeekap na teek, na
kööe,
3 na «A ba døny yi øtø mara,
naa ba ci kar niine mara;
4 nyeŋŋa ba wëëga niine,
ni ba nanna,
5 këël mano jïta ki kar bëëtö jï
Wuuö Jwøk,
eni na Jwø Jeekap na teek.»
6 Ka adïëri møn, acanduk mar
Wuuö Jwøk gïr gø awïny
kwäyø ni ge ena Eeparata,
ni jootge gø yi ŋööm jø Kiriat-
Jeerim, ni kälge gø Jerucalem.
7 'Ba ennø, beerra man cøø kar
bëëtö mare, eni na Wuuö Jwøk,
ni wøørø eni kanya näk køøm
tiete.
8 Wui Wuuö Jwøk, ö maal ni ciï
kar bëëtö marï,
ïïni, ka acanduk ni wø nyooth
teek marï.
9 Beerra man ö dïlämme moï ni
røøge bëënynyö dëëtge,
ni ö jiyï mo wø cwïnyge en køørï
ni kwöŋge ki met ec.
10 Wui Wuuö Jwøk, ki køør luumma
caanï jï dhaanhnhï ma Deebit,
kär täärnyïmï kanï ki nyeya
mana røønyï.
11 Ïïna kööŋ jï Deebit ki kööŋ ma adïëri,
miï ba døø ŋääï ki gø, na kööï,
ni «Nyec ocïba jï ŋat mo käla dëërï.
12 Ni näk jøw okäl dëërï luumma
tuuda gwøkge gwøø,
ki ciik 'moa moo pwönynya geni ki ge,
jøw okäl dëëtge thuwø nyec cøøa
jïge na bäre bäre.»
13 Wuuö Jwøk Dhayan ee jierø;
ni eni manynya gø na kar bëëtö
mare, ni kööe,
14 ni «Man beeye kar bëëtö mara na
bäre bäre;
a bëëdö kany, kiper a manynya gø.
15 Dhayan gwïëdha gwïëdhö ni tïm
cammi ni päl yie,
ni wëëga jøøa can moa en yie jäŋö.
16 Dïlämme moe owëëga ŋäc pïëm
man wø piem jiy ki gø,
ni ö jiye mo wø cwïnyge en
køøra ni kwöŋge ki met ec.
17 Kaace a röönyö ki dhaanhø mo
teek mo käla ri Deebit,
aani, a tïŋŋa maal ki nyikwaare
mo bëëdö na bäre bäre.
18 Nyïïmän moe lään wïc orøøa
dëëtge kaamar abïï,
'ba eni, aduda mare obëëdö ni paŋŋi.»
&Manøgø beeye duut wääth man
wø wär ni jøw iitha thuur ni
jøw cøøa Øt Wuuö Jwøk.
@
*#Duut Mo Cäänö Kaper Man Bëët Nyïïmëëe Ki Cwïny Aciel
1 Ka adïëri møn, beeye gïn mo
beer mo duunnö ki met ec ki man bëët nyïïmëëe ki cwïny
aciel.
2 Ni teeŋ gïnögø caala maar rööny
mana pere leth na thii wï
Aran,
na øc piny ki bäät jïëc dhee,
na tøøn bäät abïï mare.
3 Ni teeŋ gïnögø caala man ö
thööyi moa thööth na en bäät
Kïn Armön
ni joodi bäät Kïn Dhayan.
Kiper Wuuö Jwøk gwëëdhö ka
kaace,
ni gwïëth manøgø beeye kwøw
mo bëëdö na bäre bäre.
&Manøgø beeye duut Deebit, ni beeye
duut wääth man wø wär ni jøw iitha
thuur ni jøw cøøa Øt Wuuö Jwøk.
@
*#Duut Mo Köömma Jiy Nee Wuuö Jwøk Pwøcge
1 Uuni bëët ni wø tïny Wuuö Jwøk,
ni wø tïny Wuuö Jwøk ki wäär yi
øtø mare,
ööu ni pwøyu Wuuö Jwøk.
2 Thaaŋu ceŋŋu maal yi øtø mare
na en kur keere,
ni pwøyu eni na Wuuö Jwøk.
3 Wuuö Jwøk uuno gwïëdhe ki yi
Dhayan,
eni na cwääc maal ki piny.
&Manøgø beeye duut wääth man
wø wär ni jøw iitha thuur ni
jøw cøøa Øt Wuuö Jwøk.
@
*#Duut Mo Pwøca Wuuö Jwøk Kiper Tïïe Moe Na Døøŋŋø
1 Alëluya, pwøc en jï Wuuö Jwøk.
Pwøyu nyeŋ Wuuö Jwøk;
pwøyu eni, u na jic Wuuö Jwøk,
2 uuni ni en Øt Wuuö Jwøk,
ni en dï kal mare, eni na Jwøk
marø.
3 Pwøyu Wuuö Jwøk, kiper Wuuö
Jwøk beer,
pwøyu nyeŋŋe ki dudi, kiper
beeye gïn mo mïërö.
4 Kiper Wuuö Jwøk nyïïkwaac
Jeekap ee jierø kiper dëëre,
ni beege jø Icriel na näk thööge.
5 Aani ŋääa ni Wuuö Jwøk dwøŋ,
ni eni na Jwøk marø kaala juu
bëët.
6 Wuuö Jwøk gïn wø met yie ki gø
di tïïö maalø ki piny,
ki yïth näpa døøŋŋø ki yïth kudi
bëët.
7 Maal wø mooe mooø ki pøøl bäät
piny bäre;
ni tïïc køth nee pädhe ni mal,
ni wëëk jamø kwön wøk ki yi
kany wø kan gø yi gø.
8 Eni kaai moa nywøl Ijep bëët
anääe,
ni beege jiy ki lääc paac bëët.
9 Ena tïïö ki nyuuthe ki gïï mo
rëëma ec dï Ijep,
ni tïïe bäät Peerø ki jiye bëët.
10 Eni tiet mïëri mo thööth
araanynye,
ni 'näk nyeye moa teek,
11 ni beege Cëëwön nyeny jø Amör,
ki Ög nyeny Baacan,
ki nyeye mo mïëc Keenan bëët;
12 ni cïp ŋøøm moge jï jiye ma jø
Icriel
nee tïmge na moge.
13 Wui Wuuö Jwøk, nyeŋŋï bëëdö
na bäre bäre,
ni bëëdï niï ŋäc ki yïth beenhnhe
bëët, ï na Wuuö Jwøk.
14 Wuuö Jwøk jiye di ŋunnö,
ni eni cwïnye wø pädhö ki gïrge.
15 Gïï wø lam wïth juurre wø tïïc ka
warkey ki gwel-bïrö,
ni beege gïï mo tïïya jiyi ki
ceŋge.
16 Gïïögø jïge da dhøgi, 'ba ge ba
luubö;
ni jïge da nyeŋŋi, 'ba ge ba
nëënö.
17 Jïge da ïdhi, 'ba ge ba wïnyö;
ni ge ba jwïëy.
18 Jøøa tïïc geni otïmö ni bäŋ teek
jïge ni caala geni,
këël jøw bëët mo wø ŋääth geni.
19 Wui, u na jø Icriel, pwøyu Wuuö
Jwøk.
Wui, u na jø dhi øt Aran, 
pwøyu Wuuö Jwøk.
20 Wui, u na jø dhi øt Libay, 
pwøyu Wuuö Jwøk.
Uuni ni wø lwäär ki Wuuö Jwøk,
pwøyu Wuuö Jwøk.
21 Pwøyu Wuuö Jwøk Dhayan,
ni beeye Jerucalem na näk kar
bëëtö mare.
Alëluya, pwøc en jï Wuuö Jwøk.
@
*#Duut Mo Pwøca Wuuö Jwøk Kiper Mëër Mare
1 Dwøgu met ec jï Wuuö Jwøk,
kiper eni beer,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre.
2 Dwøgu met ec jï Jwøk, eni na
wïth juu bëët,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre.
3 Dwøgu met ec jïre, eni na kwääc
kwääri bëët,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre.
4 Pwøyu eni, kiper bee eni keere ni
wø tïïc gïï mo rëëma ec,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre.
5 Pwøyu eni na cwääc maal ki
køør leec wïïe,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre.
6 Pwøyu eni na cwää piny bäät pïï,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre.
7 Pwøyu eni na cwääc gïïa døøŋŋø
ni wø cïpi ki tar,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre;
8 Cäŋ acïbe nee rienye ki waŋcäŋ,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre;
9 ni cïp dwääy ki ceer nee rienyge
ki wäär,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre.
10 Pwøyu eni na dïïr wïth kaai mo
jø Ijep,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre.
11 Eni jø Icriel akäl wøk ki dï jø Ijep,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre;
12 ni ge käl wøk ka køør teek bade
na dwøŋ,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre.
13 Pwøyu eni na pääŋ pï Naama
Kwaar ki dïëre,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre;
14 ni tïïc jø Icriel nee pööthge ki
dïëre,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre;
15 'ba Peerø ki jø leny moe aleeŋ yi
Naama Kwaar,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre.
16 Pwøyu eni na bwøth jiye ki dï
paap,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre.
17 Pwøyu eni na dïïr wïth nyeye
moa døøŋŋø,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre.
18 Eni nyeye moa teek anääe,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre;
19 ni beeye Cëëwön nyeny jø Amör,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre;
20 ki Ög nyeny Baacan,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre;
21 ni cïp ŋøøm moge jï jiye nee
tïmge na moge,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre;
22 ni put ŋøøpøgø dööŋŋe jïge, ge
na jø Icriel,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre.
23 Bee eni na cädö kiperø kanya
bëëdø ni øøno dwøk piny,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre.
24 Ni bee eni na käl øøni wøk ceŋ
nyïïmän moø,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre.
25 Eni cam wø cïbe cïbö jï gïïa
kwøw bëët,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre.
26 Dwøgu met ec jï Jwø maal,
kiper mëër mare ni wø ba jøøl
bëëdö na bäre bäre.
@
*#Duut Mo Cäänö Kaper Bëët Jø Icriel Moa Mak Ki Tøŋ
1 Waana pï piny bäät näp Babiløn
ni jwöŋwa kanya caarwa gïr
Dhayan.
2 Thøme mowa alïërwa maal røk
jenni paanøgø.
3 Kiper jøøa mak waani ki tøŋ, ge
manynya man wärwa ki dudi
jïge kaace,
ni ö geni na caan waani ni
manyge dut met ec baŋwa, ni
köge,
ni «Wärru jïwa ki duut pou ma
Dhayan.»
4 ?Aŋø, duut mar Wuuö Jwøk
owärwa gø nidïï
ni wa ena po juurre?
5 Wui, ï na Jerucalem, ni näk mo
wïïa owïl ki ïïni,
wär cer cwïïa bäbe.
6 Wui, ï na Jerucalem, ni näk mo
aano tïmö naa ba lääŋ ïïni,
ni ba guma ïïni cwïnya ni kaala
jap wø met yia ki ge bëët,
leeba wär tal maal.
7 Wui Wuuö Jwøk, par wïïï ki gïna
tïïc jø Ëdömmi
dïcäŋa päth Jerucalemmi;
kiper gena kwöŋŋö ni köge, ni
«Nyaau paanøgø piny, nyaau
paanøgø piny,
këël mano ränynye na bäre
bäre.»
8 U na jø Babiløn, u ni wø räänyö,
gwïëth en jï ŋato cool kwör
dëëtu,
noo tïïö dëëtu ki teeŋ gïna tïïyu
dëëtwa.
9 Gwïëth en jï ŋato jaaŋ obwöre
mou moa therø,
ni gøc geni ki ri kïte.
@
*#Duut Mo Pwøca Wuuö Jwøk Kiper Gïïa Beyø Na Tïïe
1 Wui Wuuö Jwøk, met ec duua
duuö jïrï ki cwïnya bäre,
ni wära ki dut pwøc jïrï nyïm juu
mo juurre.
2 Cøŋŋa këëlla piny ni nyïma yaa
løø baŋ øtø marï na en kur
keere,
ni pwøa nyeŋŋï kiper mëër marï
ni wø ba jøøl ka adïëri marï;
kiper nyeŋŋï ki luummï atïŋï
maal bäät jammi bëët.
3 Dïcäŋa kwaa ïïni, mara aløgï jïra,
ni mooyï aani ki teek ni jït
cwïnya ki cer.
4 Wui Wuuö Jwøk, nyeye mo bäät
piny bëët met ec duuge duuö
jïrï,
ki køør mano wïnyge luummo
caanï ki dhiï,
5 ni wärge ki dudi kiper gïïa tïïyï, ï
na Wuuö Jwøk,
kiper ajiem marï dwøŋ.
6 Këël na bëët Wuuö Jwøki ni kare
dwøŋ,
eni poot bëëdö ni raŋŋa jøøa
kwörge bäŋgø;
'ba mar jø atöör ŋääe këël na
bëëtge ni kwörge bäyö.
7 Këël a doo bëëdö naa ena yïth gïï
mo leth,
jwïëya poot gwøgï gwøø;
cerï wø rwieyï rwieø ni joogï
wëër mar nyïïmänna,
ni piemï aani ki teek badï.
8 Wuuö Jwøk gïïo manynye kipera
tïïe tïïö ni thurge karge.
Wui Wuuö Jwøk, mëër marï ni
wø ba jøøl bëëdö na bäre bäre;
Wui Wuuö Jwøk, kär gïna tägï ki
tïïc wiiï piny.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Nyootha Gø Ni Jwøk Beeye Ni Ŋäc Cwïny Dhaanhø Bäre
1 Wui Wuuö Jwøk, cwïnya adarï ni
ŋäyï bëëtö mara.
2 Pïïnna piny ki öönynya maal ŋäyï,
na acaara mara ŋäyï kany wø
poode ni poot kär tägö.
3 Wääth mara ki nyaaŋ dëëra piny
wø neetï neetø,
ni jöör bëëtö mara bäre ŋäyï.
4 Wui Wuuö Jwøk, këël kany wø
poode ni luubö poot kär tuny
wøk ki dhaa,
luummögø ŋäyï na bäre.
5 A iï ciel dïër,
ni cerï iï peeth bääta.
6 Teeŋ ŋäc mana ŋäyï aani, yia
rëëm ki gø;
ni tiere teek døc, ni ba løny jïra
ki man kwanya gø.
7 ?Aŋø, a kaa ŋø nø noo cøøa yie
ni jwïëy moï tøør yie?
?Naa kaa nø noo reŋŋa yie naa
ŋwieya ïïni?
8 Ni näk maa cøøa maal, ï nut yie.
Ni näk maa cøøa kar bëët jwïëc
jøøa no othøw,
ï poot nut kaace thuwø.
9 Këël a doo määtö kaamar wenyø
naa tägi ka jï løø kur tuul-cäŋ,
naa cøøa jï kur pänh-cäŋ,
10 a poot bwøthï bwødhø kaace,
ni jølï aani ki teek marï.
11 Ni näk maa köö, na «A gëëŋ
muudhe gëëŋö,
ni tïm tarri mana en buuta na
muudhö,»
12 ki baŋï muudhö ba cøl,
ni wäär tar ni caala waŋcäŋ,
kiper muudhö ki tar bëët röömi
ki baŋï.
13 Wui Wuuö Jwøk, thäk dëëra bëët
tïïya ïïni,
ni cwääyï aani ni tïma ni aana
dhaanhø yi mera.
14 Ï pwøa pwøø, kiper aana cwääc
ki cwääc mo rëëma ec
miï di lwäärö ki køøre.
Tïïe moï thääŋa ec møn,
ni beeye gïna ŋääa døc na adïëri.
15 Kanya cwääc aani yi mera kany
mo kuc,
ni cwääc aani ki cwääc mo beer,
cuu dëëra nëënö jïrï, ni patha
okanø ki ïïni,
16 naa nëënö jïrï kanya pooda naa
poot kär tïmö ni aana dhaanhø;
ni ö nïne moa no okwaanø kipera
bëët
ni gööri piny yi wëëlö marï,
kanya pootge ni ge poot kär tägö.
17 Wui Jwøk, acaare moï perge leth
jïra,
ni kwäänge thööth døc;
18 ni näk mo kwaana kwaanø,
kwäänge tïmö ni kaala nyeŋ
akwöö.
Kany wø pääa, a poot bëëdö ka
ïïni.
19 Wui Jwøk, ni näk mo jøøa reyø
'nägï nääö, doo beer.
U na jø wø many rem jiy, daagu
rou buuta.
20 Wui Jwøk, nyïïmännï cäänö
dëërï ki gïï mo reyø,
ni ge raanynya nyeŋŋï ki gïn mo
bäŋ tiere.
21 ?Wui Wuuö Jwøk, aŋø, jøøa män
ki ïïni, a kär männö ki geni
thuwø?
?A kär bëëdö naa ba many dëët
jøøa thïïŋ dëëtge kiperï?
22 Aana männö ki geni na bäre
bäre,
ni tïmge na nyïïmän 'moa.
23 Wui Jwøk, dar yia ni ŋäyï mar
cwïnya;
pääny aani ni jootï gïï wø pär
cwïnya ki ge;
24 ni näk da gïn mo kännö ki pänh
cwïny jïrï ri bëëtö mara, neenï,
ni putï bëëtö na bäre bäre naa
bwøthï ki jöö mo beer.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Kwaca Wuuö Jwøk Nee Dhaanhnhe Gwøe Ceŋ Jøøa Reyø
1 Wui Wuuö Jwøk, käl aani wøk
ceŋ jøøa reyø,
ni gwøgï aani ceŋ jø kwöri,
2 jø wø caar tïï gïï mo reyø ki
cwïnyge,
ni ge bëëdö ni ge cøønna yïth jiy
kiper leny.
3 Lëëpge ege tïïö ni beth kaamar
leep thwöl,
ni luup mo wø cur dhøkge caala
cïm mar olwierø.
4 Wui Wuuö Jwøk, gwøk aani ceŋ
jøøa reyø,
ni gwøgï aani ceŋ jø kwöri,
jø wø määnyö ki jöö ki man
raanyge aani ki gø.
5 Jø atöör abïëp ege ciiø kipera,
ni cekge thøøli øtjööra,
ni cekge akupe kipera.
6 Aana lämö jï Wuuö Jwøk ni kööa,
ni «Beeye ïïni na Jwøk mara;
Wui Wuuö Jwøk, cek ïthï ki kwac
mara.
7 Wui Wuuö Jwøk, ï na kwäärö
mara, ï na teek ni wø piem
aani, aana gëëŋï dïcäŋ leny.
8 Wui Wuuö Jwøk, gïïa many jø
raayi kär tïïyï jïge,
ni ba wëëgï gïïa tuutge thur kare,
nee wïthge ba tïŋge maal.
9 «Jø wø ciel aani dïër,
beerra man ö luup mo wø carge
ki lëëpge ni døøge wïthge.
10 Beerra man päth cuki mo wärri
bäätge;
ni leeŋ geni yi maac,
ni leeŋ geni yïth buri mo bäyö,
nee ge ba duuge wøk këët.
11 Kär dee dïwääc nyeŋ mo jïti ki
kare dï paac;
beerra man ö gïïa reyø ni dwarge
jø kwöri.»
12 Ŋääa ni Wuuö Jwøk cwaga jøøa
no ocaannø,
ni luup jøøa can ŋøle na karge.
13 Wui Wuuö Jwøk, ka adïëri møn,
jøøa beyø nyeŋŋï pwøcge
pwøø,
ni ö geni na cwïnyge thïïŋ ni
bëëtge ki ïïni na aciel.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Kwaca Wuuö Jwøk Nee Dhaanhnhe Gwøe
1 Wui Wuuö Jwøk, a kwaya ïïni;
laar rwänh baŋa!
Cek ïthï ki kwac mara.
2 Beerra man ö lammi mara ni pïïe
baŋï kaamar jïrö mar gïn wø
waaŋ ni wø ŋwääi ni met,
ni ö thaaŋ cenø man wø thaaŋa
ceŋŋa baŋï ki gø
ni jïëyï gø kaamar olämi man wø
cïp ka abøøya.
3 Wui Wuuö Jwøk, gwøk dhaa,
ni koorï luup mo wø cur yie.
4 Kär cwïnya wëëk ciin køør raay,
naa ba tïma naa tïïya gïï mo
reyø,
ni ba dwäta ki jø wø tïïc gïïögø,
ni ba cämwa ki geni kany wø
wøørge juu moge.
5 Beerra man ö ŋata beerri ni pwöt
aani ni mare pwöc ki køør
mëër mare,
'ba kär wïïa wïïr ki maaw mar
jøøa reyø,
kiper a poot lämö nee gïï wø
tïïcge na reyø nee ränyge.
6 Kanyo leeŋ kwääri moge piny ki
bäät kïte,
nyeŋ jøøa reyø bany ni putge gø
ŋäc ni luumma met.
7 Cuu moge okeethi dhøk kääk,
kaamar jenni mo opetø piny.
8 Wui Wuuö Jwøk, ï na kwäärö
mara, a poot neeta jïrï;
raa yaa kan buutï; kär jwïëya
wëëk ränynyö.
9 Gwøk aani naa ba pätha ya
abïëp mana no ocek jøøa reyø
kipera,
ni mänï aani ki ciin ya akupa
marge.
10 Beerra man ö jøøa reyø ni magi
ya thøøli moa cekge,
ni pöödha ni bäŋ gïn mo tägi
dëëra.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Kwaca Wuuö Jwøk Nee Dhaanhnhe Kønye Yïth Gïï Mo Leth
1 A jwöŋö dëër Wuuö Jwøk,
ni kwaaya eni ni dwøra yaa tïŋ
maal.
2 Ni gwäära yia wøk bäre jïre,
naa cara gïïa näk aano ööl ki
geni jïre.
3 Kany wø bëëda ni bääta opädhö,
gïn tïïa ŋäya ïïni.
Jöö man wø cäädha ki yie,
ocïŋ jiyi ka abïëp.
4 Kanya raŋa bäät cwïïa ni neena
gø døøc,
bäŋ dhaanhø mo caar gïra,
ni bäŋ kany kana raa yie,
ni bäŋ ŋat cädö kiper jwïëya.
5 Wui Wuuö Jwøk, a jwöŋö dëërï,
naa köö, ni «Beeye ïïni ni wø
kana raa buute,
ni beeye ï keerï na kura bäät
pinyi en.
6 Cek ïthï ko oduuru mara,
kiper aano dwøk piny døc.
Käl aani wøk ceŋ jø wø caan aani,
kiper ge teek døc ni kaala aani.
7 Käl aani wøk ki yïth gïïa twöc
aani,
kiper nee nyeŋŋï pwøa.
Køøre jøøa beyø oööi ni cooŋge
rege buuta
kiper gïïa beyø na tïïyï kipera.»
&Manøgø beeye duut Deebit mana
caae kanya kan ree øt kïdi.
@
*#Duut Mo Kwaca Wuuö Jwøk Nee Dhaanhnhe Kønye Nee Bwødhe Ki Jööre
1 Wui Wuuö Jwøk, wïny lam mara,
ni cegï ïthï ki kwac mara,
ni løgï mara ki køør beenynyï ka
adïëri marï.
2 Kärï kän bääta ka ajäla, a na
dhaanhnhï,
kiper bäŋ dhaanhø mo mare beer
nyïmï.
3 Kiper nyïïmänna aana caange,
ni raanyge aani,
ni wëëkge aani bëëtö yi muudhö
kaamar jiy moa thøw cøøn.
4 Kiper manøgønø, bääta apädhö,
ni ö yia ni neethay.
5 'Ba ennø, a caara gïr nïne moa cääŋŋe,
naa cädö bäät tïïe moï bëët,
naa caara gïïa tïïyï bëët ki cerï.
6 Ceŋŋa wø thaaŋa maal baŋï,
ni bëëda naa lääŋŋa ïïni kaawat man wø
ö ŋøømmi mo otal wø manyge pïï.
7 Wui Wuuö Jwøk, laar mara løk,
kiper bääta opädhö.
Kär täärnyïmï kanï ki aani,
naa ba tïma kaamar jø wø koony
yi bwörö.
8 Beerra man wëëgï aani wïny
luum mëër marï ni wø ba jøøl
kany wø pääa ka amöölla,
kiper a bëëdö niï yaa gum cwïnya.
Pwöny aani ki jöör bëëtö mana
daa bëëdö ki gø,
kiper acaara mara bäre ena baŋï.
9 Wui Wuuö Jwøk, käl aani wøk
ceŋ nyïïmänna,
kiper raa yaa kan buutï.
10 Pwöny aani naa bëëda naa tïïya
mana manynyï,
kiper beeye ïïni na Jwøk mara.
Beerra man ö jwïëyï na beyø ni
bwøthge aani ki jöö mo beer.
11 Wui Wuuö Jwøk, cäŋ a mooyø ki
kwøw ki køør nyeŋŋï,
ni kälï aani wøk yïth gïïa leth ki
køør beenynyï.
12 Raany nyïïmänna ki køør mëër
marï ni wø ba jøøl,
ni dïïrï wïth jø wø caan aani,
kiper aana dhaanhnhï.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Cäänö Kaper Køny Ki Bëëtö Mo Beer Man Wø Cïp Jwøki
1 Pwøc en jï Wuuö Jwøk, eni na
teek mara, eni ni wø pwöny aani ki leny,
ni wø døøc ceŋŋa mo teek naa
këëda.
2 Bee eni ni wø mëër ki aani ki
mëër mo ba jøøl,
ni bee eni na kar gwøk røk jïra;
ni eni bëëdö kaamar kiir mo teek
jïra, ni ena pïëmi mara.
Bee eni na kwöt leny mara, ni
bee eni ni wø kana raa buute,
ni bee eni ni wø dïïm jiy ni tïmge
ni ge ena tiera.
3 ?Wui Wuuö Jwøk, dhaanhø
agïnaŋø, ni lääŋŋï gø en?
?Ni o dhaanhø agïnaŋø, ni cädï
kipere en?
4 Dhaanhø caala jam dhøk jaak,
ni nïr kwøw moe maayø kaamar
tïpö.
5 Wui Wuuö Jwøk, jap maal ni ööï
piny,
ni gutï kïte nee duuŋge ki jïrö.
6 Jääŋ agaackøth ni keethï
nyïïmänna,
ni thööyï ge ka athëëre moï ni
riemmï geni.
7 Rwää cerï piny ki maal,
ni piemï aani ni kälï aani wøk ki
yïth gïïa leth na caal naama
päŋ,
naa kälï wøk ka ceŋ jøøa path,
8 ni wø car cwøk,
ni wø kööŋ ki tööt.
9 Wui Wuuö Jwøk, a wär ki duut
mo nyään jïrï,
naa pöödö ki thoom mo thøøli
moe apaar.
10 Beeye ïïni ni wø wëëk nyec Icriel
käädhö,
ni beeye ïïni ni wø piem
dhaanhnhï ma Deebit.
11 Piem aani dho opëëlla raac,
ni kälï aani wøk ceŋ jøøa path,
ni wø car cwøk,
ni wø kööŋ ki tööt.
12 Beerra man ö wäätwa, kany wø
pootge ni ge poot therø,
ni døøŋge kaamar jaath mo
oløth;
ni tïm nyïïwa ni mïërö ni rege
ege kørø,
ni caala jer gøøt mo øt nyeya.
13 Beerra man ö odïï mowa ni päŋge
ki wïth caammi ma teeŋi,
ni ö dïëki mowa ni nyöötge ni
meetge rege ni ba løny ki
kwaan dï pwöla.
14 Beerra man ö dhäki mowa ni
tïmge ni jayø bëët,
ni bäŋe gø mo bwön wøk, ni
bäŋe ya aciel mo rwäänyi.
Ni tïme ni bäŋ ŋat mo göö ko
oduuru dï paac.
15 Gwïëth en jï jø paan wø bëëdö ki
teeŋ bëëtö manøgø;
gwïëth en jï jø paan wø Jwøge
beeye Wuuö Jwøk.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Pwøca Wuuö Jwøk
1 Wui Wuuö Jwøk, ï na nyeya
mara, nyeŋŋï tïŋa maal,
ni pwøa ïïni na bäre bäre.
2 Ïïno pwøa ki yïth nïne bëët,
ni pwøa ïïni na bäre bäre.
3 Ï na Wuuö Jwøk, ï dwøŋ, ni ïïno
rømø døc ki man pwøi,
ni dööŋö marï ba løny ki man
ŋääi bäre.
4 Wui Wuuö Jwøk, beenhnhø man
nø tïïe moï opwøcge,
ni caange gø jï beenhnhø maya,
ni køpge gïr tïïe moï na døøŋŋø.
5 Ïïno wøør jiyi ni køpge ajiem
marï na dwøŋ;	
'ba aani thuwø, a wø cädö kiper
tïïe moï ni wø rëëm ec.
6 Tïïe moï na døøŋŋø ni wø thäŋ
eci ki ge ocaan jiyi;
'ba aani thuwø, dööŋö marï køba
købø.
7 Kany wø cät jiyi kiper beer marï
na dwøŋ,
gïr gø køpge købø,
ni wärge ni yïthge met kiper
adïëri marï.
8 Wuuö Jwøk yie bäth ni mëër ki
jiy;
eni ba laar wëër, ni mëër mare
päl ni ba jøøl.
9 Wuuö Jwøk täärnyïme leer ki jiy
bëët,
ni bäth ec mare wø nyoodhe
nyoodhø jï gïïa cwääe bëët.
10 Wui Wuuö Jwøk, gïïa cwääyï
bëët ï pwøcge pwøø,
ni ö jiyi moï ni wø bëëdö ni
cwïnyge ena køørï ni pwøcge
ïïni.
11 Ajiem mar bura marï køpge
købø,
ni caange gïr teek marï,
12 kiper nee tïïe moï na døøŋŋø nee
ŋäc jiyi bëët,
këël ajiem buyï na dwøŋ.
13 Bura marï bëëdö na bäre bäre,
ni ö teek nyec marï ni bëëde ni
nut yïth beenhnhe bëët.
Gïïa caan Wuuö Jwøki bëët di
ŋäädhö,
ni tïïe moe bëët wø tïïe ka køør
mëër mare ni wø ba jøøl.
14 Wuuö Jwøk jøøa näk manynya
pädhö bëët di jølø,
ni tïŋ jøøa en yïth gïïa leth maalø.
15 Wui Wuuö Jwøk, gïïa kwøw bëët
nyeŋge ena baŋï,
ni cam marge cïpï cïbö jïge
kanya näk kare.
16 Cerï wø peerï peerø jï gïïa kwøw
bëët,
ni mooyï geni ki gïn cam ni
jäŋge kaawat man wø manyge.
17 Jöör bëëtö mar Wuuö Jwøk beer
bäre,
ni tïïe moe bëët wø tïïe ka køør
mëër mare ni wø ba jøøl.
18 Wuuö Jwøk bëëdö ni kare cään
ki jø wø cøør nyeŋŋe bëët,
ni beege jø wø cøør nyeŋŋe ki
cwïny ma adïëri.
19 Jø wø lwäär ki eni, gïï wø
manyge wø cïbe cïbö jïge,
ni wïny kwac marge, ni køny
geni.
20 Wuuö Jwøk jø wø mëër ki eni
bëët di gwøø,
'ba jøøa reyø bëët raanynye
raanynyø.
21 Wuuö Jwøk pwøa pwøø cooth,
ni ö jiyi bëët ni pwøcge eni na en
kur keere na bäre bäre.
&Manøgø beeye duut Deebit.
@
*#Duut Mo Pwøca Jwøk Kiper Køny Mare
1 Alëluya, pwøc en jï Wuuö Jwøk.
Aani, Wuuö Jwøk pwøa pwøø ki
cwïnya bäre.
2 Wuuö Jwøk pwøa pwøø ki yïth
nïr kwøw 'moa bëët,
ni wära ki dut pwøc jï Jwøk mara
kany pooda naa kwøw bäät
pinyi en.
3 Käru bëëdö nou ŋäätha kwäärö,
kiper ena dhaanhø jaak mo bäŋ
gïn mo kønye rou.
4 Jwïëy moe aay, ni ö rïŋ dëëre ni
døø yi ŋöömö,
ni put acaare moe rwäänyö
dïcäŋöce.
5 Gwïëth en bäät ŋat wø køny
mare joode baŋ Wuuö Jwøk,
Jwø Jeekap,
ni wø bëëdö ni ŋäätha Wuuö
Jwøk.
6 Wuuö Jwøk beeye Jwøa cwääc
maal ki piny,
ki naama dwøŋ, këël jammi bëët
moa en yïthge.
Eni luumme bëëdö ni di ŋäädhö
na bäre bäre.
7 Eni jøøa no othiel piny di ŋunnö
ki ŋøl ma kare,
ni mooc jøøa näk dëëtge da käc
ki cam.
Wuuö Jwøk beeye wø pät jøøa
näk otwöö.
8 Wuuö Jwøk beeye wø jap nyeŋ
cööye;
Wuuö Jwøk beeye wø tïŋ jiy
maal mo wø bëëdö no opädhö;
Wuuö Jwøk bëëdö ni mëër ki jø
wø bëëdö ni marge adïëri.
9 Wuuö Jwøk beeye wø gwøk juurre
mo wø bëëdö na wëëlle paac,
ni wø køny kïïe ki määr
thuunhnhi;
'ba gïï wø tuut jøøa reyø
raanynye raanynyø.
10 Wuuö Jwøk bëëdö na wïth jammi
bëët na bäre bäre;
u na jø Dhayan,  Jwøk maru
bëëdö ni nut yïth beenhnhe
bëët.
Alëluya, pwøc en jï Wuuö Jwøk.
@
*#Duut Mo Pwøca Wuuö Jwøk Kiper Mana Dwøk Jerucalem Kare
1 Alëluya, pwøc en jï Wuuö Jwøk!
Beeye gïn mo beer ki man wärø
ki dut pwøc jï Jwøk marø,
kiper beeye gïn mo beer mo
duunnö ki met ec.
2 Wuuö Jwøk Jerucalem cäŋe ka
geerø,
ni duu jø Icriel yie moa no
omaaø ki tøŋ.
3 Eni jøøa näk cwïnyge opädhö,
cwïnyge di cømø,
ni køny jøøa no oööl.
4 Eni kwään ceer ŋääe,
ni nyeŋge ee caaø bëët.
5 Jwøk marø dwøŋ, ni teek mare
päl,
ni leec wïïe bäre ba løny joot.
6 Wuuö Jwøk cuŋŋa kur jøøa no
ocaannø,
'ba jøøa reyø dwøge piny.
7 Wärru jï Wuuö Jwøk ki duut nou
dwøga met ec,
wärru ki dut pwøc jïre, eni na
Jwøk marø, nou pöödö ki
thoom.
8 Bee eni ni wø mooc maal ki pøøl,
ni wø jääŋ køth bäät piny,
ni wø wëëk luum tuuö bäät kïte.
9 Eni lääy wø di mooø ki cam,
ni mooc nyïï agääe thuwø kany
wø jwöŋge.
10 Patha teek mar okweeny noo
døøc yi Wuuö Jwøk mo met,
ni patha teek mar dhaanhø noo
døøc yi gø mo met;
11 'ba Wuuö Jwøk yie wø mïnni ka
jø wø lwäär ki eni,
jø wø ŋääth mëër mare ni wø ba
jøøl.
12 Wui, u na jø Jerucalem, pwøyu
Wuuö Jwøk!
Pwøyu eni na Jwøk maru, u na jø
Dhayan!
13 Kiper dïdëëdi mo dhøk kiiri mou
ee tïïö ni teek, 
ni jiy mou mo oen pou ee
gwïëdhö.
14 Eni pou bäre di mooø ki
bëët-mëër,
ni caam uuni ki beel ma liil ni
jäŋŋu.
15 Eni dwøre wø di jääŋŋö piny,
ni ö luumme ni laar thur kare.
16 Rwöc wø käle piny ni rïëp piny
kaamar aleeŋŋa,
ni wëëk thööy ööny bäät piny.
17 Pey wø gwääre gwäärö kaamar
gii;
?'ba aŋa ni løny jïre ki man
cuŋŋe yi köö mare?
18 Eni luumme wø jääŋŋe jääŋŋö ni
løc peyi,
ni kööl jamø ni tïm pïïyi ni
kwödö.
19 Luup moe wø caane caanø jï
nyïïkwaac Jeekap,
ni caan ciik moe ki luup ŋøl moe
jïge, ge na jø Icriel.
20 'Ba eni luumme käre caanø jï
wïth juurre,
ni geni ciik moe kucge.
Alëluya, pwøc en jï Wuuö Jwøk!
@
*#Duut Mo Cäänö Kaper Man Pwøc Wuuö Jwøk
1 Alëluya, pwøc en jï Wuuö Jwøk.
Pwøyu Wuuö Jwøk, u ni en maal,
ni pwøyu eni ki kwöra enu
yïthge maal.
2 Pwøyu eni, u na nyïïatwiet maal
moe;
pwøyu eni, u na lwaae moe ni en
maal.
3 Cäŋ ki dwääy, pwøyu Wuuö Jwøk;
ceer bëët ni wø cïpi ki tar maal,
pwøyu Wuuö Jwøk;
4 Maal ki pøøl bëët, pwøyu Wuuö
Jwøk.
5 Beerra man ö gïïögø bëët ni
pwøcge nyeŋ Wuuö Jwøk,
kiper kanya cwääc ge, caana dwøre
jaak, ni putge thur karge.
6 Ni cïp geni kwörge nee bëëtge na
bäre bäre,
ni mooc geni ki ciik mo ba dak.
7 Pwøyu Wuuö Jwøk ki kwöra enu
yïthge bäät piny,
ni beeye u lääc naama dwøŋ, ki
kwöra päŋ bëët,
8 ka agaackøth, ki pey, ki køth, ki pøøl,
ka atuunna ni wø kwödö ki køør
ciige.
9 Beerra man ö thuuri ki kïte bëët
ni pwøcge eni,
ki jenni mo wø nyïïge cam ki jer
geer bëët,
10 ki lääc paap ki mo paac bëët,
ki gïï wø muuli ki piny ki weny bëët.
11 Pwøyu eni, u na nyec bäät piny
ki jiy bëët,
ki kwääri ki dïŋut luup mo bäät
piny bëët,
12 ki wøpe ki nyïïakuue bëët,
ki jäle ko obwöre bëët.
13 Beerra man ö gïïögø bëët ni
pwøcge Wuuö Jwøk,
kiper dwøŋŋa nyeŋŋe keere,
na ajiem mare kaala ajiem maal
ki piny.
14 Eni teek mar jiye atïïe nee bëëde
ni cäätha maal,
ni ö jiye bëët moa cwïnyge en
køøre ni jïtge ki pwøc,
ni beege jø Icriel na bëëde dïge.
Alëluya, pwøc en jï Wuuö Jwøk.
@
*#Duut Mo Cäänö Kaper Man Pwøc Wuuö Jwøk
1 Alëluya, pwøc en jï Wuuö Jwøk.
Wärru jï Wuuö Jwøk ki duut mo
nyään,
ni pwøyu eni dï acooŋ jø wø
bëëdö ni cwïnyge ena køøre.
2 Beerra man mïn yïth jø Icrielli ki
Jwøa cwääc geni,
ni ö geni na jø Dhayan ni kwöŋge
ki met ec kipere, eni na nyeya
marge.
3 Beerra man pwøcge eni ki meeŋ,
ni wärge ki dut pwøc jïre ni ge
pöödö ki thøme ka anëët.
4 Kiper Wuuö Jwøk yie wø mïnnö
ki jiye,
ni piem jøøa en yïth gïï mo leth,
ni mooc geni ka ajiem.
5 Beerra man ö jø wø bëëdö ni
cwïnyge ena køør Wuuö Jwøk
ni kanyge ni yïthge met ki køør
ajiem mana jootge,
ni wärge ki dudi ni yïthge met
kwör niine moge.
6 Beerra man pwøcge Jwøk ki
pwøc mo dwøŋ,
ni ceŋge da opëëlle mo deŋge
karge riet beth,
7 kiper nee kwöri coolge dëët wïth
juurre,
ni jäälge jøøgø ni tïïge ki gïï mo
leth dëëtge;
8 kiper nee nyeye mo jøøgø twöcge
ki tiimme,
ni twöcge kwääri moge ko
oguudi;
9 na ajäla mana no ogöörö kiper
jøøgø nee tïïcge;
ni tïm gïïögø na ajiem kiper jiye
na näk cwïnyge ena køøre.
Alëluya, pwøc en jï Wuuö Jwøk.
@
*#Duut Mo Pwøca Wuuö Jwøk
1 Alëluya, pwøc en jï Wuuö Jwøk.
Pwøyu Jwøk kar bëëtö mare na
en kur keere,
ni pwøyu eni maal kanya en
teeki mare yie.
2 Pwøyu eni kiper tïïe moa tïïe ki
køør teek mare,
ni pwøyu eni ki køør dööŋö mare
na dwøŋ døc.
3 Pwøyu eni ki dööt tuŋi,
ni pwøyu eni ki thøme ma teeŋi.
4 Pwøyu eni nou pöödö ki bulli ka
anëët nou miel,
ni pwøyu eni ki thøp-othïënhö
ko opele.
5 Pwøyu eni ka adijeege,
ni pwøyu eni ki gare.
6 Beerra man ö gïïa näk røkge da
jwïëy bëët ni pwøcge Wuuö
Jwøk.
Alëluya, pwøc en jï Wuuö Jwøk.

"""



def clean_text(text):
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    # Additional cleaning rules can be added here if necessary
    return text


def extractPDFText(pdf_path):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        result = []
        for i in range(0, len(reader.pages)):
#             selectedPage = reader.pages[i]
            text = selectedPage.extract_text()
            result.append(text)
        return ''.join(result)

def extractPDFTextWithPdfPlumber(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            result = []
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    result.append(text)
            extracted_text = ''.join(result)
            cleaned_text = ' '.join(extracted_text.split())
            return cleaned_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def split_text_into_verses(text):
    # Regular expression to match verse numbers (numbers at the beginning of lines)
    verses = re.split(r'(?<=\d)\s', text)
    # Filter out any empty strings and strip leading/trailing whitespace
    verses = [verse.strip() for verse in verses if verse.strip()]
    return verses

# check if there is a digit in a verse 
def contains_digit(word):
    return bool(re.search(r'\d', word))

def createJson(textIntro, version, introTitle, chapterName, bookList ): 

    bible_data = {
                "textIntro": textIntro,
                "introTitle": introTitle,
                "chapterName":chapterName,
                "version" : version,
                "text": bookList
                }
    bible_json = json.dumps(bible_data, ensure_ascii=False, indent = 4)
    with open('files/anyuaB_json/OT/PSA.json', 'w',encoding='utf-8') as json_file:
        json_file.write(bible_json)
    print('JSON successfully generated!!')
    


# texts = extractPDFText("files/1joon.pdf")
# texts = extractPDFTextWithPdfPlumber("files/1joon.pdf")
# verses = split_text_into_verses(texts.split("%")[1])
# print(verses)
# print(texts)
# print(metadata)

chapterName = texts.split("%")[0].split("\n")[1]
# print(texts.split("%")[0].split("\n"))
introTitle = texts.split("%")[0].split("\n")[2]
about = texts.split("%")[1].split("\n")[0]
# print(introText)
intro = texts.split("%")[0].split('\n')[3:]
intro = ' '.join(intro)
version = "anyuaB"
myid = ""
name = ""
text = ""
verseId = ""
referece = ""


bookList = []
chapterNumber = 0
# verses = texts.split("%")

# print("===============" + chapterName + "===============")

for number in range(1, len(texts.split("%")[1].split("@"))):
   textList = []
   chapterNumber +=1
#    print(texts.split("%")[1].split("@")[1:])
   currentText = texts.split("%")[1].split("@")
   
#    print(currentText)
   myText =  split_text_into_verses(currentText[number])
#    print(myText , '\n\n')
   
#    print(myText)

#  break

   for index in range(1, len(myText)):
       thereIsTitle = False
       CurrentTitle = ''
    #    print(myText[index].split(' ')[-1])
    #    splitBySpace = currentText[number].split('*')
       if "*" in myText[index - 1]:
        #    print(myText[index].split('*'))
           for myTitle in myText[index - 1].split('*'):
               if "#" in myTitle:
                #    print(myTitle.split("\n")[0][1:])
                   CurrentTitle = myTitle.split("\n")[0][1:]
                   thereIsTitle = True
                   break
    #    for myTilte in myText:
    #        print(myTilte)
    #        break
        #    if "*" in myTilte:
        #        print(myTilte)
        #        CurrentTitle = myTilte[1:].split('\n')[0]
        #     #    print('present')
        #        break
        #    else: title = ''
       
       splittedVerse = myText[index].split(" ")
      
    #    print(splittedVerse)
       for word in splittedVerse:
           currentWordIndex = splittedVerse.index(word)

           if "\n" in word:
               splittedWord = word.split("\n")
            #    print(splittedWord)
            
               joinedWord = ' '.join(splittedWord)
               splittedVerse[currentWordIndex] = joinedWord

    #    splittedVerse.remove("\n")
       splittedVerse = [item for item in splittedVerse if item != '']
       joinedVerse =' '.join(splittedVerse)
    #    print(joinedVerse)
       splitFromNumber = joinedVerse.split(' ')
    #    print(splittedVerse)
       if  splitFromNumber[-1].isdigit():
          splitFromNumber.remove(splitFromNumber[-1])
          joinedVerse =' '.join(splitFromNumber)
    #       print(splittedVerse[-1])
    #    if(index > 0)
    #    if myText[index - 1].split(' ')[-1].split('\n')[-1].isdigit():
    #    print(myText[index - 1].split(' ')[-1].split('\n')[-1])
       
       if "#" in joinedVerse:
           joinedVerse = joinedVerse.split('#')[0].split('*')[0]
    #    print(myText[index - 1].split(' ')[-1].split('\n')[-1], joinedVerse)
    #    print(joinedVerse)
       author = ''
       if '&' in joinedVerse:
           author = joinedVerse.split('&')[1]
           joinedVerse = joinedVerse.split('&')[0]
           
       
       if thereIsTitle:
         textList.append(
                    {
                    "title": CurrentTitle,
                    "text": joinedVerse ,
                    "ID": myText[index - 1].split(' ')[-1].split('\n')[-1],
                    # "reference": referece
                    }
                )
       elif not thereIsTitle:
            textList.append(
                    {
                    "text": joinedVerse ,
                    "ID": myText[index - 1].split(' ')[-1].split('\n')[-1],
                    # "reference": referece
                    }
                )

         
   bookList.append(
                    {
                    "ID": f"OT:PSA.{chapterNumber}",
                    "name": f"Dut Pwøc {chapterNumber}",
                    "song": f"Dudi {chapterNumber}",
                    "author": author,
                    "text": textList
                    }
                )
createJson(textIntro = intro,
            version = version,
              introTitle = introTitle,
                chapterName = chapterName,
                  bookList = bookList)
           
# print(bookList) 
# for book in bookList:
#     print(book['song'])
#     # print(book['text'])
#     for text in book['text']:
#         if 'title' in text:
#             print(text['title'])
#         print(text['ID'] + " " + text['text'])
#     print(book['author'])


# print(te) 1
# print(texts)

#