#!/usr/bin/perl
# menu.cgi
# Muestra el menu de la pantalla inicial con iconos

require './hello-lib.pl';
use CGI;
my $req = CGI->new;
  $host_param = $req->param('host');
   $user_param = $req->param('user');
    $pass_param = $req->param('pass');

my $connect=&connect_node_ssh($host_param,$user_param,$pass_param);

if($connect){

local $hostname=&connected_node_name();
&ui_print_header(undef, "DRVS Administration - $hostname", '', undef, 1, 1, 0,	&help_search_link(' hosts', 'man'));


	print "<div class='row icons-row vertical-align' style='padding-left:170px;'>";
	
	##DRVS
	print "<div class='col-xs-1 icons-container forged-xx-skip grayscaled animated' style='min-height:150px; min-width:150px;'> ";
	print "<a href='drvs_info.cgi' class='icon_link' style='text-decoration: none;'>";
	print "<img class='ui_icon ui_icon_protected' src='images/drvs.gif' alt='' style='min-height:100px; min-width:100px;'><br>DRVS info</a>";
	print "</div>";


		
	##NODES
	print "<div class='col-xs-1 icons-container forged-xx-skip grayscaled animated' style='min-height:150px; min-width:150px;'> ";
	print "<a href='list_nodes.cgi' class='icon_link' style='text-decoration: none;'>";
	print "<img class='ui_icon ui_icon_protected' src='images/nodes.gif' alt='' style='min-height:100px; min-width:100px;'><br>Nodes</a>";
	print "</div>";

	##VMs
	print "<div class='col-xs-1 icons-container forged-xx-skip grayscaled animated' style='min-height:150px; min-width:150px;'> ";
	print "<a href='list_vm.cgi' class='icon_link' style='text-decoration: none;'>";
	print "<img class='ui_icon ui_icon_protected' src='images/vm.png' alt='' style='min-height:100px; min-width:100px;'><br>Virtual Machines</a>";
	print "</div>";


	#Proxies
	print "<div class='col-xs-1 icons-container forged-xx-skip grayscaled animated' style='min-height:150px; min-width:150px;'> ";
	print "<a href='list_proxies.cgi' class='icon_link' style='text-decoration: none;'>";
	print "<img class='ui_icon ui_icon_protected' src='images/proxy.png' alt='' style='min-height:100px; min-width:100px;'><br>Proxies</a>";
	print "</div>";


	print "</div>";

}else{
	&ui_print_header(undef, "DRVS Administration", '', undef, 1, 1, 0,	&help_search_link('ifconfig hosts resolve.conf nsswitch.conf', 'man'));
	print "$connect";
print "<div class='alert alert-danger text-center' style='margin-bottom: 4px; '>";
print "<i class='fa fa-fw fa-exclamation-circle'></i> <strong>Error!</strong><br>";
if($host_param!=""){
print "<h3>Cannot conect to node $host_param</h3>";
}else{

print "<h3>Cannot conect to node".&connected_node_name()."</h3>";
}


print "</div>";
	
}
&ui_print_footer("login.cgi?hostname=".&connected_node_name(), "login");


