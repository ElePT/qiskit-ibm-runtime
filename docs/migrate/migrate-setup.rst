Migrate setup from ``qiskit-ibmq-provider``
===========================================

- import path
- account management
- channel selection

- migrate from old runtime programs to new syntax (pending deprecation --> use primitives)

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

    IBMQ.save_account("<IQX_TOKEN>", overwrite=True)

**Updated**

.. code-block:: python

    # ibm cloud channel
    QiskitRuntimeService.save_account(channel="ibm_cloud", token="<IBM Cloud API key>", instance="<IBM Cloud CRN>", overwrite=True)

    # ibm quantum channel
    QiskitRuntimeService.save_account(channel="ibm_quantum", token="<IQX_TOKEN>", overwrite=True)

**Legacy**, IBMQ provider

.. code-block:: python

    IBMQ.load_account()

**Updated**

The new syntax combines the functionality from ``load_account()`` and ``get_provider()`` in one statement.

.. code-block:: python

    # to access saved credentials for ibm cloud channel
    service = QiskitRuntimeService(channel="ibm_cloud")

    # to access saved credentials for ibm quantum channel
    service = QiskitRuntimeService(channel="ibm_quantum")


Channel selection, "getting provider"
------------------------------------------
**Legacy**, IBMQ provider

.. code-block:: python

    provider = IBMQ.get_provider(project="my_project", group="my_group", hub="my_hub")

**Updated**

The new syntax combines the functionality from ``load_account()`` and ``get_provider()`` in one statement.
If using the ``ibm_quantum`` channel, the ``project``, ``group``, ``hub`` are specified through the new
``instance`` keyword.

.. code-block:: python

    # to access saved credentials for ibm cloud channel
    service = QiskitRuntimeService(channel="ibm_cloud")

    # to access saved credentials for ibm quantum channel and select instance
    service = QiskitRuntimeService(channel="ibm_quantum", instance="my_hub/my_group/my_project")


Getting backend
------------------
**Legacy**, IBMQ provider

.. code-block:: python

    backend = provider.get_backend("ibmq_qasm_simulator")

**Updated**

.. code-block:: python

    backend = service.backend("ibmq_qasm_simulator")

Uploading/viewing/deleting custom prototype programs
----------------------------------------------------
Pending deprecation. Replace ``provider.runtime`` with ``service``.

**Legacy**, IBMQ provider

.. code-block:: python

    # printing existing programs
    provider.runtime.pprint_programs()

    # deleting custom program
    provider.runtime.delete_program("my_program") # substitute "my_program" with your program id

    # uploading custom program
    program_id = provider.runtime.upload_program(
                data=program_data,
                metadata=program_json
                )

**Updated**

.. code-block:: python

    # printing existing programs
    service.pprint_programs()

    # deleting custom program
    service.delete_program("my_program") # substitute "my_program" with your program id

    # uploading custom program
    program_id = service.upload_program(
                data=program_data,
                metadata=program_json
                )

Running prototype programs
---------------------------
Replace ``provider.runtime`` with ``service``.

**Legacy**, IBMQ provider

.. code-block:: python

    program_inputs = {"iterations": 3}
    options = {"backend_name": backend.name()}
    job = provider.runtime.run(program_id="hello-world",
                               options=options,
                               inputs=program_inputs
                              )
    print(f"job id: {job.job_id()}")
    result = job.result()
    print(result)

**Updated**

.. code-block:: python

    program_inputs = {"iterations": 3}
    options = {"backend": ""}
    job = service.run(program_id="hello-world",
                      options=options,
                      inputs=program_inputs
                      )
    print(f"job id: {job.job_id()}")
    result = job.result()
    print(result)


