#!/bin/sh
echo Use this script to initially setup containers.


export DB_PASSWORD=${1:?"Pass db password to use"}
SLEEP_TIME=${2:-5}
DCM=docker-compose


echo Upping DB.
$DCM up -d db

echo Sleeping while postgres gets into contidion.
sleep $SLEEP_TIME

echo Migrating database. If it will fail, try to rerun it or increase sleep \
  time to more than 5 secs by passing it as a second parameter to this script.
$DCM run --rm liquibase

echo Upping app.
$DCM up -d app
