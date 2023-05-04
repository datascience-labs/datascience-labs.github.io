# DEBS 2022 Grand Challenge 
This github page contributes to DEBS 2022 Grand Challenge. 

## description
We participate in the DEBS GC 2022 as team Group-4.

The 2022 DEBS Grand Challenge focuses on real-time complex event processing of high-volume financial data. The goal of this challenge is to efficiently compute to EMA(Exponential Moving Average) as a trend technical indicator and to detect cross patterns that helps decisions on buying or selling on financial markets.

To meet their requirements, our solution finds the query1 answers that calculate both EMA38 and EMA100 per symbol. Besides, our solution handles the query2 answer that finds the intersactions of both EMA38 and EMA100 per symbol. 

We share the video where we explain our source code to Youtube link: https://www.youtube.com/watch?v=8dOlg4LXdGI

For more information, you can see the following link: https://2022.debs.org/call-for-grand-challenge-solutions/

## installation
We provide two kinds of execution environment for DEBS 22 GC testing

First one is online Jupyter Notebook.
1. go to **google colab**
2. move to MENU [File] -> [Open Notebook] -> Upload files 'DEBS_2022_GC_GROUP_4.ipynb'

Second one is your own local development environment through Docker. 
1. downloads the compressed zip file from github and extract it in the folder you desire.
2. Open the terminal, move to the folder, and type the following command  ( if docker is already installed, )
```
  # buid the docker image and deploy our pyspark environment/its dependencies rapidly to your system
  docker build -t pyspark:latest ./
```
3. set up your token key
4. run the debs_2022_gc.py with docker container as the following command:
```
 docker run -it pyspark:latest debs_2022_gc
```




## requirements
[Docker](https://www.docker.com) 


## Team
- Suyeon Wang: wangsunny6143 at gmail.com   (contact person)
- JaeKyeong Kim: 2143575 at donga.ac.kr
- Yoonsang Yang: yoonsang.developer at gmail.com
- Jinseong Hwang: jinseong.dev at gmail.com
- Jungkyu Han: jkhan at dau.ac.kr
- Sejin Chun: sjchun at dau.ac.kr

## Citing
If you find Stock-Influx useful in your work, and you want to cite our work, please use the following referencee:
```
@inproceedings{wang2022real,
  title={Real-time stock market analytics for improving deployment and accessibility using PySpark and Docker},
  author={Wang, Suyeon and Kim, Jaekyeong and Yang, Yoonsang and Hwang, Jinseong and Han, Jungkyu and Chun, Sejin},
  booktitle={Proceedings of the 16th ACM International Conference on Distributed and Event-Based Systems},
  pages={171--175},
  year={2022}
}
```

## license
```
Sebastian Frischbier, Jawad Tahir, Christoph Doblander, Arne Hormann, Ruben Mayer. 
The DEBS 2021 grand challenge: Detecting Trading Trends in Real Financial Tick Data. 
Proceedings of the 16th ACM International Conference on Distributed and Event-based Systems (DEBS'22) 
```
