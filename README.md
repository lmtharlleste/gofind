docker run --name postgres_container \
  -e POSTGRES_USER=tharlles_admin \
  -e POSTGRES_PASSWORD=LiLEXXhP2727 \
  -e POSTGRES_DB=gifinddb \
  -p 5432:5432 \
  -d postgres:latest
