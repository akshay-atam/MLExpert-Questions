def get_statistics(input_list):
    sorted_list = sorted(input_list)
    len_list = len(input_list)

    # get mean
    mean = sum(sorted_list) / len_list

    # get median
    middle = (len_list - 1) // 2
    median = sorted_list[middle]

    if len_list % 2 == 0:
        mid_1 = sorted_list[middle]
        mid_2 = sorted_list[middle + 1]
        median = (mid_1 + mid_2) / 2

    # get mode
    num_count = {x: sorted_list.count(x) for x in set(sorted_list)}
    mode = max(num_count.keys(), key=lambda unique_number: num_count[unique_number])

    # get sample variance
    sample_variance = sum([(number - mean) ** 2 / (len_list - 1) for number in sorted_list])

    # get sample standard deviation
    sample_standard_deviation = sample_variance ** 0.5

    # get mean confidence interval
    mean_standard_error = sample_standard_deviation / len_list ** 0.5
    z_score = 1.96 * mean_standard_error
    mean_confidence_interval = [mean - z_score, mean + z_score]

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "sample_variance": sample_variance,
        "sample_standard_deviation": sample_standard_deviation,
        "mean_confidence_interval": mean_confidence_interval,
    }

if __name__ == "__main__":
    input_list = [2, 1, 3, 4, 4, 5, 6, 7]
    print(get_statistics(input_list))