#!/usr/bin/perl
# list_dc.cgi
# Modulo que presenta el listado de nodos las maquinas virtuales levantadas en el nodo
# Se listan las carpetas contenidas en  /proc/drvs/ correspondientes a DCs

require './dvs-lib.pl';


&ui_print_header(undef, "Distributed Containers", "", "intro", 1, 1, 0,
	&help_search_link(defined(&package_help) ? ( &package_help() ) : ( ),
			  "man", "doc"));



print &ui_table_start("Running DCs on ".&connected_node_name(), "align=center");	
print &ui_columns_start(["DC name"], undef, 2, ["align=center", "align=center"]);
#Listamos las maquinas virtuales en el nodo
foreach $dc(&dc_running_list()){

	print "<tr>";
	print "<td  align=left valign=top><b><a href='dc_info.cgi?dc_name=$dc->{'dc_name'}' title='View $dc->{'dc_name'} information '><b>$dc->{'dc_name'}</b></a></td>";
	print "</tr>";
}

print &ui_table_end();

&ui_print_footer("menu.cgi", "menu");