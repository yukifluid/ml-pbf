# VectorMSE Loss
mkdir ./model/vector-mse
python main.py vector-mse > ./model/vector-mse/log.txt

# Composition Loss
mkdir ./model/composition-0.0_1.0_0.0
python main.py composition-0.0_1.0_0.0 0.0 1.0 0.0 > ./model/composition-0.0_1.0_0.0/log.txt

mkdir ./model/composition-0.0_0.0_1.0
python main.py composition-0.0_0.0_1.0 0.0 0.0 1.0 > ./model/composition-0.0_0.0_1.0/log.txt

mkdir ./model/composition-0.5_0.0_0.5
python main.py composition-0.5_0.0_0.5 0.5 0.0 0.5 > ./model/composition-0.5_0.0_0.5/log.txt

mkdir ./model/composition-0.5_0.5_0.0
python main.py composition-0.5_0.5_0.0 0.5 0.5 0.0 > ./model/composition-0.5_0.5_0.0/log.txt

mkdir ./model/composition-0.33_0.33_0.33
python main.py composition-0.33_0.33_0.33 0.33 0.33 0.33 > ./model/composition-0.33_0.33_0.33/log.txt

mkdir ./model/composition-0.5_0.25_0.25
python main.py composition-0.5_0.25_0.25 0.5 0.25 0.25 > ./model/composition-0.5_0.25_0.25/log.txt