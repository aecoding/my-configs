#!/bin/bash

# It could be better if I could especify a directory where I want this script to be started.

dir() {
  mkdir -p $1
}

file() {
  if [[ $1 = 'partials' ]]
  then
    touch src/sass/partials/_$2.scss
  else
    touch src/sass/$2.scss
  fi
}

pkgs() {
  yarn add -D $1
}

# Fix erros
write() {
  if [[ $1 = 'sass' ]] 
  then
    echo $2 >> src/sass/main.scss

  else if [[ $1 = 'other' ]] 
  then
    echo $2 >> $3
  fi
}

dir src/sass/partials
dir public/css

file 'partials' 'base'
file 'partials' 'layout'
file 'partials' 'components'
file '' 'main'

git clone https://gist.github.com/DavidWells/18e73022e723037a50d6 src/sass/partials/

# This will write some basic imports
write 'sass', '@use "partials/base";'
write 'sass', '@use "partials/layout";'
write 'sass', '@use "partials/components";'

yarn init -y

# This will install some basic packages that I always use.
pkgs 'browser-sync 
      sass'

write 'other', '"scripts": {
  sass: "sass src/sass/main.scss public/css/style.css"  
}'
