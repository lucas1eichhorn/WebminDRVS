=head1 change-user-lib.pl

This module has no actual functionality of it's own, so there isn't much to
say here.

=cut

BEGIN { push(@INC, ".."); };
use strict;
use warnings;
use WebminCore;
&init_config();
1