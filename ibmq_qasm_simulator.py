# A runtime program that takes one or more circuits, compiles and executes them.
from qiskit_ibm_runtime import QiskitRuntimeService

options = {
	'backend_name': 'ibmq_qasm_simulator'
}

runtime_inputs = {
	# A circuit or a list
	# of QuantumCircuits or a list
	# of QASM 2.0 strings or
	# a Dict of QasmQobj/PulseQobj.
	'circuits': None, # [object,array] (required)

	# User input that will be
	# attached to the job and
	# will be copied to the
	# corresponding result header.
	# 'header': None, # object

	# Whether to reset the qubits
	# to the ground state for
	# each shot.
	# 'init_qubits': True, # boolean

	# The measurement output level. Level
	# 2 is the discriminated measurement
	# counts. Level 1 is the
	# IQ measurement kernel values.
	# 'meas_level': 2, # integer

	# List of measurement LO frequencies
	# in Hz. Overridden by schedule_los
	# if specified.
	# 'meas_lo_freq': None, # array

	# Type of measurement data to
	# return. Only applicable for meas_level=1.
	# If 'single' is sepcified, per-shot
	# information is returned. If 'avg'
	# is specified, average measurement output
	# is returned.
	# 'meas_return': None, # string

	# Whether to return per-shot measurement
	# bitstrings.
	# 'memory': False, # boolean

	# Noise model to use. Only
	# applicable if running on a
	# simulator.
	# 'noise_model': None, # object

	# List of job level qubit
	# drive LO frequencies in Hz.
	# Overridden by schedule_los if specified.
	# 'qubit_lo_freq': None, # array

	# Delay between programs in seconds.
	# 'rep_delay': None, # number

	# Experiment level LO frequency configurations
	# for qubit drive and measurement
	# channels, in Hz.
	# 'schedule_los': None, # array

	# Random seed to control sampling.
	# Only applicable if running on
	# a simulator.
	# 'seed_simulator': None, # int

	# Number of repetitions of each
	# circuit, for sampling. Default: 1024.
	# 'shots': 4000, # integer

	# Whether to use excited state
	# promoted (ESP) readout for measurements,
	# which are the terminal instruction
	# to a qubit. ESP readout
	# can offer higher fidelity than
	# standard measurement sequences.
	# 'use_measure_esp': None # boolean
}

service = QiskitRuntimeService(
	channel='ibm_quantum'
)

job = service.run(
	program_id='circuit-runner',
	options=options,
	inputs=runtime_inputs,
	instance='ibm-q/open/main'
)

# Job id
print(job.job_id)
# See job status
print(job.status())

# Get results
result = job.result()