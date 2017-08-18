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
foreach $line(&execute_ssh()){
print "<h6>".$line."</h6>";
}
