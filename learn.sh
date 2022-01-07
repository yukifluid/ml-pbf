# # VectorMSE Loss
# mkdir ./model/vector-mse
# python main.py vector-mse > ./model/vector-mse/log.txt
# cp -r ./model/vector-mse /g/マイドライブ/lab/ml-pbf-result-20201226
# python simulate.py vector-mse PBFSimple/raw/test/0/config.json PBFSimple/raw/test/0/vector-mse-data.csv PBFSimple/raw/test/0/vector-mse-measure.csv
# python simulate.py vector-mse PBFSimple/raw/test/1/config.json PBFSimple/raw/test/1/vector-mse-data.csv PBFSimple/raw/test/1/vector-mse-measure.csv
# python simulate.py vector-mse PBFSimple/raw/test/2/config.json PBFSimple/raw/test/2/vector-mse-data.csv PBFSimple/raw/test/2/vector-mse-measure.csv
# python simulate.py vector-mse PBFSimple/raw/test/3/config.json PBFSimple/raw/test/3/vector-mse-data.csv PBFSimple/raw/test/3/vector-mse-measure.csv
# python simulate.py vector-mse PBFSimple/raw/test/4/config.json PBFSimple/raw/test/4/vector-mse-data.csv PBFSimple/raw/test/4/vector-mse-measure.csv
# 
# # Composition Loss
# mkdir ./model/composition-0.33_0.33_0.33
# python main.py composition-0.33_0.33_0.33 0.33 0.33 0.33 > ./model/composition-0.33_0.33_0.33/log.txt
# cp -r ./model/composition-0.33_0.33_0.33 /g/マイドライブ/lab/ml-pbf-result-20201226
# python simulate.py composition-0.33_0.33_0.33 PBFSimple/raw/test/0/config.json PBFSimple/raw/test/0/composition-0.33_0.33_0.33-data.csv PBFSimple/raw/test/0/composition-0.33_0.33_0.33-measure.csv
# python simulate.py composition-0.33_0.33_0.33 PBFSimple/raw/test/1/config.json PBFSimple/raw/test/1/composition-0.33_0.33_0.33-data.csv PBFSimple/raw/test/1/composition-0.33_0.33_0.33-measure.csv
# python simulate.py composition-0.33_0.33_0.33 PBFSimple/raw/test/2/config.json PBFSimple/raw/test/2/composition-0.33_0.33_0.33-data.csv PBFSimple/raw/test/2/composition-0.33_0.33_0.33-measure.csv
# python simulate.py composition-0.33_0.33_0.33 PBFSimple/raw/test/3/config.json PBFSimple/raw/test/3/composition-0.33_0.33_0.33-data.csv PBFSimple/raw/test/3/composition-0.33_0.33_0.33-measure.csv
# python simulate.py composition-0.33_0.33_0.33 PBFSimple/raw/test/4/config.json PBFSimple/raw/test/4/composition-0.33_0.33_0.33-data.csv PBFSimple/raw/test/4/composition-0.33_0.33_0.33-measure.csv
# 
# mkdir ./model/composition-0.5_0.5_0.0
# python main.py composition-0.5_0.5_0.0 0.5 0.5 0.0 > ./model/composition-0.5_0.5_0.0/log.txt
# cp -r ./model/composition-0.5_0.5_0.0 /g/マイドライブ/lab/ml-pbf-result-20201226
# python simulate.py composition-0.5_0.5_0.0 PBFSimple/raw/test/0/config.json PBFSimple/raw/test/0/composition-0.5_0.5_0.0-data.csv PBFSimple/raw/test/0/composition-0.5_0.5_0.0-measure.csv
# python simulate.py composition-0.5_0.5_0.0 PBFSimple/raw/test/1/config.json PBFSimple/raw/test/1/composition-0.5_0.5_0.0-data.csv PBFSimple/raw/test/1/composition-0.5_0.5_0.0-measure.csv
# python simulate.py composition-0.5_0.5_0.0 PBFSimple/raw/test/2/config.json PBFSimple/raw/test/2/composition-0.5_0.5_0.0-data.csv PBFSimple/raw/test/2/composition-0.5_0.5_0.0-measure.csv
# python simulate.py composition-0.5_0.5_0.0 PBFSimple/raw/test/3/config.json PBFSimple/raw/test/3/composition-0.5_0.5_0.0-data.csv PBFSimple/raw/test/3/composition-0.5_0.5_0.0-measure.csv
# python simulate.py composition-0.5_0.5_0.0 PBFSimple/raw/test/4/config.json PBFSimple/raw/test/4/composition-0.5_0.5_0.0-data.csv PBFSimple/raw/test/4/composition-0.5_0.5_0.0-measure.csv
# 
# mkdir ./model/composition-0.5_0.25_0.25
# python main.py composition-0.5_0.25_0.25 0.5 0.25 0.25 > ./model/composition-0.5_0.25_0.25/log.txt
# cp -r ./model/composition-0.5_0.25_0.25 /g/マイドライブ/lab/ml-pbf-result-20201226
# python simulate.py composition-0.5_0.25_0.25 PBFSimple/raw/test/0/config.json PBFSimple/raw/test/0/composition-0.5_0.25_0.25-data.csv PBFSimple/raw/test/0/composition-0.5_0.25_0.25-measure.csv
# python simulate.py composition-0.5_0.25_0.25 PBFSimple/raw/test/1/config.json PBFSimple/raw/test/1/composition-0.5_0.25_0.25-data.csv PBFSimple/raw/test/1/composition-0.5_0.25_0.25-measure.csv
# python simulate.py composition-0.5_0.25_0.25 PBFSimple/raw/test/2/config.json PBFSimple/raw/test/2/composition-0.5_0.25_0.25-data.csv PBFSimple/raw/test/2/composition-0.5_0.25_0.25-measure.csv
# python simulate.py composition-0.5_0.25_0.25 PBFSimple/raw/test/3/config.json PBFSimple/raw/test/3/composition-0.5_0.25_0.25-data.csv PBFSimple/raw/test/3/composition-0.5_0.25_0.25-measure.csv
# python simulate.py composition-0.5_0.25_0.25 PBFSimple/raw/test/4/config.json PBFSimple/raw/test/4/composition-0.5_0.25_0.25-data.csv PBFSimple/raw/test/4/composition-0.5_0.25_0.25-measure.csv
# 
# mkdir ./model/composition-0.5_0.0_0.5
# python main.py composition-0.5_0.0_0.5 0.5 0.0 0.5 > ./model/composition-0.5_0.0_0.5/log.txt
# cp -r ./model/composition-0.5_0.0_0.5 /g/マイドライブ/lab/ml-pbf-result-20201226
# python simulate.py composition-0.5_0.0_0.5 PBFSimple/raw/test/0/config.json PBFSimple/raw/test/0/composition-0.5_0.0_0.5-data.csv PBFSimple/raw/test/0/composition-0.5_0.0_0.5-measure.csv
# python simulate.py composition-0.5_0.0_0.5 PBFSimple/raw/test/1/config.json PBFSimple/raw/test/1/composition-0.5_0.0_0.5-data.csv PBFSimple/raw/test/1/composition-0.5_0.0_0.5-measure.csv
# python simulate.py composition-0.5_0.0_0.5 PBFSimple/raw/test/2/config.json PBFSimple/raw/test/2/composition-0.5_0.0_0.5-data.csv PBFSimple/raw/test/2/composition-0.5_0.0_0.5-measure.csv
# python simulate.py composition-0.5_0.0_0.5 PBFSimple/raw/test/3/config.json PBFSimple/raw/test/3/composition-0.5_0.0_0.5-data.csv PBFSimple/raw/test/3/composition-0.5_0.0_0.5-measure.csv
# python simulate.py composition-0.5_0.0_0.5 PBFSimple/raw/test/4/config.json PBFSimple/raw/test/4/composition-0.5_0.0_0.5-data.csv PBFSimple/raw/test/4/composition-0.5_0.0_0.5-measure.csv
# 
# mkdir ./model/composition-0.0_1.0_0.0
# python main.py composition-0.0_1.0_0.0 0.0 1.0 0.0 > ./model/composition-0.0_1.0_0.0/log.txt
# cp -r ./model/composition-0.0_1.0_0.0 /g/マイドライブ/lab/ml-pbf-result-20201226
# python simulate.py composition-0.0_1.0_0.0 PBFSimple/raw/test/0/config.json PBFSimple/raw/test/0/composition-0.0_1.0_0.0-data.csv PBFSimple/raw/test/0/composition-0.0_1.0_0.0-measure.csv
# python simulate.py composition-0.0_1.0_0.0 PBFSimple/raw/test/1/config.json PBFSimple/raw/test/1/composition-0.0_1.0_0.0-data.csv PBFSimple/raw/test/1/composition-0.0_1.0_0.0-measure.csv
# python simulate.py composition-0.0_1.0_0.0 PBFSimple/raw/test/2/config.json PBFSimple/raw/test/2/composition-0.0_1.0_0.0-data.csv PBFSimple/raw/test/2/composition-0.0_1.0_0.0-measure.csv
# python simulate.py composition-0.0_1.0_0.0 PBFSimple/raw/test/3/config.json PBFSimple/raw/test/3/composition-0.0_1.0_0.0-data.csv PBFSimple/raw/test/3/composition-0.0_1.0_0.0-measure.csv
# python simulate.py composition-0.0_1.0_0.0 PBFSimple/raw/test/4/config.json PBFSimple/raw/test/4/composition-0.0_1.0_0.0-data.csv PBFSimple/raw/test/4/composition-0.0_1.0_0.0-measure.csv
# 
# mkdir ./model/composition-0.0_0.0_1.0
# python main.py composition-0.0_0.0_1.0 0.0 0.0 1.0 > ./model/composition-0.0_0.0_1.0/log.txt
# cp -r ./model/composition-0.0_0.0_1.0 /g/マイドライブ/lab/ml-pbf-result-20201226
# python simulate.py composition-0.0_0.0_1.0 PBFSimple/raw/test/0/config.json PBFSimple/raw/test/0/composition-0.0_0.0_1.0-data.csv PBFSimple/raw/test/0/composition-0.0_0.0_1.0-measure.csv
# python simulate.py composition-0.0_0.0_1.0 PBFSimple/raw/test/1/config.json PBFSimple/raw/test/1/composition-0.0_0.0_1.0-data.csv PBFSimple/raw/test/1/composition-0.0_0.0_1.0-measure.csv
# python simulate.py composition-0.0_0.0_1.0 PBFSimple/raw/test/2/config.json PBFSimple/raw/test/2/composition-0.0_0.0_1.0-data.csv PBFSimple/raw/test/2/composition-0.0_0.0_1.0-measure.csv
# python simulate.py composition-0.0_0.0_1.0 PBFSimple/raw/test/3/config.json PBFSimple/raw/test/3/composition-0.0_0.0_1.0-data.csv PBFSimple/raw/test/3/composition-0.0_0.0_1.0-measure.csv
# python simulate.py composition-0.0_0.0_1.0 PBFSimple/raw/test/4/config.json PBFSimple/raw/test/4/composition-0.0_0.0_1.0-data.csv PBFSimple/raw/test/4/composition-0.0_0.0_1.0-measure.csv
# 
# cp -r ./PBFSimple/raw /g/マイドライブ/lab/ml-pbf-result-20201226


mkdir ./model/no-starndardization-0108
python3 main.py no-starndardization-0108 > ./model/no-starndardization-0108/log.txt
# cp -r ./model/no-starndardization-0108 /g/マイドライブ/lab/ml-pbf-result-20201226
python3 simulate.py no-starndardization-0108 PBFSimple/raw/test/0/config.json PBFSimple/raw/test/0/tanh-data.csv PBFSimple/raw/test/0/tanh-measure.csv
python3 simulate.py no-starndardization-0108 PBFSimple/raw/test/1/config.json PBFSimple/raw/test/1/tanh-data.csv PBFSimple/raw/test/1/tanh-measure.csv
python3 simulate.py no-starndardization-0108 PBFSimple/raw/test/2/config.json PBFSimple/raw/test/2/tanh-data.csv PBFSimple/raw/test/2/tanh-measure.csv
python3 simulate.py no-starndardization-0108 PBFSimple/raw/test/3/config.json PBFSimple/raw/test/3/tanh-data.csv PBFSimple/raw/test/3/tanh-measure.csv
python3 simulate.py no-starndardization-0108 PBFSimple/raw/test/4/config.json PBFSimple/raw/test/4/tanh-data.csv PBFSimple/raw/test/4/tanh-measure.csv