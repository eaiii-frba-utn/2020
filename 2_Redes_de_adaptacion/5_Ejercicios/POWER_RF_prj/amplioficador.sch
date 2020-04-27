<Qucs Schematic 0.0.20>
<Properties>
  <View=0,-40,1787,909,1,0,28>
  <Grid=10,10,1>
  <DataSet=amplioficador.dat>
  <DataDisplay=amplioficador.dpl>
  <OpenDisplay=1>
  <Script=amplioficador.m>
  <RunScript=0>
  <showFrame=0>
  <FrameText0=Título>
  <FrameText1=Dibujado por:>
  <FrameText2=Fecha:>
  <FrameText3=Revisión:>
</Properties>
<Symbol>
</Symbol>
<Components>
  <L L5 1 570 390 -71 -26 0 3 "380 nH" 1 "" 0>
  <GND * 5 690 320 0 0 0 0>
  <L L6 1 570 250 -71 -26 0 3 "100 uH" 1 "" 0>
  <C C5 1 630 320 -26 -63 0 2 "1 nF" 1 "" 0 "neutral" 0>
  <GND *11 5 300 320 0 0 0 0>
  <C C6 1 370 320 -26 -63 0 2 "1 nF" 1 "" 0 "neutral" 0>
  <R R3 1 440 390 -102 -26 1 1 "470 Ohm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "US" 0>
  <GND *3 5 220 750 0 0 0 0>
  <GND *4 5 340 750 0 0 0 0>
  <L L1 1 280 640 -26 -56 1 0 "22 nH" 1 "" 0>
  <GND *6 5 80 740 0 0 0 0>
  <R R5 1 80 690 15 -26 0 1 "50 Ohm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "US" 0>
  <C C2 1 220 700 17 -26 0 1 "63.5 pF" 1 "" 0 "neutral" 0>
  <C C1 1 150 640 -26 -63 0 2 "21.5 pF" 1 "" 0 "neutral" 0>
  <C C9 1 340 700 17 -26 0 1 "124 pF" 1 "" 0 "neutral" 0>
  <L L9 1 440 640 -26 -56 0 2 "2.75 nH" 1 "" 0>
  <GND *1 5 570 750 0 0 0 0>
  <GND *2 5 690 750 0 0 0 0>
  <L L4 1 630 640 -26 -56 1 0 "26 nH" 1 "" 0>
  <C C4s 1 570 700 17 -26 0 1 "180 pF" 1 "" 0 "neutral" 0>
  <R R4 1 890 700 15 -26 0 1 "50 Ohm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "US" 0>
  <GND * 5 890 750 0 0 0 0>
  <C C4 1 690 700 17 -26 0 1 "64 pF" 1 "" 0 "neutral" 0>
  <BOND Line1 1 630 500 -26 9 0 0 "3 mm" 1 "50 um" 1 "2 mm" 1 "0.022e-6" 0 "1" 0 "FREESPACE" 0 "Subst1" 1 "26.85" 0>
  <SUBST Subst1 1 800 150 -30 24 0 0 "2.2" 1 "1.6 mm" 1 "35 um" 1 "6e-4" 1 "0.022e-6" 1 "0.15e-6" 1>
  <.SP SP1 1 40 230 0 78 0 0 "lin" 1 "0.108 GHz" 1 "0.11 GHz" 1 "5" 1 "no" 0 "1" 0 "2" 0 "no" 0 "no" 0>
  <GND *14 5 1640 260 0 0 0 0>
  <GND *15 5 1420 260 0 0 0 0>
  <R R7 1 1640 190 15 -26 0 1 "1.5 Ohm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "US" 0>
  <Pac P1 1 1000 170 -94 -26 1 1 "1" 1 "50 Ohm" 1 "0 dBm" 0 "1 GHz" 0 "26.85" 0>
  <GND * 5 1000 240 0 0 1 2>
  <R R8 1 1420 200 24 -26 0 1 "15 Ohm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "US" 0>
  <C C11 1 1600 120 -26 -63 1 0 "884 pF" 1 "" 0 "neutral" 0>
  <MLIN MS3 1 1470 120 -26 -107 1 0 "Subst1" 1 "6 mm" 1 "10 mm" 1 "Hammerstad" 0 "Kirschning" 0 "26.85" 0>
  <MLIN MS2 1 1360 120 -26 -107 1 0 "Subst1" 1 "3 mm" 1 "31 mm" 1 "Hammerstad" 0 "Kirschning" 0 "26.85" 0>
  <GND *17 5 1130 230 0 0 0 0>
  <GND *18 5 1250 230 0 0 0 0>
  <L L12 1 1190 120 -26 -56 1 0 "22 nH" 1 "" 0>
  <C C13 1 1060 120 -26 -63 0 2 "26 pF" 1 "" 0 "neutral" 0>
  <C C14 1 1250 180 17 -26 0 1 "136 pF" 1 "" 0 "neutral" 0>
  <C C12 1 1130 180 17 -26 0 1 "65 pF" 1 "" 0 "neutral" 0>
  <GND *12 5 1010 490 0 0 0 0>
  <Pac P2 1 1010 430 -94 -26 1 1 "2" 1 "50 Ohm" 1 "0 dBm" 0 "1 GHz" 0 "26.85" 0>
  <GND *20 5 1130 490 0 0 0 0>
  <GND *21 5 1250 490 0 0 0 0>
  <L L13 1 1190 380 -26 -56 1 0 "34.4 nH" 1 "" 0>
  <GND *19 5 1640 520 0 0 0 0>
  <R R9 1 1640 450 15 -26 0 1 "2.5 Ohm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "US" 0>
  <C C15 1 1600 380 -26 -63 1 0 "491.2 pF" 1 "" 0 "neutral" 0>
  <L L11 1 1440 430 -71 -26 0 3 "122 nH" 1 "" 0>
  <GND *16 5 1440 490 0 0 0 0>
  <L L10 1 1390 380 -26 -56 0 2 "16.5 nH" 1 "" 0>
  <MLIN MS1 1 1500 380 -26 -107 1 0 "Subst1" 1 "6 mm" 1 "10 mm" 1 "Hammerstad" 0 "Kirschning" 0 "26.85" 0>
  <C C18 1 1250 440 17 -26 0 1 "72 pF" 1 "" 0 "neutral" 0>
  <C C17 1 1130 440 17 -26 0 1 "49 pF" 1 "" 0 "neutral" 0>
  <C C16 1 1060 380 -26 -63 0 2 "20 pF" 1 "" 0 "neutral" 0>
