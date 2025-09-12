import os
import numpy as np
import matplotlib.pyplot as plt
from pynwb import NWBHDF5IO

#Note: For this plotting, be sure to only use the pre-stim values for SO1 (otherwise it will double count!)

# Directory containing your NWB files
nwb_dir = '' #TODO: POINT AT YOUR DIRECTORY OF NWB FILES

# Initialize lists to collect metrics
unit_counts = [] #per file
file_experiment = []
file_electrodes = []
#per unit
total_experiment = []
total_electrodes = []
total_snrs = []
total_firing_rates = []
total_amplitudes = []

def get_experiment_info(filename):
    experiment={'SO1':0,'BO2':1,'BO14':2}
    n_electrodes={'SO1':3,'BO2':3,'BO14':16}
    basename = os.path.basename(filename)  # remove any path
    for prefix in experiment:
        if prefix in basename:
            return {
                'prefix': prefix,
                'experiment_number': experiment[prefix],
                'electrode_count': n_electrodes[prefix]
            }
    return None  # No matching prefix

# Loop through NWB files
for file in os.listdir(nwb_dir):
    if file.endswith(".nwb"):
        filepath = os.path.join(nwb_dir, file)
        print(f"Processing: {filepath}")

        try:
            with NWBHDF5IO(filepath, 'r', load_namespaces=True) as io:
                nwbfile = io.read()

                # Check for the processing module and table
                proc_name = 'sorted_spike_metrics'
                if proc_name in nwbfile.processing:
                    mod = nwbfile.processing[proc_name]

                    if 'spike_sorted_unit_metrics' in mod.data_interfaces:
                        table = mod['spike_sorted_unit_metrics']
                        n_units = len(table)

                        if n_units > 0:
                            exp_data = get_experiment_info(filepath)
                            unit_counts.append(n_units)
                            file_experiment.append(exp_data['experiment_number'])
                            file_electrodes.append(exp_data['electrode_count'])

                            # Extract column data
                            snrs = np.array(table['snr'].data)
                            firing_rates = np.array(table['firing_rate'].data)
                            amplitudes = np.array(table['amplitude'].data)

                            total_snrs.extend(snrs.tolist())
                            total_firing_rates.extend(firing_rates.tolist())
                            total_amplitudes.extend(amplitudes.tolist())
                            total_experiment.extend((exp_data['experiment_number']*np.ones(firing_rates.shape)).tolist())
                            total_electrodes.extend((exp_data['electrode_count']*np.ones(firing_rates.shape)).tolist())

                        else:
                            unit_counts.append(0)
                            file_experiment.append(exp_data['experiment_number'])
                            file_electrodes.append(exp_data['electrode_count'])

                    else: #no units
                        unit_counts.append(0)
                        file_experiment.append(exp_data['experiment_number'])
                        file_electrodes.append(exp_data['electrode_count'])
                else: #no units
                        unit_counts.append(0)
                        file_experiment.append(exp_data['experiment_number'])
                        file_electrodes.append(exp_data['electrode_count'])

        except Exception as e:
            print(f"Error processing {file}: {e}")

print(total_firing_rates)
# --------------------------
# Plot Histograms
# --------------------------
plt.figure(figsize=(14, 10))

plt.subplot(2, 2, 1)
plt.hist(unit_counts, bins=10, edgecolor='black')
plt.title('Number of Units per Recording Session')
plt.xlabel('Unit Count')
plt.ylabel('Count')

plt.subplot(2, 2, 2)
plt.hist(total_firing_rates, bins=10, edgecolor='black')
plt.title('Average Firing Rate (Hz) per Unit')
plt.xlabel('Firing Rate (Hz)')
plt.ylabel('Count')

plt.subplot(2, 2, 3)
plt.hist(total_snrs, bins=10, edgecolor='black')
plt.title('Average Signal to Noise Ratio (SNR) per Unit')
plt.xlabel('SNR')
plt.ylabel('Count')

plt.subplot(2, 2, 4)
plt.hist(total_amplitudes, bins=10, edgecolor='black')
plt.title('Average Spike Amplitude ($\\mu$V) per Unit')
plt.xlabel('Amplitude ($\\mu$V)')
plt.ylabel('Count')

plt.tight_layout()

plt.savefig('spike_summary.png',format='png')
plt.savefig('spike_summary.svg',format='svg')
plt.show()

unit_array = np.array(unit_counts)
snr_array = np.array(total_snrs)
amplitude_array = np.array(total_amplitudes)
firing_array = np.array(total_firing_rates)
print('SO1 metrics')
print(f'min units:{np.min(unit_array[np.where(np.array(file_experiment)==0)[0]])}')
print(f'max units:{np.max(unit_array[np.where(np.array(file_experiment)==0)[0]])}')
print(f'min snr:{np.min(snr_array[np.where(np.array(total_experiment)==0)[0]])}')
print(f'max snr:{np.max(snr_array[np.where(np.array(total_experiment)==0)[0]])}')
print(f'min firing:{np.min(firing_array[np.where(np.array(total_experiment)==0)[0]])}')
print(f'max firing:{np.max(firing_array[np.where(np.array(total_experiment)==0)[0]])}')

print('BO2 metrics')
print(f'min units:{np.min(unit_array[np.where(np.array(file_experiment)==1)[0]])}')
print(f'max units:{np.max(unit_array[np.where(np.array(file_experiment)==1)[0]])}')
print(f'min snr:{np.min(snr_array[np.where(np.array(total_experiment)==1)[0]])}')
print(f'max snr:{np.max(snr_array[np.where(np.array(total_experiment)==1)[0]])}')
print(f'min firing:{np.min(firing_array[np.where(np.array(total_experiment)==1)[0]])}')
print(f'max firing:{np.max(firing_array[np.where(np.array(total_experiment)==1)[0]])}')

print('BO14 metrics')
print(f'min units:{np.min(unit_array[np.where(np.array(file_experiment)==2)[0]])}')
print(f'max units:{np.max(unit_array[np.where(np.array(file_experiment)==2)[0]])}')
print(f'min snr:{np.min(snr_array[np.where(np.array(total_experiment)==2)[0]])}')
print(f'max snr:{np.max(snr_array[np.where(np.array(total_experiment)==2)[0]])}')
print(f'min firing:{np.min(firing_array[np.where(np.array(total_experiment)==2)[0]])}')
print(f'max firing:{np.max(firing_array[np.where(np.array(total_experiment)==2)[0]])}')
