> [!IMPORTANT]  
> 2024.3.05: 更新0.1版本  
> 2024.3.05: 安装依赖时，请选择`requirements.txt`中**指定的版本**。安装命令：`pip install -r requirements.txt`。本项目完全开源免费
> 2024.3.05: 推荐电脑配置6 g RAM and 8 g VRAM
<br>

<div align=center>
<h1 aligh="center">
<img src="logo.png" width="40"> ChatPaper
</h1>
An open-source LLM based web app for summarizing articles, extracting and explaining figures &amp; tables for academic articles
    
**If you like this project, please give it a Star; If you find a bug, open an issue!**

基于web和大语言模型的开源软件，用于学术论文总结，表格图片提取和分析。

**如果喜欢这个项目，请给它一个Star；如果您使用遇到了问题，欢迎发issue！**

</div>




# 安装方法
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
4. 安装tesseract用于文字OCR
    请根据[tesseract官网](https://tesseract-ocr.github.io/tessdoc/Installation.html)进行安装。
   
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
# 使用
进入Chatpaper目录下,运行：
    ``` 
    python app.py 
    ```
打开网页[127.0.0.1:7860](127.0.0.1:7860)即可使用

# 社区支持

# Join Discord US
📢 Join [Our discord Channel](http://discord.gg/fHNM5PxfvR)

Looking forward to seeing you there!

# Contact Information
If you have any questions or feedback about this porject！Feel Free to contact us

**Email**: davidyam521@gmail.com
