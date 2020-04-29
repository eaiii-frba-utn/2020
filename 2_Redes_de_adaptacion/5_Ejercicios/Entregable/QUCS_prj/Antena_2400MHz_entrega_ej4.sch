<Qucs Schematic 0.0.20>
<Properties>
  <View=0,0,1418,800,1,0,0>
  <Grid=10,10,1>
  <DataSet=Antena_2400MHz_entrega_ej4.dat>
  <DataDisplay=Antena_2400MHz_entrega_ej4.dpl>
  <OpenDisplay=1>
  <Script=Antena_2400MHz_entrega_ej4.m>
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
  <L L1 1 430 170 -26 10 0 0 "23 nH" 1 "" 0>
  <GND * 5 500 290 0 0 0 0>
  <GND * 5 260 290 0 0 0 0>
  <GND * 5 100 290 0 0 0 0>
  <Pac P1 1 100 220 18 -26 0 1 "1" 1 "50 Ohm" 1 "0 dBm" 0 "1 GHz" 0 "26.85" 0>
  <R R1 1 500 230 15 -26 0 1 "90 Ohm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "US" 0>
  <C C1 1 330 170 -26 -63 1 0 "0.2 pF" 1 "" 0 "neutral" 0>
  <C C2 1 260 220 17 -26 0 1 "0.6 pF" 1 "" 0 "neutral" 0>
  <.SP SP1 1 660 160 0 77 0 0 "lin" 1 "2 GHz" 1 "3 GHz" 1 "41" 1 "no" 0 "1" 0 "2" 0 "no" 0 "no" 0>
</Components>
<Wires>
  <100 250 100 290 "" 0 0 0 "">
  <100 170 100 190 "" 0 0 0 "">
  <260 250 260 290 "" 0 0 0 "">
  <100 170 260 170 "" 0 0 0 "">
  <260 170 300 170 "" 0 0 0 "">
  <260 170 260 190 "" 0 0 0 "">
  <360 170 400 170 "" 0 0 0 "">
  <460 170 500 170 "" 0 0 0 "">
  <500 170 500 200 "" 0 0 0 "">
  <500 260 500 290 "" 0 0 0 "">
</Wires>
<Diagrams>
  <Smith 900 460 310 310 3 #c0c0c0 1 00 1 0 1 1 1 0 4 1 1 0 1 1 315 0 225 "" "" "" "">
	<"S[1,1]" #0000ff 0 3 0 0 0>
	  <Mkr 2.4e+09 17 -199 3 0 0 1>
  </Smith>
</Diagrams>
<Paintings>
</Paintings>
