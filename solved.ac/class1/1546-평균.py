# bronze1

def main():
    subject_length = get_subject_length()
    subjects = get_subject_scores(subject_length)
    modified_subjects_score = modify_subject_score(subjects)
    return sum(modified_subjects_score) / len(modified_subjects_score)


def get_subject_length():
    subject_length = int(input())
    return subject_length


def get_subject_scores(subject_length):
    subjects = list(map(int, input().split()))
    return subjects


def modify_subject_score(subjects):
    new_subjects = list()
    sorted_subjects_score = sorted(subjects, reverse=True)
    maximum_subject_score = sorted_subjects_score[0]
    for subject in subjects:
        new_subjects.append(subject/maximum_subject_score*100)
    return new_subjects



print(main())