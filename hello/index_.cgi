#!/usr/bin/perl
# index.cgi
# Muestra el menu de la pantalla inicial con iconos

require './hello-lib.pl';
&ui_print_header(undef, 'DRVS Administration', '', undef, 1, 1, 0,
	&help_search_link('ifconfig hosts resolve.conf nsswitch.conf', 'man'));

	print "<div class='row icons-row vertical-align' style='padding-left:170px;'>";
	
##DRVS
print "<div class='col-xs-1 icons-container forged-xx-skip grayscaled animated' style='min-height:150px; min-width:150px;'> ";
print "<a href='drvs_info.cgi' class='icon_link' style='text-decoration: none;'>";
print "<img class='ui_icon ui_icon_protected' src='images/drvs.gif' alt='' style='min-height:100px; min-width:100px;'><br>DRVS</a>";
print "</div>";


	
##NODES
print "<div class='col-xs-1 icons-container forged-xx-skip grayscaled animated' style='min-height:150px; min-width:150px;'> ";
print "<a href='list_nodes.cgi' class='icon_link' style='text-decoration: none;'>";
print "<img class='ui_icon ui_icon_protected' src='images/nodes.gif' alt='' style='min-height:100px; min-width:100px;'><br>Nodes</a>";
print "</div>";

##VMs
print "<div class='col-xs-1 icons-container forged-xx-skip grayscaled animated' style='min-height:150px; min-width:150px;'> ";
print "<a href='vm_info.cgi?idVM=0' class='icon_link' style='text-decoration: none;'>";
print "<img class='ui_icon ui_icon_protected' src='images/vm.png' alt='' style='min-height:100px; min-width:100px;'><br>Virtual Machines</a>";
print "</div>";


#Proxies
print "<div class='col-xs-1 icons-container forged-xx-skip grayscaled animated' style='min-height:150px; min-width:150px;'> ";
print "<a href='ssh.cgi' class='icon_link' style='text-decoration: none;'>";
print "<img class='ui_icon ui_icon_protected' src='images/proxy.png' alt='' style='min-height:100px; min-width:100px;'><br>Proxies</a>";
print "</div>";


print "</div>";

&ui_print_footer('/', $text{'index'});

