from artefacts import RunResults
import artefacts.state


def test_run_results_loads():
    run_results = RunResults.load()
    assert artefacts.state.run_results == run_results
