from libs.conversion_to_wav import conver_mp3_to_wav 
from libs.split_in_10_sec_intervel import split_10sec
import yaml

if __name__ == "__main__":
    config = yaml.load(open('config/config.yaml' , 'r'), Loader=yaml.FullLoader)
    conver_mp3_to_wav(SRC_IMG_PATH=config['SRC_IMG'] , DST_IMG_PATH=config['DST_IMG'])
    split_10sec(input_dir=config['INPUT_DIR'] , output_dir=config['OUTPUT_DIR'])
