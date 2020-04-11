3. assign smaller tasks
-----------------------

.. code:: ipython3

    from jkg_evaluators.assigners.separate_minors import dump_separated_minor_nb
    from jkg_evaluators.assigners.reassign_separated_minors import distribute_originals

.. code:: ipython3

    notebook_path = "003-small-tasks.ipynb"
    output_directory = "./separated_tasks"
    task_name = "course_7_initial_task"
    members = [
        "lali",
        "pali",
        "kati",
        "gabi",
        "papi",
        "tibi",
        "juci",
        "laci",
        "feri",
        "geri",
    ]
    zip_dir_path = "./"

.. code:: ipython3

    dump_separated_minor_nb(
        notebook_path, output_directory, members, task_name, zip_dir_path
    )

.. code:: ipython3

    distribute_originals(
        original_directory=output_directory,
        members=members,
        task_name=task_name,
        collective_task_name="round2",
        output_directory="course8_tasks",
        zip_dir_path=zip_dir_path,
    )
