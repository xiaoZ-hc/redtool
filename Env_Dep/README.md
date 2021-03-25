<h4 align="center">一款红/蓝队环境自动化部署工具,支持多种场景,渗透,开发,代理环境,服务可选项等.</h4>

<p align="center">
  <a href="#开始">开始</a> •
  <a href="#支持选项">支持选项</a> •
  <a href="#实际效果">实际效果</a> •
</p>

---

**说明**：此脚本出自[404Team 星链计划2.0](https://github.com/ffffffff0x/f8x)中的 f8x，版权归原作者所有，最新版可至原版出处寻找。

大多数场景下，在不同的云购买一些 vps 服务器用于部署红 / 蓝队设施，不能做到开箱即用，使用此工具可以快速部署所需要的各类服务。同时兼顾到本地 VM 虚拟机的需求，可以选择走 socket 代理进行安装部署，Proxychains-ng 也会自动安装，只需做好 Proxychains-ng 配置即可。

## 开始

**使用**
```bash
bash f8x -h
```

**系统依赖**

f8x 基本上不需要任何依赖,或者说它就是为了帮助你安装各种依赖而生的😁

---

## 支持选项

目前 f8x 支持以下部署选项

**1. 批量化安装**

- 使用 -b 选项安装基本环境        (gcc、make、git、vim、telnet、jq、unzip 等基本工具)
- 使用 -p 选项安装代理环境        (警告:国外云服务器上不要用,会降速)
- 使用 -d 选项安装开发环境        (python3、pip3、Go、Docker、Docker-Compose、SDKMAN)
- 使用 -k 选项安装渗透环境        (hashcat、ffuf、OneForAll、ksubdomain、impacket 等渗透工具)
- 使用 -s 选项安装蓝队环境        (Fail2Ban、chkrootkit、rkhunter、河马webshell查杀工具)
- 使用 -f 选项安装其他工具        (Bash_Insulter、vlmcsd、AdguardTeam、trash-cli)
- 使用 -cloud 选项安装云应用      (Terraform、Serverless Framework、wrangler)
- 使用 -all 选项全自动化部署      (默认不走代理,兼容 CentOS7/8,Debain10/9,Ubuntu20/18,Fedora33)

**2. 开发环境**

- 使用 -nn 选项安装 npm & NodeJs 环境
- 使用 -oraclejdk 选项安装 oraclejdk 环境
- 使用 -openjdk 选项安装 openjdk 环境
- 使用 -python3 选项安装 python3 环境
- 使用 -python2 选项安装 python2 环境
- 使用 -pip2-f 选项强制安装 pip2 环境          (建议在 -python2 选项失败的情况下运行)
- 使用 -perl 选项安装 perl 环境
- 使用 -ruby 选项安装 ruby 环境
- 使用 -rust 选项安装 rust 环境
- 使用 -chromium 选项安装 Chromium 环境        (用于配合 -k 选项中的 rad、crawlergo)

**3. 蓝队服务**

- 使用 -binwalk 选项安装 binwalk 环境
- 使用 -binwalk-f 选项强制安装 binwalk 环境    (建议在 -binwalk 选项失败的情况下运行)
- 使用 -clamav 选项安装 ClamAV 工具
- 使用 -hfish 选项安装 HFish 蜜罐
- 使用 -lt 选项部署 LogonTracer 环境           (非超高配置机器不要部署,这个应用太吃配置了)
- 使用 -suricata 选项部署 Suricata 环境
- 使用 -vol 选项安装 volatility 取证工具
- 使用 -vol3 选项安装 volatility3 取证工具

**4. 红队服务**

- 使用 -bypass 选项部署 Bypass 环境
- 使用 -cs 选项部署 CobaltStrike 环境
- 使用 -frp 选项部署 frp 环境
- 使用 -goby 选项部署 Goby 环境                (需要图形化环境)
- 使用 -nps 选项部署 nps 环境

**5. 基于 Docker 的环境部署**

- 使用 -arl 选项部署 ARL 环境(872 MB)
- 使用 -awvs13 选项部署 AWVS13 环境(1.04 GB)
- 使用 -mobsf 选项部署 MobSF 环境(1.54 GB)
- 使用 -nodejsscan 选项部署 nodejsscan 环境(873 MB)
- 使用 -viper 选项部署 Viper 环境(2.1 GB)
- 使用 -vulhub 选项部署 vulhub 环境(210 MB)
- 使用 -vulfocus 选项部署 vulfocus 环境(1.04 GB)

**6. 杂项服务**

- 使用 -asciinema 选项安装 asciinema 截图工具
- 使用 -bt 选项部署宝塔服务
- 使用 -music 选项部署 UnblockNeteaseMusic 服务
- 使用 -sharry 选项部署 sharry 文件服务
- 使用 -ssh 选项配置 SSH 环境                  (RedHat 系默认可用,无需重复安装)
- 使用 -ssr 选项部署 ssr 工具

**7. 其他**

- 使用 -clear 选项清理系统使用痕迹
- 使用 -info 选项查看系统各项信息
- 使用 -optimize 选项改善设备选项,优化性能
- 使用 -remove 选项卸载国内 vps 云监控
- 使用 -rmlock 选项运行除锁模块
- 使用 -swap 选项配置 swap 分区
- 使用 -update 选项更新 f8x 工具

---

## 实际效果

**-all 全自动化部署**

以 vultr vps 为例,$10/mo 的配置,结果分别如下

| <br><b><p align="center">CentOS 7(完全兼容)</p> | <br><b><p align="center">Debian 10(完全兼容)</p> |
| - | - |
| <p align="center"><a href="https://asciinema.org/a/387124"><img src="https://asciinema.org/a/387124.svg" /></p></a> | <p align="center"><a href="https://asciinema.org/a/387123"><img src="https://asciinema.org/a/387123.svg" /></p></a> |
| <br><b><p align="center">Fedora 33(完全兼容)</p> | <br><b><p align="center">Ubuntu 20.10(完全兼容)</p> |
| <p align="center"><a href="https://asciinema.org/a/391443"><img src="https://asciinema.org/a/391443.svg" /></p></a> | <p align="center"><a href="https://asciinema.org/a/391433"><img src="https://asciinema.org/a/391433.svg" /></p></a> |

---

## 免责声明

1. 此仓库所有文章、代码部分来源于互联网，版权归原作者所有，转载留存的都会写上原著出处，如有遗漏，还请说明，谢谢！
2. 此仓库仅供学习参考使用，不被允许通过本仓库中所提及技术手段进行非法行为，使用技术的风险由您自行承担，严禁用于任何非法行为！使用即代表你同意自负责任！
