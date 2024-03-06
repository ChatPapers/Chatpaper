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
    git clone https://github.com/ChatPapers/Chatpaper.git
    cd ChatPaper
    ```

2. 配置API_KEY等变量

    用记事本打开```.env ```文件， 填写```openai_api_key```。请访问[https://openai.com/blog/openai-api](https://openai.com/blog/openai-api)了解如何获取api key

3. 安装依赖
    ```sh
     pip install -r requirements.txt

    # （选择II: 使用Anaconda）步骤也是类似的 (https://www.bilibili.com/video/BV1rc411W7Dr)：
    conda create -n gptac_venv python=3.11    # 创建anaconda环境
    conda activate gptac_venv                 # 激活anaconda环境
    python -m pip install -r requirements.txt # 这个步骤和pip安装一样的步骤
    ```

