liquibase --changeLogFile=/changelogs/changelog.xml \
  --username=postgres \
  --password=2451 \
  --url="jdbc:postgresql://db/postgres" \
  --classpath=/opt/jdbc_drivers/postgresql-9.3-1102.jdbc41.jar \
  update
