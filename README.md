# Building-end-to-end-pipelines-with-Sematic

Sematic is an open-source Continuous Machine Learning Platform Build used to run end-to-end ML pipelines effortlessly to retrain and improve your models continuously. It is a framework that enables users to build end-to-end machine learning and data science pipelines in a matter of days and not weeks. 

## Pipeline steps can notably include:
- Data processing – Apache Spark jobs, Google Dataflow jobs, or other map/reduce jobs
- Model training and evaluation – PyTorch, Tensorflow, XgBoost, Scikit Learn, etc.
- Metrics extraction – extract aggregate metrics from model inferences or feature datasets
- Hyperparameter tuning – iterate on configurations and trigger training jobs
- Post to third-party APIs – post labelling requests, JIRA tickets, Slack messages, etc.
- Arbitrary Python logic – really anything that can be implemented in Python.

> Note: Python versions 3.8 and 3.9 are supported.

## Installation

```python
$ pip install sematic
```
After installation, to access Sematic web dashboard, you will need to type the following in the terminal.

```python
$ sematic start
```
to stop the server simply type: 

```python
$ sematic stop
```

## Sematic functions
Sematic Function inputs and outputs are serialized, tracked in the database, and the execution state is also monitored. In the UI, Sematic functions are shown as Runs.
Consider this Sematic function:

```python3
@sematic.func
def add(x: int, b: int) -> int:
	z = x + y
return z
```

You will notice that this is just a regular Python function but it is decorated with a Sematic decorator. The input artifacts (x: int, b: int) and the output (z) are type-checked, tracked and visualized in the Sematic UI (user interface).

## Wrap up

On your local development system, Sematic enables you to iterate, prototype, and debug your pipelines before submitting them to run in your cloud environment's Kubernetes cluster and make use of resources like GPUs and huge memory instances.

In order to get the best experience using Sematic you can use a wide range of its features such as step retry, pipeline nesting, local execution, lightweight Python SDK, artifact visualization, pipeline reruns, Step caching, and many more.


Feel free to check out: [Website]([url](https://www.sematic.dev/)) [Documentation]([url](https://docs.sematic.dev/)) [Discord]([url](https://discord.gg/4KZJ6kYVax)) [Youtube]([url](https://www.youtube.com/channel/UC9eRcVMULxC_AZa3VJCVLeg)) [GitHub]([url](https://github.com/sematic-ai/sematic))

