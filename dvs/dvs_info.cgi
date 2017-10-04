#!/usr/bin/perl
# dvs_info.cgi
# Muestra la informacion del dvs en el nodo actual
# Se lee la informacion del archiv /proc/drvs/info

require './dvs-lib.pl';
use CGI;
$request = new CGI;
my $idnode = $request->param('idnode');

#header
&ui_print_header(undef, "DVS Information", "", "intro", 1, 1, 0,
	&help_search_link(defined(&package_help) ? ( &package_help() ) : ( ),
			  "man", "doc"));
		local (@hcols, @tds);
		push(@tds, "width=5 align=center", "width=10% nowrap align=center");

local $hostname=&connected_node_name();
print &ui_table_start("Running on: $hostname", undef, 2);
	
foreach $node(&node_info($idnode)){

#print &ui_table_row("$node->{name}", "$node->{value}",undef,\@tds  );
print "<tr>";
print "<td width='25%' align=left valign=top style='padding-left:15px !important;'><i class='fa fa-caret-right'aria-hidden='true'></i>&nbsp; &nbsp;<b>$node->{'name'}:<b></td>";
print "<td width='75%' align=left valign=top>$node->{'value'}</td>";
print "</tr>";
}
	
print &ui_table_end();




#print ui_form_start('save.cgi');


&ui_print_footer("menu.cgi", "menu");