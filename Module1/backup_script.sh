rsync -av /var/www/html ~/backup/daily
zip -9pr ~/backup/date_$(date +%Y%m%d).zip ~/backup/daily/