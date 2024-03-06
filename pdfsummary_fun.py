from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_openai import OpenAIEmbeddings
from sklearn.cluster import KMeans
import numpy as np
from sklearn.decomposition import PCA
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os 


from dotenv import load_dotenv
load_dotenv()  # This loads the variables from .env
openai_api_key = os.getenv('openai_api_key')

def pdf_summary(ocr_results_folder):


    loader = DirectoryLoader(ocr_results_folder, glob="**/*.txt", loader_cls=TextLoader)

    docs = loader.load()
    page_contents = [doc.page_content for doc in docs]

    embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small",openai_api_key=openai_api_key)
    embeddings = embeddings_model.embed_documents(page_contents)

    X = np.array(embeddings)
    num_clusters = 20
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(X)
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    centroids = kmeans.cluster_centers_
    centroids_pca = pca.transform(centroids)

    closest_point_indices = find_closest_point_indices(X, centroids, 1)
    extracted_contents = [page_contents[index[0]] for index in closest_point_indices[:num_clusters]]

    prompt = ChatPromptTemplate.from_template("Summarize the article based on the texts provided from four aspects: Goal, Method, Results, and Conclusion: {topic}")
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)
    output_parser = StrOutputParser()

    chain = prompt | model | output_parser

    results = chain.invoke({"topic": ' '.join(extracted_contents)})

    return results

def find_closest_point_indices(X, centroids, num_points=1):
    closest_indices = []
    for center in centroids:
        # Calculating Euclidean distances from each point in X to the centroid
        distances = np.linalg.norm(X - center, axis=1)

        # Getting the indices of the closest 'num_points' points
        closest_idx = np.argsort(distances)[:num_points]

        # Adding the indices of the closest points for this centroid
        closest_indices.append(closest_idx)

    return closest_indices