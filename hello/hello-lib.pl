BEGIN { push(@INC, ".."); };

use WebminCore;
 
&init_config();

# list_hosts()
# obtiene la informacion de los host cargados en /etc/hosts
sub list_hosts
{
local @rv;

local $line="";

&open_readfile(HOSTS, "/etc/hosts");
while($line=<HOSTS>) {
	##analizamos la linea, si tiene una IP corresponde a un host
	if (!($line =~ /\#/) && ($line=~ /[0-9a-zA-Z]/) ){
	#separamos cada columna por los espacios (REGEXP) y los guardamos en una array
		local(@f)=split(/\s+/, $line);
	local($ip)=@f[0];
	local($hostname)=@f[1];

	
	#colocamos cada campo en un array hash
		push(@rv, { 'ip' => $ip,
					'hostname'=>$hostname,
					'line'=> $line
				
			     });
		}
	}
	
close(HOSTS);
return @rv;
}



# list_nodes()
# obtiene la informacion de los nodos activos de /proc/drvs/nodes
sub list_nodes
{
local @rv;

local $line="";

#&open_readfile(NODES, "/proc/drvs/nodes");
my $file=&execute_ssh_command("cat /proc/drvs/nodes");
local @lines=split(/\n/,$file);
foreach $line(@lines){
	##analizamos la linea, si tiene---X corresponde a un nodo, sino es el titulo del archivo
	if ($line =~ m/-X/){
	#separamos cada columna por los espacios (REGEXP) y los guardamos en una array
		local(@f)=split(/\s+/, $line);
	local($id)=@f[1];
	local($flags)=@f[2];
	local($proxies)=@f[3];
	local($pxsent)=@f[4];
	local($pxrcvd)=@f[5];
	local($host)=@f[6];
	local($name)=@f[7];
	
	#colocamos cada campo en un array hash
		push(@rv, { 'id' => $id,
					'flags'=>$flags,
					'proxies'=>$proxies,
					'pxsent'=>$pxsent,
					'pxrcvd'=>$pxrcvd,
					'host'=>$host,
					'name'=>$name,			   
					'line'=> $line,
				
			     });
		}
	}
	

return @rv;
}


# vm_info()
# obtiene la informacion de una maquina virtual pasada como parametro - lee el archivo /proc/drvs/VMo/info
sub vm_info
{
 my  @args = @_;
 my  $idVM=@args[0];
local @rv;

local $line="";

#&open_readfile(VM, "/proc/drvs/VM$idVM/info");
my $file=&execute_ssh_command("cat /proc/drvs/VM$idVM/info");
local @lines=split(/\n/,$file);
foreach $line(@lines){
	##analizamos la linea, si tiene = es un campo de informacion de la MV
	if ($line =~ m/=/){
	
	#separamos cada columna por los espacios (REGEXP) y los guardamos en una array
	
		local(@f)=split(/=/, $line);
	local($name)=@f[0];
	local($value)=@f[1];
	
	
	#colocamos cada campo en un array hash
		push(@rv, { 'name' => $name,
					'value'=>$value,
								   
					'line'=> $line,
				
			     });
	}else{
	#en caso contrario verificamos si es la linea que contiene la informacion 
	#de los nodos en que se ejecuta la MV
	if ($line =~ m/X+/){
	#colocamos cada campo en un array hash
		push(@rv, { 'name' => 'Running in nodes',
					
								   
					'value'=> $line,
					'nodes_list'=>1
				
			     });
	}
	}	
	}
	

return @rv;
}

# node_info()
# obtiene la informacion del nodo local - lee el archivo /proc/drvs/info
sub node_info
{
 my  @args = @_;
 my  $idnode=@args[0];
local @rv;

my $file=&execute_ssh_command("cat /proc/drvs/info");
#&open_readfile(NODE, "/proc/drvs/info");


local @lines=split(/\n/,$file);
foreach $line(@lines){
	##analizamos la linea, si tiene = es un campo de informacion del nodo
	if ($line =~ m/=/){
	
	#separamos cada columna por los espacios (REGEXP) y los guardamos en una array
	
		local(@f)=split(/=/, $line);
	local($name)=@f[0];
	local($value)=@f[1];
	
	
	#colocamos cada campo en un array hash
		push(@rv, { 'name' => $name,
					'value'=>$value,
								   
					'line'=> $line,
				
			     });
	}	
	}
	

return @rv;

}


# vm_procs_info
# obtiene la informacion de los procesos activos en la VM pasada como parametro
# leyendo el archivo /proc/drvs/VMx/procs
sub vm_procs_info
{
 my  @args = @_;
 my  $idVM=@args[0];
local @rv;

local $line="";

#&open_readfile(PROC, "/proc/drvs/VM$idVM/procs");
my $file=&execute_ssh_command("cat /proc/drvs/VM$idVM/procs");
local $i=0;
local @lines=split(/\n/,$file);
foreach $line(@lines){
	##analizamos la linea, la primera linea posee los titulos
	if ($i!=0&&$line =~ m/[0-9a-zA-Z]/){
	#separamos cada columna por los espacios (REGEXP) y los guardamos en una array
	local(@f)=split(/\s+/, $line);
	local($VMid)=@f[1];
	local($p_nr)=@f[2];
	local($endp)=@f[3];
	local($lpid)=@f[4];
	local($node)=@f[5];
	local($flag)=@f[6];
	local($misc)=@f[7];
	local($getf)=@f[8];
	local($sndt)=@f[9];
	local($wmig)=@f[10];
	local($proxy)=@f[11];
	local($name)=@f[12];
	
	#colocamos cada campo en un array hash
		push(@rv, { 'VMid' => $VMid,
					'p_nr'=>$p_nr,
					'endp'=>$endp,
					'lpid'=>$lpid,
					'node'=>$node,
					'flag'=>$flag,
					'misc'=>$misc,			   
					'getf'=> $getf,
					'sndt'=> $sndt,
					'wmig'=> $wmig,
					'proxy'=> $proxy,
					'name'=>$name,
					'line'=>$line
				
			     });
		
		
	}
	$i++;
	}
close(PROC);
return @rv;
}


# vm_stats_info
# obtiene la informacion de stats en la VM pasada como parametro
# leyendo el archivo /proc/drvs/VMx/stats
sub vm_stats_info
{
 my  @args = @_;
 my  $idVM=@args[0];
local @rv;

local $line="";

#&open_readfile(STAT, "/proc/drvs/VM$idVM/stats");
my $file=&execute_ssh_command("cat /proc/drvs/VM$idVM/stats");

local $i=0;

local @lines=split(/\n/,$file);
foreach $line(@lines){
	##analizamos la linea, la primera linea posee los titulos
	if ($i!=0&&$line =~ m/[0-9a-zA-Z]/){
	#separamos cada columna por los espacios (REGEXP) y los guardamos en una array
	local(@f)=split(/\s+/, $line);
	local($VMid)=@f[1];
	local($p_nr)=@f[2];
	local($endp)=@f[3];
	local($lpid)=@f[4];
	local($node)=@f[5];
	local($lsnt)=@f[6];
	local($rsnt)=@f[7];
	local($lcopy)=@f[8];
	local($rcopy)=@f[9];

	
	#colocamos cada campo en un array hash
		push(@rv, { 'VMid' => $VMid,
					'p_nr'=>$p_nr,
					'endp'=>$endp,
					'lpid'=>$lpid,
					'node'=>$node,
					'lsnt'=>$lsnt,
					'rsnt'=>$rsnt,			   
					'lcopy'=> $lcopy,
					'rcopy'=> $rcopy,
					'line'=>$line
				
			     });
		
		
	}
	$i++;
	}

return @rv;
}

#get_running_VM
#metodo que devuelve un arreglo con los ids de la maquina que se estan ejecutando en el nodo, a partir de un string como parametro
#El string de parametro es del tipo -----X, donde X se encuentra en la posicion correspondiente al id de la VM
sub get_running_VM(){
local @id_list;
my @args=@_;

my $string = @args[0];
  my $char = 'X';
  my $offset = 0;

  my $result = index($string, $char, $offset);
local $str_len=length($string);
  while ($result != -1) {

    #colocamos cada campo en un array hash
	
		push(@id_list, { 'VMid' => $str_len-$result-1});

    $offset = $result + 1;
    $result = index($string, $char, $offset);

  }
  return @id_list;
}
#get_running_NODES
#metodo que devuelve un arreglo con los id del nodo que se estan ejecutando la VM, a partir de un string como parametro
#El string de parametro es del tipo -----X, donde X se encuentra en la posicion correspondiente al id del nodo
sub get_running_NODE(){
local @id_list;
my @args=@_;

my $string = @args[0];

  my $char = 'X';
  my $offset = 0;

  my $result = index($string, $char, $offset);
local $str_len=length($string);
  while ($result != -1) {

    #colocamos cada campo en un array hash
	
		push(@id_list, { 'idnode' => $str_len-$result-2});

    $offset = $result + 1;
    $result = index($string, $char, $offset);

  }
  return @id_list;
}
#metodo que permite conectarse a uno nodo mediante ssh
sub connect_node_ssh(){

my @args=@_;

local $node=@args[0];
local $usr=@args[1];
local $pass=@args[2];

#guardamos los datos de login en un archivo las futuras conexiones
&store_login_data($node,$usr,$pass);

local $command="cat /proc/drvs/info";

my $cmd = "cd /usr/local/webmin/hello; ./execute_ssh.sh $node $usr $pass \"$command\"";
my $Output = `$cmd`;

return $Output ;
}

#metodo que permite ejecutar un comando en un nodo remoto mediante ssh
#se leen las credenciales del archivo login.dat
sub execute_ssh_command(){

my @args=@_;
#leemos las credenciales de login del archivo
local $command=@args[0];
open my $handle, '<', 'login.dat';
chomp(my @connection_data = <$handle>);
close $handle;

#ejecutamos el comando mediante sshpass en el nodo remoto, con las credenciales obtenidas del archivo
local $cmd = "cd /usr/local/webmin/hello; ./execute_ssh.sh \"@connection_data[0]\" \"@connection_data[1]\" \"@connection_data[2]\" \"$command\"";
local $Output = `$cmd`;

return $Output ;

}




#metodo que alamacena las credenciales de registro en un archivo
sub store_login_data(){
my @args=@_;

local $node=@args[0];
local $usr=@args[1];
local $pass=@args[2];

my $filename = 'login.dat';
open(my $fh, '>', $filename) or die "Could not open file '$filename' $!";
print $fh "$node\n";
print $fh "$usr\n";
print $fh "$pass\n";
close $fh;
}
1;