import os

grid_search = {
    "supervised_ratio": [0.25, 0.125, 0.05, 0.02, 0.01],
    "conf_thresh": [0.8, 0.85, 0.9, 0.95],
    "fold": [1, 2, 3, 4, 5],
    "seed": [1, 2, 3],
}

grid_search = {
    "supervised_ratio": [0.25],
    "conf_thresh": [0.8],
    "fold": [1],
    "seed": [1],
}

run_template = """
python -u {}.py --cuda 0 --seed {} \
--exp {} --dataset {} --sup_ratio {} \
--conf_thres {} --fold {} --debug 1
"""
for exp in ["cps"]:
    for dataset in ["bccd"]:
        for supervised_ratio in grid_search["supervised_ratio"]:
            for conf_thresh in grid_search["conf_thresh"]:
                for fold in grid_search["fold"]:
                    for seed in grid_search["seed"]:
                        # check if the experiment has been run
                        exp_name = f"{exp}_{dataset}_supervised_ratio_{supervised_ratio}_conf_thresh_{conf_thresh}_fold_{fold}_seed_{seed}"
                        current_dir = os.getcwd()
                        exp_folder = f"{current_dir}/checkpoints/{dataset}/{exp_name}_{supervised_ratio}"
                        if os.path.exists(exp_folder):
                            print(f"This {exp_name} exists! Skip")
                            continue

                        run = run_template.format(
                            exp,
                            seed,
                            exp_name,
                            dataset,
                            supervised_ratio,
                            conf_thresh,
                            fold,
                        )
                        print(run)
                        try:
                            os.system(run)
                        except Exception as e:
                            print(e)
                            continue
