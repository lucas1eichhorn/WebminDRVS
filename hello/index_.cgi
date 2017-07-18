#!/usr/bin/perl
# index.cgi
# Display the user's current language, theme and password

use strict;
use warnings;
require './hello-lib.pl';
our (%text, %access, $base_remote_user, $default_lang, %gconfig);
&ui_print_header(undef, $text{'index_title'}, "", undef, 0, 1);

my @users = &acl::list_users();
my ($user) = grep { $_->{'name'} eq $base_remote_user } @users;


print &text('index_desc2', "hola"),"<p>\n";
print ui_form_start("save.cgi");

print ui_table_row($text{'edit_username'},
    ui_textbox("username", "LUCAS", 40));

print ui_table_row($text{'edit_pass'},
    ui_password("pass", "Password", 40));

print ui_form_end([ [ undef, $text{'save'} ], [ 'delete', $text{'delete'} ] ]);

&ui_print_footer("/", $text{'index'});

