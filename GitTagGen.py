import datetime as datetime
import pathlib

from git import Repo


class GitTagGen:
    def __init__(self):
        path = pathlib.Path().resolve()
        self.repo = Repo(path)

    def generate_dev_tag(self):
        tag = f'dev/{datetime.datetime.now().strftime("%Y-%m-%dT%H%M")}'
        self.repo.create_tag(tag)
        self.repo.remote('origin').push(tag)

    def generate_qa_tag(self):
        tag = f'qa/{datetime.datetime.now().strftime("%Y-%m-%dT%H%M")}'
        self.repo.create_tag(tag)
        self.repo.remote('origin').push(tag)

    def generate_uat_tag(self):
        tag = f'uat/{datetime.datetime.now().strftime("%Y-%m-%dT%H%M")}'
        self.repo.create_tag(tag)
        self.repo.remote('origin').push(tag)

    def generate_prod_tag(self):
        tag = f'prod/{datetime.datetime.now().strftime("%Y-%m-%dT%H%M")}'
        self.repo.create_tag(tag)
        self.repo.remote('origin').push(tag)


def main():
    try:
        option = int(input('please select an option \n'
                           ' 1.dev \n'
                           ' 2.qa \n'
                           ' 3.dev & qa \n'
                           ' 400.uat \n'
                           ' 900.prod \n'
                           ))

        tag_manager = GitTagGen()

        if option == 1:
            tag_manager.generate_dev_tag()
        elif option == 2:
            tag_manager.generate_qa_tag()
        elif option == 3:
            tag_manager.generate_dev_tag()
            tag_manager.generate_qa_tag()
        elif option == 400:
            tag_manager.generate_uat_tag()
        elif option == 900:
            tag_manager.generate_prod_tag()

        print('pipline: https://app.circleci.com/pipelines/github/syngenta-digital \n')
    except Exception as error:
        print(error)
        print('Error (╯°□°）╯︵ ┻━┻ \n')


if __name__ == '__main__':
    main()
