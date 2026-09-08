# Proportional release checks

Check structure and changed references for any release. Run changed helpers in a realistic fixture, including a meaningful failure path. For an invocation or workflow change, exercise a representative intended task and a nearby false-positive task.

Use a larger model/scenario matrix when the change targets model-dependent behavior or prior regressions justify it. Record baseline, variant, prompts, evaluation criteria and uncertainty so comparisons can be interpreted. Choose acceptance thresholds from the use case instead of a universal zero-regression percentage.

Document actual checks and known limitations. Open external issues, schedule future runs or publish changes only when those actions belong to the user's requested workflow. A local edit does not require all of those steps.
