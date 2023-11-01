import matplotlib.pyplot as plt
import json
import ipdb

def main():
    completed_steps = []
    r1_list = []
    r2_list = []
    rl_list = []

    with open('HW2/training_curve.json', 'r') as json_file:
        curve_data = json.load(json_file)
        curve_data = curve_data["curve"]
        for data in curve_data:
            completed_steps.append(data["completed_steps"])
            r1_list.append(data["metric"]["rouge1"])
            r2_list.append(data["metric"]["rouge2"])
            rl_list.append(data["metric"]["rougeL"])

    plt.subplot(111)
    plt.plot(completed_steps, r1_list,label='Rouge1')
    plt.plot(completed_steps, r2_list,label='Rouge2')
    plt.plot(completed_steps, rl_list,label='RougeL')
    plt.xlabel("Completed Steps")
    plt.ylabel("Rouge")
    plt.title("Rouge Curve")
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()