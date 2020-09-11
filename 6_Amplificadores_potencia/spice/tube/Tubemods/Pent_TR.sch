*version 6.3 586053028
u 670
TU? 5
V? 3
E? 3
@libraries
@analysis
.DC 1 0 0 0 1 1
+ 0 0 VP
+ 0 4 0
+ 0 5 600
+ 0 6 5
.STEP 1 0 0
+ 0 VG1
+ 4 0
+ 5 -70
+ 6 -10
.OP 0 
.PROBE 0 0 1 1 0 3
@targets
@attributes
@translators
a 0 u 13 0 0 0 hln 100 PSPICE=PSPICE
a 0 u 13 0 0 0 hln 100 PCBOARDS=PCB
a 0 u 13 0 0 0 hln 100 CADSTAR=PCB
a 0 u 13 0 0 0 hln 100 EDIF=PCB
a 0 u 13 0 0 0 hln 100 ORCAD=PCB
a 0 u 13 0 0 0 hln 100 PADS=PCB
a 0 u 13 0 0 0 hln 100 PCAD=PCB
a 0 u 13 0 0 0 hln 100 PROTEL=PCB
a 0 u 13 0 0 0 hln 100 TANGO=PCB
a 0 u 13 0 0 0 hln 100 SCICARDS=PCB
a 0 u 13 0 0 0 hln 100 POLARIS=PCB
@index
pageloc 1 0 2678 
@status
n 0 101:08:02:12:48:39;999456519 e 
s 0 101:08:02:12:48:39;999456519 e 
*page 1 0 970 720 iA
@ports
port 2 AGND 240 245 h
a 1 s 3 0 16 16 hln 100 LABEL=0
@parts
part 5 VSRC 145 185 h
a 1 u 0 0 0 0 hcn 100 DC=0
a 1 u 0 0 0 0 hcn 100 AC=0
a 0 x 0 0 0 0 hln 100 PKGREF=VG1
a 1 xp 9 0 22 40 hcn 100 REFDES=VG1
part 6 VSRC 240 180 h
a 0 x 0 0 0 0 hln 100 PKGREF=VP
a 1 xp 9 0 0 40 hcn 100 REFDES=VP
a 1 u 0 0 0 0 hcn 100 DC=0
a 1 u 0 0 0 0 hcn 100 AC=0
part 361 VSRC 50 200 h
a 1 u 13 0 12 -4 hcn 100 DC=300
a 1 u 0 0 0 0 hcn 100 AC=0
a 0 x 0 0 0 0 hln 100 PKGREF=VG2NOM
a 1 xp 9 0 22 -14 hcn 100 REFDES=VG2NOM
part 384 EVALUE 70 200 h
a 0 u 13 0 -20 66 hln 100 EXPR=V(%IN+, %IN-)*0+V(1P)*1
a 0 sp 11 0 4 36 hln 100 PART=EVALUE
a 0 a 0 0 0 0 hln 100 PKGREF=E2
a 1 ap 9 0 20 2 hln 100 REFDES=E2
part 156 6550 195 160 h
a 0 s 11 0 -12 22 hlb 100 PART=6550
a 0 x 0 0 0 0 hln 100 PKGREF=TU1
a 1 xp 9 0 -10 10 hln 100 REFDES=TU1
part 0 titleblk 970 720 h
a 1 s 13 0 350 10 hcn 100 PageSize=A
a 1 s 13 0 180 60 hcn 100 PageTitle=
a 1 s 13 0 300 95 hrn 100 PageNO=1
a 1 s 13 0 340 95 hrn 100 PageCount=1
@conn
w 473
a 0 sr 3 0 147 175 hln 100 LABEL=1G
s 155 165 145 165 472
a 0 sr 3 0 149 175 hln 100 LABEL=1G
s 145 185 145 165 515
w 615
a 0 sr 3 0 197 202 hln 100 LABEL=1C
s 195 245 195 200 604
a 0 sr 3 0 197 202 hln 100 LABEL=1C
s 145 245 195 245 583
s 145 245 145 225 585
s 120 245 145 245 622
s 120 245 70 245 625
s 70 245 50 245 629
s 120 210 120 245 642
s 70 210 70 245 644
s 240 245 195 245 650
s 240 245 240 220 660
s 50 240 50 245 662
w 619
a 0 sr 3 0 148 153 hln 100 LABEL=2G
s 120 155 155 155 618
a 0 sr 3 0 148 153 hln 100 LABEL=2G
s 120 155 120 200 646
w 641
s 70 200 50 200 648
w 653
a 0 sr 3 0 177 124 hln 100 LABEL=1P
s 240 120 195 120 652
a 0 sr 3 0 179 126 hln 100 LABEL=1P
s 240 180 240 120 658
@junction
j 145 185
+ p 5 +
+ w 473
j 155 165
+ p 156 G
+ w 473
j 145 225
+ p 5 -
+ w 615
j 145 245
+ w 615
+ w 615
j 195 200
+ p 156 C
+ w 615
j 155 155
+ p 156 G2
+ w 619
j 120 245
+ w 615
+ w 615
j 70 245
+ w 615
+ w 615
j 120 210
+ p 384 OUT-
+ w 615
j 70 210
+ p 384 IN-
+ w 615
j 120 200
+ p 384 OUT+
+ w 619
j 70 200
+ p 384 IN+
+ w 641
j 240 245
+ s 2
+ w 615
j 195 245
+ w 615
+ w 615
j 195 120
+ p 156 P
+ w 653
j 240 180
+ p 6 +
+ w 653
j 240 220
+ p 6 -
+ w 615
j 50 240
+ p 361 -
+ w 615
j 50 200
+ p 361 +
+ w 641
@attributes
a 0 s 0 0 0 0 hln 100 PAGETITLE=
a 0 s 0 0 0 0 hln 100 PAGENO=1
a 0 s 0 0 0 0 hln 100 PAGESIZE=A
a 0 s 0 0 0 0 hln 100 PAGECOUNT=1
@text
s 5 40 115 hln 100 PENTODE
s 5 40 140 hln 100 Plate char.
s 5 40 130 hln 100 Triode mode
s 5 40 155 hln 100 Plate current
s 5 40 165 hln 100 is -I(VP)
s 5 50 280 hln 80 (Pentode mode is V(%IN+, %IN-)*1+V(1P)*0)
s 5 50 270 hln 80 (UL mode is   V(%IN+, %IN-)*.4+V(1P)*.6)
