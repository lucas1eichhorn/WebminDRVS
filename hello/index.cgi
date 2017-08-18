#!/usr/bin/perl
# index.cgi
# Muestra el menu de la pantalla inicial con iconos
require './hello-lib.pl';
&ui_print_header(undef, 'DRVS Administration');
=pod
require './hello-lib.pl';
&ui_print_header(undef, 'DRVS Administration');

print &ui_form_start("", "post");
print &ui_hidden("page", $in{'page'});
print &ui_table_start("Login",
		      "width=40% class='loginform'", 2);

# Login message

print &ui_table_row(undef,"Enter your access credentials", 2, [ "align=center width=20%", "align=center" ]);

# Username and password
print &ui_table_row("Hostname",
	&ui_textbox("hostname", $in{'failed'}, 20, 0, undef, $tags));
print &ui_table_row("Username",
	&ui_textbox("user", $in{'failed'}, 20, 0, undef, $tags));
print &ui_table_row("Password",
	&ui_password("pass", undef, 20, 0, undef, $tags));



print &ui_table_end(),"\n";

print "<button class='btn btn-info ui_submit ui_form_end_submit' type='button'>&nbsp;<span data-entry='session_login'>Login&nbsp;</span></button>";
print "<button class='btn btn-info ui_reset' style='padding-left: 28px; vertical-align:middle' type='reset'>Clear</button>";
print &ui_form_end();



&ui_print_footer();
=cut

print "'<div id='createFolderDialog' class='modal show'>";
print &ui_form_start("save_host.cgi","post");
    print "<div class='modal-dialog'>
        <div class='modal-content'>
            <div class='modal-header'>
             
                <h4 class='text-center'>Host login</h4>
            </div>
            <div class='modal-body'>
					
					<div class='input-group form-group'>
						<span class='input-group-addon'><i class='fa fa-fw fa-desktop'></i></span>
						<input class='form-control session_login' name='host' autocomplete='off' placeholder='Hostname' autofocus='' type='text'>
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