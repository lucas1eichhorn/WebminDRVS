#!/usr/bin/perl
# list_dns.cgi
# Example

require './hello-lib.pl';
use CGI;
$request = new CGI;
my $idnode = $request->param('idnode');

#header
&ui_print_header(undef, "DRVS Information", "", "intro", 1, 1, 0,
	&help_search_link(defined(&package_help) ? ( &package_help() ) : ( ),
			  "man", "doc"));
		local (@hcols, @tds);
		push(@tds, "width=5 align=center", "width=10% nowrap align=center");
#print &ui_form_start("create_route.cgi", "post");
	print &ui_table_start("Node$idnode", undef, 2);
foreach $node(&node_info($idnode)){

#print &ui_table_row("$node->{name}", "$node->{value}",undef,\@tds  );
print "<tr>";
print "<td width='25%' align=left valign=top style='padding-left:15px !important;'><i class='fa fa-caret-right'aria-hidden='true'></i>&nbsp; &nbsp;<b>$node->{name}:<b></td>";
print "<td width='75%' align=left valign=top>$node->{value}</td>";
print "</tr>";
}
	
print &ui_table_end();


#print ui_form_start('save.cgi');


&ui_print_footer("", "DRVS Administration");