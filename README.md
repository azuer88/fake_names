# fake_names
Python script to generate fake names


## Usage
./generate.py [spec]+
     where spec is [\d+](FfMmBb)[\d+]
     e.g.:  30B2 means 30 names from [B]oth gender, with 1-2 first names
            b    means 1 name either gender, 1 first name, same as '1B1'
            1F1  means 1 female with 1 first name, same as 'F'
