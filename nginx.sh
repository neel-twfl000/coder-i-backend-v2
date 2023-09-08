sudo nginx -t
sudo systemctl restart nginx
sudo systemctl restart gunicorn
sudo systemctl status nginx
echo "Setup Done"