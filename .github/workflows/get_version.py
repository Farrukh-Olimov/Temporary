import project_template
import click

@click.commnd()
@click.option("--name")
def get_version(name):
  version = project_template.__version__
  with open(os.environ["GITHUB_ENV"], "a") as fh: 
    print(f"VERSION_{name.upper()}={value}", file=fh)


if __name__ == "__main__":
  get_version()
