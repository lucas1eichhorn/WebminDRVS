#!/usr/bin/perl
# list_dns.cgi
# Example

require './hello-lib.pl';
use CGI;
$request = new CGI;
my $vm_name = $request->param('vm_name');

#header
&ui_print_header(undef, "VM Information", "", "intro", 1, 1, 0,
	&help_search_link(defined(&package_help) ? ( &package_help() ) : ( ),
			  "man", "doc"));
		local (@hcols, @tds);
		push(@tds, "width=5 align=center", "width=10% nowrap align=center");
		
#print &ui_form_start("create_route.cgi", "post");
##Informacion de la Maquina Virtual
	print &ui_table_start("$vm_name", undef, 2);
foreach $VM(&vm_info($vm_name)){

#print &ui_table_row("$node->{name}", "$node->{value}",undef,\@tds  );

print "<tr>";
print "<td width='25%' align=left valign=top style='padding-left:15px !important;'><i class='fa fa-caret-right'aria-hidden='true'></i>&nbsp; &nbsp;<b>$VM->{name}:<b></td>";
#verificamos si la fila correponde a un dato o al listado de nodos en ejecucion
if($VM->{'nodes_list'}!=1){
print "<td width='75%' align=left valign=top>$VM->{value}</td>";
}else{
##si es el listado de nodos, ingresamos los links para acceder a la informacion
print "<td  align=left valign=top>";
foreach $node(&get_running_NODE($VM->{'value'})){
print "<a href='node_info.cgi?idnode=$node->{'idnode'}' title='View node$node->{'idnode'} information'><b><$node->{'idnode'}></b> &nbsp; &nbsp;</a>";
}
print "</td>";
}

print "</tr>";
}
	
print &ui_table_end();
print "<div class='clear-fix'>&nbsp;</div>";

##Informacion de los procesos ejecuntadose en la VM
	print &ui_table_start("Process", undef, 2);
	print &ui_columns_start(["<b>VM</b>", "<b>p_nr</b>", "<b>endp</b>", "<b>lpid</b>", "<b>node</b>","<b>flag</b>", "<b>misc</b>", "<b>getf</b>", "<b>sndt</b>", "<b>wmig</b>", "<b>prxy</b>", "<b>name</b>"], undef, 0, ["align=center"]);

foreach $proc(&vm_procs_info($vm_name)){

#colocamos los campos de cada proceso en su columna
print "<tr>";
print "<td  align=center valign=top>$proc->{'VMid'}</td>";
print "<td  align=center valign=top>$proc->{'p_nr'}</td>";
print "<td  align=center valign=top>$proc->{'endp'}</td>";
print "<td  align=center valign=top>$proc->{'lpid'}</td>";
print "<td  align=center valign=top>$proc->{'node'}</td>";
print "<td  align=center valign=top>$proc->{'flag'}</td>";
print "<td  align=center valign=top>$proc->{'misc'}</td>";
print "<td  align=center valign=top>$proc->{'getf'}</td>";
print "<td  align=center valign=top>$proc->{'sndt'}</td>";
print "<td  align=center valign=top>$proc->{'wmig'}</td>";
print "<td  align=center valign=top>$proc->{'proxy'}</td>";
print "<td  align=center valign=top>$proc->{'name'}</td>";
print "</tr>";

}
	
print &ui_table_end();
print "<div class='clear-fix'>&nbsp;</div>";


##Stats
	print &ui_table_start("Stats", undef, 2);
	print &ui_columns_start(["<b>VM</b>", "<b>p_nr</b>", "<b>endp</b>", "<b>lpid</b>", "<b>node</b>","<b>lsnt</b>", "<b>rsnt/b>", "<b>lcopy</b>", "<b>rcopy</b>"], undef, 0, ["align=center"]);

foreach $stat(&vm_stats_info($idVM)){

#colocamos los campos de stat en su columna
print "<tr>";
print "<td  align=center valign=top>$stat->{'VMid'}</td>";
print "<td  align=center valign=top>$stat->{'p_nr'}</td>";
print "<td  align=center valign=top>$stat->{'endp'}</td>";
print "<td  align=center valign=top>$stat->{'lpid'}</td>";
print "<td  align=center valign=top>$stat->{'node'}</td>";
print "<td  align=center valign=top>$stat->{'lsnt'}</td>";
print "<td  align=center valign=top>$stat->{'rsnt'}</td>";
print "<td  align=center valign=top>$stat->{'lcopy'}</td>";
print "<td  align=center valign=top>$stat->{'rcopy'}</td>";
print "</tr>";

}
	
print &ui_table_end();



#print ui_form_start('save.cgi');


&ui_print_footer("", "DRVS Administration");