# BuptGatewayLib
专门用于解决远程ssh登录校内机的时候上下网的问题

两个python类：
    LoginRequest 实现登录逻辑
        使用的时候直接python LoginRequest.py -e <登陆点，如 http://10.3.8.211 > -u <学号> -p <密码> 即可实现登录
    LogoutRequest 实现下线逻辑

依赖requests包，请在使用前安装

####注意！！！！####
因为不怎么用扩展功能，因此这个库写的很"薄"。如果你有什么好的想法，请关注我的项目并且提出issue，我会及时关注的。^_^
