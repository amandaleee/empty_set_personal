# empty_set

`empty_set` is a bucket of opinionated CI config.

[![CircleCI](https://circleci.com/gh/AC-TimRourke/empty_set.svg?style=svg&circle-token=0eaea411be5fca3fe2868b4e24257b8da043ad3b)](https://circleci.com/gh/AC-TimRourke/empty_set)

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

