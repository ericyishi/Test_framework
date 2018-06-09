# Test_framework
### 文件结构
```
 Test_framework
    |--config（配置文件）
    |--data（数据文件）
    |--drivers（驱动）
    |--log（日志）
    |--report（报告）
    |--test（测试用例）
    |--utils（公共方法）
    |--ReadMe.md（加个说明性的文件，告诉团队成员框架需要的环境以及用法）
```

### PO模型
```
 test
    |--case（用例文件）
    |--common（跟项目、页面无关的封装）
    |--page（页面）
    |--suite（测试套件，用来组织用例）
```

### 在test层下新建一个interface接口层
* requests库（接口是HTTP类型的）
* socket库测TCP接口
* suds库测SOAP接口
* 不论你是什么类型的接口，总能找到对应的Python库的。
```
 test
    |--case（用例文件）
    |--common（跟项目、页面无关的封装）
    |--page（页面）
    |--suite（测试套件，用来组织用例）
    |--interface（接口层）
```
* 这里你也可以在test下分成API和UI两层，分别在其中再进行分层
   ```
      test
         |--UI（UI层）
             |--case（用例文件）
             |--common（跟项目、页面无关的封装）
             |--page（页面）
             |--suite（测试套件，用来组织用例）
         |--interface（接口层）
   ```
   