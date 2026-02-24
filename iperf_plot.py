import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_throughput(distance):
    tcp_file = f"iperf_tcp_{distance}m.csv"
    udp_file = f"iperf_udp_{distance}m.csv"

    # Check if files exist before plotting
    if not os.path.exists(tcp_file) or not os.path.exists(udp_file):
        print(f"Data files for {distance}m not found. Skipping.")
        return

    # Read the CSVs. We only want the last row (most recent run) as instructed.
    tcp_df = pd.read_csv(tcp_file)
    udp_df = pd.read_csv(udp_file)
    
    tcp_latest = tcp_df.iloc[-1]
    udp_latest = udp_df.iloc[-1]

    # Extract Run 1 to 5 data
    runs = ['Run1', 'Run2', 'Run3', 'Run4', 'Run5']
    tcp_throughput = [tcp_latest[run] for run in runs]
    udp_throughput = [udp_latest[run] for run in runs]

    # Plotting
    plt.figure(figsize=(8, 5))
    plt.plot(runs, tcp_throughput, marker='o', linestyle='-', color='orange', label='TCP Throughput (Mbps)')
    plt.plot(runs, udp_throughput, marker='s', linestyle='--', color='coral', label='UDP Throughput (Mbps)')

    plt.title(f'TCP & UDP Throughput at {distance}m Distance')
    plt.xlabel('Test Runs')
    plt.ylabel('Throughput (Mbps)')
    plt.ylim(bottom=0) # Start Y-axis at 0 for accurate visual scale
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)
    
    # Save the plot
    output_filename = f"throughput_plot_{distance}m.png"
    plt.savefig(output_filename)
    print(f"Saved {output_filename}")
    plt.close()

if __name__ == "__main__":
    distances = [2, 4, 8, 10, 15] 
    
    for d in distances:
        plot_throughput(d)
