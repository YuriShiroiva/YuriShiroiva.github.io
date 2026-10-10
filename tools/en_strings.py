"""Traduções usadas por build_en.py: cada trecho de texto das páginas em português -> inglês.

A chave é o texto exatamente como aparece na página (espaços repetidos viram um só).
Trechos que ficam iguais nas duas línguas vão em KEEP. Números sozinhos (0,87, 99,9%) são convertidos
automaticamente para ponto decimal.
"""

KEEP = {
    "Yuri Shiroiva", "Yuri", "Shiroiva", "Data Science", "Deep Learning", "GitHub", "LinkedIn", "PUCPR", "UFJF", "IBM",
    "Kaggle", "DeepLearning.AI", "Supervised ML: Regression and Classification", "Google", "Data Analytics", "IoTag",
    "LLM", "Claude · Vertex AI", "MCP", "Python", "Cassandra", "PostgreSQL", "CAN · ISOBUS · J1939", "GCP", "Optcore",
    "Streamlit", "Appsmith", "FolhaSã", "EfficientNet, Transfer learning, PyTorch, timm, FastAPI, ONNX, MLflow, pytest,",
    "pandas · Plotly · Prophet", "scikit-learn · pandas", "NetworkX · pandas", "Python · pandas", "pandas", "NumPy",
    "scikit-learn", "LightGBM", "SQL", "RAG", "LangChain", "Hugging Face", "Prompt engineering", "ETL / ELT", "GeoJSON",
    "PyTorch", "U-Net", "DeepLabV3+", "CNNs", "Ensembles", "Sentinel-2", "Stack", "Modern", "Claude API", "Google Cloud",
    "Docker", "yurishiroivabr@gmail.com", "Currículo (PT) ↓", "Resume (EN) ↓", "shiroiva",
    "Python · PyTorch · segmentation-models · Rasterio · xarray · Shapely", "Fig. 1", "Fig. 2", "Fig. 3", "Fig. 4",
    "Python · PyTorch · scikit-learn · pandas · Matplotlib", "Python · PyTorch · timm · FastAPI · ONNX · MLflow", "27 min",
    "Python · OpenCV · NumPy · Matplotlib", "PT", "EN",
}

