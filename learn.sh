# VectorMSE Loss
mkdir ./model/vector-mse
python3 main.py vector-mse > ./model/vector-mse/log.txt

# Composition Loss
mkdier ./model/composition-0.0_1.0_0.0
python3 main.py composition-0.0_1.0_0.0 0.0 1.0 0.0 > ./model/composition-0.0_1.0_0.0/log.txt

mkdier ./model/composition-0.0_0.0_1.0
python3 main.py composition-0.0_0.0_1.0 0.0 0.0 1.0 > ./model/composition-0.0_0.0_1.0/log.txt

mkdier ./model/composition-0.5_0.0_0.5
python3 main.py composition-0.5_0.0_0.5 0.5 0.0 0.5 > ./model/composition-0.5_0.0_0.5/log.txt

mkdier ./model/composition-0.5_0.5_0.0
python3 main.py composition-0.5_0.5_0.0 0.5 0.5 0.0 > ./model/composition-0.5_0.5_0.0/log.txt

mkdier ./model/composition-0.33_0.33_0.33
python3 main.py composition-0.33_0.33_0.33 0.33 0.33 0.33 > ./model/composition-0.33_0.33_0.33/log.txt

mkdier ./model/composition-0.5_0.25_0.25
python3 main.py composition-0.5_0.25_0.25 0.5 0.25 0.25 > ./model/composition-0.5_0.25_0.25/log.txt