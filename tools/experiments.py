from pandas import Timestamp as Ts


class Experiments:
    def __init__(self):
        self.scenarios = []
        self.init_scenarios()

    def init_scenarios(self):
        temp = Experiments.options_data()
        for x in temp:
            trajectory_generator_options = Experiments.set_tr_gen_options(**x)
            data_generation_options = Experiments.set_data_generation_options()
            define_csvs_options = Experiments.set_df_csv_options()
            genetic_options = Experiments.set_gen_options()
            scenario = {"trajectory_generator_options": trajectory_generator_options,
                        "data_generation_options": data_generation_options,
                        "define_csvs_option": define_csvs_options,
                        "genetic_options": genetic_options}
            self.scenarios.append(scenario)

    def get_scenarios(self):
        return self.scenarios

    def add_scenario(self, scenario):

        self.scenarios.append(scenario)

    def remove_scenario(self, scenario):
        self.scenarios.remove(scenario)

    @staticmethod
    def set_tr_gen_options(first_lat=37.295493,
                           first_lon=23.824322,
                           init_bearing=90,
                           init_speed=5,
                           samples=20,
                           timestamp=Ts(2015, 2, 1, 12),
                           freq=3,
                           reset_data=False):

        tr_gen_options = {"first_lat": first_lat,
                          "first_lon": first_lon,
                          "init_bearing": init_bearing,
                          "init_speed": init_speed,
                          "samples": samples,
                          "timestamp": timestamp,
                          "freq": freq,
                          "reset_data": reset_data}
        return tr_gen_options

    @staticmethod
    def set_data_generation_options(filename="testing_",
                                    n_test=10):
        dt_gen_options = {"filename": filename,
                          "n_test": n_test}
        return dt_gen_options

    @staticmethod
    def set_df_csv_options(ts_class=["Bearing","Speed"],
                           file=["train.csv", "test.csv"]):
        df_csv_options = {"ts_class": ts_class,
                          "file": file}
        return df_csv_options

    @staticmethod
    def set_gen_options(population_size=25,
                        iterations=5,
                        verbose=True,
                        normed=True,
                        add_noise_prob=0.3,
                        add_shapelet_prob=0.3,
                        wait=10,
                        plot=None,
                        remove_shapelet_prob=0.3,
                        crossover_prob=0.66,
                        n_jobs=4):
        gen_options = {"population_size": population_size,
                       "iterations": iterations,
                       "verbose": verbose,
                       "normed": normed,
                       "add_noise_prob": add_noise_prob,
                       "add_shapelet_prob": add_shapelet_prob,
                       "wait": wait,
                       "plot": plot,
                       "remove_shapelet_prob": remove_shapelet_prob,
                       "crossover_prob": crossover_prob,
                       "n_jobs": n_jobs}
        return gen_options

    @staticmethod
    def fix_df_csvs_options(df_csvs_options):
        ts_class = df_csvs_options["ts_class"]
        file = df_csvs_options["file"]
        train_options = {"ts_class": ts_class, "file": file[0]}
        test_options = {"ts_class": ts_class, "file": file[1]}
        return train_options, test_options

    @staticmethod
    def options_data():
        tr_gen_options = [{"samples": 50, "freq": 3, "reset_data": True},
                          {"samples": 100, "freq": 3, "reset_data": True},
                          {"samples": 200, "freq": 3, "reset_data": True},
                          {"samples": 500, "freq": 3, "reset_data": True},
                          {"samples": 1000, "freq": 3, "reset_data": True}]
        return tr_gen_options