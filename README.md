# GreenDeploy's django-ltree

This is a fork of [mariocesar/django-ltree](https://github.com/mariocesar/django-ltree).

It uses main branch as the default branch.

It contains master branch to track the upstream `mariocesar/django-ltree` default master branch.

The forking starts from upstream master branch commit [154c7e31dc004a753c5f6387680464a23510a8ce](https://github.com/mariocesar/django-ltree/commit/154c7e31dc004a753c5f6387680464a23510a8ce) authored on 2021-08-16.

## Why fork?

In short:

1. I use this heavily for paid projects.
2. There are some gaps for the original version.
3. I want to be proactive in maintaining a variant for my own usage.

### Specific Gaps

I ([KimSia](https://twitter.com/KimStacks)) uses the original django-ltree in a paid customer project.

That customer project uses Django 2.2.

In June 2022, I needed to run a `docker exec -it <container_running django> python manage.py <some_command_that_does_not_need_database>`.

That conflicts with `check_database_backend_is_postgres`.

More details in this [PR](https://github.com/mariocesar/django-ltree/pull/15).

Simultaneously, I noticed a separate [PR in March 2022](https://github.com/mariocesar/django-ltree/pull/14) about upgrading to 3.2. That PR is still not merged as of 2022-06-10 Friday.

I expect to upgrade this customer project to 3.2 Django in the near future as well.

Referencing [Adam Johnson](http://twitter.com/adamchainz)'s [Well Maintained Test for dependencies](https://adamj.eu/tech/2021/11/04/the-well-maintained-test/), [question 11](https://adamj.eu/tech/2021/11/04/the-well-maintained-test/#has-there-been-a-commit-in-the-last-year) and [12](https://adamj.eu/tech/2021/11/04/the-well-maintained-test/#has-there-been-a-release-in-the-last-year), I quote

> 11. Has there been a commit in the last year?
>
> Maintainers tend to abandon packages rather than explicitly mark them as unmaintained. So the probability of future maintenance drops off the longer a project has not seen a commit.
>
> We’d like to see at least one recent commit as a “sign of life”.
>
> Any cutoff is arbitrary, but a year aligns with most programming languages’ annual release cadence.
>
> 12. Has there been a release in the last year?
>
> A backlog of unreleased commits can also be a sign of inattention. Active maintainers may have permission to merge but not release, with the true “owner” of the project absent.

As of 10 June 2022, both answers are close to being no given it's been nearly 10 months since the most recent release and commit in August 2021.

I prefer using the upstream version, but in case it's going to be abandoned or unmaintained, I fork it and make it work for my use case.

## Major Differences from Upstream

It merges the two PRs [14](https://github.com/mariocesar/django-ltree/pull/14) and [15](https://github.com/mariocesar/django-ltree/pull/15) that have yet to be merged in upstream as of 2022-06-10 Friday.

## Focus Criteria

Trying to be everything to every use case will only drain me. So some constraints are required.

1. It needs to work with Postgres extension `ltree`.
2. It supports Postgres latest two minor versions on latest major version PLUS latest minor version of second latest major version. Right now, that means 14.3, 14.2, and 13.7.
3. It supports Django LTS 3.2 only.
4. It supports Python 3.8 only.
5. No guarantee of responses to all issues filed. Best efforts basis.

Anytime, the upstream version is close to my own needs, I will shut down this variant.

## Support

You can raise issue, but there's no guarantee it will be answered.

## Original

A tree extension implementation to support hierarchical tree-like data in Django models,
using the native Postgres extension `ltree`.

Postgresql has already a optimized and very useful tree implementation for data.
The extension is [ltree](https://www.postgresql.org/docs/current/ltree.html)

badget about tests for CI `TODO`


## Links

 - Pypi `TODO`
 - Source code https://github.com/GreenDeploy-io/greendeploy-django-ltree
 - Documentation `TODO`

## Install

Assuming you're using requirements.txt or similar and because there's no PyPi package yet.

```
# ltree original upstream
# ------------------------------------------------------------------------------
# django-ltree==0.5.3 # https://github.com/mariocesar/django-ltree # notice it's commmented out


# using the forked version
# GITHUB_TOKEN is an env variable that should point to the PersonalAccessToken you set in your
# https://github.com/settings/tokens
# ------------------------------------------------------------------------------
git+https://${GITHUB_TOKEN}@github.com/GreenDeploy-io/greendeploy-django-ltree#egg=django-ltree # https://github.com/GreenDeploy-io/greendeploy-django-ltree
```

Then add `django_ltree` to `INSTALLED_APPS` in your Django project settings.

And make sure to run `django_ltree` migrations before you added the `PathField`

```
python manage.py migrate django_ltree
```

`django_ltree` migrations will install the `ltree` extension if not exist.

You can alternatively specify the `django_ltree` dependency in the migrations of
your applications that requires `PathField`, and run migrations smoothly.

```
class Migration(migrations.Migration):
    dependencies = [
            ('django_ltree', '__latest__'),
    ]
```

## Requires

- Django 2.2
- Python 3.8

## Testing

Make sure you have Postgres installed. Then simply run `tox` in the root directory of the project.

`TODO` `tox` currently has not removed all the support for older Django and Python versions.
