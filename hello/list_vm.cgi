#!/usr/bin/perl
# list_vm.cgi
# Modulo que presenta el listado de nodos las maquinas virtuales levantadas en el nodo
# Se listan las carpetas contenidas en  /proc/drvs/ correspondientes a VMs

require './hello-lib.pl';


&ui_print_header(undef, "Virtual Machines", "", "intro", 1, 1, 0,
	&help_search_link(defined(&package_help) ? ( &package_help() ) : ( ),
			  "man", "doc"));



print &ui_table_start("Running VMs on ".&connected_node_name(), "align=center");	
print &ui_columns_start(["VM name"], undef, 2, ["align=center", "align=center"]);
#Listamos las maquinas virtuales en el nodo
foreach $vm(&vm_running_list()){

	print "<tr>";
	print "<td  align=left valign=top><b><a href='vm_info.cgi?vm_name=$vm->{'vm_name'}' title='View $vm->{'vm_name'} information '><b>$vm->{'vm_name'}</b></a></td>";
	print "</tr>";
}

print &ui_table_end();

&ui_print_footer("menu.cgi", "menu");