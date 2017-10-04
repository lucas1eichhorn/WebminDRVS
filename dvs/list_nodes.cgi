#!/usr/bin/perl
# list_dns.cgi
# Example

require './dvs-lib.pl';


&ui_print_header(undef, "Nodes Information", "", "intro", 1, 1, 0,
	&help_search_link(defined(&package_help) ? ( &package_help() ) : ( ),
			  "man", "doc"));


 @tds = ( "height=22");
print &ui_table_start("Nodes list", "align=center");	
print &ui_columns_start(["ID","Name","Flags","Proxies","PX msg Sent","PX msg Received","Runnign DC"], undef, 0, ["align=center"]);
#Listamos los nodos
foreach $node(&list_nodes()){

print "<tr>";
print "<td  align=center valign=top><b>$node->{'id'}<b></td>";
print "<td  align=center valign=top><b><a href='node_info.cgi?idnode=$node->{'id'}' title='View $node->{'name'} information'></b>$node->{'name'}<b></a></td>";
print "<td  align=center valign=top><b>$node->{'flags'}<b></td>";
print "<td  align=center valign=top><b>$node->{'proxies'}<b></td>";
print "<td  align=center valign=top><b>$node->{'pxsent'}<b></td>";
print "<td  align=center valign=top><b>$node->{'pxrcvd'}<b></td>";
print "<td  align=center valign=top>";
foreach $dc(&get_running_DC($node->{'host'})){
print "<a href='dc_info.cgi?idDC=$dc->{'DCid'}' title='View DC$dc->{'DCid'} information'><b><$dc->{'DCid'}></b> &nbsp; &nbsp;</a>";
}
print "</td>";
print "</tr>";
}
#print &ui_form_end([ [ undef, 'Add node' ] ]);
print &ui_table_end();

&ui_print_footer("menu.cgi", "menu");