# sudo cp -rf testnginx /etc/nginx/sites-available
chmod 710 /var/lib/jenkins/workspace/coder-i-backend
# sudo ln -s /etc/nginx/sites-available/testnginx /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
sudo systemctl restart gunicorn
sudo systemctl status nginx
echo "Setup Done"