# FROM httpd
FROM nginx:stable

EXPOSE 443

# COPY . /usr/local/apache2/htdocs/
COPY . /usr/share/nginx/html/

STOPSIGNAL SIGQUIT

CMD ["nginx","-g","daemon off;"]


