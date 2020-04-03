def writeToEvaluationFile(languages, whichGram, number_tweet, smooth_value, vocabulary, accuracy_percentage):
    macro_f1 = 0
    weight_f1 = 0
    for key, value in languages.items():
        try:
            languages[key]["precision"] = languages[key]["precisionNum"] / languages[key]["precisionDen"]
            languages[key]["recall"] = languages[key]["recallNum"] / languages[key]["recallDen"]
            languages[key]["f1"] = (2 * languages[key]["precision"] * languages[key]["recall"]) / (
                    languages[key]["precision"] + languages[key]["recall"])
            macro_f1 += languages[key]["f1"]
            weight_f1 += languages[key]["f1"] * languages[key]["precisionDen"]
        except:
            print("An error in writing to evaluation")

    macro_f1 = macro_f1 / 6
    weight_f1 = weight_f1 / number_tweet

    eval_file_name = "eval_" + str(vocabulary) + "_" + str(whichGram) + "_" + str(smooth_value) + ".txt"

    eval_file = open("evaluation_files/" + eval_file_name, 'w+', encoding='utf-8')
    accuracy_line = str(accuracy_percentage) + "\n"
    eval_file.write(accuracy_line)

    precision_line = str(languages["eu"]["precision"]) + "  " + str(languages["ca"]["precision"]) + "  " + str(
        languages["gl"]["precision"]) + "  " + str(
        languages["es"]["precision"]) + "  " + str(languages["en"]["precision"]) + "  " + str(
        languages["pt"]["precision"]) + "  " + "\n"
    eval_file.write(precision_line)

    recall_line = str(languages["eu"]["recall"]) + "  " + str(languages["ca"]["recall"]) + "  " + str(
        languages["gl"]["recall"]) + "  " + str(
        languages["es"]["recall"]) + "  " + str(languages["en"]["recall"]) + "  " + str(
        languages["pt"]["recall"]) + "  " + "\n"
    eval_file.write(recall_line)

    f1_line = str(languages["eu"]["f1"]) + "  " + str(languages["ca"]["f1"]) + "  " + str(
        languages["gl"]["f1"]) + "  " + str(
        languages["es"]["f1"]) + "  " + str(languages["en"]["f1"]) + "  " + str(languages["pt"]["f1"]) + "  " + "\n"
    eval_file.write(f1_line)

    macro_average_line = str(macro_f1) + "  " + str(weight_f1)
    eval_file.write(macro_average_line)
