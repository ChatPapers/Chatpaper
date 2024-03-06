
> **🚨 IMPORTANT UPDATES 🚨**
> - **2024-03-05**: Version 0.1 update released.
> - **2024-03-05**: When installing dependencies, please use **the specified versions** in `requirements.txt`. Install using the command: `pip install -r requirements.txt`. This project is fully open source and free to use.
> - **2024-03-05**: Recommended system requirements: 6GB RAM and 8GB VRAM.

<div align="center">
    <h1>
        <img src="logo.png" width="40"> ChatPaper
    </h1>
    <p>An innovative open-source LLM-based web app for summarizing academic articles, extracting, and analyzing figures & tables.</p>
    <p><strong>Love this project? Give it a Star! 🌟 Found a bug? Open an issue! 🐛</strong></p>
    <p>基于大语言模型的开源Web应用程序，用于学术文章摘要、表格和图片的提取与分析。</p>
    <p><strong>喜欢这个项目？请给它一个星标！🌟 发现错误？请提交问题！🐛</strong></p>
    
[![Github][Github-image]][Github-url]
[![License][License-image]][License-url]
[![Discord][Discord-image]][Discord-url]
</div>


[Discord-image]: https://img.shields.io/badge/Discord-Join%20Us-7289DA?style=flat&logo=Discord
[Discord-url]: https://discord.com/invite/uQJXzE3K8G
[Github-image]: https://img.shields.io/badge/GitHub-View%20on%20GitHub-blue
[Github-url]: https://github.com/ChatPapers/Chatpaper
[License-image]: https://img.shields.io/badge/License-MIT-green
[License-url]: https://opensource.org/license/mit


## 安装指南 (Installation Guide)

1. **克隆项目 (Clone the Project)**
    ```sh
    git clone https://github.com/ChatPapers/ChatPaper.git
    cd ChatPaper
    ```

2. **配置环境变量 (Set Up Environment Variables)**
    - Open the `.env` file with a text editor and fill in the `openai_api_key`. Visit [OpenAI API documentation](https://openai.com/api/) for details on obtaining an API key.

3. **安装依赖 (Install Dependencies)**
    ```sh
    pip install -r requirements.txt
    ```

4. **安装Tesseract OCR (Install Tesseract for OCR)**
    - Follow the instructions on the [Tesseract OCR official website](https://tesseract-ocr.github.io/tessdoc/Installation.html) for installation.

5. **安装模型 (Install Models for Text, Tables, and Images Extraction)**
    - **Detectron2** for object detection:
        ```sh
        git clone https://github.com/facebookresearch/detectron2.git
        ```
    - **Unilm** with a minor bug fix:
        ```sh
        git clone https://github.com/microsoft/unilm.git
        sed -i 's/from collections import Iterable/from collections.abc import Iterable/' unilm/dit/object_detection/ditod/table_evaluation/data_structure.py
        ```
    - **Download Dit document layout model**:
        ```sh
        curl -LJ -o publaynet_dit-b_cascade.pth 'https://layoutlm.blob.core.windows.net/dit/dit-fts/publaynet_dit-b_cascade.pth'
        ```

## 运行应用 (Running the App)

Navigate to the ChatPaper directory and run:
```sh
python app.py
```
Access the web app at [http://127.0.0.1:7860](http://127.0.0.1:7860).

## 社区支持与联系方式 (Community Support & Contact Info)

### Join Our Discord
- 📢 Join our Discord channel [here](https://discord.gg/uQJXzE3K8G) and connect with the community!

### Contact Information
For any questions or feedback about this project, feel free to reach out.
- **Email**: davidyam521@gmail.com

