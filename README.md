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
    
    ```
    安装[tesseract](https://tesseract-ocr.github.io/tessdoc/Installation.html)用于文字OCR， 请根据tesseract官网进行安装。
   
5. 安装模型用于提取文字，表格和图片

    下载detectron2：
    ```sh
     git clone https://github.com/facebookresearch/detectron2.git

    ```
    下载unilm,并修改一处bug：
    ```sh
     git clone https://github.com/microsoft/unilm.git
     sed -i 's/from collections import Iterable/from collections.abc import Iterable/' unilm/dit/object_detection/ditod/table_evaluation/data_structure.py"
    ```
    下载Dit document layout model：
    ```sh
    curl -LJ -o publaynet_dit-b_cascade.pth 'https://layoutlm.blob.core.windows.net/dit/dit-fts/publaynet_dit-b_cascade.pth?sv=2022-11-02&ss=b&srt=o&sp=r&se=2033-06-08T16:48:15Z&st=2023-06-08T08:48:15Z&spr=https&sig=a9VXrihTzbWyVfaIDlIT1Z0FoR1073VB0RLQUMuudD4%3D'
    ```
    
