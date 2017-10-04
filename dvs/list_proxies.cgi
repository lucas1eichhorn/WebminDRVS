#!/usr/bin/perl

require './dvs-lib.pl';


&ui_print_header(undef, "Proxies Information", "", "intro", 1, 1, 0,
	&help_search_link(defined(&package_help) ? ( &package_help() ) : ( ),
			  "man", "doc"));

 @tds = ( "height=22");
print &ui_table_start("Proxies list", "align=center");	
print &ui_columns_start(["Proxy","Proxies_Name", "Flags","Sender","Receiver", "Running on nodes"], undef, 0, ["align=center"]);
#Listamos los nodos


foreach $proxy(&list_proxies()){

	print "<tr>";
	print "<td  align=center valign=top>$proxy->{'proxy'}</td>";
	print "<td  align=center valign=top>$proxy->{'prox_name'}</td>";
	print "<td  align=center valign=top>$proxy->{'flags'}</td>";
	print "<td  align=center valign=top>$proxy->{'sender'}</td>";
	print "<td  align=center valign=top>$proxy->{'reciver'}</td>";
	print "<td  align=left valign=top>";
	foreach $node(&get_running_NODE($proxy->{'nodo'})){
		print "<a href='node_info.cgi?idnode=$node->{'idnode'}' title='View node$node->{'idnode'} information'><b><$node->{'idnode'}></b> &nbsp; &nbsp;</a>";
	}
	print "</td>";
	print "</tr>";
}

print &ui_table_end();

#Segunda tabla con los datos del archivo /proxies/procs
print &ui_table_start("Process", "align=center");	
print &ui_columns_start(["Id","name","Type", "lpid","Flag","Misc","Pxsent", "Pxrcvd","Getf","Sendt","Wmig"], undef, 0, ["align=center"]);


foreach $prox(&proxies_procs_info()){

	print "<tr>";
	print "<td  align=center valign=top><b>$prox->{'proxid'}<b></td>";
	print "<td  align=center valign=top><b>$prox->{'name'}<b></td>";
	print "<td  align=center valign=top><b>$prox->{'type'}<b></td>";
	print "<td  align=center valign=top><b>$prox->{'lpid'}<b></td>";
	print "<td  align=center valign=top><b>$prox->{'flag'}<b></td>";
	print "<td  align=center valign=top><b>$prox->{'misc'}<b></td>";
	print "<td  align=center valign=top><b>$prox->{'pxsent'}<b></td>";
	print "<td  align=center valign=top><b>$prox->{'pxrcvd'}<b></td>";
	print "<td  align=center valign=top><b>$prox->{'getf'}<b></td>";
	print "<td  align=center valign=top><b>$prox->{'sendt'}<b></td>";
	print "<td  align=center valign=top><b>$prox->{'wmig'}<b></td>";
	print "</tr>";
}

print &ui_table_end();

&ui_print_footer("menu.cgi", "menu");

