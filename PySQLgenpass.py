#!/usr/bin/env python
# ---
# PySQLgenpass.py
# ---
# This script takes password input on stdin and
# does a double-SHA1 hash on it to produce MySQL
# password hashes, without echoing the password
# to STDOUT, unlike: SELECT PASSWORD('blah');
# The password is read twice to ensure a match.
#
# Copyright (c) 2016, Salvatore LaMendola <salvatore@lamendola.me>

from hashlib import sha1
import getpass


def gen_pass_hash(prompt):
    return sha1(sha1(getpass.getpass(prompt)).digest()).hexdigest().upper()

hash1 = gen_pass_hash("New MySQL Password (will be hidden): ")
hash2 = gen_pass_hash("Please re-enter your password (will be hidden): ")

if hash1 == hash2:
    print "\n*" + hash1
else:
    print "\nPasswords don't match."
