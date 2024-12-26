import os

base_path = "./train_data"
output_path = "./my_output_results"
mipnerf_path = os.path.join(base_path, "mipnerf")
tandt_path = os.path.join(base_path, "tandt")
db_path = os.path.join(base_path, "db")


command = f"python full_eval.py --mipnerf360 {mipnerf_path} 
 --tanksandtemples {tandt_path} --deepblending {db_path} --output_path {output_path}"
# command = f"python full_eval.py --skip_training 1 --skip_rendering 1 --mipnerf360 {mipnerf_path} 
#  --tanksandtemples {tandt_path} --deepblending {db_path} --output_path {output_path}"
#仅评估
os.system(command)