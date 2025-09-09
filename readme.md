# 配置指南

**交流群**：QQ 群：746855036
**版本号**：v0.2
**更新日期**：2025/09/09

本项目依赖第三方工具和 SDK，可根据以下官方文档指引自行下载、安装并配置相关环境。

常见问题详见 [question.md](question.md)。

---

## 第一步：手机端配置（Reqable 协同模式）

### 1. 安装 Reqable App
请前往[Reqable 官网](https://reqable.com)下载并安装移动端应用：
### 2. 配置协同模式
请参考官方文档进行协同模式配置：[https://reqable.com/zh-CN/docs/getting-started/collaboration/](https://reqable.com/zh-CN/docs/getting-started/collaboration/)

> ⚠️ 特别注意：Android 7.0 及以上系统默认不信任用户安装的证书。若目标 App 目标 SDK ≥ 24，必须将证书安装为**系统级证书**，否则无法抓取 HTTPS 流量。此操作需要 **Root 权限**。

---

## 第二步：电脑端配置（Python 脚本环境）

### 1. 安装 Reqable 电脑客户端
请前往官网下载并安装桌面版： [https://reqable.com](https://reqable.com)

### 2. 安装 Python 环境
确保已安装 Python 3.6 或更高版本。

官网未指定具体版本要求，建议使用最新稳定版： [https://www.python.org/downloads/](https://www.python.org/downloads/)

验证安装：
```bash
python --version
```

### 3. 安装腾讯云 COS Python SDK
请执行以下命令安装腾讯云 COS Python SDK：

```bash
pip install -U cos-python-sdk-v5
```

## 第三步：导入脚本并配置规则

### 1. 启用 Reqable 脚本功能
打开电脑端 Reqable：
- 点击顶部菜单 **“工具” → “脚本”**
- 点击 **“启用脚本”**
- 点击 **“导入”**，选择项目目录下的 `reqable-scripts.config` 文件

### 2. 配置拦截规则
在 Reqable 中添加如下规则：
- **URL**: `https://download.nature.qq.com/SnsShare/SocialProfile/*`
- **模式**: 可从 `ANY` 改为 `GET`

**关键提示**：
点击 URL 输入框最右侧的 `*?` 图标，**确保其变为黄色**，表示**通配符已启用**（启用后图标为黄色）。

  > ⚠️ 若未启用，规则将不会使用通配符匹配，将会导致拦截/转发失败！

### 3. 修改脚本配置
打开导入的 Python 脚本，找到以下变量并修改：
```python
IMG_PATH = r"你的本地图片路径"  # 例如：C:/your_image.jpg 或 /Users/xxx/image.png
```

确保该路径存在且图片可读。

---

## 第四步：开始抓包

1. 确保手机已连接到电脑端 Reqable（协同模式已生效）
2. 手机端开启 SSL 代理（通过 Reqable App 自动处理）
3. 打开目标应用，进入稷下学院拍照页面，点击上传

---

## 官方文档索引（请自行查阅）

| 内容                 | 链接                                                         |
| -------------------- | ------------------------------------------------------------ |
| Reqable 协同模式配置 | [https://reqable.com/zh-CN/docs/getting-started/collaboration/](https://reqable.com/zh-CN/docs/getting-started/collaboration/) |
| Reqable 下载地址     | [https://reqable.com](https://reqable.com)                   |

---

## 免责声明

本指南仅用于技术学习与调试目的，请遵守相关法律法规，不得用于非法用途。因使用本工具引发的任何问题，与维护者无关。