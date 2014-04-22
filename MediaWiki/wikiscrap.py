# -*- coding: utf-8 -*-

import re, sys, operator

miasta = ['Bardo',  'Bielawa',  'Bierutów',  'Bogatynia',  'Boguszów-Gorce',  'Bolesławiec',  'Bolków',  'Brzeg Dolny',  'Bystrzyca Kłodzka',  'Chocianów',  'Chojnów',  'Duszniki-Zdrój',  'Dzierżoniów',  'Głogów',  'Głuszyca',  'Góra',  'Gryfów Śląski',  'Jawor',  'Jaworzyna Śląska',  'Jedlina-Zdrój',  'Jelcz-Laskowice',  'Jelenia Góra',  'Kamienna Góra',  'Karpacz',  'Kąty Wrocławskie',  'Kłodzko',  'Kowary',  'Kudowa-Zdrój',  'Lądek-Zdrój',  'Legnica',  'Leśna',  'Lubań',  'Lubawka',  'Lubin',  'Lubomierz',  'Lwówek Śląski',  'Mieroszów',  'Międzybórz',  'Międzylesie',  'Milicz',  'Mirsk',  'Niemcza',  'Nowa Ruda',  'Nowogrodziec',  'Oborniki Śląskie',  'Oleśnica',  'Olszyna',  'Oława',  'Piechowice',  'Pieńsk',  'Pieszyce',  'Piława Górna',  'Polanica-Zdrój',  'Polkowice',  'Prochowice',  'Prusice',  'Przemków',  'Radków',  'Siechnice',  'Sobótka',  'Stronie Śląskie',  'Strzegom',  'Strzelin',  'Syców',  'Szczawno-Zdrój',  'Szczytna',  'Szklarska Poręba',  'Ścinawa',  'Środa Śląska',  'Świdnica',  'Świebodzice',  'Świeradów-Zdrój',  'Świerzawa',  'Trzebnica',  'Twardogóra',  'Wałbrzych',  'Wąsosz ',  'Węgliniec',  'Wiązów',  'Wleń',  'Wojcieszów',  'Wołów',  'Wrocław',  'Zawidów',  'Ząbkowice Śląskie',  'Zgorzelec',  'Ziębice',  'Złotoryja',  'Złoty Stok',  'Żarów',  'Żmigród',  'Aleksandrów Kujawski',  'Barcin',  'Brodnica',  'Brześć Kujawski',  'Bydgoszcz',  'Chełmno',  'Chełmża',  'Chodecz',  'Ciechocinek',  'Dobrzyń nad Wisłą',  'Gniewkowo',  'Golub-Dobrzyń',  'Górzno',  'Grudziądz',  'Inowrocław',  'Izbica Kujawska',  'Jabłonowo Pomorskie',  'Janikowo',  'Janowiec Wielkopolski',  'Kamień Krajeński',  'Kcynia',  'Koronowo',  'Kowal',  'Kowalewo Pomorskie',  'Kruszwica',  'Lipno',  'Lubień Kujawski',  'Lubraniec',  'Łabiszyn',  'Łasin',  'Mogilno',  'Mrocza',  'Nakło nad Notecią',  'Nieszawa',  'Nowe nad Wisłą',  'Pakość',  'Piotrków Kujawski',  'Radziejów',  'Radzyń Chełmiński',  'Rypin',  'Sępólno Krajeńskie',  'Skępe',  'Solec Kujawski',  'Strzelno',  'Szubin',  'Świecie',  'Toruń',  'Tuchola',  'Wąbrzeźno',  'Więcbork',  'Włocławek',  'Żnin',  'Annopol',  'Bełżyce‎',  'Biała Podlaska‎ ',  'Biłgoraj‎',  'Bychawa‎ ',  'Chełm‎ ',  'Dęblin‎',  'Frampol‎ ',  'Hrubieszów‎',  'Janów Lubelski',  'Józefów',  'Kock‎ ',  'Krasnobród‎',  'Krasnystaw',  'Kraśnik‎',  'Lubartów‎',  'Łaszczów‎ ',  'Łęczna‎',  'Łuków‎ ',  'Międzyrzec Podlaski‎',  'Nałęczów‎',  'Opole Lubelskie',  'Ostrów Lubelski',  'Parczew‎',  'Piaski ',  'Poniatowa‎ ',  'Puławy‎ ',  'Radzyń Podlaski‎',  'Rejowiec Fabryczny‎ ',  'Ryki‎ ',  'Stoczek Łukowski‎ ',  'Szczebrzeszyn‎ ',  'Świdnik‎',  'Tarnogród‎ ',  'Terespol',  'Tomaszów Lubelski',  'Tyszowce‎',  'Włodawa‎ ',  'Zwierzyniec‎',  'Kazimierz Dolny',  'Lublin',  'Międzyrzec Podlaski',  'Modliborzyce',  'Ryki',  'Zamość',  'Babimost',  'Bytom Odrzański',  'Cybinka',  'Czerwieńsk',  'Dobiegniew',  'Drezdenko',  'Gorzów Wielkopolski',  'Gozdnica',  'Gubin',  'Iłowa',  'Jasień',  'Kargowa',  'Kostrzyn nad Odrą',  'Kożuchów',  'Krosno Odrzańskie',  'Lubniewice',  'Lubsko',  'Łęknica',  'Małomice',  'Międzyrzecz',  'Nowa Sól',  'Nowe Miasteczko',  'Nowogród Bobrzański',  'Ośno Lubuskie',  'Rzepin',  'Skwierzyna',  'Sława',  'Słubice',  'Strzelce Krajeńskie',  'Sulechów',  'Sulęcin',  'Szlichtyngowa',  'Szprotawa',  'Świebodzin',  'Torzym',  'Trzciel',  'Witnica',  'Wschowa',  'Zbąszynek',  'Zielona Góra',  'Żagań',  'Żary',  'Aleksandrów Łódzki‎ ',  'Bełchatów‎ ',  'Biała Rawska‎ ',  'Błaszki‎ ',  'Brzeziny‎ ',  'Drzewica‎ ',  'Działoszyn‎ ',  'Głowno‎ ',  'Kamieńsk‎ ',  'Koluszki‎ ',  'Konstantynów Łódzki‎',  'Krośniewice‎ ',  'Kutno‎ ',  'Łask‎ ',  'Łęczyca‎ ',  'Łowicz‎',  'Opoczno‎ ',  'Ozorków‎',  'Pabianice‎',  'Pajęczno‎ ',  'Piotrków Trybunalski',  'Poddębice‎',  'Przedbórz‎',  'Radomsko‎',  'Rawa Mazowiecka‎',  'Rzgów‎',  'Sieradz‎ ',  'Skierniewice‎',  'Stryków‎ ',  'Sulejów‎',  'Szadek',  'Tuszyn‎',  'Uniejów‎',  'Warta',  'Wieruszów‎',  'Wolbórz‎',  'Zduńska Wola‎ ',  'Zelów‎ ',  'Zgierz‎ ',  'Złoczew‎ ',  'Żychlin‎ ',  'Łódź',  'Piotrków Trybunalski',  'Tomaszów Mazowiecki',  'Wieluń',  'Alwernia',  'Andrychów',  'Biecz',  'Bobowa',  'Bochnia',  'Brzesko',  'Brzeszcze',  'Bukowno',  'Chełmek',  'Chrzanów',  'Ciężkowice',  'Czchów',  'Dąbrowa Tarnowska',  'Dobczyce',  'Gorlice',  'Grybów',  'Jordanów',  'Kalwaria Zebrzydowska',  'Kęty',  'Kraków',  'Krynica-Zdrój',  'Krzeszowice',  'Libiąż',  'Limanowa',  'Maków Podhalański',  'Miechów',  'Mszana Dolna',  'Muszyna',  'Myślenice',  'Niepołomice',  'Nowe Brzesko',  'Nowy Sącz',  'Nowy Targ',  'Nowy Wiśnicz',  'Olkusz',  'Oświęcim',  'Piwniczna-Zdrój',  'Proszowice',  'Rabka-Zdrój',  'Radłów',  'Ryglice',  'Skała ',  'Skawina',  'Słomniki',  'Stary Sącz',  'Sucha Beskidzka',  'Sułkowice',  'Szczawnica',  'Szczucin',  'Świątniki Górne',  'Tarnów',  'Trzebinia',  'Tuchów',  'Wadowice',  'Wieliczka',  'Wojnicz',  'Wolbrom',  'Zakliczyn',  'Zakopane',  'Zator',  'Żabno',  'Białobrzegi',  'Bieżuń',  'Błonie',  'Brok',  'Brwinów',  'Chorzele',  'Ciechanów',  'Drobin',  'Garwolin',  'Gąbin',  'Glinojeck',  'Gostynin',  'Góra Kalwaria',  'Grodzisk Mazowiecki',  'Grójec',  'Halinów',  'Iłża',  'Józefów',  'Kałuszyn',  'Karczew',  'Kobyłka',  'Konstancin-Jeziorna',  'Kosów Lacki',  'Kozienice',  'Legionowo',  'Lipsko',  'Łaskarzew',  'Łochów',  'Łomianki',  'Łosice',  'Maków Mazowiecki',  'Marki',  'Milanówek',  'Mińsk Mazowiecki',  'Mława',  'Mogielnica',  'Mordy',  'Mrozy',  'Mszczonów',  'Myszyniec',  'Nasielsk',  'Nowe Miasto nad Pilicą',  'Nowy Dwór Mazowiecki',  'Ostrołęka',  'Ostrów Mazowiecka',  'Otwock',  'Ożarów Mazowiecki',  'Piaseczno',  'Piastów',  'Pilawa',  'Pionki',  'Płock',  'Płońsk',  'Podkowa Leśna',  'Pruszków',  'Przasnysz',  'Przysucha',  'Pułtusk',  'Raciąż',  'Radom',  'Radzymin',  'Różan',  'Serock',  'Siedlce',  'Sierpc',  'Skaryszew',  'Sochaczew',  'Sokołów Podlaski',  'Sulejówek',  'Szydłowiec',  'Tarczyn',  'Tłuszcz',  'Warka',  'Warszawa',  'Węgrów',  'Wołomin',  'Wyszków',  'Wyszogród',  'Wyśmierzyce',  'Zakroczym',  'Ząbki',  'Zielonka',  'Zwoleń',  'Żelechów',  'Żuromin',  'Żyrardów',  'Kietrz',  'Olesno',  'Baborów',  'Biała',  'Byczyna',  'Dobrodzień',  'Głogówek',  'Głubczyce',  'Głuchołazy',  'Gogolin',  'Gorzów Śląski',  'Grodków',  'Kędzierzyn-Koźle',  'Kluczbork',  'Kolonowskie',  'Korfantów',  'Krapkowice',  'Leśnica',  'Lewin Brzeski',  'Namysłów',  'Niemodlin',  'Nysa',  'Opole',  'Otmuchów',  'Ozimek',  'Paczków',  'Praszka',  'Prószków',  'Prudnik',  'Strzelce Opolskie',  'Ujazd',  'Wołczyn',  'Zawadzkie',  'Zdzieszowice',  'Baranów Sandomierski‎ ',  'Błażowa‎ ',  'Boguchwała‎',  'Brzostek‎',  'Brzozów‎ ',  'Cieszanów‎ ',  'Dębica‎ ',  'Dukla‎ ',  'Dynów‎',  'Głogów Małopolski‎ ',  'Iwonicz-Zdrój‎ ',  'Jasło‎ ',  'Jedlicze‎ ',  'Kańczuga‎ ',  'Kolbuszowa‎ ',  'Kołaczyce‎ ',  'Lesko‎ ',  'Leżajsk‎ ',  'Lubaczów‎ ',  'Łańcut‎ ',  'Narol‎ ',  'Nisko‎',  'Nowa Dęba‎ ',  'Nowa Sarzyna‎ ',  'Oleszyce‎ ',  'Pilzno ',  'Pruchnik‎',  'Przecław‎ ',  'Radomyśl Wielki‎ ',  'Radymno‎',  'Ropczyce‎ ',  'Rudnik nad Sanem‎ ',  'Rymanów‎',  'Sanok‎ ',  'Sędziszów Małopolski‎',  'Sieniawa‎',  'Sokołów Małopolski‎ ',  'Stalowa Wola‎',  'Strzyżów‎ ',  'Tarnobrzeg‎ ',  'Tyczyn‎ ',  'Ulanów‎',  'Ustrzyki Dolne‎',  'Zagórz‎',  'Jarosław',  'Kolbuszowa',  'Krosno',  'Mielec',  'Przemyśl',  'Przeworsk',  'Rzeszów',  'Zaklików',  'Augustów',  'Bielsk Podlaski‎ ',  'Brańsk‎ ',  'Choroszcz‎',  'Ciechanowiec‎',  'Czarna Białostocka‎',  'Czyżew‎ ',  'Dąbrowa Białostocka‎',  'Drohiczyn‎ ',  'Goniądz‎ ',  'Grajewo‎ ',  'Hajnówka',  'Jedwabne‎',  'Kleszczele‎',  'Knyszyn',  'Kolno‎',  'Krynki',  'Lipsk',  'Łapy‎',  'Łomża‎',  'Michałowo‎',  'Nowogród',  'Rajgród‎ ',  'Sejny‎ ',  'Siemiatycze‎ ',  'Sokółka‎ Stawiski‎',  'Suchowola‎ ',  'Supraśl‎ ',  'Suraż‎ ',  'Suwałki‎ ',  'Szczuczyn',  'Szepietowo‎ ',  'Tykocin‎',  'Wasilków‎',  'Wysokie Mazowieckie‎',  'Zabłudów',  'Zambrów‎',  'Augustów',  'Białystok',  'Mońki',  'Brusy‎',  'Bytów‎',  'Chojnice‎',  'Czarne‎',  'Człuchów‎',  'Debrzno‎',  'Dzierzgoń',  'Gdynia‎ ',  'Gniew',  'Hel‎',  'Jastarnia‎ ',  'Kartuzy‎',  'Kępice',  'Kościerzyna',  'Krynica Morska‎',  'Łeba‎',  'Miastko‎',  'Nowy Dwór Gdański‎ ',  'Nowy Staw‎',  'Pelplin',  'Prabuty‎',  'Pruszcz Gdański‎',  'Puck',  'Reda',  'Rumia‎',  'Skarszewy‎',  'Skórcz‎',  'Sopot‎ ',  'Starogard Gdański',  'Sztum‎',  'Tczew‎',  'Ustka‎',  'Wejherowo',  'Władysławowo‎',  'Żukowo‎',  'Czarna Woda',  'Czersk',  'Gdańsk',  'Kwidzyn',  'Lębork',  'Malbork',  'Słupsk',  'Dąbrowa Górnicza‎',  'Knurów',  'Koniecpol‎',  'Koziegłowy',  'Krzanowice',  'Krzepice',  'Kuźnia Raciborska‎',  'Lędziny‎ ',  'Lubliniec‎',  'Łaziska Górne‎',  'Łazy‎',  'Poręba',  'Pszczyna',  'Pszów',  'Pyskowice‎',  'Radlin',  'Radzionków‎',  'Ruda Śląska‎',  'Rydułtowy‎',  'Siemianowice Śląskie‎',  'Siewierz',  'Skoczów',  'Sławków‎',  'Sosnowiec‎',  'Sośnicowice‎',  'Strumień',  'Szczekociny‎',  'Szczyrk',  'Świętochłowice‎',  'Tarnowskie Góry‎',  'Toszek‎',  'Tychy‎',  'Ustroń',  'Wilamowice‎',  'Wisła‎',  'Wojkowice',  'Woźniki‎',  'Zabrze‎',  'Zawiercie‎',  'Żarki',  'Żory‎',  'Żywiec',  'Będzin',  'Bielsko-Biała',  'Bieruń',  'Blachownia',  'Bytom',  'Chorzów',  'Cieszyn',  'Czechowice-Dziedzice',  'Czeladź',  'Czerwionka-Leszczyny',  'Częstochowa',  'Gliwice',  'Imielin',  'Jastrzębie-Zdrój',  'Jaworzno',  'Kalety',  'Katowice',  'Kłobuck',  'Miasteczko Śląskie',  'Mikołów',  'Mysłowice',  'Myszków',  'Ogrodzieniec',  'Orzesze',  'Piekary Śląskie',  'Pilica',  'Racibórz',  'Rybnik',  'Wilamowice',  'Wodzisław Śląski',  'Bodzentyn‎',  'Busko-Zdrój‎',  'Chęciny',  'Chmielnik',  'Ćmielów‎',  'Daleszyce‎',  'Działoszyce',  'Jędrzejów‎',  'Kazimierza Wielka',  'Końskie‎',  'Koprzywnica‎',  'Kunów‎',  'Małogoszcz‎',  'Opatów‎',  'Osiek',  'Ostrowiec Świętokrzyski',  'Ożarów',  'Pińczów‎',  'Połaniec',  'Sandomierz‎',  'Sędziszów',  'Skalbmierz‎',  'Skarżysko-Kamienna‎',  'Starachowice‎',  'Staszów‎',  'Stąporków‎',  'Suchedniów',  'Wąchock',  'Włoszczowa‎',  'Zawichost',  'Kielce',  'Barczewo‎',  'Bartoszyce‎',  'Biała Piska',  'Biskupiec',  'Bisztynek',  'Braniewo‎',  'Dobre Miasto‎',  'Działdowo‎',  'Elbląg‎',  'Ełk‎',  'Frombork‎',  'Giżycko‎',  'Gołdap',  'Górowo Iławeckie',  'Iława‎',  'Jeziorany‎',  'Kętrzyn',  'Kisielice‎',  'Korsze‎',  'Lidzbark‎ ',  'Lidzbark Warmiński',  'Lubawa‎',  'Mikołajki',  'Miłakowo‎',  'Miłomłyn',  'Młynary‎',  'Morąg‎',  'Mrągowo',  'Nidzica',  'Nowe Miasto Lubawskie',  'Olecko‎',  'Olsztynek‎',  'Orneta‎',  'Orzysz‎',  'Ostróda',  'Pasłęk',  'Pasym‎',  'Pieniężno',  'Pisz‎',  'Reszel',  'Ruciane-Nida‎',  'Ryn‎',  'Sępopol‎',  'Susz',  'Szczytno‎',  'Tolkmicko',  'Węgorzewo',  'Zalewo',  'Olsztyn',  'Bojanowo',  'Borek Wielkopolski',  'Buk ',  'Chodzież',  'Czarnków',  'Czempiń',  'Czerniejewo',  'Dąbie',  'Dobra ',  'Dobrzyca',  'Dolsk',  'Gniezno',  'Golina',  'Gołańcz',  'Gostyń',  'Grabów nad Prosną',  'Grodzisk Wielkopolski',  'Jarocin',  'Jastrowie',  'Jutrosin',  'Kalisz',  'Kępno',  'Kleczew',  'Kłecko',  'Kłodawa',  'Kobylin',  'Koło ',  'Konin',  'Kostrzyn',  'Kościan',  'Koźmin Wielkopolski',  'Kórnik',  'Krajenka',  'Krobia',  'Krotoszyn',  'Krzywiń',  'Krzyż Wielkopolski',  'Książ Wielkopolski',  'Leszno',  'Luboń',  'Lwówek',  'Łobżenica',  'Margonin',  'Miejska Górka',  'Międzychód',  'Mikstat',  'Miłosław',  'Mosina',  'Murowana Goślina',  'Nekla',  'Nowe Skalmierzyce',  'Nowy Tomyśl',  'Oborniki',  'Obrzycko',  'Odolanów',  'Okonek',  'Opalenica',  'Osieczna',  'Ostroróg',  'Ostrów Wielkopolski',  'Ostrzeszów',  'Piła ',  'Pleszew',  'Pniewy',  'Pobiedziska',  'Pogorzela',  'Poniec',  'Poznań',  'Przedecz',  'Puszczykowo',  'Pyzdry',  'Rakoniewice',  'Raszków',  'Rawicz',  'Rogoźno',  'Rychwał',  'Rydzyna',  'Sieraków',  'Skoki',  'Słupca',  'Sompolno',  'Stawiszyn',  'Stęszew',  'Sulmierzyce',  'Swarzędz',  'Szamocin',  'Szamotuły',  'Ślesin',  'Śmigiel',  'Śrem',  'Środa Wielkopolska',  'Trzcianka',  'Trzemeszno',  'Tuliszków',  'Turek',  'Ujście',  'Wągrowiec',  'Wieleń',  'Wielichowo',  'Witkowo',  'Wolsztyn',  'Wronki',  'Września',  'Wyrzysk',  'Wysoka',  'Zagórów',  'Zbąszyń',  'Zduny',  'Złotów',  'Żerków',  'Barlinek',  'Barwice',  'Białogard',  'Biały Bór',  'Bobolice',  'Borne Sulinowo',  'Cedynia',  'Chociwel',  'Chojna',  'Choszczno',  'Czaplinek',  'Człopa',  'Darłowo',  'Dębno',  'Dobra',  'Dobrzany',  'Drawno',  'Drawsko Pomorskie',  'Dziwnów',  'Golczewo',  'Goleniów',  'Gościno',  'Gryfice',  'Gryfino',  'Ińsko',  'Kalisz Pomorski',  'Kamień Pomorski',  'Karlino',  'Kołobrzeg',  'Koszalin',  'Lipiany',  'Łobez',  'Maszewo',  'Mieszkowice',  'Międzyzdroje',  'Mirosławiec',  'Moryń',  'Myślibórz',  'Nowe Warpno',  'Nowogard',  'Pełczyce',  'Płoty',  'Polanów',  'Police',  'Połczyn-Zdrój',  'Pyrzyce',  'Recz',  'Resko',  'Sianów',  'Sławno',  'Stargard Szczeciński',  'Stepnica',  'Suchań',  'Szczecin',  'Szczecinek',  'Świdwin',  'Świnoujście',  'Trzcińsko-Zdrój',  'Trzebiatów',  'Tuczno',  'Tychowo',  'Wałcz',  'Węgorzyno',  'Wolin',  'Złocieniec', ]
for x in sys.stdin:
	print "<item>"

	for x in sys.stdin:
		wyn = re.search(r'^<title>.*– Wikipedia, wolna encyklopedia</title>$', x)  
		if wyn:
			title = re.sub(r' – Wikipedia, wolna encyklopedia', "", wyn.group())
			print title
			break
			
	print "\n<url>"
	
	for x in sys.stdin:
		wyn = re.search(r'<link rel="canonical" href=".*" />', x)
		if wyn:
			wyn2 = re.sub(r'^<link rel="canonical" href="', "", wyn.group())
			url = re.sub(r'" />$', "", wyn2);
			print url
			break
			
	print "</url>\n<content>"
	content = ""
	city = ""		
	for x in sys.stdin:
		pocz = re.search(r'<div id="mw-content-text"', x)
		if pocz:
			for x in sys.stdin:
				kat = re.search(r'^.*mw-normal-catlinks.*$', x)
				if not(kat):
					wyn = re.search(r'<p>.*</p>', x)
					if wyn:
						content = content + wyn.group()
				else:
					break
			print re.sub(r'<.*?>', "", content)
			print "</content>\n<city>"
			freq = {}
			for word in miasta:
				wyn = re.findall(word, content)
				freq[word] = len(wyn)
			print max(freq, key=freq.get)
			break

			
	print "</city>\n<category>"

	for x in sys.stdin:
		if kat:
			wyn0 = re.search(r'Kategoria:Miasta', kat.group())
			if wyn0:
				print "miasto"
				break
			wyn1 = re.search(r'Kategoria:Kina', kat.group())
			if wyn1:
				print "kino"
				break
			wyn2 = re.search(r'Kategoria:Teatry', kat.group())
			if wyn2:
				print "teatr"
				break
			wyn4 = re.search(r'Kategoria:Obiekty_sportowe', kat.group())
			wyn5 = re.search(r'Kategoria:Stadiony', kat.group())
			wyn6 = re.search(r'Kategoria:Tory_', kat.group())
			wyn7 = re.search(r'Kategoria:Lodowiska', kat.group())
			wyn8 = re.search(r'Kategoria:Skocznie', kat.group())
			if (wyn4 or wyn5 or wyn6 or wyn7 or wyn8):
				print "obiekt sportowy"
				break
			wyn9 = re.search(r'Kategoria:Hotele', kat.group())
			if wyn9:
				print "hotel"
				break
			wyn10 = re.search(r'Kategoria:Muzea', kat.group())
			wyn13 = re.search(r'Kategoria:Żywe muzea', kat.group())
			wyn21 = re.search(r'Kategoria:Skanseny', kat.group())
			if (wyn10 or wyn13 or wyn21):
				print "muzeum"
				break
			wyn11 = re.search(r'Kategoria:Zabytki', kat.group())
			wyn17 = re.search(r'Kategoria:Zabytkowe', kat.group())
			if (wyn11 or wyn17):
				print "zabytek"
				break
			wyn12 = re.search(r'Kategoria:Pomniki', kat.group())
			if wyn12:
				print "pomnik"
				break
			wyn14 = re.search(r'Kategoria:Szlaki_turystyczne', kat.group())
			if wyn14:
				print "szlak turystyczny"
				break
			wyn15 = re.search(r'Kategoria:Schroniska', kat.group())
			if wyn15:
				print "schronisko"
				break
			wyn16 = re.search(r'Kategoria:Uzdrowiska', kat.group())
			if wyn16:
				print "uzdrowisko"
				break
			wyn18 = re.search(r'Kategoria:Zamki', kat.group())
			wyn19 = re.search(r'Kategoria:Pałace', kat.group())
			wyn20 = re.search(r'Kategoria:Twierdze',kat.group())
			if (wyn18 or wyn19 or wyn20):
				print "zamek"
				break
			break
	
	print "</category>"


	print "</item>"