</Components>
<Wires>
  <570 320 570 360 "" 0 0 0 "">
  <570 320 600 320 "" 0 0 0 "">
  <660 320 690 320 "" 0 0 0 "">
  <570 280 570 320 "" 0 0 0 "">
  <300 320 340 320 "" 0 0 0 "">
  <400 320 440 320 "" 0 0 0 "">
  <440 320 440 360 "" 0 0 0 "">
  <440 200 440 320 "" 0 0 0 "">
  <370 200 440 200 "VGS" 410 170 12 "">
  <570 200 570 220 "" 0 0 0 "">
  <570 200 640 200 "VDD" 640 170 35 "">
  <310 640 340 640 "" 0 0 0 "">
  <220 730 220 750 "" 0 0 0 "">
  <220 640 250 640 "" 0 0 0 "">
  <220 640 220 670 "" 0 0 0 "">
  <340 640 340 670 "" 0 0 0 "">
  <340 730 340 750 "" 0 0 0 "">
  <80 640 120 640 "" 0 0 0 "">
  <80 720 80 740 "" 0 0 0 "">
  <80 640 80 660 "" 0 0 0 "">
  <180 640 220 640 "" 0 0 0 "">
  <340 640 410 640 "" 0 0 0 "">
  <560 800 620 800 "" 0 0 0 "">
  <570 730 570 750 "" 0 0 0 "">
  <690 730 690 750 "" 0 0 0 "">
  <660 640 690 640 "" 0 0 0 "">
  <490 640 570 640 "" 0 0 0 "">
  <570 640 600 640 "" 0 0 0 "">
  <570 640 570 670 "" 0 0 0 "">
  <690 640 690 670 "" 0 0 0 "">
  <890 730 890 750 "" 0 0 0 "">
  <890 640 890 670 "" 0 0 0 "">
  <690 640 890 640 "" 0 0 0 "">
  <1640 220 1640 260 "" 0 0 0 "">
  <1640 120 1640 160 "" 0 0 0 "">
  <1630 120 1640 120 "" 0 0 0 "">
  <1500 120 1570 120 "" 0 0 0 "">
  <1420 230 1420 260 "" 0 0 0 "">
  <1390 120 1420 120 "" 0 0 0 "">
  <1420 120 1440 120 "" 0 0 0 "">
  <1420 120 1420 170 "" 0 0 0 "">
  <1000 200 1000 240 "" 0 0 0 "">
  <1000 120 1000 140 "" 0 0 0 "">
  <1000 120 1030 120 "" 0 0 0 "">
  <1130 210 1130 230 "" 0 0 0 "">
  <1090 120 1130 120 "" 0 0 0 "">
  <1130 120 1160 120 "" 0 0 0 "">
  <1130 120 1130 150 "" 0 0 0 "">
  <1220 120 1250 120 "" 0 0 0 "">
  <1250 120 1330 120 "" 0 0 0 "">
  <1250 120 1250 150 "" 0 0 0 "">
  <1250 210 1250 230 "" 0 0 0 "">
  <1010 380 1030 380 "" 0 0 0 "">
  <1010 460 1010 490 "" 0 0 0 "">
  <1010 380 1010 400 "" 0 0 0 "">
  <1220 380 1250 380 "" 0 0 0 "">
  <1130 470 1130 490 "" 0 0 0 "">
  <1090 380 1130 380 "" 0 0 0 "">
  <1130 380 1160 380 "" 0 0 0 "">
  <1130 380 1130 410 "" 0 0 0 "">
  <1250 380 1250 410 "" 0 0 0 "">
  <1250 470 1250 490 "" 0 0 0 "">
  <1250 380 1360 380 "" 0 0 0 "">
  <1640 480 1640 520 "" 0 0 0 "">
  <1640 380 1640 420 "" 0 0 0 "">
  <1630 380 1640 380 "" 0 0 0 "">
  <1530 380 1570 380 "" 0 0 0 "">
  <1440 460 1440 490 "" 0 0 0 "">
  <1420 380 1440 380 "" 0 0 0 "">
  <1440 380 1470 380 "" 0 0 0 "">
  <1440 380 1440 400 "" 0 0 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
</Paintings>
