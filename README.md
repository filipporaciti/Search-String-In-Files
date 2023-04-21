# Search-String-In-Files

## Use
Giving a string and the path of the directory where you want to search, this program give to you every files and the row where this string is.

### Basic usage
``` bash
ssif "local" "./directory"

# Output
# ./install.sh --> (0) cp ssif.py /usr/local/bin
# ./install.sh --> (1) mv /usr/local/bin/ssif.py /usr/local/bin/ssif
# ./README.md --> (7) ssif "local" "./directory"
# ./remove.sh --> (0) rm /usr/local/bin/ssif
# ./.git/hooks/fsmonitor-watchman.sample --> (64) 	local $, = "\0";
# ./.git/hooks/fsmonitor-watchman.sample --> (107) 	my $response = do {local $/; <CHLD_OUT>};
# ./.git/hooks/pre-push.sample --> (16) #   <local ref> <local oid> <remote ref> <remote oid>
# ./.git/hooks/pre-push.sample --> (26) while read local_ref local_oid remote_ref remote_oid
# ./.git/hooks/pre-push.sample --> (28) 	if test "$local_oid" = "$zero"
# ./.git/hooks/pre-push.sample --> (36) 			range="$local_oid"
# ./.git/hooks/pre-push.sample --> (39) 			range="$remote_oid..$local_oid"
# ./.git/hooks/pre-push.sample --> (46) 			echo >&2 "Found WIP commit in $local_ref, not pushing"
# ./.git/hooks/push-to-checkout.sample --> (37) # branches while keeping the local changes in the working tree that do

```
The first string is the string that you want to search, while the second string is the directory.

### Verbose
You can see also the file where the string is not here with the fiels `--verbose` or `-v`
``` bash
ssif "local" "./" -v 

# Output (only first 10 lines)
# ./install.sh --> (0) cp ssif.py /usr/local/bin
# ./install.sh --> (1) mv /usr/local/bin/ssif.py /usr/local/bin/ssif
# Not here --> ./README.md
# Not here --> ./README.md
# Not here --> ./README.md
# Not here --> ./README.md
# Not here --> ./README.md
# Not here --> ./README.md
# Not here --> ./README.md
# ./README.md --> (7) ssif "local" "./directory"
```

### Blacklist
With this field you can set directory or file's blacklist. You can set one file/directory with tag `--blacklist fileordirectory` or more file/directory with tag `--blacklist "1fileordirectory 2fileordirectory 3fileordirectory..."`
``` bash
ssif --blacklist "README.md .git" "local" "./"

# Output 
# ./install.sh --> (0) cp ssif.py /usr/local/bin
# ./install.sh --> (1) mv /usr/local/bin/ssif.py /usr/local/bin/ssif
# ./remove.sh --> (0) rm /usr/local/bin/ssif
```


## Install
``` bash
./install.sh
```

## Uninstall
``` bash
./remove.sh
```