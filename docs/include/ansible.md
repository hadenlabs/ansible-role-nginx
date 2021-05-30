## Requirements

## Role Variables

The default role variables in `defaults/main.yml` are:

```{.yaml}
# defaults file for nginx
nginx_keepalive_timeout: "65"
nginx_keepalive_requests: "1000"

nginx_client_max_body_size: "64m"
nginx_client_body_timeout: "3m"
nginx_client_header_timeout: "3m"

nginx_server_names_hash_bucket_size: "64"
```
