# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
# ======================================================================
#   Copyright (C) 2020 liaozhimingandy@qq.com Ltd. All Rights Reserved.
#
#   @Author      : zhiming
#   @Project     : Demo
#   @File Name   : test_xml2dict.py
#   @Created Date: 2020-07-26 8:40
#      @Software : PyCharm
#         @e-Mail: liaozhimingandy@qq.com
#   @Description :
#
# ======================================================================
import ssl


class client_ssl:
    def send_hello(self, ):
        # 生成SSL上下文
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

        # 加载信任根证书
        context.load_verify_locations('cert/server.crt')
        # 若出现 certificate verify failed: IP address mismatch, certificate is not valid for '127.0.0.1',则不校验,建议校验
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        # 与服务端建立socket连接
        with socket.create_connection(('127.0.0.1', 9101)) as sock:
            # 将socket打包成SSL socket
            # 一定要注意的是这里的server_hostname不是指服务端IP，而是指服务端证书中设置的CN，我这里正好设置成127.0.1而已
            with context.wrap_socket(sock, server_hostname='127.0.0.1') as ssock:
                # 向服务端发送信息
                msg = "<data>您好,这是来自客户端的消息</data>".encode("utf-8")
                ssock.send(msg)
                # 接收服务端返回的信息
                msg = ssock.recv(1024).decode("utf-8")
                print(f"来自服务端的消息: {msg}")
                ssock.close()


class server_ssl:
    def build_listen(self):
        # 生成SSL上下文
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        # 加载服务器所用证书和私钥
        context.load_cert_chain('cert/server.crt', 'cert/server.key')

        # 监听端口
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
            sock.bind(('192.168.1.105', 9003))
            sock.listen(5)
            # 将socket打包成SSL socket
            with context.wrap_socket(sock, server_side=True) as ssock:
                while True:
                    print("正在进行端口监听...")
                    # 接收客户端连接
                    client_socket, addr = ssock.accept()
                    # 接收客户端信息
                    msg = client_socket.recv(1024).decode("utf-8")
                    print(f"来自客户端: {addr}的消息：{msg}")
                    # 向客户端发送信息
                    msg = f"服务端已接收到你的数据.\r\n".encode("utf-8")
                    client_socket.send(msg)
                    client_socket.close()


def main():
    # client(host='127.0.0.1', port=9100, cafile=None)
    client_ssl().send_hello()
    # server_ssl().build_listen()


if __name__ == "__main__":
    main()
