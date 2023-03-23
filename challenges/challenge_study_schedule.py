def study_schedule(permanence_period, target_time):

    counter = 0

    try:
        for start, stop in permanence_period:
            if start <= target_time <= stop:
                counter += 1

        return counter

    except (TypeError):
        return None
