# Auth-Kerberos

## Install

安装Kerberos环境

```bash
sudo yum install -y krb5-devel krb5-server krb5-workstation
```

安装Python运行环境

```bash
pip3 install -r requirements.txt
```

## BackUp

备份Kerberos配置文件

```bash
sudo cp /etc/krb5.conf /etc/krb5.conf.bk
sudo cp /var/kerberos/krb5kdc/kdc.conf /var/kerberos/krb5kdc/kdc.conf.bk
sudo cp /var/kerberos/krb5kdc/kadm5.acl /var/kerberos/krb5kdc/kadm5.acl.bk
```

## Config

样例配置文件位于Sample文件夹内

创建Kerberos数据库

```bash
sudo kdb5_util create -s -r EXAMPLE.COM
```

配置防火墙

```bash
sudo firewall-cmd --permanent --add-service kerberos
sudo firewall-cmd --reload
```

配置principle

```bash
sudo kadmin.local
```

```bash
addprinc HTTP/kerberos.example.com@EXAMPLE.COM
```

导出管理员keytab

```bash
xst -norandkey -k /var/kerberos/krb5kdc/kadm5.keytab kadmin/admin kadmin/changepw
```

导出HTTP认证 http.keytab

```bash
xst -norandkey -k http.keytab HTTP/kerberos.example.com@EXAMPLE.COM
```

## Test

测试流程如下：

申请票据

```bash
kinit -kt http.keytab HTTP/kerberos.example.com@EXAMPLE.COM
```

单元测试

```bash
KRB5_KTNAME=/home/admin/PycharmProjects/auth-kerberos/http.keytab pytest
```
