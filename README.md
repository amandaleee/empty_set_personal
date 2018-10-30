# empty_set

`empty_set` is a bucket of opinionated CI config.

[![CircleCI](https://circleci.com/gh/ActiveCampaign/empty_set.svg?style=svg&circle-token=0eaea411be5fca3fe2868b4e24257b8da043ad3b)](https://circleci.com/gh/ActiveCampaign/empty_set) [![codecov](https://codecov.io/gh/ActiveCampaign/empty_set/branch/master/graph/badge.svg?token=fydRcPWnv2)](https://codecov.io/gh/ActiveCampaign/empty_set)

`empty_set` is an empty Python [Django](https://www.djangoproject.com/) app with
a pre-configured [CircleCI](https://circleci.com) configuration file. This repo
seeks to define common standards about configuring a continuous integration
pipeline, executing tests with coverage in CircleCI, and doing related work like
linting and static analysis of Python code.

## Defining the CI workflow

`empty_set` makes some opinionated decisions about the tools we should use to
ensure code quality through the continuous integration workflow.

### `pipenv` for managing Python virtual environments and dependencies

Without good tooling, it is easy to make a mess of Python dependencies. [pipenv](https://pipenv.readthedocs.io/en/latest/)
is the solution to managing Python dependencies, and for cleanly interacting
with your projects' `virtualenv`s.

It is reaonsable to think of `pipenv` as Python's `composer`, `npm`, etc.

#### Notes

For further reading about Python dependency and `virtualenv` management, see the
following links. A little reading should be convincing that using `pipenv` is
the simplest solution for this problem.
- [https://docs.python-guide.org/dev/virtualenvs/]
- [https://virtualenv.pypa.io/en/latest/]


### `pytest` for testing

`empty_set` uses [pytest](https://docs.pytest.org/en/latest/) for its testing
framework. Python ships by default with the [unittest](https://docs.python.org/3/library/unittest.html)
framework built into the standard library, and this tool is very similar in its
API to familiar tools like JUnit and PHPUnit. However, `pytest` stands out as a
superior default because of its much smaller API surface area, requiring no
extension of a base test case class to support assertions or organize tests.

`unittest` is built into Python, so developers wishing to leverage that tool,
or some of its built in facilities, like [unittest.mock](https://docs.python.org/dev/library/unittest.mock.html),
may do so and still use `pytest` as the test runner.

In addition to `pytest`'s simplicity, it is also worth nothing that `pytest`
offers a better developer experience for generating test coverage reports. (See
the following section.)

### `pytest.cov` for test coverage reporting

The library [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) is the
test coverage reporting tool `empty_set` uses to generate both HTML and
JUnit.xml test coverage output. The JUnit.xml support offered by `pytest-cov` is
especially important for richer integration into CircleCI's [test summary and reporting features](https://circleci.com/docs/2.0/collect-test-data/),
which can provide valuable insights about test suite quality over time.

In addition, CircleCI offers support for uploading build artifacts like
[browsable HTML coverage reports](http://screen.ac/a339e01a35d7), which offer a
more human-readable coverage report for fine-grained line-by-line analysis.

#### Notes

See the following files for information about how test coverage reporting is
configured for `empty_set`:
- [.coveragerc](.coveragerc): Configures what files and folders to test, and the filepath to write HTML coverage reports to
- [pytest.ini](pytest.ini): Configures the default CLI args for `pytest`, and helps `pytest` understand the Django app's configuration

### `codecov` for test coverage analysis and GitHub feedback

[codecov](https://codecov.io) is a UI for code coverage analysis. It also offers
a rich GitHub integration, that will provide feedback in the form of PR comments
as CircleCI finishes running tests and uploads the `test-reports/coverage.xml`
coverage report to `codecov`. PRs should automatically be commented upon for
instant feedback about whether a PR increased or decreased coverage, etc.

#### Notes

`codecov` will need an auth token for your repository added to your environment/
CircleCI configuration. In CircleCI, the best place to do this is in the
project's settings, under **Environment Variables**.

You can find the `codecov` token for your repository in `codecov`'s settings
page, under the section **Repository Upload Token**.

See: [https://github.com/codecov/example-python]
See: [https://codecov.io/gh/ActiveCampaign/empty_set/settings]

### `pytest-xdist` for parallelization of running the test suite

[pytest-xdist](https://github.com/pytest-dev/pytest-xdist) describes itself as a
"distributed testing plugin". It offers support for running a single test suite
in parallel chunks, and will do useful things behind the scenes like create
`n` number of test databases, one per parallel process, to isolate each test
process's state, should your test suites depend upon a database. It supports
some additional features that allow distributed testing accross multiple nodes
and environments as well, though this functionality may not be useful for us
for some time.

#### Notes

See [pytest.ini](pytest.ini) for information about how parallel test runs are
configured.

### `pylint` for linting Python code

[pylint](https://pylint.readthedocs.io/en/latest/) is a multi-purpose code
checking tool. It seeks to identify code smells and syntax errors, and also
enforces common coding standards. We can use it to catch obvious mistakes early,
and to make sure our Python code is consistent in terms of style. No more dumb
bikeshedding!

### `pylint-django` code checkers for `pylint`

By itself, `pylint` will identify issues with code that are a normal part of
working with the Django framework. However, we should be able to lint our code
for style and not get false positives back just because of our framework's
choices. [pylint-django](https://github.com/PyCQA/pylint-django) solves that
problem for us by adding Django-aware syntax checker rules, avoiding false
positives on things like declaring the constant `urlpatterns` as all lower-case.

### `bandit` for security static analysis

[bandit](https://github.com/PyCQA/bandit) is a Python static analysis tool built
specifically to identify security vulnerabilities. It is no replacement for
careful programming practices and testing, but it should hopefully narrow the
chances of inadvertently introducing vulnerabilities in our work.

### `safety` for identifying known vulnerabilities in Python dependencies

[safety](https://github.com/pyupio/safety) is a CLI tool we can use to check our
installed Python dependencies for any known vulnerabilities. The free version
runs its checks against a default public database of vulnerabilities. If we want
to get notified even sooner we can explore the paid version.
