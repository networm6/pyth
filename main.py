import requests
import time

url = "http://192.168.1.40/api/v1/configs"
headers = {
    "CSRF-Token": "86575c73930a2c4e33c9ab17590fb468e7fa4b892a99949210ec269db2bd5005",
    "Cookie": "session=a607c6bf-28cf-4fc0-ac7e-a66cf8964107.u8EpeqFa5z6OOp08lv2DyLB8Vrg",
    "Content-Type": "application/json"
}
data = {"whale:docker_api_url": "unix:///var/run/docker.sock", "whale:docker_credentials": "",
        "whale:docker_swarm_nodes": "linux-1", "whale:docker_ssl_ca_cert": "None",
        "whale:docker_ssl_client_cert": "None", "whale:docker_ssl_client_key": "None",
        "whale:docker_auto_connect_network": "", "whale:docker_dns": "127.0.0.1",
        "whale:docker_auto_connect_containers": "", "whale:docker_subnet": "174.1.0.0/16",
        "whale:docker_subnet_new_prefix": "24", "whale:frp_api_url": "http://frpc:7400",
        "whale:frp_http_domain_suffix": "", "whale:frp_http_port": "9123",
        "whale:frp_direct_ip_address": "172.23.12.73", "whale:frp_direct_port_minimum": "10000",
        "whale:frp_direct_port_maximum": "11000",
        "whale:frp_config_template": "[common]\r\nserver_addr = 172.1.0.3\r\nserver_port = 7000\r\nadmin_addr = "
                                     "172.1.0.4\r\nadmin_port = 7400\r\n",
        "whale:docker_max_container_count": "200", "whale:docker_max_renew_count": "3", "whale:docker_timeout": "3600",
        "whale:template_http_subdomain": "{{ container.uuid }}",
        "whale:template_chall_flag": "{{ \"flag{\"+uuid.uuid4()|string+\"}\" }}", "whale:refresh": True,
        "whale:docker_use_ssl": False}


def req(myip):
    data2 = data
    data2["whale:frp_direct_ip_address"] = myip
    res = requests.patch(url, headers=headers, json=data2)
    print(res.text)


def getip():
    res = requests.get("http://124.220.11.247:10800/address.php").text
    return res


while True:
    time.sleep(60)
    ip = getip()
    req(ip)
