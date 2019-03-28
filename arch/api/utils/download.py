import argparse
import json
import os
from arch.api import eggroll


def do_export_file(job_id, _data):
    try:
        work_mode = _data.get("work_mode")
        name = _data.get("name")
        namespace = _data.get("namespace")
        delimitor = _data.get("delimitor", ",")
        output_path = _data.get("output_path")
        scene_id = _data.get("scene_id")
        role = _data.get("role")
        my_party_id = _data.get("my_party_id") 
        partner_party_id = _data.get("partner_party_id")
        
        eggroll.init(job_id, work_mode)

        with open(os.path.abspath(output_path), "w") as fout:
            if scene_id and role and my_party_id and partner_parity_id:
                data_table = feture.get_feature_data_table(name)
            else:
                data_table = eggroll.table(name, namespace)
               
            print('===== begin to export data =====')
            lines = 0

            for key, value in data_table.collect():
                if not value:
                    fout.write(key + "\n")
                else:
                    fout.write(key + delimitor + value + "\n")
                
                lines += 1
                if lines % 2000 == 0:
                    print("===== export {} lines =====".format(lines))

            print("===== export {} lines totally =====".format(lines))
            print('===== export data finish =====')
    except:
        raise ValueError("cannot export data, please check json file")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-j', '--job_id', required=True, type=str, help="job id to use")
    parser.add_argument('-c', '--config', required=True, type=str, help="you should provide a path of configure file with json format")
    args = parser.parse_args()

    try:
        with open(args.config, 'r') as f:
            data = json.load(f)

        do_export_file(args.job_id, data)
    except:
        raise ValueError("export file failed")