TR = {
    # ---------------- comum (topo, menu, rodapé)
    "Curitiba, PR": "Curitiba, Brazil",
    "Curitiba, PR ·": "Curitiba, Brazil ·",
    "Data Science · IA · Python": "Data Science · AI · Python",
    "Formação": "Education",
    "IA Aplicada · PUCPR": "Applied AI · PUCPR",
    "Fale comigo": "Let's talk",
    "Idioma": "Language",
    "Voltar ao topo ↑": "Back to top ↑",
    "Navegação principal": "Main navigation",
    "Início": "Home",
    "Sobre": "About",
    "Experiência": "Experience",
    "Projetos": "Projects",
    "O que faço": "What I do",
    "Contato": "Contact",
    "Aberto a oportunidades": "Open to opportunities",
    "Cientista de dados, Engenheiro de IA, LLMs e agentes, Machine Learning, Deep Learning, Séries temporais, CAN bus e ISOBUS,":
        "Data scientist, AI engineer, LLMs and agents, Machine Learning, Deep Learning, Time series, CAN bus and ISOBUS,",
    "Abrir menu": "Open menu",
    "E-mail": "Email",
    "Todos os projetos": "All projects",
    "Próximo": "Next",
    "Próximo projeto": "Next project",
    "Papel": "Role",
    "Contexto": "Context",
    "Ano": "Year",
    "Autor": "Author",
    "Entrega": "Delivery",
    "Limitações e próximos passos": "Limitations and next steps",

    # ---------------- página inicial
    "Yuri Shiroiva | Cientista de Dados e Engenheiro de IA": "Yuri Shiroiva | Data Scientist and AI Engineer",
    "Portfólio de Yuri Shiroiva, cientista de dados e engenheiro de IA. Trabalho com LLMs, séries temporais, machine learning e deep learning com imagens de satélite.":
        "Portfolio of Yuri Shiroiva, data scientist and AI engineer. I work with LLMs, time series, machine learning and deep learning on satellite imagery.",
    "Cientista de dados e engenheiro de IA. LLMs, séries temporais, machine learning e deep learning.":
        "Data scientist and AI engineer. LLMs, time series, machine learning and deep learning.",
    "Olá! Eu sou": "Hi! I'm",
    "Ver projetos": "See projects",
    "Currículo": "Resume",
    "Cientista de dados · Engenheiro de IA": "Data Scientist · AI Engineer",
    "Data Science, LLMs e agentes, deep learning": "Data Science, LLMs and agents, deep learning",
    "LLMs &amp; Agentes": "LLMs &amp; Agents",
    "Há mais de 3 anos trabalho com dados e IA, hoje no agro. Coloco LLMs e agentes em produção, construo pipelines de séries temporais e pesquiso deep learning com imagens de satélite.":
        "I've been working with data and AI for over 3 years, currently in agtech. I ship LLMs and agents to production, build time series pipelines and research deep learning on satellite imagery.",
    "Role para conhecer": "Scroll to explore",
    "Sobre mim": "About me",
    "Sou cientista de dados e engenheiro de IA, com mais de 3 anos de experiência. Na IoTag, cuido do pipeline de dados e da parte de IA de uma plataforma que recebe a telemetria de máquinas agrícolas. Fora do trabalho, pesquiso deep learning com imagens de satélite. Sou curioso e adoro aprender coisas novas: quase todo projeto meu começou com a vontade de entender algo que eu ainda não sabia fazer.":
        "I'm a data scientist and AI engineer with over 3 years of experience. At IoTag, I'm responsible for the data pipeline and the AI layer of a platform that collects telemetry from agricultural machinery. Outside work, I research deep learning on satellite imagery. I'm curious and love learning new things: almost every project of mine started with wanting to understand something I didn't know how to do yet.",
    "2024 a 2026": "2024 to 2026",
    "2021 a 2023": "2021 to 2023",
    "2023 a 2024": "2023 to 2024",
    "Tecnólogo em Inteligência Artificial Aplicada": "Technologist Degree in Applied Artificial Intelligence",
    "Média 9,27 de 10 e Menção Honrosa pelo desempenho no curso.": "GPA of 9.27 out of 10 and an Honorable Mention for academic performance.",
    "Engenharia Elétrica (Robótica e Automação)": "Electrical Engineering (Robotics and Automation)",
    "Saí em 2024 para cursar IA Aplicada na PUCPR.": "Left in 2024 to study Applied AI at PUCPR.",
    "Certificados": "Certificates",
    "Generative AI Engineering e Generative AI Engineering with LLMs": "Generative AI Engineering and Generative AI Engineering with LLMs",
    "Computer Vision e Intermediate Machine Learning": "Computer Vision and Intermediate Machine Learning",
    "Data Science Professional e Applied Data Science": "Data Science Professional and Applied Data Science",
    "Idiomas": "Languages",
    "Português nativo, inglês técnico (leio bem documentação e artigos) e espanhol básico.":
        "Native Portuguese, technical English (I read documentation and papers comfortably) and basic Spanish.",
    "Desde 2024": "Since 2024",
    "Cientista de Dados / Engenheiro de IA": "Data Scientist / AI Engineer",
    "Cuido do pipeline de dados e da parte de IA da plataforma de telemetria de máquinas agrícolas.":
        "I'm responsible for the data pipeline and the AI layer of an agricultural machinery telemetry platform.",
    "Ver tudo o que fiz na IoTag": "See everything I did at IoTag",
    "O que fiz na IoTag": "What I did at IoTag",
    "Diagnóstico de máquinas com LLM": "LLM machine diagnostics",
    "Projetei do começo ao fim um recurso com o Claude na Vertex AI que resume a telemetria do Cassandra e entrega diagnósticos estruturados, validados por schema, para a equipe de data science. O diagnóstico de falhas caiu de 2 semanas para 5 dias.":
        "I designed end to end a feature with Claude on Vertex AI that summarizes telemetry from Cassandra and delivers structured, schema-validated diagnostics to the data science team. Fault diagnosis went from 2 weeks to 5 days.",
    "Agentes para o CAN bus": "Agents for the CAN bus",
    "Arquitetei um sistema com vários agentes de LLM que roda kernels Python em paralelo por servidores MCP para decifrar mensagens CAN sem documentação. O tempo por modelo de máquina caiu de 1 mês para 2 semanas, e mais de 20 sinais decodificados já estão em produção. Tudo é conferido com dados conhecidos e testado num conjunto separado.":
        "I architected a multi-agent LLM system that runs Python kernels in parallel through MCP servers to decode undocumented CAN messages. Time per machine model dropped from 1 month to 2 weeks, and more than 20 decoded signals are already in production. Everything is checked against known data and tested on a held-out set.",
    "Mais de 10 marcas": "10+ brands",
    "Criei um registro de plugins para a decodificação J1939/ISOBUS que isola cada marca do núcleo do pipeline. Com ele, a plataforma passou a suportar mais de 10 marcas e modelos de equipamento.":
        "I built a plugin registry for J1939/ISOBUS decoding that isolates each brand from the pipeline core. With it, the platform now supports more than 10 equipment brands and models.",
    "Dados de um fornecedor": "Data from a vendor",
    "Liberei os dados geoespaciais de mais de 200 talhões que estavam presos ao formato proprietário de um fornecedor, integrando esse formato ao pipeline de dados, sem depender da API do parceiro.":
        "I unlocked the geospatial data of more than 200 fields that were stuck in a vendor's proprietary format by integrating that format into the data pipeline, with no dependency on the partner's API.",
    "ISOXML automático": "Automated ISOXML",
    "Antes, um arquivo ISOXML era montado à mão para cada operação de cada máquina. Troquei isso por um modelo único gerado por um pipeline em Python, junto com mapas de cobertura em GeoJSON feitos a partir da telemetria bruta do CAN bus.":
        "ISOXML files used to be assembled by hand for every operation of every machine. I replaced that with a single template generated by a Python pipeline, along with GeoJSON coverage maps built from raw CAN bus telemetry.",
    "Histórico auditável": "Auditable history",
    "Modelei no Cassandra um esquema bitemporal que só acrescenta dados (append-only). Dá para reconstruir a configuração de qualquer operação de campo em qualquer ponto do histórico.":
        "I modeled a bi-temporal, append-only schema in Cassandra. The configuration of any field operation can be reconstructed at any point in its history.",
    "Correções em produção": "Production fixes",
    "Corrigi os totais de produto aplicado que iam para os clientes depois de achar dois defeitos no serviço de ingestão: a conversão de unidade na compensação do atraso de vazão e o escopo de uma agregação.":
        "I fixed the applied-product totals sent to customers after finding two defects in the ingestion service: the unit conversion in the flow delay compensation and the scope of an aggregation.",
    "Estagiário de Desenvolvimento de Software": "Software Development Intern",
    "Dashboards em Streamlit e Appsmith e tratamento de dados para clientes.": "Streamlit and Appsmith dashboards and data processing for clients.",
    "Ver tudo o que fiz na Optcore": "See everything I did at Optcore",
    "O que fiz na Optcore": "What I did at Optcore",
    "Dashboards para a diretoria": "Dashboards for leadership",
    "Evoluí os dashboards em Streamlit e Appsmith que a diretoria de uma empresa cliente usava para acompanhar os resultados da sua carteira de cerca de 30 clientes.":
        "I evolved the Streamlit and Appsmith dashboards that a client company's leadership used to track results across a portfolio of about 30 customers.",
    "Tratamento de dados": "Data processing",
    "Desenvolvi em Python a limpeza, a padronização e a deduplicação de dados de shoppings vindos de fontes diferentes, para um protótipo de análise de varejo.":
        "I built Python routines to clean, standardize and deduplicate shopping mall data coming from different sources, for a retail analytics prototype.",
    "Qualidade de dados": "Data quality",
    "Deduplicação": "Deduplication",
    "Ver projeto": "View project",
    "Talhões por satélite": "Field boundaries from satellite",
    "TCC": "Thesis",
    "Deep Learning, PyTorch, Sentinel-2, Segmentação, U-Net, Ensemble, Rasterio, GeoJSON,":
        "Deep Learning, PyTorch, Sentinel-2, Segmentation, U-Net, Ensemble, Rasterio, GeoJSON,",
    "Redes neurais: câmbio e CO₂": "Neural networks: exchange rate and CO₂",
    "LSTM, Séries temporais, Agrupamento, PyTorch, scikit-learn, pandas, Regressão,":
        "LSTM, Time series, Clustering, PyTorch, scikit-learn, pandas, Regression,",
    "Visão computacional": "Computer vision",
    "Falhas industriais": "Industrial defects",
    "Indústria 4.0": "Industry 4.0",
    "OpenCV, CLAHE, Canny, Morfologia, Segmentação, NumPy,": "OpenCV, CLAHE, Canny, Morphology, Segmentation, NumPy,",
    "Mais em dados": "More in data",
    "Covid-19 no Brasil": "Covid-19 in Brazil",
    "Análise exploratória dos casos no Brasil e previsão com ARIMA e Prophet.": "Exploratory analysis of cases in Brazil and forecasting with ARIMA and Prophet.",
    "Previsão de chuva na Austrália": "Rain prediction in Australia",
    "Comparei cinco modelos (regressão linear, KNN, árvore de decisão, regressão logística e SVM) para prever se vai chover no dia seguinte.":
        "I compared five models (linear regression, KNN, decision tree, logistic regression and SVM) to predict whether it will rain the next day.",
    "Redes de Game of Thrones": "Game of Thrones networks",
    "Grafos de quem interage com quem na 1ª e na 8ª temporada: métricas da rede, personagens mais centrais e comunidades.":
        "Graphs of who interacts with whom in seasons 1 and 8: network metrics, most central characters and communities.",
    "Registros duplicados com Levenshtein": "Duplicate records with Levenshtein",
    "Workshop de extensão em que ensinei a usar distância de edição para achar clientes duplicados numa base.":
        "An extension workshop where I taught how to use edit distance to find duplicate customers in a database.",
    "Mais no GitHub": "More on GitHub",
    "O que eu faço": "What I do",
    "Trabalho em quatro frentes que se conectam: dados, machine learning, LLMs e visão computacional. Também cuido da nuvem e das APIs para que tudo isso chegue em quem vai usar.":
        "I work on four connected fronts: data, machine learning, LLMs and computer vision. I also take care of the cloud and the APIs so all of it reaches the people who use it.",
    "Data Science e Machine Learning": "Data Science and Machine Learning",
    "Análise exploratória, estatística, séries temporais e modelos de machine learning, sempre com validação cruzada e métricas que façam sentido para o problema.":
        "Exploratory analysis, statistics, time series and machine learning models, always with cross-validation and metrics that make sense for the problem.",
    "Validação cruzada": "Cross-validation",
    "IA generativa e agentes": "Generative AI and agents",
    "LLMs rodando em produção: vários agentes trabalhando juntos, ferramentas via MCP, RAG e respostas estruturadas validadas por schema.":
        "LLMs running in production: multiple agents working together, tools via MCP, RAG and structured responses validated by schema.",
    "Engenharia de dados": "Data engineering",
    "Pipelines ETL/ELT para séries temporais com muito volume, modelagem no Cassandra e no PostgreSQL e rotinas de qualidade de dados, inclusive geoespaciais.":
        "ETL/ELT pipelines for high-volume time series, data modeling in Cassandra and PostgreSQL, and data quality routines, including for geospatial data.",
    "Visão computacional e deep learning": "Computer vision and deep learning",
    "Segmentação, classificação e detecção com PyTorch, usando ensembles, TTA e transfer learning. Já trabalhei com imagens de satélite, de lavoura e industriais.":
        "Segmentation, classification and detection with PyTorch, using ensembles, TTA and transfer learning. I've worked with satellite, crop and industrial imagery.",
    "Stack moderna": "Modern stack",
    "Moderna": "Modern",
    "Profissional em": "Proficient in",
    "Precisa de alguém para dados e IA?": "Need someone for data and AI?",
    "Vamos conversar.": "Let's talk.",
    "Currículo (PDF)": "Resume (PDF)",

    # ---------------- talhões
    "Detecção de talhões por satélite | Yuri Shiroiva": "Field boundary detection from satellite imagery | Yuri Shiroiva",
    "Meu TCC: deep learning para encontrar talhões agrícolas em imagens Sentinel-2 e entregar os polígonos numa plataforma web.":
        "My undergraduate thesis: deep learning that finds agricultural field boundaries in Sentinel-2 imagery and delivers the polygons in a web platform.",
    "Detecção de talhões agrícolas por satélite": "Agricultural field boundary detection from satellite imagery",
    "Deep learning com Sentinel-2: Dice mediano de 0,87, fine-tuning regional de 0,25 para 0,72 e separação de talhões.":
        "Deep learning on Sentinel-2: median Dice of 0.87, regional fine-tuning from 0.25 to 0.72 and separation of adjacent fields.",
    "TCC · IA Aplicada · PUCPR · 2026": "Thesis · Applied AI · PUCPR · 2026",
    "Meu TCC: um pipeline de deep learning que encontra cada talhão em imagens Sentinel-2 de várias datas e entrega os polígonos numa plataforma web.":
        "My undergraduate thesis: a deep learning pipeline that finds every field in multi-date Sentinel-2 imagery and delivers the polygons in a web platform.",
    "Título do trabalho:": "Thesis title:",
    "Segmentação Automática de Limites de Talhões Agrícolas com Redes Neurais Profundas e Imagens Sentinel-2 Multitemporais":
        "Automatic Segmentation of Agricultural Field Boundaries with Deep Neural Networks and Multitemporal Sentinel-2 Imagery",
    "Ver código no GitHub ↗": "View code on GitHub ↗",
    "Autor (pesquisa, modelagem e engenharia)": "Author (research, modeling and engineering)",
    "TCC de IA Aplicada na PUCPR": "Applied AI undergraduate thesis at PUCPR",
    "Três etapas lado a lado: imagem Sentinel-2, talhões detectados sobrepostos e máscara de instâncias com um talhão por cor":
        "Three stages side by side: Sentinel-2 image, detected fields overlaid and an instance mask with one color per field",
    "O problema": "The problem",
    "Desenhar talhões à mão dá muito trabalho. Eu queria automatizar isso usando só imagem de satélite gratuita e um computador comum.":
        "Drawing field boundaries by hand takes a lot of work. I wanted to automate it using only free satellite imagery and an ordinary computer.",
    "O talhão é a unidade básica da fazenda: é por ele que se planeja plantio, aplicação e colheita. No TCC, montei o caminho completo, da imagem do Sentinel-2 (10 m, gratuita) até polígonos com a área em hectares, e validei tudo num benchmark público para que qualquer pessoa possa reproduzir.":
        "A field is the basic unit of a farm: planting, spraying and harvesting are all planned around it. In my thesis, I built the full path, from the Sentinel-2 image (10 m, free) to polygons with their area in hectares, and validated everything on a public benchmark so anyone can reproduce it.",
    "Resultados principais": "Key results",
    "Dice mediano no teste, em 1.139 tiles do AI4Boundaries": "Median test Dice across 1,139 AI4Boundaries tiles",
    "Dice no Brasil depois do fine-tuning regional. Sem ajuste, era 0,25": "Dice in Brazil after regional fine-tuning. Without it, it was 0.25",
    "no F1 de objeto ao separar os talhões (de 0,455 para 0,594)": "in object F1 by separating adjacent fields (from 0.455 to 0.594)",
    "canais de entrada: 5 bandas em 6 datas diferentes": "input channels: 5 bands across 6 different dates",
    "Como funciona": "How it works",
    "Entrada multitemporal": "Multitemporal input",
    "Seis datas do Sentinel-2 com as bandas B2, B3, B4, B8 e o NDVI, somando 30 canais. Assim o modelo vê a cultura mudando ao longo do tempo, e não só a cor de um dia.":
        "Six Sentinel-2 dates with bands B2, B3, B4, B8 and NDVI, 30 channels in total. This way the model sees the crop change over time, not just its color on a single day.",
    "Ensemble de 6 redes": "Ensemble of 6 networks",
    "U-Net, DeepLabV3+ e U-Net++ com encoders ResNet-34/50. As previsões são combinadas e reforçadas com TTA (flips).":
        "U-Net, DeepLabV3+ and U-Net++ with ResNet-34/50 encoders. Predictions are combined and reinforced with TTA (flips).",
    "Pós-processamento": "Post-processing",
    "Limiar e área mínima calibrados na validação. Depois a máscara vira polígonos com Rasterio e Shapely.":
        "Threshold and minimum area calibrated on the validation set. Then the mask is turned into polygons with Rasterio and Shapely.",
    "Separação de talhões": "Field separation",
    "Um modelo de 3 classes (interior, borda e fundo) separa talhões vizinhos que a segmentação comum acabava juntando.":
        "A 3-class model (interior, boundary and background) separates neighboring fields that plain segmentation would merge.",
    "Um GeoJSON com um polígono e a área em hectares para cada talhão, servido por uma plataforma web com mapa.":
        "A GeoJSON with one polygon and its area in hectares for each field, served by a web platform with a map.",
    "Grade de exemplos: imagem Sentinel-2, mapa de probabilidade, talhões preditos e gabarito, com Dice entre 0,97 e 0,98":
        "Grid of examples: Sentinel-2 image, probability map, predicted fields and ground truth, with Dice between 0.97 and 0.98",
    "Do começo ao fim: imagem Sentinel-2, mapa de probabilidade e talhões previstos, comparados com o gabarito.":
        "End to end: Sentinel-2 image, probability map and predicted fields, compared with the ground truth.",
    "Generalização": "Generalization",
    "Na Europa o modelo foi muito bem. No Brasil, sem ajuste, ele quase não via os talhões.":
        "In Europe the model did very well. In Brazil, without fine-tuning, it barely saw the fields.",
    "O modelo foi treinado no AI4Boundaries, que é europeu. No benchmark Fields of The World (Brasil), o Dice caiu para cerca de 0,25. Fiz um fine-tuning com poucos dados locais e ele voltou para 0,72. A lição: reconhecer talhão depende muito da região e do sensor, e ajustar o modelo sai bem mais barato do que treinar outro do zero.":
        "The model was trained on AI4Boundaries, a European dataset. On the Fields of The World benchmark (Brazil), Dice dropped to about 0.25. I fine-tuned it with a small amount of local data and it went back up to 0.72. The lesson: recognizing fields depends heavily on the region and the sensor, and adapting a model is much cheaper than training a new one from scratch.",
    "Dice médio por cenário, de 0 a 1": "Mean Dice by scenario, from 0 to 1",
    "Dice médio, de 0 a 1": "Mean Dice, from 0 to 1",
    "Europa, onde foi treinado: Dice 0,77": "Europe, where it was trained: Dice 0.77",
    "Europa (onde foi treinado)": "Europe (where it was trained)",
    "Brasil sem ajuste: Dice 0,25": "Brazil without fine-tuning: Dice 0.25",
    "Brasil sem ajuste (zero-shot)": "Brazil without fine-tuning (zero-shot)",
    "Brasil depois do fine-tuning: Dice 0,72": "Brazil after fine-tuning: Dice 0.72",
    "Brasil depois do fine-tuning": "Brazil after fine-tuning",
    "Comparação no Brasil: imagem, gabarito, predição zero-shot quase vazia e predição após fine-tuning recuperando os talhões":
        "Comparison in Brazil: image, ground truth, a nearly empty zero-shot prediction and the fine-tuned prediction recovering the fields",
    "Sem ajuste, o modelo não enxerga o talhão brasileiro. Depois do fine-tuning, ele aparece.":
        "Without fine-tuning, the model can't see Brazilian fields. After fine-tuning, they show up.",
    "De pixel para talhão": "From pixels to fields",
    "Acertar os pixels não é a mesma coisa que encontrar os talhões.": "Getting the pixels right is not the same as finding the fields.",
    "O Dice mede área. Só que quem usa o sistema precisa de cada talhão como um polígono separado, e a segmentação comum juntava talhões vizinhos. Por isso treinei um modelo de 3 classes (interior, borda e fundo) e avaliei talhão por talhão, em 653 talhões de teste.":
        "Dice measures area. But users need each field as a separate polygon, and plain segmentation merged neighboring fields. So I trained a 3-class model (interior, boundary and background) and evaluated it field by field, on 653 test fields.",
    "Métricas de objeto, de 0 a 1": "Object metrics, from 0 to 1",
    "F1 de objeto (IoU ≥ 0,5), de 0 a 1": "Object F1 (IoU ≥ 0.5), from 0 to 1",
    "Baseline semântico: F1 de objeto 0,455": "Semantic baseline: object F1 0.455",
    "Baseline semântico": "Semantic baseline",
    "Borda + separação: F1 de objeto 0,594": "Boundary + separation: object F1 0.594",
    "Borda + separação": "Boundary + separation",
    "Panoptic Quality, de 0 a 1": "Panoptic Quality, from 0 to 1",
    "Baseline semântico: PQ 0,381": "Semantic baseline: PQ 0.381",
    "Borda + separação: PQ 0,512": "Boundary + separation: PQ 0.512",
    "Grade comparando imagem, gabarito de instâncias, baseline semântico que funde talhões e o modelo de borda que os separa":
        "Grid comparing the image, instance ground truth, the semantic baseline that merges fields and the boundary model that separates them",
    "O baseline junta talhões vizinhos. Com a cabeça de borda, eles ficam separados.":
        "The baseline merges neighboring fields. With the boundary head, they stay separate.",
    "Na plataforma": "In the platform",
    "Depois virou produto: você desenha uma área no mapa e recebe os talhões.":
        "Then it became a product: you draw an area on the map and get the fields back.",
    "O frontend, em React com Leaflet, recebe a área desenhada. O backend, em FastAPI, baixa as imagens Sentinel-2 L2A via STAC (sem precisar de login), roda o modelo de 3 classes com janela deslizante e TTA e devolve um polígono por talhão, com a área em hectares. Buscar as 6 datas e rodar o modelo leva de 30 a 60 segundos.":
        "The frontend, in React with Leaflet, receives the drawn area. The backend, in FastAPI, downloads Sentinel-2 L2A imagery via STAC (no login needed), runs the 3-class model with a sliding window and TTA, and returns one polygon per field with its area in hectares. Fetching the 6 dates and running the model takes 30 to 60 seconds.",
    "Exportação em GeoJSON, Shapefile e GeoPackage": "Export to GeoJSON, Shapefile and GeoPackage",
    "Detecção de pivôs centrais com transformada de Hough": "Center-pivot detection with the Hough transform",
    "Docker para CPU e GPU, com docker-compose": "Docker for CPU and GPU, with docker-compose",
    "Testes com pytest e CI no GitHub Actions": "Tests with pytest and CI on GitHub Actions",
    "Também apliquei a solução na IoTag, como projeto de extensão. Cinco profissionais de engenharia, ciência de dados e DevOps avaliaram a ferramenta com nota média de 4,6 de 5 em utilidade e precisão.":
        "I also deployed the solution at IoTag as a university extension project. Five professionals from engineering, data science and DevOps rated the tool 4.6 out of 5 on average for usefulness and accuracy.",
    "Três exemplos da plataforma: imagem Sentinel-2, talhões separados sobrepostos e máscara com um polígono por talhão":
        "Three platform examples: Sentinel-2 image, separated fields overlaid and a mask with one polygon per field",
    "A plataforma entregando um polígono para cada talhão.": "The platform delivering one polygon per field.",
    "Decisões de engenharia": "Engineering decisions",
    "Multitemporal em vez de RGB": "Multitemporal instead of RGB",
    "Testei segmentar uma única imagem RGB e desisti: cor e textura mudam demais de uma cena para outra. Com 6 datas, o modelo acompanha o ciclo da cultura.":
        "I tried segmenting a single RGB image and gave up: color and texture change too much from one scene to another. With 6 dates, the model follows the crop cycle.",
    "Pré-processamento idêntico": "Identical preprocessing",
    "A ordem das bandas e datas e a normalização por percentil (2 a 98) são iguais no treino e na inferência. Descobri que uma ordem errada zerava a previsão, então corrigi e deixei o código conferindo isso.":
        "Band and date order and the percentile normalization (2 to 98) are the same in training and inference. I found that a wrong order zeroed out the predictions, so I fixed it and made the code check for it.",
    "Avaliação sem vazamento": "Leak-free evaluation",
    "Usei a divisão oficial do FTW. Calibrei só na validação e calculei as métricas finais em 188 tiles de teste que o modelo nunca viu, com intervalos de confiança de 95% e tamanho de efeito (Cohen's d).":
        "I used the official FTW split. I calibrated only on validation and computed the final metrics on 188 test tiles the model had never seen, with 95% confidence intervals and effect size (Cohen's d).",
    "Hardware modesto": "Modest hardware",
    "Treinei numa GTX 1650, em fp32 (com fp16 dava NaN) e com batch pequeno. Deu trabalho, mas funcionou.":
        "I trained on a GTX 1650, in fp32 (fp16 produced NaN) and with a small batch size. It took effort, but it worked.",
    "Talhões muito pequenos (menos de 5% do tile) ainda são o ponto fraco, com Dice entre 0,18 e 0,49. Os grandes e médios ficam entre 0,70 e 0,93. Como próximos passos, quero mais exemplos de talhões pequenos, imagens com resolução maior e uma comparação com modelos fundacionais como o SAM.":
        "Very small fields (under 5% of the tile) are still the weak spot, with Dice between 0.18 and 0.49. Large and medium fields stay between 0.70 and 0.93. As next steps, I want more examples of small fields, higher-resolution imagery and a comparison with foundation models such as SAM.",

    # ---------------- redes neurais
    "Redes neurais: câmbio e CO₂ | Yuri Shiroiva": "Neural networks: exchange rate and CO₂ | Yuri Shiroiva",
    "LSTM em PyTorch para prever a cotação do dólar (R² de 0,92 no teste) e rede competitiva para agrupar veículos por cilindrada, eficiência e emissão de CO₂.":
        "An LSTM in PyTorch to forecast the US dollar exchange rate (R² of 0.92 on the test set) and a competitive network to cluster vehicles by engine size, efficiency and CO₂ emissions.",
    "Data Science · Redes Neurais · PUCPR · 2026": "Data Science · Neural Networks · PUCPR · 2026",
    "Redes neurais para prever o dólar e agrupar carros": "Neural networks to forecast the dollar and cluster cars",
    "Duas redes em PyTorch numa atividade de Redes Neurais da PUCPR: uma LSTM que prevê a cotação do dólar e uma rede competitiva que agrupa veículos pela relação entre cilindrada, eficiência e emissão de CO₂.":
        "Two PyTorch networks for a Neural Networks assignment at PUCPR: an LSTM that forecasts the US dollar exchange rate and a competitive network that clusters vehicles by the relationship between engine size, efficiency and CO₂ emissions.",
    "Autor (ajuste, treino e avaliação dos modelos)": "Author (tuning, training and evaluation of the models)",
    "Disciplina de Redes Neurais da PUCPR, a partir do código-base do curso": "Neural Networks course at PUCPR, built on the course's starter code",
    "Gráfico das previsões da LSTM para o dólar e gráfico de dispersão dos veículos agrupados por cilindrada e CO₂":
        "Chart of the LSTM dollar forecast and a scatter plot of vehicles clustered by engine size and CO₂",
    "de R² da LSTM no teste, em dados que ela não viu no treino": "LSTM R² on the test set, on data it never saw in training",
    "valores anteriores usados pela LSTM para prever o próximo": "previous values the LSTM uses to predict the next one",
    "de R² da curva entre eficiência e emissão de CO₂": "R² of the curve between efficiency and CO₂ emissions",
    "neurônios na rede competitiva, um para cada grupo de veículos": "neurons in the competitive network, one per vehicle group",
    "Prevendo o dólar": "Forecasting the dollar",
    "A LSTM acompanhou bem as subidas e descidas do dólar no teste.": "The LSTM closely followed the dollar's ups and downs on the test set.",
    "Ela olha os 10 últimos valores da série para prever o próximo. Usei uma camada LSTM com 64 neurônios, uma camada densa de 16 e treinei por 150 épocas com Adam. A normalização (MinMaxScaler) foi ajustada só com os dados de treino, para não vazar informação do teste.":
        "It looks at the last 10 values in the series to predict the next one. I used an LSTM layer with 64 units and a dense layer with 16, and trained for 150 epochs with Adam. The normalization (MinMaxScaler) was fit only on the training data, so no information leaked from the test set.",
    "R² da LSTM no treino e no teste": "LSTM R² on training and test",
    "R² da LSTM, de 0 a 1": "LSTM R², from 0 to 1",
    "Treino: 0,983": "Training: 0.983",
    "Treino": "Training",
    "Teste: 0,919": "Test: 0.919",
    "Teste": "Test",
    "Linha das previsões da LSTM sobreposta aos valores reais do dólar no conjunto de teste":
        "LSTM prediction line overlaid on the actual dollar values in the test set",
    "Previsões da LSTM (laranja) sobre os valores reais do dólar (azul) no conjunto de teste.":
        "LSTM predictions (orange) over the actual dollar values (blue) on the test set.",
    "Agrupando carros": "Clustering cars",
    "A rede competitiva separou os carros em grupos parecidos, sem ninguém dizer quais eram os grupos.":
        "The competitive network split the cars into similar groups without anyone telling it what the groups were.",
    "Cada um dos 5 neurônios vira o representante de um grupo de veículos. Depois ajustei uma curva polinomial em cada relação para ver a tendência e fazer previsões, como a emissão estimada de um carro com motor de 8,2 litros (cerca de 498 g/km).":
        "Each of the 5 neurons becomes the representative of a vehicle group. Then I fit a polynomial curve to each relationship to see the trend and make predictions, such as the estimated emissions of a car with an 8.2-liter engine (about 498 g/km).",
    "R² das curvas de tendência por relação": "R² of the trend curves by relationship",
    "R² da curva de tendência, de 0 a 1": "Trend curve R², from 0 to 1",
    "Cilindrada × eficiência: 0,63": "Engine size × efficiency: 0.63",
    "Cilindrada × eficiência": "Engine size × efficiency",
    "Cilindrada × CO₂: 0,65": "Engine size × CO₂: 0.65",
    "Cilindrada × CO₂": "Engine size × CO₂",
    "Eficiência × CO₂: 0,98": "Efficiency × CO₂: 0.98",
    "Eficiência × CO₂": "Efficiency × CO₂",
    "Gráfico de dispersão de veículos por cilindrada e emissão de CO₂, coloridos por grupo, com curva de tendência":
        "Scatter plot of vehicles by engine size and CO₂ emissions, colored by group, with a trend curve",
    "Veículos coloridos pelo grupo que a rede competitiva encontrou, com a curva de tendência entre cilindrada e CO₂.":
        "Vehicles colored by the group the competitive network found, with the trend curve between engine size and CO₂.",
    "O que os números mostram": "What the numbers show",
    "A cilindrada sozinha explica só parte da variação (R² perto de 0,64), enquanto eficiência e emissão andam quase juntas (R² de 0,98). Para melhorar, eu usaria mais variáveis, como tipo de combustível e peso do carro. Na LSTM, o R² caiu de 0,98 no treino para 0,92 no teste: ela generaliza bem, mas ainda erra nos picos mais bruscos.":
        "Engine size alone explains only part of the variation (R² around 0.64), while efficiency and emissions move almost together (R² of 0.98). To improve it, I would add more variables, such as fuel type and vehicle weight. For the LSTM, R² dropped from 0.98 in training to 0.92 on test: it generalizes well but still misses the sharpest spikes.",

    # ---------------- FolhaSã
    "FolhaSã: diagnóstico de doenças em folhas de tomate | Yuri Shiroiva": "FolhaSã: tomato leaf disease diagnosis | Yuri Shiroiva",
    "Classificador de 10 condições da folha do tomateiro com EfficientNet-B0. 99,9% de acurácia, F1-macro de 0,999, API em FastAPI e demo web.":
        "A classifier for 10 tomato leaf conditions with EfficientNet-B0. 99.9% accuracy, macro F1 of 0.999, a FastAPI API and a web demo.",
    "FolhaSã: diagnóstico de doenças em folhas de tomate": "FolhaSã: tomato leaf disease diagnosis",
    "Visão computacional · Práticas Extensionistas · PUCPR · 2026": "Computer vision · Extension Practice · PUCPR · 2026",
    "Um classificador que reconhece 10 condições da folha do tomateiro a partir de uma única foto. Acertou 99,9% das imagens de teste, que ele nunca tinha visto.":
        "A classifier that recognizes 10 tomato leaf conditions from a single photo. It got 99.9% of the test images right, images it had never seen.",
    "Autor (dados, modelo, API e interface)": "Author (data, model, API and interface)",
    "Práticas Extensionistas (prestação de serviço) na PUCPR": "Extension Practice (service project) at PUCPR",
    "Página de demonstração do FolhaSã aberta no navegador": "FolhaSã demo page open in the browser",
    "Quanto antes a doença aparece, menos a lavoura perde. A ideia era fazer o diagnóstico com uma foto.":
        "The earlier a disease is spotted, the less the crop loses. The idea was to diagnose it from a photo.",
    "Fiz como prestação de serviço, pensando no dia a dia de uma empresa de agtech. É um sistema completo de visão computacional, dos dados até a API, que reconhece nove doenças do tomateiro e a folha saudável.":
        "I built it as a service project, with the daily routine of an agtech company in mind. It is a complete computer vision system, from data to API, that recognizes nine tomato diseases and the healthy leaf.",
    "de acurácia no teste, em 2.180 imagens que não foram usadas no treino": "test accuracy, on 2,180 images not used in training",
    "erros em 2.180 folhas. Todo o resto foi classificado certo": "errors out of 2,180 leaves. Everything else was classified correctly",
    "de F1-macro: o modelo vai bem em todas as classes, inclusive nas raras": "macro F1: the model does well on every class, including the rare ones",
    "de treino numa GPU Tesla P100 na nuvem (30 épocas)": "of training on a cloud Tesla P100 GPU (30 epochs)",
    "Dados": "Data",
    "PlantVillage (tomate): 14.529 imagens divididas de forma estratificada em 10.169, 2.180 e 2.180 (treino, validação e teste). Imagens corrompidas ficaram de fora.":
        "PlantVillage (tomato): 14,529 images split in a stratified way into 10,169, 2,180 and 2,180 (training, validation and test). Corrupted images were left out.",
    "Transfer learning em duas fases": "Two-phase transfer learning",
    "Usei uma EfficientNet-B0 pré-treinada. Primeiro treinei só a cabeça, com o resto congelado, e depois liberei a rede inteira.":
        "I used a pretrained EfficientNet-B0. First I trained only the head with the rest frozen, then unfroze the whole network.",
    "Classes desbalanceadas": "Imbalanced classes",
    "Dei peso maior às classes raras na função de perda e escolhi o melhor modelo pelo F1-macro.":
        "I gave the rare classes a higher weight in the loss function and picked the best model by macro F1.",
    "Treino moderno": "Modern training",
    "Precisão mista (AMP), warmup com decaimento por cosseno, early stopping e checkpoints para retomar o treino.":
        "Mixed precision (AMP), warmup with cosine decay, early stopping and checkpoints to resume training.",
    "Modelo exportado para TorchScript e ONNX, API REST em FastAPI e uma página de demonstração em português.":
        "Model exported to TorchScript and ONNX, a REST API in FastAPI and a demo page in Portuguese.",
    "Página inicial do FolhaSã com o título Toda folha conta uma história":
        "FolhaSã home page with the headline “Toda folha conta uma história” (Every leaf tells a story)",
    "A página de demonstração que entreguei junto com o modelo.": "The demo page I delivered along with the model.",
    "O salto": "The jump",
    "Quando liberei a rede inteira, a acurácia de validação pulou de 0,63 para 0,97.":
        "When I unfroze the whole network, validation accuracy jumped from 0.63 to 0.97.",
    "Na primeira fase, só a cabeça aprende. Quando a rede toda passa a treinar, ela se ajusta às texturas das folhas e o resultado sobe de uma vez.":
        "In the first phase, only the head learns. Once the whole network trains, it adapts to the leaf textures and the result rises all at once.",
    "Curvas de perda e acurácia ao longo das épocas, com salto visível na segunda fase":
        "Loss and accuracy curves over the epochs, with a visible jump in the second phase",
    "Curva de treino, com as duas fases bem visíveis.": "Training curve, with both phases clearly visible.",
    "Todas as classes": "Every class",
    "As 10 classes passaram de 0,997 de F1, inclusive a mais rara.": "All 10 classes scored above 0.997 F1, including the rarest one.",
    "O vírus do mosaico tinha só 45 imagens no teste. Com o peso extra na função de perda, o modelo acertou todas (F1 = 1,0) em vez de ignorar essa classe.":
        "The mosaic virus had only 45 images in the test set. With the extra weight in the loss function, the model got all of them right (F1 = 1.0) instead of ignoring that class.",
    "Matriz de confusão com praticamente todos os valores na diagonal": "Confusion matrix with nearly all values on the diagonal",
    "Matriz de confusão no teste, com os 2 únicos erros fora da diagonal.": "Test confusion matrix, with the only 2 errors off the diagonal.",
    "Engenharia": "Engineering",
    "Configuração num lugar só": "Configuration in one place",
    "Um YAML tipado (OmegaConf com dataclasses) controla o experimento. Para trocar a EfficientNet por uma ResNet ou ConvNeXt, basta mudar uma linha.":
        "A typed YAML (OmegaConf with dataclasses) controls the experiment. To swap EfficientNet for a ResNet or ConvNeXt, you change a single line.",
    "Experimentos registrados": "Tracked experiments",
    "TensorBoard e MLflow ficam atrás da mesma interface, e cada execução salva métricas, curvas e relatórios.":
        "TensorBoard and MLflow sit behind the same interface, and every run saves metrics, curves and reports.",
    "Pronto para produção": "Production ready",
    "Exportei para TorchScript e ONNX conferindo se as saídas batem com o modelo original, e os checkpoints são carregados de forma segura.":
        "I exported to TorchScript and ONNX, checking that the outputs match the original model, and checkpoints are loaded safely.",
    "Sem GPU boa em casa": "No good GPU at home",
    "Minha GPU de 4 GB não dava conta, então levei o treino para uma Tesla P100 gratuita na nuvem e automatizei o ajuste da versão do PyTorch.":
        "My 4 GB GPU couldn't handle it, so I moved training to a free Tesla P100 in the cloud and automated the PyTorch version setup.",

    # ---------------- falhas
    "Detecção de falhas em peças metálicas | Yuri Shiroiva": "Defect detection in metal parts | Yuri Shiroiva",
    "Pipeline de visão computacional com OpenCV (CLAHE, Canny, morfologia e segmentação por forma) que detecta uma fissura em chapa metálica.":
        "A computer vision pipeline with OpenCV (CLAHE, Canny, morphology and shape-based segmentation) that detects a crack in a metal sheet.",
    "Detecção de falhas em peças metálicas": "Defect detection in metal parts",
    "Processamento de imagens · IA na Indústria 4.0 · PUCPR · 2026": "Image processing · AI in Industry 4.0 · PUCPR · 2026",
    "Um pipeline de visão computacional clássica, sem rede neural, que encontra e destaca uma rachadura numa chapa de metal.":
        "A classical computer vision pipeline, with no neural network, that finds and highlights a crack in a metal sheet.",
    "Disciplina IA na Indústria 4.0, na PUCPR": "AI in Industry 4.0 course at PUCPR",
    "Peça original, bordas detectadas pelo Canny e a fissura destacada em vermelho":
        "Original part, edges detected by Canny and the crack highlighted in red",
    "A ideia": "The idea",
    "Nem sempre precisa de deep learning. Neste caso, técnicas clássicas aplicadas uma depois da outra deram conta.":
        "You don't always need deep learning. Here, classical techniques applied one after another did the job.",
    "Cada técnica trabalha em cima do resultado da anterior, e salvei todas as imagens intermediárias para o relatório técnico.":
        "Each technique works on the output of the previous one, and I saved every intermediate image for the technical report.",
    "A peça é uma chapa sintética que o próprio script gera, sempre igual (semente fixa). Ela tem rebites e manchas de corrosão que o pipeline não pode confundir com a falha.":
        "The part is a synthetic sheet generated by the script itself, always the same (fixed seed). It has rivets and corrosion spots that the pipeline must not mistake for the defect.",
    "O pipeline": "The pipeline",
    "Escala de cinza": "Grayscale",
    "A cor não ajuda a achar a fissura, e com um canal só as próximas etapas ficam mais simples.":
        "Color doesn't help find the crack, and a single channel keeps the next steps simpler.",
    "Suavização gaussiana": "Gaussian blur",
    "Kernel 7×7 remove o ruído da superfície antes de procurar bordas.": "A 7×7 kernel removes surface noise before looking for edges.",
    "Realce com CLAHE": "CLAHE enhancement",
    "Equalização adaptativa (clip 2,0, grade 8×8) compensa a iluminação desigual da chapa.":
        "Adaptive equalization (clip 2.0, 8×8 grid) compensates for the uneven lighting on the sheet.",
    "Bordas com Canny": "Canny edges",
    "Limiares 50/150 destacam as transições fortes, que são a fissura e os rebites.":
        "Thresholds of 50/150 highlight the strong transitions, which are the crack and the rivets.",
    "Fechamento morfológico": "Morphological closing",
    "Elipse 5×5 em 2 iterações reconecta os trechos quebrados da fissura.": "A 5×5 ellipse over 2 iterations reconnects the broken parts of the crack.",
    "Segmentação por forma": "Shape-based segmentation",
    "Mantém só componentes longos (diagonal &gt; 60 px) e alongados (razão &gt; 2), descartando os rebites redondos.":
        "Keeps only long (diagonal &gt; 60 px) and elongated (ratio &gt; 2) components, discarding the round rivets.",
    "Resultado": "Result",
    "A fissura é pintada de vermelho e marcada com uma caixa “FALHA DETECTADA”.": "The crack is painted red and marked with a “DEFECT DETECTED” box.",
    "Painel com as oito etapas do pipeline, da imagem original ao resultado": "Panel with the eight pipeline steps, from the original image to the result",
    "As etapas lado a lado, da imagem original à falha detectada.": "The steps side by side, from the original image to the detected defect.",
    "Os limiares foram ajustados para esta cena. Em fotos reais, com iluminação e texturas variadas, o próximo passo seria calibrá-los num conjunto de imagens ou trocar a segmentação por um modelo treinado.":
        "The thresholds were tuned for this scene. On real photos, with varied lighting and textures, the next step would be to calibrate them on a set of images or replace the segmentation with a trained model.",
}
