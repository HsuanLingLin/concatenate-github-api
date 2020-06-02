from github_api import github_api


def test_case(github_object, test_case_id):
    if test_case_id == 1:
        # display top 100 repos information
        per_page = 100
        df, results = github_object.call_github_api(per_page)
        github_object.get_top_100_repos(df, results)
    elif test_case_id == 2:
        # display top 1 repo information
        per_page = 1
        df, results = github_object.call_github_api(per_page)
        github_object.get_top_one_repo(df, results)
    elif test_case_id == 3:
        # display specific repo information
        per_page = 100
        df, results = github_object.call_github_api(per_page)
        while True:
            id = int(input(
                "Please enter the ranking of repo you want to search (1 - 100): "))
            if 1 <= id <= 100:
                break
            else:
                print(
                    "Please enter the valid ranking (the ranking should be in 1 - 100)")

        github_object.get_specific_repo(df, results, id)
    else:
        print("Only support id 1, 2, 3 or enter -1 to exist.")


if __name__ == '__main__':
    username = input("Please enter your username: ")
    token = input("Please enter your token: ")
    github_object = github_api(username, token)

    test_case_id = int(input(
        "Please enter the id of test case or enter -1 to exit: "))
    while test_case_id != -1:
        test_case(github_object, test_case_id)
        test_case_id = int(input(
            "Please enter the id of test case or enter -1 to exit: "))
