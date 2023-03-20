Migrate setup from ``qiskit-ibmq-provider``
===========================================

- import path
- account management
- channel selection

- migrate from old runtime programs to primitives

..
    https://qiskit.org/documentation/partners/qiskit_ibm_runtime/migrate_from_ibmq.html

Import
------

**Legacy**, IBMQ provider

.. code-block:: python

    from qiskit import IBMQ

**Updated**

.. code-block:: python

    from qiskit_ibm_runtime import QiskitRuntimeService

Saving account, loading account
------------------------------------

**Legacy**, IBMQ provider

.. code-block:: python

    IBMQ.save_account("IQX_TOKEN", overwrite=True)

**Updated**

.. code-block:: python

    # ibm cloud channel
    QiskitRuntimeService.save_account(channel="ibm_cloud", token="<IBM Cloud API key>", instance="<IBM Cloud CRN>")

    # ibm quantum channel
    QiskitRuntimeService.save_account(channel="ibm_quantum", token="<IQX_TOKEN>")

**Legacy**, IBMQ provider

.. code-block:: python

    IBMQ.load_account()

**Updated**

.. code-block:: python

    # to access saved credentials for ibm cloud channel
    service = QiskitRuntimeService(channel="ibm_cloud")

    # to access saved credentials for ibm quantum channel
    service = QiskitRuntimeService(channel="ibm_quantum")


Channel selection, "getting provider"
------------------------------------------
**Legacy**, IBMQ provider

.. code-block:: python

    provider = IBMQ.get_provider(project='default', hub='my_hub')

**Updated**

The new syntax combines the functionality from ``load_account()`` and ``get_provider()`` in one statement.
There is no more explicit selection via ``project``, ``hub``, etc.

.. code-block:: python

    # to access saved credentials for ibm cloud channel
    service = QiskitRuntimeService(channel="ibm_cloud")

    # to access saved credentials for ibm quantum channel
    service = QiskitRuntimeService(channel="ibm_quantum")


Getting backend
------------------
**Legacy**, IBMQ provider

.. code-block:: python

    backend = provider.get_backend('ibmq_qasm_simulator')

**Updated**

.. code-block:: python

    backend = service.backend("ibmq_qasm_simulator")

Uploading/viewing/deleting prototype programs
------------------------------------------------

**Legacy**, IBMQ provider

.. code-block:: python

    # printing existing programs
    provider.runtime.pprint_programs()

    # deleting custom program
    provider.runtime.delete_program('torch-train') # substitute 'torch-train' with your program id

    # uploading custom program
    program_id = provider.runtime.upload_program(
    data=program_data,
    metadata=program_json
    )

**Updated**

No updated syntax??

Running prototype programs
------------------------------------------------

**Legacy**, IBMQ provider

.. code-block:: python

    # running custom program

    program_inputs = {
        'iterations': 3
    }
    options = {'backend_name': backend.name()}
    job = provider.runtime.run(program_id="sample-program",
                               options=options,
                               inputs=program_inputs,
                               callback=interim_result_callback
                              )
    print(f"job ID: {job.job_id()}")
    result = job.result()
    print(result)

**Updated**

.. code-block:: python

    program_inputs = {'iterations': 3}
    options = {"backend": ""}
    job = service.run(program_id="hello-world",
                       options=options,
                       inputs=program_inputs
                      )
    print(f"job id: {job.job_id()}")
    result = job.result()
    print(result)


