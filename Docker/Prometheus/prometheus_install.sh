useradd --no-create-home --shell /usr/sbin/nologin prometheus
mkdir /etc/prometheus
mkdir /var/lib/prometheus
chown prometheus:prometheus /etc/prometheus
chown prometheus:prometheus var/lib/prometheus

wget https://github.com/prometheus/prometheus/releases/download/v2.51.2/prometheus-2.51.2.linux-amd64.tar.gz 
tar xvf prometheus-2.51.2.linux-amd64.tar.gz
cd prometheus-2.51.2.linux-amd64
cp prometheus /usr/local/bin
cp promtool /usr/local/bin
chown prometheus:prometheus /usr/local/bin/prometheus
chown prometheus:prometheus /usr/local/bin/promtool

cp -r consoles /etc/prometheus
cp -r console_libraries /etc/prometheus
chown -R prometheus:prometheus /etc/prometheus/consoles
chown -R prometheus:prometheus /etc/prometheus/console_libraries
