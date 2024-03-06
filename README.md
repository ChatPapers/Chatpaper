> [!IMPORTANT]  
> 2024.3.05: 更新0.1版本  
> 2024.3.05: 安装依赖时，请选择`requirements.txt`中**指定的版本**。 安装命令：`pip install -r requirements.txt`。本项目完全开源免费
<br>

<div align=center>
<h1 aligh="center">
<img src="logo.png" width="40"> ChatPaper
</h1>
An open-source web app for summarizing articles, extracting and explaining figures &amp; tables for academic articles  
**If you like this project, please give it a Star; If you find a bug, open an issue!*

**如果喜欢这个项目，请给它一个Star；如果您使用遇到了问题，欢迎发issue！**

</div>






# Installation
1. 下载项目

    ```sh
    git clone https://github.com/binary-husky/gpt_academic.git](https://github.com/ChatPapers/Chatpaper.git
    cd ChatPaper
    ```

2. 配置API_KEY等变量

    在```sh.env ```

3. 安装依赖
    ```sh
    # （选择I: 如熟悉python, python推荐版本 3.9 ~ 3.11）备注：使用官方pip源或者阿里pip源, 临时换源方法：python -m pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
    python -m pip install -r requirements.txt

    # （选择II: 使用Anaconda）步骤也是类似的 (https://www.bilibili.com/video/BV1rc411W7Dr)：
    conda create -n gptac_venv python=3.11    # 创建anaconda环境
    conda activate gptac_venv                 # 激活anaconda环境
    python -m pip install -r requirements.txt # 这个步骤和pip安装一样的步骤
    ```

