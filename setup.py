# setup.py
from setuptools import setup, find_packages
import re
import os

# Function to extract version from __init__.py
def get_version_from_init(init_file_path):
    with open(init_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r"^__version__\s*=\s*['\"]([^'\"]*)['\"]", content, re.M)
    if match:
        return match.group(1)
    raise RuntimeError(f"Unable to find __version__ string in {init_file_path}")

here = os.path.abspath(os.path.dirname(__file__))
init_py_path = os.path.join(here, 'email_notifier', '__init__.py')
PACKAGE_VERSION = get_version_from_init(init_py_path)

try:
    with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = '一个简单的邮件通知库，用于在程序完成后发送邮件。'

setup(
    name='email_notifier',
    version=PACKAGE_VERSION,
    author='YOUR_NAME_HERE', # 请替换成你的名字
    author_email='YOUR_EMAIL_HERE@example.com', # 请替换成你的邮箱
    description='一个简单的Python库，用于发送邮件通知，尤其是在脚本执行完毕后。',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https_YOUR_GITHUB_REPO_URL_HERE',  # 例如: https://github.com/yourusername/email_notifier_project
    packages=find_packages(exclude=['tests*', 'docs*']),
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Communications :: Email',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)