in main.py

you will see two fields
KeyName

and

ami ID

basically, in AWs or GCP or Azure,
ami id is the operating system id 
(like ubuntu would have ami id - 123e
        mint would have ami id - 124e
        amazon linux would have ami id - 125e
        etc.. etc..)

now, each region would have separate id.
example -
ubuntu in usa would have different ami id
ubuntu in eurpoe or india would have different ami id

example -

ami id of ubuntu os in usa - 123e
ami id of ubuntu os in india would be - 666e
ami id of ubunutu in eurpoe would be - 777u

and so on... so on...

so, in order to run this project... 

you would manually need to -
_log into aws account (cloud console)
_select region, which you set up while configuring aws 

(as mentioned in  read_this_file 1st file)

_in that region, goto ec2
_then goto ami on left
_select the os of your choice, 
_get the ami id of that operating system and region
_use this ami id in main.py 

likewise ....

in aws, goto keypair
_create a keypair
_give it name - keypair_1st_January
_choose .pem format
_give this name in 'KeyName' in main.py

like -

KeyName='keypair_1st_January.pem'

(add suffix.pem)

~~


~~
