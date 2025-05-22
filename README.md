# Email Notifier (邮件通知库)

一个简单的Python库，用于在程序或脚本执行完毕后发送邮件通知。它提供了多种快捷方式来简化邮件发送，包括零参数的完成通知。


## 特性

* 通用的邮件发送功能 `send_notification`，可灵活配置。
* 快捷邮件发送功能 `quick_send_my_notification` (需用户配置发件人信息)。
* “超级定制”邮件发送功能 `send_my_default_status_update` (需用户配置发件人、默认收件人和主题)。
* 零参数的程序完成通知功能 `notify_program_done` (需用户配置发件人、默认收件人、主题和正文)。
* 发送失败自动重试机制。

## 安装

1.  克隆此仓库 (或下载代码)：
    ```bash
    git clone https_YOUR_GITHUB_REPO_URL_HERE # 替换为你的仓库URL
    cd your_project_directory_name
    ```
2.  (推荐) 在虚拟环境中安装：
    ```bash
    python -m venv venv
    # Linux/macOS:
    source venv/bin/activate
    # Windows:
    # venv\Scripts\activate
    ```
3.  安装库：
    ```bash
    pip install .
    ```
    或者，对于开发者，使用可编辑模式安装：
    ```bash
    pip install -e .
    ```

## 使用方法

### 发送程序完成通知 (最简单的方式)

首先，你需要编辑 `email_notifier/sender.py` 文件，在 `quick_send_my_notification` 函数和 `PROGRAM_DONE_RECIPIENT`, `PROGRAM_DONE_SUBJECT`, `PROGRAM_DONE_BODY` 常量中填入你自己的邮箱配置和期望的邮件内容。**注意安全！**

```python
# 在你的脚本中
from email_notifier import notify_program_done

# 你的主程序逻辑
print("正在执行主要任务...")
# ... 你的代码 ...
print("主要任务执行完毕。")

# 发送邮件
if notify_program_done():
    print("程序完成通知邮件已发送。")
else:
    print("程序完成通知邮件发送失败。")