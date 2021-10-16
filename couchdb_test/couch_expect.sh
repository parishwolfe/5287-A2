#!/usr/bin/expect -f
set geo 12
set city 5
set config 1
set intf 0.0.0.0
set pw Welcome

#Command
spawn apt install couchdb -y

#look for prompts
expect "?Geographic area:*"
send "$geo\r"

expect "?ime zone:*"
send "$city\r"

expect "?eneral type of CouchDB configuration:*"
send "$config\r"

expect "?ouchDB interface bind address:*"
send "$intf\r"

expect "?assword for the CouchDB*"
send "$pw\r"

expect "?epeat password for the CouchDB*"
send "$pw\r"

