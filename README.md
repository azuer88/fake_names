# Python Helper Scripts
Python scripts to 

1) generate fake names, used 
2) generate usernames from 1) above
3) generate file approriate for use by linux command 'newusers'



## Usage

__generate.py__
```
./generate.py [spec]+
     where spec is [\d+](FfMmBb)[\d+]
     e.g.:  30B2 means 30 names from [B]oth gender, with 1-2 first names
            b    means 1 name either gender, 1 first name, same as '1B1'
            1F1  means 1 female with 1 first name, same as 'F'
```

__mknewusersfrom.py__
```
./mknewusersfrom.py [-h] [-p PREFIX | -n] [source]

positional arguments:
  source                Text file containing a user's full name per line

optional arguments:
  -h, --help            show this help message and exit
  -p PREFIX, --prefix PREFIX
                        Prefix to prepend to generated username
  -n                    Do not get prefix from file name. Otherwise, prefix
                        will be the first word in the filename components, as
                        separated by a '.'
```
