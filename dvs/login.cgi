#!/usr/bin/perl
# index.cgi
# Muestra el menu de la pantalla inicial con  el login
use CGI;
my $req = CGI->new;
require './dvs-lib.pl';
&ui_print_header(undef, 'DVS Administration');

  $hostname_req = $req->param('hostname');
print "'<div id='createFolderDialog' class='modal show'>";
print &ui_form_start("menu.cgi","post");
    print "<div class='modal-dialog'>
        <div class='modal-content'>
            <div class='modal-header'>
             
                <h4 class='text-center'>Host Login:</h4>
            </div>
            <div class='modal-body'>
					
					<div class='input-group form-group'>
						<span class='input-group-addon'><i class='fa fa-fw fa-desktop'></i></span>
						<input class='form-control session_login' name='host' autocomplete='off' placeholder='Hostname' value='$hostname_req' autofocus='' type='text'>
					</div>
					<div class='input-group form-group'>
						<span class='input-group-addon'><i class='fa fa-fw fa-user'></i></span>
						<input class='form-control session_login' name='user' autocomplete='off' placeholder='Username' autofocus='' type='text'>
					</div>
                   
					<div class='input-group form-group'>
						<span class='input-group-addon'><i class='fa fa-fw fa-lock'></i></span>
						<input class='form-control session_login' name='pass' autocomplete='off' placeholder='Password' type='password'>
					</div>
        
             </div>
            <div class='modal-footer'>
              <p><button class='btn btn-info' type='submit'><i class='fa fa-sign-in'></i> Sign in</button>
          </div>
        </div>
    </div>
	</form>
</div>";

