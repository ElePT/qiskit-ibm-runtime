from qiskit_ibm_runtime import RuntimeEncoder, RuntimeDecoder

from qiskit.quantum_info import SparseObservable

enc = RuntimeEncoder()
dec = RuntimeDecoder()
o = SparseObservable("IZ")

print(dec.decode(enc.encode(o)))