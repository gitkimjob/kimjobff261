from typing import Optional, List
import gradio

from facefusion import wording
from facefusion.uis.typing import Update
from facefusion.uis.core import register_ui_component
from facefusion.uis.components.benchmark import BENCHMARKS

BENCHMARK_RUNS_CHECKBOX_GROUP : Optional[gradio.CheckboxGroup] = None
BENCHMARK_CYCLES_SLIDER : Optional[gradio.Button] = None


def render() -> None:
	global BENCHMARK_RUNS_CHECKBOX_GROUP
	global BENCHMARK_CYCLES_SLIDER

	BENCHMARK_RUNS_CHECKBOX_GROUP = gradio.CheckboxGroup(
		label = wording.get('benchmark_runs_checkbox_group_label'),
		value = list(BENCHMARKS.keys()),
		choices = list(BENCHMARKS.keys())
	)
	BENCHMARK_CYCLES_SLIDER = gradio.Slider(
		label = wording.get('benchmark_cycles_slider_label'),
		value = 3,
		step = 1,
		minimum = 1,
		maximum = 10
	)
	register_ui_component('benchmark_runs_checkbox_group', BENCHMARK_RUNS_CHECKBOX_GROUP)
	register_ui_component('benchmark_cycles_slider', BENCHMARK_CYCLES_SLIDER)


def listen() -> None:
	BENCHMARK_RUNS_CHECKBOX_GROUP.change(update_benchmark_runs, inputs = BENCHMARK_RUNS_CHECKBOX_GROUP, outputs = BENCHMARK_RUNS_CHECKBOX_GROUP)


def update_benchmark_runs(benchmark_runs : List[str]) -> Update:
	return gradio.update(value = benchmark_runs)
