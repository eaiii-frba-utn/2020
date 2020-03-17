The two files included in this zip ("SA612.asc" & "SA612.asy") implement an LTSpice circuit model for the Signetics NE602/SA612 mixer/oscillator IC. The ".asc" file is a schematic equivalent circuit of the IC, and the ".asy" file is a symbol that will appear on the LTSpice schematic editor to represent the circuit.

To install the circuit model:
1) In the LTSPice folder tree, navigate to the "sym" folder and create a new folder of your choice there (eg, "MyFiles")
2) Copy both of the files to the new "MyFiles" folder that you just created.
3) In the LTSpice schematic editor, click on the "Component" icon in the icon bar.
4) At the top of the "Select Component Symbol" window, drop down the list box that says "Top Directory". Select ".../lib/sym/MyFiles".
5) Select the component "SA612" and drop it into your schematic.

You can modify the behavior of the component model by opening "SA612.asc" in the schematic editor.

The file "NE602 Rx.asc" is a basic receiver implemented with this model.

A special ".plt" file is included to display impedances in the circuit in both series and parallel R/jX form. To use it, first save "plot.defs" to the SWCADIII (or LTSpiceIV) folder. Then, from the "Plot Settings" menu, select "Open Plot Settings" and select "SA612 Input R+jX.plt". You display an impedance as the ratio of a node voltage to the node current. Right click on one of the plot labels at the top of the plot display to see an example.

The model was built by carefully analyzing the SA612 data sheet schematic, observing actual DC pin voltage and current measurements at various supply voltages, and filling in the unknown blocks and values based on some informed assumptions about what would be possible on a piece of silicon. It is not fully AC tested yet, so any comments or improvements are greatly appreciated.

Contact:
Joe Rocci
W3JDR
joe@roccis.com