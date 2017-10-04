#!/usr/bin/perl
# list_hosts.cgi
# Modulo que presenta el listado de nodos cargados como pantalla de inicio
# Se lee la informacion contenida en el archivo /etc/hosts

require './dvs-lib.pl';


&ui_print_header(undef, "DVS Administration", "", "intro", 1, 1, 0,
	&help_search_link(defined(&package_help) ? ( &package_help() ) : ( ),
			  "man", "doc"));



print &ui_table_start("Hosts ", "align=center");	
print &ui_columns_start(["Hostname","IP"], undef, 2, ["align=center", "align=center"]);
#Listamos los host
foreach $host(&list_hosts()){

	print "<tr>";
	print "<td  align=left valign=top><b><a href='login.cgi?hostname=$host->{'hostname'}' title='Connect to $host->{'hostname'} '><b>$host->{'hostname'}</b></a></td>";
	print "<td  align=left valign=top><b>$host->{'ip'}<b></td>";
	print "</tr>";
}

print &ui_table_end();

&ui_print_footer("", "Main");