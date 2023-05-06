#!/bin/bash

sed -i.orig 's/git@github.com:/..\/..\//g' .gitmodules

