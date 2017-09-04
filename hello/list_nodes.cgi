#!/usr/bin/perl
# list_dns.cgi
# Example

require './hello-lib.pl';


&ui_print_header(undef, "Nodes Information", "", "intro", 1, 1, 0,
	&help_search_link(defined(&package_help) ? ( &package_help() ) : ( ),
			  "man", "doc"));
my $filename = "/proc/drvs/nodes";
open(my $fh, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";
  
=pod
while (my $row = <$fh>) {
  chomp $row;
 print "$row<br>";
}
=cut


#print ui_form_start('save.cgi');

#print &ui_table_start("Nodes", ["align=center"], 7);
#print &ui_table_row("Titulo 1",	"ASDa");
#	print &ui_table_row("Titulo 2",	"ASDa",4);
#	print &ui_table_row("Titulo 3",	"ASDa",4);
#	print &ui_table_row("Titulo 4",	"ASDa",4);
	#print &ui_table_row("Hola",
 @tds = ( "height=22");
print &ui_table_start("Nodes list", "align=center");	
print &ui_columns_start(["ID","Name","Flags","Proxies","PX msg Sent","PX msg Received","Runnign MV"], undef, 0, ["align=center"]);
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
foreach $vm(&get_running_VM($node->{'host'})){
print "<a href='vm_info.cgi?idVM=$vm->{'VMid'}' title='View VM$vm->{'VMid'} information'><b><$vm->{'VMid'}></b> &nbsp; &nbsp;</a>";
}
print "</td>";
print "</tr>";
}
#print &ui_form_end([ [ undef, 'Add node' ] ]);
print &ui_table_end();

&ui_print_footer("menu.cgi", "menu");