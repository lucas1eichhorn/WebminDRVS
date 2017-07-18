#!/usr/bin/perl
# list_dns.cgi
# Example

#require './hello-lib.pl';
use WebminCore;

require './hello-lib.pl';
&ui_print_header(undef, "Modulo de prueba", "", "intro", 1, 1, 0,
	&help_search_link(defined(&package_help) ? ( &package_help() ) : ( ),
			  "man", "doc"));

print ui_form_start('save.cgi');
print &ui_table_start("Tabla", "align=center", 2);
# IP address
print &ui_table_row("Titulo 1",
	&ui_textbox("address", "texto1", 30));

print &ui_table_end();
print ui_form_end([ [ undef, 'Save' ] ]);
&ui_print_footer("list_hosts.cgi", "volver");