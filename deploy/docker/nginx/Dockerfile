FROM nginx:1.19.0-alpine

COPY nginx.conf /etc/nginx/sites-available/localhost

RUN rm /etc/nginx/conf.d/default.conf && \
    mkdir -p /etc/nginx/sites-enabled/ && \
    ln -s /etc/nginx/sites-available/localhost /etc/nginx/sites-enabled/localhost
