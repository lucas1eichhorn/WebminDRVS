BEGIN { push(@INC, ".."); };

use WebminCore;
use CGI;

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

#list_proxies()
#obtiene la informacion de los proxys activos de /procs/drvs/proxies/info
sub list_proxies
{
local @rv;
my $file=&execute_ssh_command("cat /proc/drvs/proxies/info");
local @lines=split(/\n/,$file);

local $i=0;
foreach $line(@lines){
		#la primer linea contiene los titulos
		
		if($i>0){
			local(@f) = split(/\s+/,$line);
			local($prox) =@f[1];
			local($flags) = @f[2];
			local($sender) = @f[3];
			local($reciver) = @f[4];
			local($prox_name) = @f[5];
			local($nodo) = @f[6];
			
			

		#colocamos cada campo en un array hash	
		push(@rv, { 'proxy' => $prox,
					'flags' => $flags,
					'sender' => $sender,
					'reciver' => $reciver,
					'prox_name' => $prox_name,
					'nodo'=>$nodo,
					'line' => $line

			});

		}
	}
	
	return @rv;

}

#prox_procs_info
#Obtiene la información de los procesos activos en el proxy
sub proxies_procs_info
{
local @rv;

my $file=&execute_ssh_command("cat /proc/drvs/proxies/procs");
local @lines=split(/\n/,$file);
local $i=0;
foreach $line(@lines){
		#Si la linea no tiene numeros, es la primera con los nombres de las columnas
		if($i>0){
			local(@f) = split(/\s+/, $line);
			local($proxid) =  @f[1];
			local($type) = @f[2];
			local($lpid) = @f[3];
			local($flag) = @f[4];
			local($misc) = @f[5];
			local($pxsent) = @f[6];
			local($pxrcvd) = @f[7];
			local($getf) = @f[8];
			local($sendt) = @f[9];
			local($wmig) = @f[10];
			local($name) = @f[11];


			push(@rv, {
				'proxid' => $proxid,
				'type'=> $type,
				'lpid' => $lpid,
				'flag' => $flag,
				'misc' => $misc,
				'pxsent' => $pxsent,
				'pxrcvd' => $pxrcvd,
				'getf' => $getf,
				'sendt' => $sendt,
				'wmig' => $wmig,
				'name' => $name,
				'line' => $line
				});

		}
		$i++;
	}

	return @rv;
}
# dc_info()
# obtiene la informacion de una maquina virtual pasada como parametro - lee el archivo /proc/drvs/{dc_name}/info
sub dc_info
{
 my  @args = @_;
 my  $dc_name=@args[0];
local @rv;

local $line="";


my $file=&execute_ssh_command("cat /proc/drvs/$dc_name/info");
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


# dc_procs_info
# obtiene la informacion de los procesos activos en el DC pasada como parametro
# leyendo el archivo /proc/drvs/{dc_nombre}/procs
sub dc_procs_info
{
 my  @args = @_;
 my  $dc_name=@args[0];
local @rv;

local $line="";


my $file=&execute_ssh_command("cat /proc/drvs/$dc_name/procs");
local $i=0;
local @lines=split(/\n/,$file);
foreach $line(@lines){
	##analizamos la linea, la primera linea posee los titulos
	if ($i>1&&$line =~ m/[0-9a-zA-Z]/){
	#separamos cada columna por los espacios (REGEXP) y los guardamos en una array
	local(@f)=split(/\s+/, $line);
	local($DCid)=@f[1];
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
		push(@rv, { 'DCid' => $DCid,
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

return @rv;
}

#dc_running_list
#metodo que lista el nombre las carpetas de las MV en /proc/drvs/
sub dc_running_list()
{
local @rv;
local $line="";

#ejecutamos el comando para listar todos los directorios
my $find=&execute_ssh_command("find /proc/drvs/ -type d");

local @lines=split(/\n/,$find);
foreach $line(@lines){
	##analizamos la linea, la carpeta proxies no corresponde a 
	$line =~ s/\/proc\/drvs\///g;
	if ($i!=0 && !($line =~ m/proxies/)){

	#colocamos cada campo en un array hash
		push(@rv, { 'dc_name' => $line});
		
		
	}
		$i++;	
	}

return @rv;
}
# dc_stats_info
# obtiene la informacion de stats en el DC pasada como parametro
# leyendo el archivo /proc/drvs/{dc_name}/stats
sub dc_stats_info
{
 my  @args = @_;
 my  $dc_folder=@args[0];
local @rv;

local $line="";


my $file=&execute_ssh_command("cat /proc/drvs/$dc_folder/stats");

local $i=0;

local @lines=split(/\n/,$file);
foreach $line(@lines){
	##analizamos la linea, la primera linea posee los titulos
	if ($i>1&&$line =~ m/[0-9a-zA-Z]/){
	#separamos cada columna por los espacios (REGEXP) y los guardamos en una array
	local(@f)=split(/\s+/, $line);
	local($DCid)=@f[1];
	local($p_nr)=@f[2];
	local($endp)=@f[3];
	local($lpid)=@f[4];
	local($node)=@f[5];
	local($lsnt)=@f[6];
	local($rsnt)=@f[7];
	local($lcopy)=@f[8];
	local($rcopy)=@f[9];

	
	#colocamos cada campo en un array hash
		push(@rv, { 'DCid' => $DCid,
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

#get_running_DC
#metodo que devuelve un arreglo con los ids de la maquina que se estan ejecutando en el nodo, a partir de un string como parametro
#El string de parametro es del tipo -----X, donde X se encuentra en la posicion correspondiente al id del DC
sub get_running_DC(){
local @id_list;
my @args=@_;

my $string = @args[0];
  my $char = 'X';
  my $offset = 0;

  my $result = index($string, $char, $offset);
local $str_len=length($string);
  while ($result != -1) {

    #colocamos cada campo en un array hash
	
		push(@id_list, { 'DCid' => $str_len-$result-1});

    $offset = $result + 1;
    $result = index($string, $char, $offset);

  }
  return @id_list;
}
#get_running_NODES
#metodo que devuelve un arreglo con los id del nodo que se estan ejecutando el DC, a partir de un string como parametro
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
	
		push(@id_list, { 'idnode' => $str_len-$result-1});

    $offset = $result + 1;
    $result = index($string, $char, $offset);

  }
  return @id_list;
}
#metodo que permite conectarse a uno nodo mediante ssh
sub connect_node_ssh(){

my @args=@_;

local $param_node="@args[0]";
local $param_usr="@args[1]";
local $param_pass="@args[2]";
#verificamos si vienen los datos para conectarse al nodo  en los argumentos
	if(length $param_node ==0 && length $param_usr ==0 && length $param_pass ==0){
	
	#sino los obtenemos de session
	 my $cgi = CGI->new;
	$sid = $cgi->cookie("CGISESSID") || undef;
	$session=new CGI::Session(undef, $sid, {Directory=>'/usr/local/webmin/dvs/tmp'});
	 $node = $session->param("node");
	 $usr = $session->param("usr");
	 $pass=$session->param("pass");
	
	}else{##si viene desde el login, utilizamos los argumentos para conectarnos
	 $node = $param_node;
	 $usr = $param_usr;
	 $pass = $param_pass;
	
	#guardamos los datos de login en un archivo las futuras conexiones
	&store_login_data($param_node,$param_usr,$param_pass);
	}



local $command="hostname";

my $cmd ="cd /usr/local/webmin/dvs; ./execute_ssh.sh \"$node\" \"$usr\" \"$pass\" \"$command\"";
my $Output = `$cmd`;
#my $Output ="$param_node $param_usr $param_pass" ;
return $Output ;
}

#metodo que devuelve el hostname del nodo conectado almacenado en cookies de session
sub connected_node_name(){
 my $cgi = CGI->new;
$sid = $cgi->cookie("CGISESSID");
$session=new CGI::Session(undef, $sid, {Directory=>'/usr/local/webmin/dvs/tmp'});
$node = $session->param("node");
return "$node";
}
#metodo que permite ejecutar un comando en un nodo remoto mediante ssh
#se leen las credenciales del archivo login.dat
sub execute_ssh_command(){
     my $cgi = CGI->new;

#leemos las credenciales de login de session;
$sid = $cgi->cookie("CGISESSID");
$session=new CGI::Session(undef, $sid, {Directory=>'/usr/local/webmin/dvs/tmp'});
$node = $session->param("node");
$usr = $session->param("usr");
$pass = $session->param("pass");

#obtenemos el comando a ejecutar pasado como parametro
my @args=@_;

local $command=@args[0];
#ejecutamos el comando mediante sshpass en el nodo remoto, con las credenciales obtenidas del archivo
local $cmd = "cd /usr/local/webmin/dvs; ./execute_ssh.sh \"$node\" \"$usr\" \"$pass\" \"$command\"";
local $Output = `$cmd`;

return  $Output;

}




#metodo que alamacena las credenciales de registro en un archivo
sub store_login_data(){
 use CGI::Session;

my @args=@_;
#valores pasados como parametro en la funcion
local $node=@args[0];
local $usr=@args[1];
local $pass=@args[2];

#session parametros: 1-tipo de almacenamiento(default:File) 2-session id (undef crea una nueva) 3: dir de almacenamiento
local $session = new CGI::Session(undef, undef, {Directory=>'/usr/local/webmin/dvs/tmp'});

#almacenamos en cookies de session
$session->param("node", "$node");
$session->param("usr", "$usr");
$session->param("pass", "$pass");

 $sid = $session->id();
 #guaramos el id de session creada en una cookie
  my $cgi = CGI->new;
 $cookie = $cgi->cookie("CGISESSID" => $sid);
print $cgi->header(-cookie=>$cookie);
 return $sid;
}
1;