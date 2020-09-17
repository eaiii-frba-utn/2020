*version 6.3 752429688
u 14016
R? 102
C? 38
D? 13
V? 10
L? 4
U? 2
HB? 2
PM? 2
@libraries
@analysis
.AC 1 3 0
+0 20
+1 .01
+2 100MEG
+3 V(LINE_OUT)
+4 VIN
+5 1
.TRAN 0 0 0 1
+0 .1MS
+1 1MS
+2 0
+3 .02MS
+4 1K
+5 V(PHONO_IN) V(LINE_IN)  V(LINE_OUT)
+6 9
.OPT 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
.STEP 0 2 4
+ 0 PARVOL
+ 4 .01
+ 5 1
+ 6 3
.OP 0 
.PROBE 0 0 1 1 0 3
.LIB C:\PSPICE\WORK\TUBE.LIB
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
a 0 u 13 0 0 0 hln 100 XILINX=XILINX
@index
pageloc 1 0 12066 MODIFIED PAS PREAMPLIFIER
@status
n 0 97:03:27:16:51:32;862185092 e 
s 0 97:03:27:16:51:33;862185093 e 
*page 1 0 1520 970 iA
@ports
port 5986 GND_EARTH 400 295 h
port 6284 BUBBLE 620 75 d
a 1 x 14 0 10 -34 hcn 100 LABEL=V+280
port 7348 BUBBLE 715 50 h
a 1 x 14 0 10 -2 hcn 100 LABEL=V+280
port 7350 GND_EARTH 715 90 h
port 8345 BUBBLE 255 180 h
a 1 x 14 0 8 2 hcn 100 LABEL=PHONO_IN
port 8346 BUBBLE 300 180 h
a 1 x 14 0 22 2 hcn 100 LABEL=PHONO_IN
port 8356 BUBBLE 725 175 d
a 1 x 14 0 20 -14 hcn 100 LABEL=LINE_IN
port 8367 GND_EARTH 255 285 h
port 10557 GND_EARTH 105 315 h
port 10558 BUBBLE 105 275 h
a 1 x 14 0 10 -2 hcn 100 LABEL=PH_IN
port 10565 BUBBLE 100 185 v
a 1 x 14 0 10 2 hcn 100 LABEL=PH_IN
@parts
part 5969 R 305 185 h
a 0 u 13 0 13 27 hln 100 VALUE=10k
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 x 0 0 0 0 hln 100 PKGREF=R1GS
a 0 s 0 0 0 0 hln 100 GATE=
a 0 xp 9 0 9 2 hln 100 REFDES=R1GS
part 5970 R 300 265 v
a 0 u 13 0 11 37 hln 100 VALUE=47k
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 x 0 0 0 0 hln 100 PKGREF=R1G
a 0 s 0 0 0 0 hln 100 GATE=
a 0 xp 9 0 23 40 hln 100 REFDES=R1G
part 5972 R 400 285 v
a 0 u 13 0 13 1 hln 100 VALUE=1k
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 x 0 0 0 0 hln 100 PKGREF=R1C
a 0 s 0 0 0 0 hln 100 GATE=
a 0 xp 9 0 23 4 hln 100 REFDES=R1C
part 5974 R 460 235 v
a 0 u 13 0 11 45 hln 100 VALUE=1MEG
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 x 0 0 0 0 hln 100 PKGREF=R2G
a 0 s 0 0 0 0 hln 100 GATE=
a 0 xp 9 0 23 40 hln 100 REFDES=R2G
part 5975 R 400 120 v
a 0 u 13 0 15 45 hln 100 VALUE=150k
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 x 0 0 0 0 hln 100 PKGREF=R1P
a 0 s 0 0 0 0 hln 100 GATE=
a 0 xp 9 0 15 0 hln 100 REFDES=R1P
part 5976 R 515 260 v
a 0 u 13 0 9 3 hln 100 VALUE=750
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 x 0 0 0 0 hln 100 PKGREF=R2C
a 0 s 0 0 0 0 hln 100 GATE=
a 0 xp 9 0 21 4 hln 100 REFDES=R2C
part 5977 R 495 120 v
a 0 u 13 0 17 43 hln 100 VALUE=120k
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 x 0 0 0 0 hln 100 PKGREF=R2P
a 0 s 0 0 0 0 hln 100 GATE=
a 0 xp 9 0 17 2 hln 100 REFDES=R2P
part 5978 R 580 250 v
a 0 u 13 0 9 5 hln 100 VALUE=120k
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 x 0 0 0 0 hln 100 PKGREF=R5C
a 0 s 0 0 0 0 hln 100 GATE=
a 0 xp 9 0 21 4 hln 100 REFDES=R5C
part 5981 C 460 135 d
a 0 u 13 0 29 35 hln 100 VALUE=.1UF
a 0 sp 0 0 0 10 hlb 100 PART=C
a 0 x 0 0 0 0 hln 100 PKGREF=C1P
a 0 s 0 0 0 0 hln 100 GATE=
a 0 xp 9 0 11 34 hln 100 REFDES=C1P
part 5983 C 675 175 h
a 0 u 13 0 19 3 hln 100 VALUE=.47UF
a 0 sp 0 0 0 10 hlb 100 PART=C
a 0 x 0 0 0 0 hln 100 PKGREF=C5C
a 0 s 0 0 0 0 hln 100 GATE=
a 0 xp 9 0 -9 2 hln 100 REFDES=C5C
part 6034 R 665 270 v
a 0 u 13 0 13 55 hln 100 VALUE=2.2MEG
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 x 0 0 0 0 hln 100 PKGREF=RIA2
a 0 s 0 0 0 0 hln 100 GATE=
a 0 xp 9 0 23 44 hln 100 REFDES=RIA2
part 6035 R 665 220 v
a 0 u 13 0 11 47 hln 100 VALUE=86.6k
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 x 0 0 0 0 hln 100 PKGREF=RIA1
a 0 s 0 0 0 0 hln 100 GATE=
a 0 xp 9 0 21 42 hln 100 REFDES=RIA1
part 6036 C 630 265 v
a 0 u 13 0 3 9 hln 100 VALUE=2850PF
a 0 sp 0 0 0 10 hlb 100 PART=C
a 0 x 0 0 0 0 hln 100 PKGREF=CIA2
a 0 s 0 0 0 0 hln 100 GATE=
a 0 xp 9 0 23 8 hln 100 REFDES=CIA2
part 6037 C 630 215 v
a 0 u 13 0 1 7 hln 100 VALUE=876PF
a 0 sp 0 0 0 10 hlb 100 PART=C
a 0 x 0 0 0 0 hln 100 PKGREF=CIA1
a 0 s 0 0 0 0 hln 100 GATE=
a 0 xp 9 0 21 4 hln 100 REFDES=CIA1
part 7346 VSRC 715 50 h
a 1 u 0 0 0 0 hcn 100 DC=280
a 1 u 0 0 0 0 hcn 100 AC=0
a 0 x 0 0 0 0 hln 100 PKGREF=V+280
a 1 xp 9 0 32 8 hcn 100 REFDES=V+280
part 7497 R 100 185 h
a 0 u 13 0 13 27 hln 100 VALUE=300
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 x 0 0 0 0 hln 100 PKGREF=RIV1
a 0 s 0 0 0 0 hln 100 GATE=
a 0 xp 9 0 11 2 hln 100 REFDES=RIV1
part 7498 R 150 185 h
a 0 u 13 0 3 25 hln 100 VALUE=2.2MEG
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 x 0 0 0 0 hln 100 PKGREF=RIV2
a 0 s 0 0 0 0 hln 100 GATE=
a 0 xp 9 0 13 2 hln 100 REFDES=RIV2
part 7499 R 205 185 h
a 0 u 13 0 9 25 hln 100 VALUE=186K
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 x 0 0 0 0 hln 100 PKGREF=RIV3
a 0 s 0 0 0 0 hln 100 GATE=
a 0 xp 9 0 9 2 hln 100 REFDES=RIV3
part 7500 C 155 230 h
a 0 u 13 0 -3 25 hln 100 VALUE=1447PF
a 0 sp 0 0 0 10 hlb 100 PART=C
a 0 x 0 0 0 0 hln 100 PKGREF=CIV1
a 0 s 0 0 0 0 hln 100 GATE=
a 0 xp 9 0 7 0 hln 100 REFDES=CIV1
part 7501 C 210 230 h
a 0 u 13 0 -1 25 hln 100 VALUE=403.1PF
a 0 sp 0 0 0 10 hlb 100 PART=C
a 0 x 0 0 0 0 hln 100 PKGREF=CIV2
a 0 s 0 0 0 0 hln 100 GATE=
a 0 xp 9 0 5 0 hln 100 REFDES=CIV2
part 7600 R 255 285 v
a 0 u 13 0 11 3 hln 100 VALUE=724
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 x 0 0 0 0 hln 100 PKGREF=RIV4
a 0 s 0 0 0 0 hln 100 GATE=
a 0 xp 9 0 23 4 hln 100 REFDES=RIV4
part 8378 R 715 250 v
a 0 u 13 0 11 55 hln 100 VALUE=2.2MEG
a 0 sp 0 0 0 10 hlb 100 PART=R
a 0 x 0 0 0 0 hln 100 PKGREF=RPL
a 0 s 0 0 0 0 hln 100 GATE=
a 0 xp 9 0 23 40 hln 100 REFDES=RPL
part 8962 C 355 170 v
a 0 u 13 0 21 39 hln 100 VALUE=39PF
a 0 sp 0 0 0 10 hlb 100 PART=C
a 0 x 0 0 0 0 hln 100 PKGREF=C1M
a 0 s 0 0 0 0 hln 100 GATE=
a 0 xp 9 0 21 8 hln 100 REFDES=C1M
part 10546 VSRC 105 275 h
a 1 u 0 0 0 0 hcn 100 DC=0
a 1 u 0 0 0 0 hcn 100 AC=1
a 1 u 0 0 0 0 hcn 100 TRAN=SIN(0  1.136 1K)
a 0 x 0 0 0 0 hln 100 PKGREF=VIN
a 1 xp 9 0 -12 24 hcn 100 REFDES=VIN
part 7281 12AX7 400 185 h
a 0 s 0 0 0 10 hlb 100 PART=12AX7
a 0 x 0 0 0 0 hln 100 PKGREF=TU1
a 1 xp 9 0 -8 64 hln 100 REFDES=TU1
part 7282 12AX7 515 175 h
a 0 s 0 0 0 10 hlb 100 PART=12AX7
a 0 x 0 0 0 0 hln 100 PKGREF=TU2
a 1 xp 9 0 68 64 hln 100 REFDES=TU2
part 7283 12AX7 580 130 h
a 0 s 0 0 0 10 hlb 100 PART=12AX7
a 0 x 0 0 0 0 hln 100 PKGREF=TU5
a 1 xp 9 0 62 4 hln 100 REFDES=TU5
part 13705 titleblk 970 720 h
a 1 s 13 0 350 10 hcn 100 PageSize=A
a 1 s 13 0 180 60 hcn 100 PageTitle=MODIFIED PAS PREAMPLIFIER
a 1 u 13 0 10 10 hln 100 CompanyName=Koren Audio
a 1 u 13 0 10 20 hln 100 Line1=2230 Woodwind Drive
a 1 u 13 0 10 30 hln 100 Line2=Encinitas, CA 92024
a 1 u 13 0 10 40 hln 100 Line3=619-942-2284
a 1 u 13 0 110 95 hln 100 Date=September 28, 1996
a 1 s 13 0 340 95 hrn 100 PageCount=1
a 1 s 13 0 300 95 hrn 100 PageNO=1
part 12602 VIEWPOINT 515 130 h
a 0 s 0 0 0 0 hln 100 MARKERTYPE=VIEWPOINT
a 0 s 0 0 0 0 hln 100 NODE=$N_0005
a 1 s 13 0 22 6 hcn 100 BIASVALUE=
part 12623 VIEWPOINT 440 130 h
a 0 s 0 0 0 0 hln 100 MARKERTYPE=VIEWPOINT
a 0 s 0 0 0 0 hln 100 NODE=1P
a 1 s 13 0 18 6 hcn 100 BIASVALUE=
part 12625 VIEWPOINT 540 275 h
a 0 s 0 0 0 0 hln 100 MARKERTYPE=VIEWPOINT
a 0 s 0 0 0 0 hln 100 NODE=1C
a 1 s 13 0 20 6 hcn 100 BIASVALUE=
part 13391 IPROBE 620 75 d
a 0 s 0 0 0 0 hln 100 MARKERTYPE=VIEWPOINT
a 1 a 0 0 10 23 hcn 100 refdes=V9
a 1 s 13 0 -4 45 hln 100 BIASVALUE=3.275E-03
@conn
w 13863
a 0 sr 3 0 403 242 hln 100 LABEL=1C
s 400 230 435 230 13862
a 0 sr 3 0 403 242 hln 100 LABEL=1C
s 400 230 400 225 13864
s 400 245 400 230 13866
s 435 275 435 230 13868
s 630 275 540 275 13870
s 630 265 630 275 13872
s 665 270 665 275 13874
s 665 275 630 275 13876
s 540 275 435 275 13878
w 13881
a 0 sr 3 0 402 140 hln 100 LABEL=1P
s 440 130 400 130 13880
a 0 sr 3 0 402 140 hln 100 LABEL=1P
s 400 120 400 130 13882
s 355 130 400 130 13884
s 400 145 400 130 13886
s 355 140 355 130 13888
s 460 130 440 130 13890
s 460 135 460 130 13892
w 13895
s 300 225 300 185 13894
s 305 185 300 185 13896
s 300 180 300 185 13898
w 13901
a 0 sr 3 0 355 195 hln 100 LABEL=1G
s 345 185 355 185 13902
s 355 185 360 185 13906
a 0 sr 3 0 355 195 hln 100 LABEL=1G
s 355 170 355 185 13904
w 13908
s 580 75 580 90 13907
s 400 80 400 75 13909
s 400 75 495 75 13913
s 495 75 580 75 13917
s 495 75 495 80 13915
w 13919
a 0 sr 3 0 470 171 hln 100 LABEL=2G
s 460 175 475 175 13918
a 0 sr 3 0 470 171 hln 100 LABEL=2G
s 460 175 460 195 13920
s 460 165 460 175 13922
w 13925
s 300 265 300 295 13924
s 460 295 460 235 13926
s 400 285 400 295 13928
s 400 295 460 295 13930
s 300 295 400 295 13932
s 715 295 715 250 13934
s 715 295 580 295 13936
s 580 250 580 295 13938
s 580 295 515 295 13942
s 515 295 460 295 13946
s 515 260 515 295 13944
w 13948
s 245 185 255 185 13947
s 255 185 255 230 13951
s 255 230 255 245 13955
s 240 230 255 230 13953
s 255 180 255 185 13956
w 13959
s 200 230 200 185 13958
s 185 230 200 230 13960
s 210 230 200 230 13962
s 190 185 200 185 13964
s 200 185 205 185 13966
w 13969
s 145 230 145 185 13968
s 155 230 145 230 13970
s 140 185 145 185 13972
s 145 185 150 185 13974
w 13977
a 0 sr 3 0 560 177 hln 100 LABEL=5C
s 580 175 580 210 13976
a 0 sr 3 0 560 177 hln 100 LABEL=5C
s 580 175 630 175 13978
s 580 170 580 175 13980
s 630 185 630 175 13982
s 665 175 630 175 13984
s 665 180 665 175 13986
s 675 175 665 175 13988
w 13991
s 715 175 715 210 13990
s 705 175 715 175 13992
s 715 175 725 175 13994
w 13997
a 0 sr 3 0 639 223 hln 100 LABEL=3FB
s 630 225 665 225 13996
a 0 sr 3 0 639 223 hln 100 LABEL=3FB
s 630 225 630 215 13998
s 665 220 665 225 14000
s 630 235 630 225 14002
s 665 225 665 230 14004
w 14007
s 495 130 515 130 14006
s 495 120 495 130 14008
s 515 130 540 130 14010
s 515 130 515 135 14012
w 14015
s 515 220 515 215 14014
@junction
j 400 225
+ p 7281 C
+ w 13863
j 400 245
+ p 5972 2
+ w 13863
j 400 230
+ w 13863
+ w 13863
j 540 275
+ p 12625 +
+ w 13863
j 630 265
+ p 6036 1
+ w 13863
j 665 270
+ p 6034 1
+ w 13863
j 630 275
+ w 13863
+ w 13863
j 440 130
+ p 12623 +
+ w 13881
j 400 120
+ p 5975 1
+ w 13881
j 400 130
+ w 13881
+ w 13881
j 400 145
+ p 7281 P
+ w 13881
j 355 140
+ p 8962 2
+ w 13881
j 460 135
+ p 5981 1
+ w 13881
j 300 225
+ p 5970 2
+ w 13895
j 305 185
+ p 5969 1
+ w 13895
j 300 180
+ s 8346
+ w 13895
j 300 185
+ w 13895
+ w 13895
j 360 185
+ p 7281 G
+ w 13901
j 345 185
+ p 5969 2
+ w 13901
j 355 170
+ p 8962 1
+ w 13901
j 355 185
+ w 13901
+ w 13901
j 580 90
+ p 7283 P
+ w 13908
j 580 75
+ p 13391 -
+ w 13908
j 400 80
+ p 5975 2
+ w 13908
j 495 80
+ p 5977 2
+ w 13908
j 495 75
+ w 13908
+ w 13908
j 475 175
+ p 7282 G
+ w 13919
j 460 195
+ p 5974 2
+ w 13919
j 460 165
+ p 5981 2
+ w 13919
j 460 175
+ w 13919
+ w 13919
j 300 265
+ p 5970 1
+ w 13925
j 460 235
+ p 5974 1
+ w 13925
j 400 285
+ p 5972 1
+ w 13925
j 400 295
+ s 5986
+ w 13925
j 715 250
+ p 8378 1
+ w 13925
j 580 250
+ p 5978 1
+ w 13925
j 580 295
+ w 13925
+ w 13925
j 460 295
+ w 13925
+ w 13925
j 515 260
+ p 5976 1
+ w 13925
j 515 295
+ w 13925
+ w 13925
j 245 185
+ p 7499 2
+ w 13948
j 255 245
+ p 7600 2
+ w 13948
j 240 230
+ p 7501 2
+ w 13948
j 255 230
+ w 13948
+ w 13948
j 255 180
+ s 8345
+ w 13948
j 255 185
+ w 13948
+ w 13948
j 185 230
+ p 7500 2
+ w 13959
j 210 230
+ p 7501 1
+ w 13959
j 200 230
+ w 13959
+ w 13959
j 190 185
+ p 7498 2
+ w 13959
j 205 185
+ p 7499 1
+ w 13959
j 200 185
+ w 13959
+ w 13959
j 155 230
+ p 7500 1
+ w 13969
j 140 185
+ p 7497 2
+ w 13969
j 150 185
+ p 7498 1
+ w 13969
j 145 185
+ w 13969
+ w 13969
j 580 210
+ p 5978 2
+ w 13977
j 580 170
+ p 7283 C
+ w 13977
j 580 175
+ w 13977
+ w 13977
j 630 185
+ p 6037 2
+ w 13977
j 630 175
+ w 13977
+ w 13977
j 665 180
+ p 6035 2
+ w 13977
j 675 175
+ p 5983 1
+ w 13977
j 665 175
+ w 13977
+ w 13977
j 715 210
+ p 8378 2
+ w 13991
j 705 175
+ p 5983 2
+ w 13991
j 725 175
+ s 8356
+ w 13991
j 715 175
+ w 13991
+ w 13991
j 630 215
+ p 6037 1
+ w 13997
j 665 220
+ p 6035 1
+ w 13997
j 630 235
+ p 6036 2
+ w 13997
j 630 225
+ w 13997
+ w 13997
j 665 230
+ p 6034 2
+ w 13997
j 665 225
+ w 13997
+ w 13997
j 515 130
+ p 12602 +
+ w 14007
j 495 120
+ p 5977 1
+ w 14007
j 540 130
+ p 7283 G
+ w 14007
j 515 135
+ p 7282 P
+ w 14007
j 515 220
+ p 5976 2
+ w 14015
j 515 215
+ p 7282 C
+ w 14015
j 100 185
+ p 7497 1
+ s 10565
j 255 285
+ p 7600 1
+ s 8367
j 105 315
+ p 10546 -
+ s 10557
j 105 275
+ p 10546 +
+ s 10558
j 620 75
+ s 6284
+ p 13391 +
j 715 50
+ p 7346 +
+ s 7348
j 715 90
+ p 7346 -
+ s 7350
@attributes
a 0 s 0 0 0 0 hln 100 PAGETITLE=MODIFIED PAS PREAMPLIFIER
a 0 s 0 0 0 0 hln 100 PAGENO=1
a 0 s 0 0 0 0 hln 100 PAGESIZE=A
a 0 s 0 0 0 0 hln 100 PAGECOUNT=1
@text
s 5 125 45 hln 240 "SPICED" PAS
s 5 635 130 hln 100 (CIA1 = 820//56)
s 5 620 145 hln 100 (CIA2 = 2200//470//180)
s 5 350 220 hln 100 12AX7
s 5 530 210 hln 100 12AX7
s 5 600 105 hln 100 12AX7
s 5 75 160 hln 120 INVERSE RIAA NETWORK
s 5 125 265 hln 120 500KHz POLE
s 5 160 70 hln 100 WORK\PASPHON.SCH  April 27, 1996
s 5 70 315 hln 100 INPUT   SIGNAL
s 5 70 280 hln 100 (easily   moved)
s 5 170 100 hln 200 PHONO PREAMP 