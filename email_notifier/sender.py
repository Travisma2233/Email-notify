# email_notifier/sender.py
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_notification(
    to_addr,
    subject,
    body,
    from_addr,
    password,
    smtp_server='smtp.qq.com', # 默认SMTP服务器，可根据你的邮箱服务商修改
    smtp_port=587,             # 默认SMTP端口，可根据你的邮箱服务商修改
    sender_display_name='自动通知脚本',
    receiver_display_name='目标用户',
    max_retries=3,
    retry_delay=60
):
    """
    通用的邮件发送函数，带有重试逻辑。
    """
    message = MIMEText(body, 'plain', 'utf-8')
    message['From'] = _format_addr(f'{sender_display_name} <{from_addr}>')

    if isinstance(to_addr, list):
        to_address_list = to_addr
        message['To'] =  _format_addr(f'{receiver_display_name} <{", ".join(to_address_list)}>')
    else: # 单个收件人
        to_address_list = [to_addr]
        message['To'] =  _format_addr(f'{receiver_display_name} <{to_addr}>')

    message['Subject'] = Header(subject, 'utf-8')
    msg_string = message.as_string()

    for attempt in range(max_retries):
        try:
            if smtp_port == 587: # 使用TLS
                smtpObj = smtplib.SMTP(smtp_server, smtp_port)
                smtpObj.ehlo()
                smtpObj.starttls()
            elif smtp_port == 465: # 使用SSL
                smtpObj = smtplib.SMTP_SSL(smtp_server, smtp_port)
            else: # 不加密或未知端口
                smtpObj = smtplib.SMTP(smtp_server, smtp_port)

            smtpObj.login(from_addr, password)
            smtpObj.sendmail(from_addr, to_address_list, msg_string)
            print(f"邮件已成功发送到 {', '.join(to_address_list)}!")
            smtpObj.quit()
            return True
        except smtplib.SMTPException as e:
            print(f"邮件发送失败 (尝试 {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                print(f"将在 {retry_delay} 秒后重试...")
                time.sleep(retry_delay)
            else:
                print("所有邮件发送尝试均失败。")
                return False
        except Exception as e:
            print(f"发生预料之外的错误 (尝试 {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                print(f"将在 {retry_delay} 秒后重试...")
                time.sleep(retry_delay)
            else:
                print("所有邮件发送尝试均因未知错误失败。")
                return False
    return False

def quick_send_my_notification(to_address, subject_line, body_content):
    """
    快捷邮件发送函数，使用预设的发件人信息和SMTP服务器。
    **重要安全警告**: 此函数默认版本可能包含硬编码的凭据。
                  在公开代码前，请务必使用安全方式管理敏感信息。
    """
    # --- 在这里预设你的固定信息 ---
    # !!! 警告：请勿在公共仓库中硬编码真实密码/授权码 !!!
    # 建议使用环境变量或安全的配置文件代替。
    my_personal_from_addr = 'YOUR_SENDER_EMAIL_HERE@example.com'  # 例如: 你的QQ邮箱
    my_personal_password = 'YOUR_SENDER_APP_PASSWORD_HERE'     # 例如: 你的QQ邮箱授权码
    my_personal_smtp_server = 'YOUR_SMTP_SERVER_HERE'          # 例如: 'smtp.qq.com'
    my_personal_smtp_port = 587                                # 或 465 (SSL)
    my_personal_sender_name = '我的脚本通知器'                   # 你希望的发件人显示名

    print(f"快捷发送: 从 {my_personal_from_addr} 发送至 {to_address}...")
    return send_notification(
        to_addr=to_address,
        subject=subject_line,
        body=body_content,
        from_addr=my_personal_from_addr,
        password=my_personal_password,
        smtp_server=my_personal_smtp_server,
        smtp_port=my_personal_smtp_port,
        sender_display_name=my_personal_sender_name
    )

# --- 你可以根据你的常用场景修改以下预设值 ---
# 示例：为某个特定类型的状态更新预设邮件信息
DEFAULT_STATUS_UPDATE_RECIPIENT = 'YOUR_DEFAULT_RECIPIENT_HERE@example.com'
DEFAULT_STATUS_UPDATE_SUBJECT = '代码运行状态更新（由你定义）'

def send_my_default_status_update(body_content):
    """
    发送一封邮件到预设的收件人，使用预设的主题。只需要提供邮件正文。
    内部调用 quick_send_my_notification，因此依赖其发件人配置。
    """
    print(f"准备发送定制状态邮件至 {DEFAULT_STATUS_UPDATE_RECIPIENT}，主题为 '{DEFAULT_STATUS_UPDATE_SUBJECT}'...")
    return quick_send_my_notification(
        to_address=DEFAULT_STATUS_UPDATE_RECIPIENT,
        subject_line=DEFAULT_STATUS_UPDATE_SUBJECT,
        body_content=body_content
    )

# 示例：为“程序完成”通知预设邮件所有信息
PROGRAM_DONE_RECIPIENT = 'YOUR_PROGRAM_DONE_RECIPIENT_HERE@example.com'
PROGRAM_DONE_SUBJECT = '程序运行完毕通知（由你定义）'
PROGRAM_DONE_BODY = '你好，\n\n你的Python脚本已顺利执行完成。\n这是预设的通知邮件。\n\n祝好！'

def notify_program_done():
    """
    发送一封完全预设的邮件，通知程序已运行完成。此函数不需要任何参数。
    内部调用 quick_send_my_notification，因此依赖其发件人配置。
    """
    print(f"准备发送程序完成通知邮件至 {PROGRAM_DONE_RECIPIENT}...")
    return quick_send_my_notification(
        to_address=PROGRAM_DONE_RECIPIENT,
        subject_line=PROGRAM_DONE_SUBJECT,
        body_content=PROGRAM_DONE_BODY
    )